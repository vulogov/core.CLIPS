from gevent import monkey  # isort:skip # noqa
monkey.patch_all()
import os
from setuptools import setup, find_packages
try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license_txt = fh.read()

VERSION_PY="""
VERSION='%s'
RELEASE='%s'
URL='%s'
AUTHOR='%s'
AUTHOR_EMAIL='%s'
READ_me = \"\"\"%s\"\"\"

def nsVersion(ns):
    return VERSION
def nsRelease(ns):
    return RELEASE
"""

name="corec"
version="0.1"
release="0.1.0"
author='Vladimir Ulogov'
author_email='vladimir.ulogov@me.com'
url='https://github.com/vulogov/core.CLIPS'
license='Apache2.0'

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    #print([str(ir.requirement) for ir in reqs])
    return [str(ir.requirement) for ir in reqs]

def write_version(fname):
    f = open("{}/{}".format(root_dir, fname), 'w')
    f.write(VERSION_PY % (version, release, url, author, author_email, long_description))

write_version("corec/version.py")



setup(name=name,
    setup_requires=['pytest-runner'],
    version=release,
    description='Namespace-based expert system shell',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    python_requires='>=3.6',
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    install_requires=load_requirements("requirements.txt"),
    packages=find_packages())
