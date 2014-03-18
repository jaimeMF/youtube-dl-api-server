youtube-dl-api-server Changelog
===============================

Version 0.1
-----------
(in development)

- The endpoint for getting the video information is now ``/api/info``.
  ``/api/`` redirects now to it, but it's deprecated and will be removed in a future version.
- The server can be run now with ``python -m youtube_dl_server``.
- Added ``flatten`` option to ``/api/info`` to select between a single dictionary result or a list of videos, it's ``True`` by default.
