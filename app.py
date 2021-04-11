import os 
import sys
import subprocess as sp
import fileinput
import configparser
#import psutil
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello, world!"
@app.route("/temp")
def new():
    temp = sp.getoutput('vcgencmd measure_temp')
    tempx=temp[5:9]+"°C"
    return tempx
