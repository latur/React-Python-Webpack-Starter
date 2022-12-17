# -*- coding: utf-8 -*-
import os, sys
import arg
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_url_path='', static_folder='build')
opt = arg.parse({
  '-p': [9400, 'Server port', lambda x: int(x)],
})


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/api/test', methods=['GET','POST'])
def api_test():
    return jsonify({'result': True})


@app.route('/<path>/<any>')
def all(path, any):
    return root()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=opt['-p'])
