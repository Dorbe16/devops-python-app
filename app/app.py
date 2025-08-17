from flask import Flask 
import redis
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379) 

@app.route('/') 
def index(): 
    count = r.incr('hits') 
    return f'Hello! This page has been viewed {count} times.' 

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8080)
