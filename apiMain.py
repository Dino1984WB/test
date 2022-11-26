#william bukowski
from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
from flask import render_template

#init flask application
app=Flask(__name__, static_folder='static/', static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def renderhome(): #function to search db for name entered

    return render_template("home.html")


@app.route('/data', methods =['GET', 'POST'])
def data():
    queryName=""
    if request.method == 'POST':
            queryName = request.get_json() #this needs to grab the json and convert to string

    print(queryName)


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8000, debug=True) #run apps