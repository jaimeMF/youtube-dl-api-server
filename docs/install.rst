Install the server
##################

How to install **youtube-dl-api-server**

Using pip
*********
Just run :command:`pip install --pre youtube_dl_server`.

Then you can start using the server with :program:`youtube-dl-server`.

From source
***********
Download the source code and install the dependecies with :command:`pip install -r requirements.txt`.
Then just run :command:`python -m youtube_dl_server`

Alternatively you can use pip to install it, run :command:`pip install -e .` and then you'll be able to run :program:`youtube-dl-server` (you won't need to rerun the pip command if you do some changes).


App Engine
**********

You can setup an app in the `Google App Engine <https://developers.google.com/appengine/>`_ 
by changing the ``application`` key in app.yaml to your application name. 
For using it you just need to do the API calls to :samp:`http://{your-app-name}.appspot.com`.
It needs some external python modules in :samp:`lib`, you can download them by running :command:`./devscripts/setup-gae.sh`

Heroku
******
You can also run the server on `Heroku <https://heroku.com>`_ by adding ``gunicorn`` to ``requirements.txt``
and creating a ``Procfile`` with ``web: gunicorn --pythonpath youtube_dl_server app:app -w 4 --log-file -``.

Commit, push to Heroku and you can make your API calls to :samp:`https://{app-name}.herokuapp.com/`.
