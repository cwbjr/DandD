from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit
import utils
import json

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.secret_key = utils.secretkey
app.debug = True
socketio = SocketIO(app)

#-------------------HOME PAGE------------
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")
#---------------------END HOME PAGE----------

#---------------GAME MASTER METHODS----------------
@app.route('/games', methods=['GET', "POST"])# Page for viewing the list of all of your games
def games():
    if request.method == "GET":
        if 'user' in session and session['user']:
            games = utils.getGames(session['user'])
            games = json.dumps(games)
            return render_template("games.html", games = games)
        else:
            return redirect("/login/redirect")
    elif request.method == "POST":
        user = request.form['user']
        return json.dumps(utils.getGames(user))

@app.route('/getgame')
@app.route('/getgame/<id>')
def getgame(id=0):
    if 'user' in session and session['user']:
        if id == 0:
            return json.dumps(utils.getGames(session['user']))
        else:
            return json.dumps(utils.getGame(id))
    else:
        return json.dumps(utils.getGame(id))

@app.route('/creategame', methods=['GET','POST'])
def creategame():
    if request.method == "POST":
        form = request.form.copy().to_dict()
        form['user'] = session['user']
        print form
        return utils.creategame(form)
    else:
        return redirect("/games")


@app.route("/gameinfo")
@app.route("/gameinfo/<id>", methods=["GET", "POST"]) #The page where you can view the details  a game
def gameinfo(id=0):
    if id == 0:
        return redirect("/games")
    if request.method == "GET": # So people can only access it while logged in
        if 'user' in session and session['user']:
            return render_template("gameinfo.html")
        else:
            return redirect("/login/redirect")
    else:
        form = request.form.copy().to_dict()
        form['id'] = int(form['id'])
        return str(utils.updateGame(int(id), form))
#----------------END GAME MASTER METHODS---------------

#------------CHARACTER PAGE METHODS--------------------
@app.route("/characters", methods=['GET', 'POST'])
def characters():
    if request.method == 'GET':
        if 'user' in session and session['user']:
            return render_template("character.html")
        else:
            return redirect("/login/redirect")
    else:
        form = request.form.copy().to_dict()
        form['user'] = session['user']
        answer = utils.createChar(form)
        return str(answer)

@app.route("/getchars", methods=["GET"])
def getchars():
    if request.method == "GET":
        if 'user' in session and session['user']:
            names = json.dumps(utils.getChars(session['user']))
            return names
        else:
            return ""

@app.route("/charinfo")
@app.route("/charinfo/<id>", methods=["GET", "POST"])
def charinfo(id=0):
    if id == 0:
        return redirect("/characters")
    if request.method == "GET":
        if 'user' in session and session['user']:
            return render_template("charinfo.html")
        else:
            return redirect("/login/redirect")
    else:
        print id
        char = utils.getChar(id)
        if char:
            char.pop('_id')
            print char
            return json.dumps(char)
        else:
            return  ""
#-------------END CHARACTER METHODS-----------------


#---------------LOGIN Methods REGISTER + LOGOUT------------------------------
@app.route("/login", methods=["GET", "POST"])
@app.route("/login/<r>")
def login(r=None):
    if request.method == "GET": # What people see when they click "Login"
        if 'user' in session and session['user']:
            return redirect("/home")
        return render_template("login.html", r=r)
    else:
        form = request.form
        username = form['username'] or ""
        password = form['password'] or ""
        if utils.auth(username, password):
            session['user'] = username
            return 'success'
        return 'fail'

@app.route("/register", methods=["GET", "POST"]) # ----REGISTER-------
def register():
    if request.method == "GET": # What people see when they click "Login"
        if 'user' in session and session['user']:
            print session['user']
            return redirect("/home")
        return render_template("register.html")
    else:
        form = request.form.copy().to_dict()
        username = form['username'] or ""
        password = form['password'] or ""
        confmpwd = form['confmpwd'] or ""
        if utils.register(username, password, confmpwd):
            session['user'] = username
            return 'success'
        return 'fail'

@app.route("/editaccount", methods=['GET', 'POST'])
def editaccount():
    if request.method == 'GET':
        if 'user' in session and session['user']:
            return render_template("editaccount.html")
        else:
            return redirect("/login/redirect")
    else:
        form = request.form.copy().to_dict()
        username = session['user']
        newusername = form['newUsername'] or ""
        newpassword = form['newPassword'] or ""
        oldpassword = form['oldPassword']

        if form['newUsername'] and form['newPassword']:
            if utils.update_user(username,newusername,oldpassword):
                if utils.update_pw(newusername,oldpassword,newpassword):
                    return 'bothSuccess'
            return 'fail'

        if form['newUsername']:
            if utils.update_user(username,newusername,oldpassword):
                return 'userSucess'
            return 'fail'

        if form['newPassword']:
            if utils.update_pw(username,oldpassword,newpassword):
                return 'pwSuccess'
            return 'fail'
        return 'fail'

@app.route("/logout")#---------------------------LOGOUT--------------
def logout():
    session['user'] = None
    return redirect('/login')
#-----------------END LOGIN METHODS----------------------------------

#------------------------------SOCKET METHODS FOR GAMEINFO-----------------
@socketio.on('connected')
def connected(packet):
    print packet['data']

@socketio.on('clicked!!!')
def clicked(packet):
    print packet['data'], "\n"
    pass

@socketio.on('changed!')
def changed(packet):
    emit('changed',room = packet[id])
#------------------------------- END SOCKET METHODS-----------------------


#-----------RUN--------------
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000)
