from flask import Flask, render_template, request

from models.section import Section

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    from os import listdir
    from os.path import isdir, join

    basepath = './static/js'
    sections = [Section(basepath[2:], section) for section in listdir(basepath) if isdir(join(basepath, section))]

    return render_template('home.jinja2', sections=sections)

@app.route('/workspace')
def workspace():
    name = request.args.get('name')
    return render_template('workspace.jinja2', name=name)