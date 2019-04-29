import os

from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return url_for('show_user_profile', username = 'richard')

#método GET e POST (botão para submitt) POST tem mais segurança por não aparece o q foi digitado na url
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'username is ' + str(request.values["username"])
    else: 
        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submitt">Submit</button></form>'

@app.route('/username/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return "User %s visited" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the give id, the id must be an integeger
    return "Post %d" % post_id

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    app.debug = True
    app.run(host = host, port = port)
