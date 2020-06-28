import json 
import pandas as pd 
import numpy as np
#Open the text file and load json
with open('nyt_jun.txt') as json_file:
    data=json.load(json_file)
    #Create dataframe with coulmns for the data that will be extracted from the json 
    df=pd.DataFrame(columns=['abstract','pub_date','type_of_material','word_count','print_page','headline','section_name','subsection_name'])
    idx=0
    #Accessing the right keys from the nested dictionary  
    for p in data['response']['docs']:
        #try and except block is used to avoid exceptions for missing values 
        try:
            df.loc[idx,'subsection_name']=p["subsection_name"]    
        except: 
            pass
        try:
            df.loc[idx,'print_page']=p["print_page"]    
        except: 
            pass
        try:
            df.loc[idx,'type_of_material']=p["type_of_material"]    
        except: 
            pass
        #The below keys didn't need the try and except block as they were always present
        df.loc[idx,'abstract']=p["abstract"]
        df.loc[idx,'pub_date']=p["pub_date"]
        df.loc[idx,'word_count']=p["word_count"]
        df.loc[idx,'headline']=p["headline"]["main"]
        df.loc[idx,'section_name']=p["section_name"]
        idx+=1
#Write dataframe into csv
print(df.columns)
df.to_csv("../news_jun.csv",index=False)