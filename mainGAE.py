import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'gae/lib'))

# Monkeypatch some youtube_dl functions that use features not available in GAE
import youtube_dl  # noqa: E402
# Modifying youtube_dl.utils.get_cachedir doesn't work
youtube_dl.extractor.youtube.get_cachedir = lambda *args, **kargs: None


from youtube_dl_server.app import app  # noqa: app is used by GAE
