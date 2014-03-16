# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='youtube_dl_server',
    version='alpha.5',
    description='An API server based on youtube_dl',
    long_description='Get the videos from different sites using a server running youtube_dl',
    author='Jaime Marquínez Ferrándiz',
    author_email='jaime.marquinez.ferrandiz@gmail.com',
    url='https://github.com/jaimeMF/youtube-dl-api-server',
    packages=['youtube_dl_server'],
    entry_points={
        'console_scripts': [
            'youtube-dl-server = youtube_dl_server.server:main',
        ],
    },

    install_requires=[
        'Flask',
        'youtube_dl >= 2014.03.12',
    ],

    classifiers=[
        'Topic :: Multimedia :: Video',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
