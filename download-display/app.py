from flask import Flask, render_template	
app = Flask(__name__)

from google.cloud import firestore

# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()

users_ref = db.collection(u'downloads')
docs = users_ref.stream()

l = []
for doc in docs:
    l.append(doc.to_dict())

@app.route('/')
def hello_world():
    return render_template('downloads.html', users=l)