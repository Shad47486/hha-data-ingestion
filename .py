#Prereq#
#### Install the the modules through pip command in the bash/powersell terminal#### 
import pandas as pd 
import json
import bs4 
import sqlalchemy
import image
import requests 
import pydub
import re
import openpyxl 
import db_dtypes
from google.cloud import bigquery
# Importing modules intstalled from pyenv into the python terminal (making sure its the right version 3.8.0) #


#Section 1: seeing datasets of two different tabs  
tab1 = pd.read_excel("C:/Users/Shad/.pyenv/PProjects/hha-data-ingestion/Data/assigment1.xlsx")  # Name is set to "tab1" for the first sheet, excuting command for pd first tab and change file direction to directory of downloaded file
tab2 = pd.read_excel('C:/Users/Shad/.pyenv/PProjects/hha-data-ingestion/Data/assigment1.xlsx', sheet_name= 1) # Name is set to "tab2" for second sheet however, sheet_name was required on top of the orginal code to access second sheet
############# trouble with using relative file instead of the whole pathway ##############
tab1
tab2
# Typing "tab1" and "tab2" will now show the different sheets pages respectivly 


#Section 2: trying to get dataset from an api 

data = requests.get('https://data.cms.gov/data-api/v1/dataset/60ccbf1c-d3f5-4354-86a3-465711d81c5a/data') #command allows data to be aquired via api from the website 
data = data.json() 
data #allows data to be seen with its categories

#Section 3: 

gcp_project= 'reshad-507' #identifies the project folder
bq_dataset = 'reshad-507.covid_19_genome_sequence_dataset' #the data set and var name to give as 'bq_dataset'
bq_dataset1 = 'reshad-507.rxrx19' 
client = bigquery.Client(project=gcp_project) 
dataset_ref = client.dataset(bq_dataset, bq_dataset1) #refrenceing the datset that will be used for the bq

def gcp2df(sql) :
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe() #lines 40-43 define the use of sql and defininging the resutlts and where the query would return to I THINK

query = """SELECT * FROM 
`reshad-507.covid_19_genome_sequence_dataset.metadata` 
LIMIT 100"""
query2 = """SELECT * FROM 
`reshad-507.rxrx19.rxrx19a_metadata` 
LIMIT 100"""
#querys of what of all the the columns but only the first 100 from the datasets

bigquery1 = gcp2df(query)
bigquery1

bigquery2 = gcp2df(query2)
bigquery2
#deinfed the name of the dataset to bigquery1 and bigquery 2 and writing only the variable name results in the 