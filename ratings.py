#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-04 18:15:51
# @Author  : David Adewoyin (david.adewoyin@baruchmail.cuny.edu)

print ("Welcome to the Border Protection Customer Feedback Database".upper())
print ("Would you like to add a service rating or check past ratings?")
print (" ")
action = int(input("Enter 1 to add a rating, or 2 to view ratings."))

# Validation
if action != 1 and action != 2:
    print("INVALID INPUT")
    action = int(input("There are only two options! Choose '1' to add rating or '2' to view ratings")) 
# Add rating in cbpss.txt
if action == 1:
    writable = open("cbpss.txt")
    score = int(input("Enter a rating on a 1-4 scale. Invalid ratings won't be counted"))
    writable.write(score)
    writable.close()
    print("Rating submitted! Thank you.")
# View rating
elif action == 2:
    highest = 1
    lowest = 4
    aggregate = 0
    rating_count = 0 # _count are counter variables
    one_count = 0
    two_count = 0   
    three_count = 0
    four_count = 0

    readable = open("cbpss.txt")
    ratings = readable.readlines()

    for rating in ratings:
        if int(rating) > 4 or int(rating) <= 0:
            print("Invalid rating bypassed")
            continue
        
        print(rating)       
        rating_count += 1
        aggregate += int(rating)

        # Count ratings
        if int(rating) == 4:
            four_count += 1
        elif int(rating) == 3:
            three_count += 1
        elif int(rating) == 2:
            two_count += 1
        else:
            one_count += 1
            
        if int(rating) > highest:
            highest = int(rating)
            
        if int(rating) < lowest:
            lowest = int(rating)
    # Print ratings
    readable.close()
    print("Ratings count:")
    print("1s: " + str(one_count))
    print("2s: " + str(two_count))
    print("3s: " + str(three_count))
    print("4s: " + str(four_count))
    print("Total: " + str(rating_count))
    print(" ")
    print("Highest rating: " + str(highest))
    print("Lowest rating : " + str(lowest))   
    mean = aggregate/rating_count
    print("Average: " + str(mean))
    StDev = abs(aggregate - (mean * rating_count))/(rating_count - 1)
    print("Std. Deviation: " + str(StDev))