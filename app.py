import time
import math
import redis
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def hex2binary(number):
    retries = 5
    while True:
        try:
            binary = cache.get(number)
            if binary == None:
                binary = f"{int(number, 16):b}" 
                cache.set(number, binary)
            return binary

        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('index.html', count=count)


@app.route('/h2b/<number>')
def display_binary(number):
    binary = hex2binary(number)
    return render_template('value.html', value=binary)
