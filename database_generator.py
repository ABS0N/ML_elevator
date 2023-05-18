# Generating the database for the project
# Generating a building with 20 floors and 10 rooms per floor
# Each room has 1-4 persons
# Each person has a job and works 3-5 days a week for 4-8 hours a day
# The most common work-style is 5 days a week for 8 hours a day
# The most common work hours are 9-5, but some people work night shifts
# The most common work days are Monday-Friday, but some people work weekends
# Each person has a sleep schedule, and sleeps 6-10 hours a day
# The most common sleep schedule is 10pm-6am, but some people sleep during the day
# Most people go out on the weekends, but some people go out on weekdays and some people don't go out at all
# Each person leaves the room 1-4 times a day, and stays away for 1-4 hours
# Each person has 1-4 friends, but not necessarily in the same room
# Each person visits their friends 1-4 times a week, and stays for 1-4 hours
# Each group of friends go out together 1-4 times a week, and stays for 2-6 hours
# These activities are all random, but the people are not
# The people are generated in a way that they are friends with people in the same room, and people in other rooms
# The people are also generated in a way that they are friends with people on the same floor, and people on other floors
# These activities vary from person to person, but the average is the same for all people
# These activities are also generated in a way that they are not the same for all people
# These activities are also generated in a way that they are not the same for all groups of friends
# These activities are also generated in a way that they are not the same for all floors
# These activities depend on the time of day, and the day of the week

import random
import json
import datetime
import time
import os

# The number of floors in the building
floors = 20

# The number of rooms per floor
rooms = 10

# The number of people per room
max_people = 4
min_people = 1

# The number of friends per person
max_friends = 4
min_friends = 1

# The number of times a person leaves the room per day
max_leaves = 4
min_leaves = 1

# The number of times a person visits their friends per week
max_visits = 4
min_visits = 1

# The number of times a group of friends goes out together per week
max_outings = 4
min_outings = 1

# The number of days a person works per week
max_work_days = 5
min_work_days = 3

# The number of hours a person works per day
max_work_hours = 8
min_work_hours = 4

# The number of hours a person sleeps per day
max_sleep_hours = 10
min_sleep_hours = 6

# The number of hours a person stays away from their room when not working or sleeping
max_stay_away_hours = 4
min_stay_away_hours = 1

# The number of hours a person stays at their friend's room when visiting
max_visit_hours = 4
min_visit_hours = 1

# The number of hours a group of friends stays out together when going out
max_outing_hours = 6
min_outing_hours = 2

# The number of days a person goes out per week
max_go_out_days = 2
min_go_out_days = 0

# The number of days a person goes out per week
max_go_out_hours = 4
min_go_out_hours = 1

# Generating the people with their attributes and IDs
def generate_people():
    people = []
    for floor in range(floors):
        for room in range(rooms):
            for person in range(random.randint(min_people, max_people)):
                person = {}
                person["id"] = str(floor) + "-" + str(room) + "-" + str(person)
                person["floor"] = floor
                person["room"] = room
                person["friends"] = []
                person["work_days"] = []
                person["work_hours"] = []
                person["sleep_hours"] = []
                person["stay_away_hours"] = []
                person["visit_hours"] = []
                person["outing_hours"] = []
                person["go_out_days"] = []
                person["go_out_hours"] = []
                people.append(person)
    return people

# Generating the friends of each person using their IDs
def generate_friends(people):
    for person in people:
        for friend in range(random.randint(min_friends, max_friends)):
            friend = random.choice(people)
            if friend["id"] not in person["friends"] and friend["id"] != person["id"]:
                person["friends"].append(friend["id"])
                friend["friends"].append(person["id"])

# Generating the work days of each person in a way that the most common work days are Monday-Friday
def generate_work_days(people):
    for person in people:
        for day in range(random.randint(min_work_days, max_work_days)):
            day = random.randint(0, 6)
            if day not in person["work_days"]:
                person["work_days"].append(day)

# Generating the work hours of each person in a way that the most common work hours are 9-5
# and the work hours are consecutive
def generate_work_hours(people):
    for person in people:
        work_hour = range(random.randint(min_work_hours, max_work_hours))
        for hour in range(random.randint(min_work_hours, max_work_hours)):
            hour = random.randint(0, 23)
            if hour not in person["work_hours"]:
                person["work_hours"].append(hour)