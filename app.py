import os
from flask import Flask, render_template, jsonify, redirect
from bson.objectid import ObjectId
import ML_scott.py

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('find_dog'):
    return {'dog_breed':dog_breed},
           {'dog_jpg':dog_jpg}

if __name__ == "__main__":
	app.run(debug = False)
