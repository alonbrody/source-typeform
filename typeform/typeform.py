import time
import copy
import json
import panoply
import urllib2
import datetime


FETCH_LIMIT = 500
DESTINATION = 'typeform'
DESTINATION_POSTFIX = '_{__table}'
BASE_URL = 'https://api.typeform.com/v1'
DATE_PARSER_FORMAT = '%Y-%m-%dT%H:%M:%S'


class Typeform(panoply.DataSource):

    # constructor
    def __init__(self, source, options):
        super(Typeform, self).__init__(source, options)

        if 'destination' not in source:
            source['destination'] = DESTINATION

        # append the destination postfix, which represent the form name
        source['destination'] += DESTINATION_POSTFIX

        # since we're retrieving only completed surveys we can
        # allow incremental pulling from the last successful batch
        incval = source.get('lastTimeSucceed')
        self._incval = getTimestamp(incval)


        forms = source.get('forms', [])
        self._forms = copy.deepcopy(forms)

        # add an 'offset' attribute used for pagination for each
        # different form, used as the actual number to use as offset
        for f in self._forms:
            f['offset'] = 0

        self._key = source.get('key')
        self._total = len(self._forms)

    def read(self, n = None):
        if len(self._forms) == 0:
            # no more data to consume
            return None

        form = self._forms[0]

        # construct the GET url and make the request
        url = self._url(form)
        body = self._request(url)

        # 'completed' represent the number of completed forms that
        # returned from the server
        stats = body.get('stats', {}).get('responses', {})
        total = stats.get('completed', 0)

        if (form['offset'] + FETCH_LIMIT) >= total:
            # we're done paginating with the current form.
            form['offset'] = None

            # no more results for this form, remove it
            self._forms.pop(0)

            # report progress
            loaded = self._total - len(self._forms)
            msg = '%s of %s forms fetched' % (loaded, self._total)
            self.progress(loaded, self._total, msg)
        else:
            # prepare the offset to the next set of records
            form['offset'] += FETCH_LIMIT


        # we only need the 'questions' and 'responses' results
        # that returned from the server. On top of that, add the
        # destination table name

        # add the questions records
        dest = (form['name'] + '_questions').replace(' ', '_')
        results = map(lambda x: dict(__table=dest, **x), body['questions'])

        # add the responses (answers) records
        dest = (form['name'] + '_responses').replace(' ', '_')
        responses = map(lambda x: dict(__table=dest, **x), body['responses'])

        results.extend(responses)
        return results


    # GET all the forms.
    def get_forms(self):
        # provides us with all of the user forms
        url = '%s/forms?key=%s' % (
            BASE_URL,
            self._key
        )

        # the body of the result is a list of forms
        return self._request(url)

    # Helper function for issuing GET requests 
    def _request(self, url):
        self.log('GET', url)

        try:
            res = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            raise TypeformError.from_http_error(e)


        # read the result and return it's parsed value
        body = res.read()
        return json.loads(body)

    # construct the relevant url according to the Typeform API
    def _url(self, form):
        url = '%s/form/%s?key=%s&completed=true&offset=%s&limit=%s' % (
            BASE_URL,
            form['id'],
            self._key,
            form['offset'],
            FETCH_LIMIT
        )

        # pull data incrementally if configured to do so.
        if self._incval:
            url += '&since=%s' % (self._incval)

        return url


# Typeform API exception class
class TypeformError(Exception):

    @classmethod
    def from_http_error(cls, err):
        """
        Provide a more descriptive error message from the returned
        Typeform API result, which should generally return a human
        readable error message adjacent to the HTTP StatusCode.
        """
        try:
            body = err.read()
            parsed = json.loads(body)
            if 'message' in parsed:
                return cls(parsed['message'])
            elif 'status' in parsed:
                msg = 'HTTP StatusCode %s' % (parsed['status'])
                return cls(msg)
        except:
            # unable to read a structured error message nor status hint,
            # just return the original error
            pass

        # no descriptive error message was extracted, return the
        # original generic error
        return err

# Helper function to validate a date and return the Unix timestamp
def getTimestamp(value):
    try:
        # this is kind of ugly, but we need to convert a date string
        # (e.g. '2016-09-21T10:23:42.819Z') to Unix timestamp
        value = value.split('.')[0]
        dt = datetime.datetime.strptime(value, DATE_PARSER_FORMAT)
        return int(time.mktime(dt.timetuple()))
    except:
        # if we can't parse the date to a timestamp (so it could
        # be used in the url GET request), don't use it at all.
        return None
