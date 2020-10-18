# WACollections (Downloadr)

This project was originally called "WACollections", an interesting take on the Java Collections framework, but I decided to switch over to this project, Downloadr. It simply...downloads data, and shows much data you downloaded compared to others. More specifically, it will query google.com, download the front end assets on the search page, and save it to your local directory. Downloadr will record how many times you downloaded the google.com, well the front end assets, how big your total number of downloads, and display it on a very basic front end.

## Usage

### Download data app (Java)
This does the heavy work of downloading google.com. First, set up a GCP account, allow Firestore access, and store your credentials in this project's root folder. Then you can run:

'''
	# powershell cmds 
	$env:GOOGLE_APPLICATION_CREDENTIALS="[PATH_TO_PROJECT]/credentials.json"
	$env:GCLOUD_PROJECT="YOUR_PROJECT_NAME"	
	# end powershell cmds

	mvn install
	mvn exec:java
'''

### Front end (Flask)
Set up a virtualenv, activate it, and then run:
'''
	$env:FLASK_ENV="development" # this is a powershell cmd
	pip install -r requirements.txt
	flask run
'''


