#### Install the the modules through pip command in the bash terminal#### 
import pandas as pd 
import json
import bs4 
import sqlalchemy
import image
import requests 
import pydub
import re
import openpyxl 
# importing modules intstalled from pyenv into the python terminal (making sure its the right version 3.8.0) #
tab1 = pd.read_excel('Data/assigment1.xlsx')  # name is set to "tab1" for the first sheet, excuting command for pd first tab
tab2 = pd.read_excel('Data/assigment1.xlsx', sheet_name= 1) # name is set to "tab2" for second sheet however, sheet_name was required on top of the orginal code to access second sheet
tab1
tab2
# "tab1" and "tab2" will now show the different sheets pages respectivly
