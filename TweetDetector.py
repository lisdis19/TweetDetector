"""
@author: Lisa DiSalvo
"""
from re import X
import sys
from tkinter import image_names 
sys.path.append('C:\Python39\Lib\site-packages')
import pandas as pd
import torch
import tweepy
import os
from datetime import datetime
import csv 
import nest_asyncio
import csv
import urllib.request 
nest_asyncio.apply()
import twint
import requests 
import PySimpleGUI as sg

#Basic Pre-req's needed to scrape twitter API
#Also, Our PySimpleGui Theme is initialized here 
consumer_key = "Ifi9mfwumswcxnFBhhmzRFL24"
consumer_secret = "JLbIBJUncsQ5vOYNBb6g6nCvzjadEgVRRUqyMitazmdt3VJCLx"
access_key = "1543238186343751683-vT1AUqXG9YGEZ3GZt8FP0kDpXtRuBw"
access_secret = "VaPh20PBYKLSV7j3rWQKU7YpmQV0Ft8vKzMghKX9fEhzj"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
sg.theme('LightBlue')  


def labelTextTweet():
#A simple function that calls upon our corpus to search
#The users selected CSV tweet post file to then extract and place those rows
#In another csv file called violentposts
    corpus = {"Covid-19", "COVID", "hate", "ew", "gross", "sick", 
        "disease", "sneeze", "cough",
        "pandemic", "epidemic","new","fear","toll",
        "spreading", "declare","infect","Wuhan","China",
        "COVID-19","impact","fight","patient","death",
        "concern","epidemic","strain","symptom",
        "spreading","scary","scared","shooting",
        "school shooting","2019-nCoV","infect",
        "deadly","outbreak","respiratory","quarantine",
        "virus","infect","nCov","SARS","PPE","disinfect",
        "isolation","self-isolation","lockdown","sanitizer",
        "sanitise","evacuee","distancing","impeachment",
        "airstrike","bombed","strikes","riot","crowds",
        "non-essential","corona","militia","evacuate","war","plague",
        "emergency","infection","deportation","swine","punishment",
        "nuisance","shoot","lowlife","drugs","cocaine","meth","marijuana",
        "fighting","fights","violent","violence","brutality","cruelty","bloodshed",
        "deport","wanker","beating","propganga","fake","clash","murder","foul play",
        "blood","attack","beating","jumped","rape","coercion",
        "assault","crimes","crime","mortality",
        "fatality","fatalities"}  # all your keywords
    df = pd.read_csv('C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master/scraped_posts.csv', sep=",")
    listMatchPosition = []
    for i in range(len(df.index)):
        if any(x in df['tweet'][i] for x in corpus):
            listMatchPosition.append(df['tweet'][i])
    output = pd.DataFrame({'tweet':listMatchPosition})
    output.to_csv("labeled_data.csv", index=False)
                

def labelImage():
#Function that uses violence-detection library to filter images
#In order for this to work, we must download images from CSV file 
#Specifically, download CSV twint image links, store in a local folder
#Then, place folder path as image variable
#Write a loop to iterate through each image in folder & label    
    #allfiles = os.listdir('C://Users//lisa//Desktop//searchImages//scraped_images.jpg')
    #Read in CSV file through DF   
    df = pd.read_csv ('C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master/scraped_images.csv')
    df["photos"] = df["photos"].str.split(",")
    df
    df = df.explode("photos")
    df
    df2 = pd.DataFrame(df)
    #Drop all rows but Photos row in search_images DF, save as new DF2 variable
    df3 = df2.loc[:, df2.columns.intersection(['photos'])] 
    x = df3.apply(lambda x: x.str.split(',').explode()).reset_index()
    x
    df4 = df3['photos'].str.replace(r'[][]', '', regex=True).str.strip("'")
    savefile = df4.to_csv('C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master/photoslinks.csv',index=False)
    savefile
    folder = "C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master"
    file_list = "C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master/image_{0}.jpg"
    errorCount=0
