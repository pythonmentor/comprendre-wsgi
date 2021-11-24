from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

routes = {}


def route(path):
    def inner(fct):
        routes[path] = fct
        return fct

    return inner


@route("/hello/")
def hello(environ=None, query_string=None):
    data = environ["wsgi.input"].read()
    return str(parse_qs(data.decode("utf8")))


@route("/adios/")
def goodbye(environ=None, query_string=None):
    return "Bonjour depuis goodbye"


def application(environ, start_response):
    view = routes.get(environ["PATH_INFO"])
    if view is not None:
        response_body = view(
            environ=environ, query_string=parse_qs(environ["QUERY_STRING"])
        ).encode("latin1")

        response_status = "200 OK"

        response_headers = [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(response_body))),
        ]
    else:
        response_body = "Page pas trouvée".encode("latin1")
        response_status = "404 Not Found"
        response_headers = [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(response_body))),
        ]

    start_response(response_status, response_headers)
    return [response_body]
