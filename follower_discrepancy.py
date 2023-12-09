#!/usr/bin/env python
from zwift import Client

username = ''
password = ''
player_id = 0
client = Client(username, password)
zwift_limit = 200


profile = client.get_profile()

print("===================")
print("Checking Followees:")
print("===================")

follow_count = profile.profile['socialFacts']['followeesCount']
follow_pages = follow_count / zwift_limit 

for x in range(1, round(follow_pages+0.5)+1):
    start = (x-1)*zwift_limit

    for follower in profile.get_followees(start=start):
        if follower['followeeProfile']['socialFacts']['followeeStatusOfLoggedInPlayer'] != "IS_FOLLOWING":
            print("Looks like >> " + follower['followeeProfile']['firstName']
		+ " "
		+ follower['followeeProfile']['lastName']
		+ " << doesn't follow you.")

print("===================")
print("Checking Followers:")
print("===================")

follow_count = profile.profile['socialFacts']['followersCount']
follow_pages = follow_count / zwift_limit 

for x in range(1, round(follow_pages+0.5)+1):
	start = (x-1)*zwift_limit
	for follower in profile.get_followers(start=start):
		if follower['followerProfile']['socialFacts']['followerStatusOfLoggedInPlayer'] == "REQUESTS_TO_FOLLOW":
			print(follower['followerProfile']['firstName'] +
				" " +
				follower['followerProfile']['lastName'] +
				" is following you but hasn't answered your request.")
		elif follower['followerProfile']['socialFacts']['followerStatusOfLoggedInPlayer'] == "NO_RELATIONSHIP":
			print(follower['followerProfile']['firstName'] +
				" " +
				follower['followerProfile']['lastName'] +
				" follows you, but you don't.")
