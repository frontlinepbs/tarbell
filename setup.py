#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup, find_packages
from tarbell import __VERSION__ as VERSION

APP_NAME = 'tarbell'

settings = dict()

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name=APP_NAME,
    version=VERSION,
    author=u'Tarbell Project',
    author_email='davideads@gmail.com',
    url='http://github.com/tarbell-project/tarbell',
    license='MIT',
    description='A very simple content management system',
    long_description="""Read the docs at http://tarbell.readthedocs.org

Tarbell makes it simple to put your work on the web, whether you’re a team of one or a dozen. With Tarbell, you can collaboratively build beautiful websites and publish them with ease.

Tarbell makes use of familiar, flexible tools to take the magic (and frustration) out of publishing to the web. Google spreadsheets handle content management, so changes to your stories are easy to make without touching a line of code. Step-by-step prompts help you set up and configure your project, so that publishing it is a breeze.""",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==3.0.2",
        "Frozen-Flask==1.0.2",
        "Jinja2==3.1.3",
        "Markdown==3.5.2",
        "MarkupSafe==2.1.5",
        "PyYAML==4.2b4",
        "boto==2.48.0",
        "clint==0.4.1",
        "gnureadline>=6.3.3",
        "google-api-python-client==1.8.0",
        "keyring==24.3.1",
        "oauth2client==4.1.3",
        "python-dateutil>=2.2",
        "requests==2.31.0",
        "sh==2.0.6",
        "six>=1.16.0",
        "xlrd==2.0.1",
    ],

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tarbell = tarbell.cli:main',
        ],
    },
    keywords=['Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet',
          ],
)


setup(**settings)
