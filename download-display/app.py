from flask import Flask, render_template, jsonify
app = Flask(__name__)
import datetime
import threading
from time import sleep

from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client() 

callback_done = threading.Event()

def get_downloads():
    while False:
        print("listening to doc updates")
        def on_snapshot(col_snapshot, changes, read_time):
            for doc in col_snapshot:
                user_dict = doc.to_dict()
                temp = user_dict['user']
                print(f'Received document snapshot: {temp}')
            callback_done.set()
        col_query = db.collection(u'downloads')
        query_watch = col_query.on_snapshot(on_snapshot)
        sleep(1)

@app.route('/_downloads')
def downloads():
    data = []
    users_ref = db.collection(u'downloads').stream()
    for user in users_ref:
        data.append(user.to_dict())
    print(data)
    return jsonify(data)

@app.route('/')
def hello_world():
    data = []
    users_ref = db.collection(u'downloads').stream()
    for user in users_ref:
        data.append(user.to_dict())
    user_downloads= len(data)
    return render_template('layouts/downloads.html', user_downloads=user_downloads)
