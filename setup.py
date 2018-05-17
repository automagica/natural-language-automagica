#!/usr/bin/env python

from distutils.core import setup

setup(name='Natural Language for Automagica',
      version='0.1',
      description='Natural Language Interface for Automagica',
      author='Koen van Eijk',
      author_email='koen@oakwood.ai',
      url='https://oakwood.ai/',
      entry_points = {
        'console_scripts': ['nla=nla.command_line:main'],
      },
      packages=['nla']
)