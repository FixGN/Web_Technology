#!/usr/bin/env python

def app(env, start_response):
    data2 = env['QUERY_STRING'].split('&')
    data3 = b''
    for i in range(len(data2)):
        data2[i] = data2[i].encode('utf-8')
        data3 += data2[i]+b'\n' 
    print(data3)
    start_response('200 OK', [ ("Content-Type", "text/plain") ])#, ("Content-length", str(len(data3))) ])
    return [data3]
