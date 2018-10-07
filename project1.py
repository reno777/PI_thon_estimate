#!/usr/bin/python2.7

import fractions
import random
import math
import sys
sys.path.insert(0, '/home/reno/fall2018/cosc274/cosc274Project')
import randomapi
from randomapi import RandomJSONRPC

def seed_input() :
    seed1 = input("Please enter a seed number: ")
    seed2 = input("Please enter a second seed number: ")
    return seed1,seed2

def prng_one(seed_num) :
    random.seed(seed_num)
    list1 = []
    for i in range(1000) :
        list1.append(random.randrange(1,1000))
    return list1

def prng_two(seed_num) :
    random.seed(seed_num)
    list2 = []
    for i in range(1000) :
        list2.append(random.randrange(1,1000))
    return list2 

def trng() :
    list3 = []
    random_client = RandomJSONRPC("a7f40e35-769a-49b1-a6be-96028460cd23")
    list3 = random_client.generate_integers(n=1000, min=0, max=1000)
    return list3 

def pi_calculation(rng_list) :
    total = 0.0
    for i in range(len(rng_list)-1) :
        if fractions.gcd(rng_list[i],rng_list[i+1]) == 1 :
            total += 1
    pi = math.sqrt((6*1000)/total)
    return pi

if __name__ == "__main__" :
    x, y = seed_input()
    prng1 = pi_calculation(prng_one(x))
    prng2 = pi_calculation(prng_two(y))
    trng_var = pi_calculation(trng())
    print "PRNG with seed number one Pi estimate is: ", prng1
    print "PRNG with seed number two Pi estimate is: ", prng2
    print "TRNG using random.org Pi estimate is: ", trng_var
