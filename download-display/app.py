from flask import Flask, render_template, jsonify
app = Flask(__name__)
import datetime
import threading
from time import sleep

from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client() 
users_ref = db.collection(u'downloads').document('Bronny James').get()
print(users_ref.to_dict())

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
def hello_world():
    users_ref = db.collection(u'downloads').document('Bronny James').get()
    return jsonify(users_ref.to_dict())

@app.route('/')
def downloads():
    return render_template('layouts/downloads.html', users=None)
