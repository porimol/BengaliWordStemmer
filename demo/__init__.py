# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

# Configurations
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    print("Error Message: {0}".format(error))
    return render_template('errors/404.html', response=error), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from demo.stemmer.bnstemmer import bnstemmer

# Register blueprint(s)
app.register_blueprint(bnstemmer)
