from distutils.core import setup

setup(
    name="panoply_typeform",
    version="1.0.0",
    description="Panoply Data Source for the Typeform API",
    author="Alon Weissfeld",
    author_email="alon.weissfeld@panoply.io",
    url="http://panoply.io",
    package_dir={"panoply": ""},
    install_requires=[
        "panoply-python-sdk",
        "mock==1.0.1"
    ],
    packages=["panoply.typeform"]
)
