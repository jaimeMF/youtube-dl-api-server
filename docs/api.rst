API
===

API methods
-----------

.. http:get:: /api/

    :status 301: redirects to :http:get:`/api/info`

.. http:get:: /api/info

    Get the video information

    :query url: The video url
    :resheader Content-Type: ``application/json``
    :resheader Access-Control-Allow-Origin: ``*``

    :status 200: On success
    :status 500: If the extraction fails

    |ex-request|

    .. sourcecode:: http

        GET /api/info?url=http://www.ted.com/talks/dan_dennett_on_our_consciousness.html HTTP/1.1

    **Example response**

    .. include:: example_info.rst.inc


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
