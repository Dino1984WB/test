#william bukowski
from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask import render_template

#init flask application
app=Flask(__name__, static_folder='static/', static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def search(): #function to search db for name entered
    
    return render_template("home.html")


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8000, debug=True) #run app