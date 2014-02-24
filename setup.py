# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='youtube_dl_server',
    version='alpha.3.5',
    description='An API server based on youtube_dl',
    long_description='Get the videos from different sites using a server running youtube_dl',
    author='Jaime Marquínez Ferrándiz',
    author_email='jaime.marquinez.ferrandiz@gmail.com',
    url='https://github.com/jaimeMF/youtube-dl-api-server',
    packages=['youtube_dl_server', 'youtube_dl_server.API'],
    scripts=['bin/youtube-dl-server'],

    install_requires=[
        'WebOb',
        'Paste',
        'webapp2',
        'pyyaml',
        'youtube_dl >= 2013.12.04'
    ],

    classifiers=[
        'Topic :: Multimedia :: Video',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
)
