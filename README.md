# microservice-Tone-Analyzer-API
this project is a microservice that call tone analyzer API and retrive data
all functions and notebooks written in python 3.5
# dependcies 
* Flask 
* elasticsearch 
* pandas  
this project devided into 2 parts 
### 1- Hotel Review Tone Analyzer 
* I select 2000 English review (cause lite plan in Ibm tone analyzer just gives you 2500 free api call per month) then I extracted the Tones for each hotel using Tone analyzer API you will find code for this part in this notebook call-tone-analzer.ipynb
* then I grouped hotel reviews by name and get the normalized tones (aggregate by mean) for each hotel
this means every hotel has only one one document with all its data, including data obtained from Watson api.
and saved it to result.json file to use it later in eleastic search 

to run this project 
you have to insall elastic search server in your device on defult port; 9200
then insert all hotels data into elasticsearch server (indexing) you can see insert-to-elasticsearch.py file 
then I ceated flask api to serve those data from elasticsearch on port 3000
you can see code in flask_api.py file
