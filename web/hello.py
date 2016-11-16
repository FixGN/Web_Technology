#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

def application (environ, start_response):
    resp = ""

    d = parse_qs(environ['QUERY_STRING'])

    dlist = sorted(d.keys())
    for item in dlist:
        dlistlen = len(d[item])
        i = 0
        while i < dlistlen: 
            resp += item + "=" + "".join(d[item][i]) + "\n"
            i += 1

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(resp)))
    ]

    start_response(status, response_headers)
    return [resp]


