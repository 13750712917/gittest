#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import urllib.parse


class Request(object):
    def __init__(self):
        self.path = ''

        self.query = {}
        self.method = 'GET'
        self.body = ''
    def form(self):
        body = urllib.parse.unquote(self.body)
        log('body 是', body)
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f

class Message(object):
    def __init__(self):
        self.message = ''
        self.author = ''

    def __repr__(self):
        return '{}: {}'.format(self.author, self.message)

request = Request()
message_list = []

def template(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def route_index():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello world</h1>'
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')

def route_shine():
    header = 'HTTP/1.1 200 NOT OK\r\nContent-Type: text/html\r\n'
    body = '<h1>200</h1><img src="img/shine.gif"/>'
    r = header + '\r\n' +body
    return r.encode(encoding='utf-8')

def route_image_shine():
    with open('img/shine.gif', 'rb') as f:
        header = b'HTTP/1.1 200 NOT OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img
def route_message():
    if request.method == 'POST':
        msg = Message()
        form = request.form()
        msg.author = form.get('author', '')
        msg.message = form.get('message', '')
        message_list.append(msg)

    header = 'HTTP/1.1 200 VERY OK\r\nContent-Type: text/html\r\n'
    body = template('message.html')
    msgs = '<br>'.join([str(m) for m in message_list])
    body = body.replace('{{message}}', msgs)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')

def error(code=404):
    error_dict = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n<h1>404 NOT FOUND</h1>'
    }
    return error_dict.get(code, b'')

def log(*args, **kwargs):
    print(args, kwargs)


def parsed_path(path):
    index = path.find('?')
    if index == -1:
        return path, {}
    else:
        path, query_s = path.split('?', 1)
        args = query_s.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query


def response_for_path(path):
    path, query = parsed_path(path)
    request.path = path
    request.query = query
    log('path and query', path, query)
    r = {
        '/': route_index,
        '/shine': route_shine,
        '/img/shine.gif': route_image_shine,
        '/message': route_message,
    }
    response = r.get(path, error)
    return response()


def run(host='', port=3000):
    with socket.socket() as s:
        s.bind((host, port))
        while True:
            s.listen(5)
            conn, add = s.accept()
            print(add)
            r = conn.recv(1024)
            r = r.decode('utf-8')
            try:
                request.method = r.split()[0]
                request.body = r.split('\r\n\r\n')[1]
                path = r.split()[1]
                response = response_for_path(path)
                conn.sendall(response)
            except Exception as e:
                log('error', e)
            conn.close()
run('', 3000)