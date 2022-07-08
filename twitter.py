import tweepy

def postTweet(status="", file=None):
#post tweet to twitter. 
#no text in tweet body if no status specified.
#if no file specified, post only text.
#file and/or text must be specified.
#possible values for file_type:
#tweet_gif, tweet_video, tweet_image

  auth = tweepy.OAuth1UserHandler(
    "",  # API KEY
    "", #API SECRET
    "", # ACCESS TOKEN
    "" # ACCESS TOKEN SECRET
  )
  
  api = tweepy.API(auth)
  if file:
    file_type = file.split(".")[-1]
    if file_type == "jpg" or file_type == "png":
      file_type = "tweet_image"
    elif file_type == "gif":
      file_type = "tweet_gif"

    media = api.media_upload(file, media_category=file_type)
    api.update_status(status=status, media_ids=[media.media_id])
  else:
    api.update_status(status=status)