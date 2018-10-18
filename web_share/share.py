    #!/usr/bin/python3

"""
    web_share - A Simple Flask App to Share Files Over the Network

    This is a simple flask app that runs on port 0.0.0.0 and which serves a
    specific folder to share files from the host to the client browser or upload
    to host from a client browser. 

"""
from __future__ import print_function
import os
import sys

from flask import Flask, render_template, send_file, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index(query_url=None):
    currentpath = os.getcwd()
    if query_url:
        currentpath = query_url

    _listdir = os.listdir(currentpath)
    isdir = os.path.isdir
    dirlist = {x: isdir(currentpath + '/' + x) for x in _listdir}
    # Sorting the dictionary by values, if folder
    # dirlist = {x:y for x,y in sorted(dirlist.items())}
    
    # Handling File Uplaods
    if request.method == 'POST':
        f = request.files['myfile']
        filename = f.filename.replace(' ','_')
        f.save(currentpath + '/' + filename)
        message = "File Uploaded Successfully"
    else:
        message = None

    return render_template('index.html',
                            dirlist=dirlist,
                            currentpath=currentpath,
                            message=message)


@app.route('/<path:query_url>', methods=['POST', 'GET'])
def query_handler(query_url):
    message = None

    if not query_url.startswith('/'):
        query_url = '/' + query_url 

    # Saving the file in the current Directory
    if request.method == 'POST':
        f = request.files['myfile']
        filename = f.filename.replace(' ','_')
        f.save(query_url + '/' + filename)
        message = 'File Uploaded Successfully'

        # Listing directory
        _listdir = os.listdir(query_url)
        isdir = os.path.isdir
        dirlist = {x: isdir(currentpath + '/' + x) for x in _listdir}

        return render_template('index.html',
                                dirlist = dirlist,
                                currentpath=query_url,
                                message=message)

    else:
        if os.path.isfile(query_url):
            return send_file(query_url)

        elif os.path.isdir(query_url):
            return index(query_url)

        else:
            return 'File is not found or Doesnt \
                    have enough permission to access \
                    at: ' + query_url