.. sourcecode:: http

    HTTP/1.1 200 OK
    Access-Control-Allow-Origin: *
    Content-Type: application/json

    {
      "info": {
        "description": "Philosopher Dan Dennett makes a compelling argument that not only don't we understand our own consciousness, but that half the time our brains are actively fooling us.",
        "display_id": "102",
        "ext": "mp4",
        "extractor": "TED",
        "extractor_key": "TED",
        "format": "high",
        "format_id": "high",
        "formats": [
          {
            "ext": "mp4",
            "format": "low",
            "format_id": "low",
            "preference": 1,
            "url": "..."
          },
          {
            "ext": "mp4",
            "format": "medium",
            "format_id": "medium",
            "preference": 2,
            "url": "...",
          },
          {
            "ext": "mp4",
            "format": "high",
            "format_id": "high",
            "preference": 3,
            "url": "..."
          }
        ],
        "id": "102",
        "playlist": null,
        "playlist_index": null,
        "preference": 3,
        "subtitles": null,
        "thumbnail": "http://images.ted.com/images/ted/488_480x360.jpg",
        "title": "The illusion of consciousness",
        "uploader": "Dan Dennett",
        "url": "...",
        "webpage_url": "http://www.ted.com/talks/dan_dennett_on_our_consciousness.html",
        "webpage_url_basename": "dan_dennett_on_our_consciousness.html"
      },
      "url": "http://www.ted.com/talks/dan_dennett_on_our_consciousness.html",
    }
