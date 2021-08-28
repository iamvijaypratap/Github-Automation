from typing import Type
from flask import Flask,redirect,url_for,render_template,request , json
from flask_ngrok import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def home():
    return "Welcome Guys"
@app.route('/github', methods=['POST'])
def get_response():
    if request.headers['Content-Type']=='application/json':
        info = json.dumps(request.json)
        print(info)
        return info

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run()