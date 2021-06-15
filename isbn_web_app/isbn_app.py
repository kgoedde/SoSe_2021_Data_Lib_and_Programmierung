# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:50:40 2021

@author: Katja
"""

from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/") # Decorator
def start_page():
    return "<p>Hello World! Hope you are good!!!<p>"