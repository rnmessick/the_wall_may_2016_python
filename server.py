from flask import Flask, render_template, redirect, request
from connection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'the_wall')


@app.route('/', methods=["GET"])
def main():
    return render_template('login_registration.html')

@app.route('/login', methods=["POST"])
def login():
    # PROCESS LOGIN
    return redirect('/')

@app.route('/register', methods=["POST"])
def register():
    # PROCESS REGISTRATION
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)
