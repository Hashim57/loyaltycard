import pandas as pd
import numpy as np
from clock import datetime
import mysql
import mysql.connector
import pymysql
from math import sqrt
import matplotlib.pyplot as plt



people = pd.read_csv('users.csv')

recommendations = pd.read_csv("recommendations.csv")

print(recommendations)

prefs = pd.read_csv("ratings.csv")

mydb = mysql.connector.connect(
    host ="localhost", user ="root", password= "insecure",  database= "InfinityCafe", port= "33066")

cursor = mydb.cursor()

while (True):
    name = input("Sign up now! Enter Users name")

    if name == "quit":
        exit()
    age = input ("Enter users age")
    Gender = input("enter users gender")
    password =input("Choose a password")

    sql = "INSERT INTO Users (name, password, age, Gender) VALUES (%s, %s, %s, %s)"
    vals = (name, password, age, Gender)
    cursor.execute(sql, vals)
    mydb.commit()
        
    print("Data saved to the database")






recommendations_df = pd.read_csv("recommendations.csv")

recommendations_df.head()




# metadata = pd.read_csv('people.csv', low_memory=False)

# features = ['names' ,'drinks', 'prefs' ]

# df = pd.DataFrame(np.random.randn(10, 3), index= names, columns=[features])


# def get_list(x):
#     if isinstance(x, list):
#         names = [i['name'] for i in x]
        
#         if len(names) > 3:
#             names = names[:3]
#         return names

    
#     return []



# features = ['names' ,'drinks', 'prefs' ]

# for feature in features:
#     metadata[feature] = metadata[feature].apply(get_list)


# features = ['names' ,'drinks', 'prefs' ]

# for feature in features:
#     metadata[feature] = metadata[feature].apply(literal_eval)

# def clean_data(x):
#     if isinstance(x, list):
#         return [str.lower(i.replace(" ", "")) for i in x]
#     else:
#         #Check if director exists. If not, return empty string
#         if isinstance(x, str):
#             return str.lower(x.replace(" ", ""))
#         else:
#             return ''
# features = ['Name of person' ,'name of drink', 'chosen prefs' ]

# for feature in features:
#     metadata[feature] = metadata[feature].apply(clean_data)


# metadata[['names', 'drinks', 'prefs']].head(3)




