from youtube_dl import gen_extractors

from APIHandler import APIHandler


def dict_for_IE(ie):
            return {'name': ie.IE_NAME,
                    'working': ie.working(),
                    }


class ListExtractors(APIHandler):
    def get_response(self):
        return [dict_for_IE(ie) for ie in gen_extractors()]
