from .APIresponder import Api
from .Extractors import ListExtractors

url_map = [('/api/', Api),
           ('/api/list_extactors', ListExtractors)]
