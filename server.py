from bottle import get, post, request, run, static_file


@post('/api/rcon')
def run_rcon():
    print("Running command: ", request.json)
    ret = {
        'Status': 'OK'
    }
    return ret


@get('/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='www')


@get('/')
def serve_index():
    return static_file("index.html", root='www')


run(host='localhost', port=8080)
