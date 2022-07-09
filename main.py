from pprint import pprint as print
from reddit import getPosts
from twitter import postTweet
import requests as re


def getFile(url):
  file_name = url.split("/")[-1]
  with open(file_name, "wb") as f:
    f.write(re.get(url).content)
    
  return file_name

for submission in getPosts("dankmemes", 10):
  status = f"""https://reddit.com{submission["permalink"]}
  #memes #dankmemes"""
  postTweet(status=status, file=getFile(submission["url"]))

#test