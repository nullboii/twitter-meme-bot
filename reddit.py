import praw
import config

def getPosts(subreddit, limit, nsfw=False):
  #get amount of posts from subreddit
  #do not get stickied posts.
  #do not get nsfw if False
  #returns submission metadata as list of dicts
  
  reddit = praw.Reddit(
      client_id=config.reddit_client_id,
      client_secret=config.reddit_client_secret,
      user_agent=config.reddit_user_agent,
  )
  
  subreddit = reddit.subreddit(subreddit)
  
  submission_urls = []
  for submission in subreddit.hot(limit=limit):
    if submission.stickied or submission.over_18 == True and nsfw == False:
      pass
    elif submission.url.split('.')[-1] == 'gif':
      # issues with tweepy only uploading first frame of gif. fix later
      pass
    else:
      submission_urls.append(
        {
          "title": submission.title,
          "url": submission.url,
          "author": submission.author.name,
          "permalink": submission.permalink,
          "score": submission.score,
          "file_type": submission.url.split(".")[-1],
          "sub": submission.subreddit
        }
      )
      
  return submission_urls