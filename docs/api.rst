API
===

API methods
-----------

.. http:get:: /api/

    .. deprecated:: 0.1
        Use :http:get:`/api/info` instead.

    :status 301: redirects to :http:get:`/api/info`

.. http:get:: /api/info

    Get the video information

    :query url: The video url
    :query boolean flatten: If ``True`` return a list of dictionaries in the ``videos`` field.
        Otherwise a single dictionary will be returned in the ``info`` field.

        .. warning:: This is ``True`` by default for compatibility reasons, it will be changed in a future version.
    :query \*: A whitelist of extra parameters are passed directly to the ``YoutubeDL`` object.
        Currently it supports: ``playliststart``, ``playlistend``, ``playlist_items``, ``matchtitle``, ``rejecttitle``.
        See the `youtube-dl documentation <https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L92>`_ for more info


    :resheader Content-Type: ``application/json``
    :resheader Access-Control-Allow-Origin: ``*``

    :status 200: On success
    :status 500: If the extraction fails

    |ex-request|

    .. sourcecode:: http

        GET /api/info?url=http://www.ted.com/talks/dan_dennett_on_our_consciousness.html&flatten=False HTTP/1.1

    **Example response**

    .. include:: example_info.rst.inc

    |ex-request|

    .. sourcecode:: http

        GET /api/info?url=http://www.ted.com/talks/dan_dennett_on_our_consciousness.html&flatten=True HTTP/1.1

    **Example response**

    .. include:: example_info_flatten.rst.inc


.. http:get:: /api/extractors

    Get the available extractors

    :resheader Content-Type: ``application/json``
    :resheader Access-Control-Allow-Origin: ``*``
    :status 200: On success

    |ex-request|

    .. sourcecode:: http

        GET /api/extractors HTTP/1.1

    |ex-response|

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Access-Control-Allow-Origin: *
        Content-Type: application/json

        {
            "extractors": [
                {
                    "name": "vimeo",
                    "working": true
                },
                {
                    "name": "TED",
                    "working": true
                },
                ...
            ]

        }

Test server
-----------

You can try the API by doing requests to ``http://youtube-dl.appspot.com``.



.. |ex-request| replace:: **Example request**


.. |ex-response| replace:: **Example response**
