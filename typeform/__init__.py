from typeform import *

Stream = Typeform

CONFIG = {
    'title': 'Typeform',
    'icon': 'data:image/jpeg;base64,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Fe58nubwVKU8y5zNmvJW0Yy1HYN1XAkbk9zzIOle2W1/YX6SDp4UWjqOf6g6y/h3bE3sZyaLJIOP3UJdz+GRJnIAT0Yy1SYYy1SYYy1SYGyD3CMx7xmPeCSdJvNst39/zd//2SAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA=',
    'params': [
        {
            'name': 'key',
            'required': True,
            'title': 'API Key',
            'placeholder': 'Typeform API Key',
            'help': 'Your unique API Key token. [Learn more](https://www.typeform.com/help/data-api/)'
        },
        {
            'name': 'forms',
            'required': True,
            'title': 'Forms',
            'type': 'list',
            'values': lambda source: Typeform(source, {}).get_forms(),
            'dependencies': ['key']
        }
    ],
    'categories': ['APIS'],
    'keywords': ['forms', 'surveys'],
    'createdAt': '2016-11-23'
}
