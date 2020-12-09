# SnapChatExpoer
This repository is my code for mass exporting data from Snapchat to Google Photos - and embedding photos' date information.

I used this code to successfully migrate my snapchat memories, 900+ of them, to google photos - and have their date information saved along with it.

Begin by going to https://accounts.snapchat.com/accounts/downloadmydata and requesting all of your snapchat data. It should arrive the same day.

Next mass download, using the javascript code: https://github.com/Wozzify/Snapchat-Memory-Downloader/blob/master/Snapchatdownloader.js credit to /Wozzify. You will need to use a browser that allows downloading multiple files, I had luck with firefox. Have all of these files downloaded to the same folder in your download directory.

Next, edit the directory information in the python code, and run that.  This will attach all of the image metadata to its date information.
This will allow it the photos to be stored in their appropriate date when you upload it to Google Photos.  The snapchat video memories already have date information attached.

Finally go to google photos and select all of the files and upload them all at once.
