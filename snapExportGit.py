#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:04:51 2020

@author: dely
"""


from bs4 import BeautifulSoup as soup
import piexif
import os 
import datetime

# generates a list of each download's date data
with open('/html/file/containing/snapchat/data.html', 'r') as page_html:
    page_soup = soup(page_html.read(), "html.parser")
    downloadList = page_soup.findAll('tr')
    del downloadList[0]
    i = 0
    dateList = []
    for dl in range(len(downloadList)):
        tagList = downloadList[dl].findAll('td')
        dateList.append(str(tagList[0])[4:23])
        i+=1

# this code organizes a directory by first modified, then renames it from '0' to 'len(directory)'
# for example the first snapchat downloaded will be 0.jpg, second one downloaded will be 1.jpg, etc
# this allows you to edit date information without affecting the order they appear
target = r'/folder/containing/all/snapchat/memories'
os.chdir(target)
allFiles = os.listdir(target)
allFiles.sort(key = lambda x: os.path.getmtime(x))
i = 0 
for file in allFiles:
    t = os.path.getmtime(file)
    v = datetime.datetime.fromtimestamp(t)
    x = v.strftime('%Y %m %d %s')
    print(x, end = ' ')
    fileName, ext = os.path.splitext(file)
    os.rename(file, str(i) + ext)
    i+=1

# this code will iterate through each photo in the directory and add its date's metadata
target = r'/folder/containing/all/snapchat/memories'
os.chdir(target)
allFiles = os.listdir(target)
#order by 0 to greatest int file name
allFiles.sort(key = lambda x: int(os.path.splitext(x)[0]))
i = 0 
j = 0
for file in allFiles:
    if os.path.splitext(file)[1] == '.jpg':      
        newExifDate = dateList[i]
        exif_dict = piexif.load(file)
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal]=bytes(newExifDate, 'utf-8')
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes,file)
        print('complete')
    i+=1




 