# CSV file must separate by commas
# urls.csv is set to your current working directory make sure your cd into or add the corresponding path
    with open ('C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master/photoslinks.csv') as images:
        images = csv.reader(images)
        next(images, None)
        img_count = 1
        print("Please Wait.. it will take some time")
        for image in images:
                try:
                    urllib.request.urlretrieve(image[0],
                    file_list.format(img_count))
                    img_count += 1
                except IOError:
                    errorCount+=1
                # Stop in case you reach 100 errors downloading images
                if errorCount>1000:
                    break
                else:
                    print("File does not exist")

    # Images
    img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
    folder_dir = 'C:/Users/lisa/OneDrive/Desktop/violenceDetector/yolov5-master/images'
    for images in os.listdir(folder_dir):
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom  # or file, Path, PIL, OpenCV, numpy, list
        results = model(images)
        results.print()
        results.show()
        results.xyxy[0]  # im predictions (tensor
      
def printtweetdata(n, ith_tweet):
#Function to print tweet scrape information to terminal
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Description:{ith_tweet[1]}")
        print(f"Location:{ith_tweet[2]}")
        print(f"Following Count:{ith_tweet[3]}")
        print(f"Follower Count:{ith_tweet[4]}")
        print(f"Total Tweets:{ith_tweet[5]}")
        print(f"Retweet Count:{ith_tweet[6]}")
        print(f"Tweet Text:{ith_tweet[7]}")
        print(f"Hashtags Used:{ith_tweet[8]}") 
        

def table_example():
#Function that showcases a chosen CSV file in table format
    filename = sg.popup_get_file('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        return
    if filename is not None:
        df = pd.read_csv(filename)
        data = df.values.tolist()
        header_list = list(df.columns)
        print(data)
    sg.set_options(element_padding=(0, 0))
    layout = [[sg.Table(values=data,
                            max_col_width=30,
                            headings=header_list,
                            justification='right',
                            # alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]


    window = sg.Window('Scraped Tweets', layout, grab_anywhere=False)
    event, values = window.read()

    window.close()
def scrape_images(hashtag_term,date_from,outfile):
#Function uses Twint to scrape Twitter for media links and other data
#We utilize Twint to scrape what we cant with API's and tweepy   
    c = twint.Config()
    c.Search = hashtag_term
    c.Limit = 200
    c.Since = date_from
    c.Images = True
    c.Store_csv = True
    c.Output = "./" + outfile
    twint.run.Search(c)

def scrape_posts(hashtag_term,date_from,outfile):
#Function uses Twint to scrape Twitter for media links and other data
#We utilize Twint to scrape what we cant with API's and tweepy   
    c = twint.Config()
    c.Search = hashtag_term
    c.Limit = 200
    c.Since = date_from
    c.Store_csv = True
    c.Output = "./" + outfile
    twint.run.Search(c)
    

# The Layout for our GUI, filled with text fields and buttons
font = ("Arial", 13)
layout = [
    [sg.Text('TweetDetector: Scrape, Analyze and Label Tweets.', font = font),sg.Push()],
    [sg.Text('To Scrape Twitter: Please enter your desired search tag & date')],
    [sg.Text('Enter Hashtag', size =(15, 1)), sg.Push(), sg.InputText(key = 'words')],
    [sg.Text('Date in yyyy-mm--dd', size =(15, 1)), sg.Push(), sg.InputText(key = 'date_since')],
    [sg.Submit('Scrape Posts'),sg.Submit('Scrape Images'),sg.Push(),sg.Submit('Show Output CSV Files'),sg.Cancel()],
    [sg.Text('To Detect According to your Hashtag and Corpus, Select Below.'),sg.Push(),],
    [sg.Text('Select a pre-existing file of scraped tweets.'),sg.Push(),],
    [sg.Text('The scraped tweets will then be exported into a new CSV file'),sg.Push(),],
    [sg.Submit('Detect Corpus'),sg.Submit('Detect Images'),sg.Push(),],
]

window = sg.Window('ViolenceDetector', layout, size=(500, 260))

event, values = window.read()

#The values we need to run functions that call for parameters
words = values['words']
date_since = values['date_since']
numtweet = 100


#The event handler to run functions upon pressing buttons in the GUI
if event == 'Scrape Posts':
    scrape_posts(words,date_since,'scraped_posts.csv')
    sg.Popup('Done! File name: scraped_tweets.csv', keep_on_top=True)
elif event == 'Show Output CSV Files':
    table_example()
    window.loop()
elif event == 'Scrape Images':
    scrape_images(words,date_since,'scraped_images.csv')
    sg.Popup('Done! File name: scraped_images.csv', keep_on_top=True)
elif event == 'Detect Violent Posts':
    labelTextTweet()
elif event == 'Detect Violent Images':
    labelImage()
#A flag to showcase that the program has reached the end    
print('End of File')
window.close()
