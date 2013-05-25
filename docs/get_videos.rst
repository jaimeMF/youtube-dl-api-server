Get videos
##########

Basic usage
***********

To call the API just do a GET request to ``/api/?url=the_url``

Parameters
**********

``url``
=======
The url of the page you want the videos from.


``format``
==========

The format you want the response in.
Now, two values are supported:

* json: Default format
* yaml

Response
********

The response is a dictionary with the following key/value pairs:

* ``youtube-dl.version``: The youtube-dl version the server is running.
* ``url``:
* ``videos``:

Errors
******

If an error in youtube-dl happened during the execution of the request,
the response is just a dictionary with a key ``error`` which value is just the
description of the error.
