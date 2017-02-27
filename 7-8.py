import tweepy
from tweepy import OAuthHandler

import collections
import time

consumer_key = "gJSOpNjzBKXIwVKYpA2gsCWhG"
consumer_secret = "zhY04k84OWKWCnBcoUWT3nWFSZu3wCzY0kPEoUBcirqkorfBO1"
access_token = "4059358516-ye3YzjF6aql39uOzdDAoRyPVjxo88qL1GEa0VsH"
access_secret = "8hWg7C7AjuLTv5S1D4Uhgqw5b13E4Jj80c1cbt7taF2hN"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#tweepy limit cursor raises error RateLimitErrors
#http://docs.tweepy.org/en/v3.5.0/code_snippet.html#handling-the-rate-limit-using-cursors
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def mode7_Exercise():
	userAtweets = api.user_timeline(screen_name=userA, count=10)
	userBtweets = api.user_timeline(screen_name=userB, count=10)

	userA_len = 0
	userB_len = 0

	for aUserTweet in userAtweets:
		userA_len += len(aUserTweet.text)

	for bUserTweet in userBtweets:
		userB_len += len(bUserTweet.text)


	if userA_len > userB_len:
		print ("We have a chatter here: " + userA)
		return userA
	elif userA_len < userB_len:
		print ("We have a chatter here: " + userB)
		return userB
	elif userA_len == userB_len:
		print ("We have chatter battle here: " + userA + " / " + userB)
		return userA + " / " + userB


	return ""


def mode8_Exercise():
	list_aUser = []
	list_bUser = []

	# for speed checking first ids	
	#http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
	for a_userid in limit_handled(tweepy.Cursor(api.followers_ids, screen_name=userA).items()):
		list_aUser.append(a_userid)

	for b_userid in limit_handled(tweepy.Cursor(api.followers_ids, screen_name=userB).items()):
		list_bUser.append(b_userid)

	#https://docs.python.org/2/library/sets.html
	commonFollowers = set(list_aUser) & set(list_bUser)

	list_common_users=""
	
	#https://dev.twitter.com/overview/api/users
	
	for id in commonFollowers:
		list_common_users += api.get_user(id).screen_name + " "

	if list_common_users:
		return "Common Followers are : " + list_common_users
	else:
		return "Not Common Followers"

userA, userB=input("Give two twitter Users : ").split()
mode = input("Exercise select 7 or 8?")

print (userA, userB)
print (mode)

result = ""

if int(mode) == 7:
	result = mode7_Exercise()
elif int(mode) == 8:
	result = mode8_Exercise()


print ("Exercise " + mode + " answer :: " + result)



