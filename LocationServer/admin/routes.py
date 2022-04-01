from flask import render_template, url_for, request
from admin import app

@app.route('/home')
def main():
    return render_template("index.html")


