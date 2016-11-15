'''
Simple Python file to parse the database from kaggle and create some relevant
CSV files to use for training and testing. 

Kaggle link : https://www.kaggle.com/reddit/reddit-comments-may-2015/kernels
'''
import sqlite3
import pandas as pd


sql_conn = sqlite3.connect('database.sqlite')


df = pd.read_sql("SELECT score, body FROM May2015 WHERE LENGTH(body) > 5 AND LENGTH(body) < 100 AND subreddit='pics' AND body!='[deleted]' LIMIT 100000",sql_conn)

df.to_csv("100k_Pics_Comments.csv")

df2 = pd.read_sql("SELECT score, body from May2015 WHERE LENGTH(body) > 5 and LENGTH(body) < 100 AND subreddit='pics' AND ups> 100 LIMIT 100000",sql_conn)

df2.to_csv("100k_Pics_100upvotes.csv")

df3 = pd.read_sql("SELECT score, body from May2015 WHERE LENGTH(body) > 5 and LENGTH(body) < 100 AND subreddit='pics' AND score < 1 LIMIT 100000",sql_conn)

df3.to_csv("100k_Pics_10downvotes.csv")

df4 = pd.read_sql("SELECT score, body FROM May2015 WHERE LENGTH(body) > 5 AND LENGTH(body) < 100 AND subreddit='askreddit' AND ups > 100 LIMIT 10000",sql_conn)

df4.to_csv("100k_Askreddit_100upvotes.csv")

df5 = pd.read_sql("SELECT score, body from May2015 WHERE LENGTH(body) > 5 and LENGTH(body) < 100 AND subreddit='askreddit' AND score < 1 LIMIT 100000",sql_conn)

df5.to_csv("100k_Askreddit_10downvotes.csv")
