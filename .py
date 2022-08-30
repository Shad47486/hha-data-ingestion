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
# Importing modules intstalled from pyenv into the python terminal (making sure its the right version 3.8.0) #
#Section 1: 
tab1 = pd.read_excel('Data/assigment1.xlsx')  # Name is set to "tab1" for the first sheet, excuting command for pd first tab
tab2 = pd.read_excel('Data/assigment1.xlsx', sheet_name= 1) # Name is set to "tab2" for second sheet however, sheet_name was required on top of the orginal code to access second sheet
tab1
tab2
# Typing "tab1" and "tab2" will now show the different sheets pages respectivly 
#Section 2:
data = requests.get('https://data.cms.gov/data-api/v1/dataset/60ccbf1c-d3f5-4354-86a3-465711d81c5a/data') #command allows data to be aquired via api from the website 
data = data.json() 
data #allows data to be seen with its categories

