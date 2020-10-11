package io.localhank.wac;

import com.google.api.core.ApiFuture;
import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.DocumentReference;
// [START fs_include_dependencies]
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.FirestoreOptions;
// [END fs_include_dependencies]
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.cloud.firestore.QuerySnapshot;
import com.google.cloud.firestore.WriteResult;
import com.google.common.collect.ImmutableMap;


import org.apache.commons.io.FileUtils;

import java.net.URL;

import java.io.IOException;
import java.io.File;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.io.FileNotFoundException;
import java.io.FileInputStream;

import java.security.GeneralSecurityException;

import java.util.Map;
import java.util.HashMap;
import java.util.Collections;
import java.util.List;

	
public class App 
{
	private static final String username = "Bronny James";

    public static void main( String[] args ) throws Exception, IOException, GeneralSecurityException
    {

    	FirestoreOptions firestoreOptions =
	    	FirestoreOptions.getDefaultInstance().toBuilder()
	        .setProjectId("downloader-292200")
	        .setCredentials(GoogleCredentials.getApplicationDefault())
	        .build();

		Firestore db = firestoreOptions.getService();
		DocumentReference docRef = db.collection("downloads").document(username);
		// Add document data  with id "alovelace" using a hashmap
		Map<String, Object> data = new HashMap<>();
        
        long downloads = 0;
        while (true){
        	try {
	        	URL url = new URL("http://www.google.com");
	        	String fileName = "google_" + Long.toString(downloads) + ".html";
	            File destination = new File("dumpster/" + fileName);
	        	FileUtils.copyURLToFile(url, destination);
	        	System.out.println("Downloading " + Long.toString(downloads+1) + "/10 items");
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
	        downloads++;
	        System.out.println();

	        if (downloads % 10 == 0){
				data.put("user", username);
				data.put("downloads", downloads);
				//asynchronously write data
				ApiFuture<WriteResult> result = docRef.set(data);
				System.out.println("Update time : " + result.get().getUpdateTime());
				System.out.println("New dowload number is : " + Long.toString(downloads));
	        }
        }
    }
}
