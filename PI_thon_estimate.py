#!/usr/bin/python2.7

"""
### AUTHORS: Seth Rasmussen and Chris Patania
### DATE: October 2018
### VERSION: v1.0
### LICENSE: GNU-GPL v3.0
### DESCRIPTION: This was made for COSC 274: Intro to Applied Cryptography.
### This Program is used to predict the value of PI using Ernesto Cesaro's
### Theorem using 1000 randomly generated numbers from two PRNGs and one 
### TRNG to help show which is more accurate.
###
### SOURCES: The randomapi module used below was made by Mitchell Cohen 
### (mitch.cohen@me.com) and obtained from his Github page 
### at https://github.com/mitchchn/randomapi under the MIT License.
"""

#The following block is where any modules are imported to be used in the script
import fractions
import random
import math
import sys
sys.path.insert(0, '/home/reno/fall2018/cosc274/cosc274Project') #sets env path
from randomapi import RandomJSONRPC #Credit: Mitchell Cohen

#This function is for prompting the user to input two numbers that will be used for the seeds
def seed_input() :
    seed1 = input("Please enter a seed number: ") #user input seed number 1
    seed2 = input("Please enter a second seed number: ") #user input seed number 2
    return seed1,seed2 

#This function is using one of the seed numbers to generate a list of 1000 random numbers
def prng_one(seed_num) :
    random.seed(seed_num) #initializes the generator with the seed
    list1 = [] #declares a list called list1
    for i in range(1000) : #iterates over the following 1000 times
        list1.append(random.randrange(1,1000))
        #The above generates a number between 1 and 1000 and appends it to list1
    return list1 

#This function is using one of the seed numbers to generate a list of 1000 random numbers
def prng_two(seed_num) :
    random.seed(seed_num) #initializes the generator with the seed
    list2 = [] #declares a list called list2
    for i in range(1000) : #iterates over the following 1000 times
        list2.append(random.randrange(1,1000))
        #The above generates a number between 1 and 1000 and appends it to list2
    return list2 

#This function uses Mitchell Cohen's random.org api script to generate 1000 numbers between 1 and 1000
def trng() :
    list3 = [] #declares a list called list3
    random_client = RandomJSONRPC("a7f40e35-769a-49b1-a6be-96028460cd23") 
    #Above sets a variable to random.org api key 
    list3 = random_client.generate_integers(n=1000, min=0, max=1000)
    #Above generates 1000 numbers between 1 and 1000 and enters it into list3
    return list3 

#This function does all the math in estimating PI using Ernesto Cesaro's Theorem
def pi_calculation(rng_list) :
    total = 0.0 #Declares a variable and sets it to a decimal value of 0
    for i in range(len(rng_list)-1) : #iterates over the length of the list passed to the function
        if fractions.gcd(rng_list[i],rng_list[i+1]) == 1 : 
            #Above checks if position i and i+1 GCD is equal to 1 or not
            total += 1 #if the above check passes then it increases "total"
    pi = math.sqrt((6*1000)/total) 
    #calculates PI using the probablity of any random numbers (x,y) GCD is equal to 1
    return pi

#Main function. Calls the other functions as needed.
if __name__ == "__main__" :
    x, y = seed_input() #used to set variables to the tuple that seed_input()returns
    prng1_var = pi_calculation(prng_one(x)) #Variable for PRNG1's PI estimate
    prng2_var = pi_calculation(prng_two(y)) #Variable for PRNG2's PI estimate
    trng_var = pi_calculation(trng()) #Variable for TRNG's PI estimate
    #The following displays the estimates of PI back to the user
    print "PRNG with seed number one Pi estimate is: ", prng1_var
    print "PRNG with seed number two Pi estimate is: ", prng2_var
    print "TRNG using random.org Pi estimate is: ", trng_var
