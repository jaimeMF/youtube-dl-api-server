youtube-dl-web
==============

youtube-dl rest api

###How to use it

Just do a GET request to `http://youtube-dl.appspot.com/api/?url=the_video_url`

You'll get a json file like this:

```
{"url": "http://store.steampowered.com/video/105600/",
 "ie": "Steam", 
 "youtube-dl.version": "2013.02.19",
  "videos": [
  			{"url": "http://media2.steampowered.com/steam/apps/81300/movie940.flv?t=1322762847", "ext": "flv", "id": "81300", "title": "Terraria 1.1 Trailer"}, 
  			{"url": "http://media2.steampowered.com/steam/apps/80859/movie940.flv?t=1306276243", "ext": "flv", "id": "80859", "title": "Terraria Trailer"}]}
```

Then you can use each url for downloading the video.

###Try it
You can use a web interface on: [youtube-dl-web](http://jaimemf.github.com/youtube-dl-web/)
