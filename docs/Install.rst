Install the server
##################

How to install **youtube-dl-api-server**

Using pip
*********
Just run :command:`pip install youtube_dl_server`.

Then you can start using the server with :program:`youtube-dl-server`.

From source
***********
Download the source code and install the dependecies with :command:`pip install -r requirements.txt`.
Then just run :command:`python -m youtube_dl_server`


App Engine
**********

You can setup an app in the `Google App Engine <https://developers.google.com/appengine/>`_ 
by changing the ``application`` key in app.yaml to your application name. 
For using it you just need to do the API calls to :samp:`http://{your-app-name}.appspot.com`.
