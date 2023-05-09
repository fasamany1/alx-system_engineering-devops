#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles (default=[]).
    Returns:
        list: The titles of all hot articles for the subreddit, or
        None if no results are found or the subreddit is not valid.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """return top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'Mozilla/18.05'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
