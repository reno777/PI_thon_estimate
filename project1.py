#!/usr/bin/python2.7

import os
import requests
import math
import random
import argparse

def seed_input() :
    seed1 = input("Please enter a seed number: ")
    #seed2 = input("Please enter a second seed number: ")
    #print seed1, seed2
    return seed1

def prng_one(seed_num) :
    random.seed(seed_num)
    for i in range(1000) :
        print random.randrange(1,1000)

def prng_two(seed_num) :
    random.seed(seed_num)
    for i in range(1000) :
        print random.randrange(1,1000)

#def trng() :


#def pi_calculation() :


if __name__ == "__main__" :
    prng_one(seed_input)

