# Personal Coding Project
# Author: Rhett Houston
# Start Date: 6/2/23
# End Date:
# Sources:

import praw
import time

reddit = praw.Reddit(
    client_id="kek8O6sH4IwaFde2k3EE2w",
    client_secret="h4hHOPOhIHfNCa_U7LYKdC1BzHv7UA",
    user_agent="<console:Aragorn-IntroBot:1.0>",
    username = "Aragorn-IntroBot",
    password = "botPass12Aragorn"
)

subreddit = reddit.subreddit("lotr")

aragorn_prophecy = "All that is gold does not glitter, \n Not all those who wander are lost; \n The old that is strong does not wither, \n Deep roots are not reached by the frost. \n \n From the ashes a fire shall be woken, \n A light from the shadows shall spring; \n Renewed shall be blade that was broken, \n The crownles again shall be king."

for submission in subreddit.hot(limit=100):

    for comment in submission.comments:
        if hasattr(comment, "body"): 
            lower_comment = comment.body.lower()
            if " aragorn " in lower_comment:
                comment.reply(aragorn_prophecy)
                time.sleep(660)
                



