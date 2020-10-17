from flask import Flask, render_template	
app = Flask(__name__)
import datetime
import threading
from time import sleep

from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client() 

#users_ref = db.collection(u'downloads')
# docs = users_ref.stream()

# l = []
# for doc in docs:
#     l.append(doc.to_dict())

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.user}')
    callback_done.set()
users_ref = db.collection(u'downloads')

doc_watch = users_ref.on_snapshot(on_snapshot)

# @app.route('/')
# def hello_world():
#     return render_template('downloads.html', users=l)