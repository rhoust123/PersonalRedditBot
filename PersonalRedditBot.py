# Personal Coding Project
# Author: Rhett Houston
# Start Date: 6/2/23
# End Date:
# Sources:

import praw

reddit = praw.Reddit(
    client_id="kek8O6sH4IwaFde2k3EE2w",
    client_secret="h4hHOPOhIHfNCa_U7LYKdC1BzHv7UA",
    user_agent="<console:Aragorn-IntroBot:1.0>",
)

subreddit = reddit.subreddit("lotr")

for submission in subreddit.hot(limit=100):
    #print("*********")
    #print(submission.title)

    for comment in submission.comments:
        lower_comment = comment.body.lower()
        if " aragorn " in lower_comment:
            print("----------")
            print(comment.body)



