import webapp2
import logging
import traceback
import sys

#Format modules
import json
import yaml


class APIHandler(webapp2.RequestHandler):
    """The base handler for the API methods"""
    @property
    def out_format(self):
        """The format the response must use"""
        return self.request.get("format", "json")

    @property
    def content_type(self):
        """Content type for the response"""
        if self.out_format == "json":
            return "application/json"
        if self.out_format == "yaml":
            return "application/yaml"

    def dumps(self, dic):
        """Dump a dic to a string using the format specified in the request"""
        if self.out_format == "json":
            return json.dumps(dic)
        elif self.out_format == "yaml":
            return yaml.safe_dump(dic)

    def get(self):
        #Allow javascript get requests from other domains
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.headers["Content-Type"] = self.content_type

        dic = self.get_response()
        response = self.dumps(dic)

        self.response.out.write(response)

    def get_response(self):
        """Return the response as JSON serializable object (dict, tuple or list"""
        raise NotImplementedError("This method must be implemented by sublclasses")
