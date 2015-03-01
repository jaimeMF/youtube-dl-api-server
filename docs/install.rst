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

You can also run the server on `Heroku <https://heroku.com>`_, you just need to `setup and deploy the app <https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app>`_ and you can make your API calls to :samp:`https://{app-name}.herokuapp.com/`.
