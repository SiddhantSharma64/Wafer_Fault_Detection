from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource identifier
uri = "mongodb+srv://siddhantsharmajsr301:Siddhantsharmajsr301@cluster0.aluhfvi.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="siddhant"
COLLECTION_NAME="waferfault"

# read the data a dataframe
df=pd.read_csv(r"D:\PROGRAMMING\Data Science\Projects\Wafer_fault_detection\notebooks\wafer.csv")
df=df.drop("Unnamed: 0",axis=1)

# convert data into json 
json_record=list(json.loads(df.T.to_json()).values())

# now dump the data into the database 
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)