# Personal Coding Project
# Author: Rhett Houston
# Start Date: 6/2/23
# End Date:
# Sources:

import praw

reddit = praw.Reddit(
    client_id="4kbboKRetAQSnrKvzW0HPA",
    client_secret="y_sBceYjZf5fNAsYykIIFvHLA0bXqA",
    user_agent="<console:TerminatorBot:1.0>",
)

subreddit = reddit.subreddit("Terminator")

for submission in subreddit.hot(limit=10):
    print("*********")
    print(submission.title)

    for comment in submission.comments:
        lower_comment = comment.body.lower()
        if " terminator " in lower_comment:
            print("----------")
            print(comment.body)
            


