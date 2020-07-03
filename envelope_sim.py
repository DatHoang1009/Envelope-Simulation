# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:15:44 2020

@author: datho
"""
import random

def pick_envelope(switch, verbose):
    r = random.randint(0,3)
    list1 = []
    for i in range(0,4):
        list1.append('b')
        if i == r:
            list1.pop(i)
            list1.append('r')
    choose = random.randint(0,1)
    if verbose == True:
        print("Envelop 0: " + str(list1[0]) + " " +str(list1[1]))
        print("Envelop 1: " + str(list1[2]) + " " +str(list1[3]))
    if choose == 0:
        take = random.randint(0,1)
        if verbose == True:
            print("I picked evelope " + str(choose))
            print("and drew a " + str(list1[take]))
        if list1[take] == 'r':
            return True
        elif switch == True:
            if verbose == True:
                print("Switch to envelope " + str(1-choose))
            if r > 1:
                return True
            else:
                return False
        elif switch == False:
            if r <= 1:
                return True
            else:
                return False
    if choose == 1:
        take = random.randint(2,3)
        if verbose == True:
            print("I picked evelope " + str(choose))
            print("and drew a " + str(list1[take]))
        if list1[take] == 'r':
            return True
        elif switch == True:
            if verbose == True:
                print("Switch to envelope " + str(1-choose))
            if r <= 1:
                return True
            else:
                return False
        elif switch == False:
            if r > 1:
                return True
            else:
                return False

def run_simulation(n):
    count_sw = 0
    count_no_sw = 0
    for i in range(0,n):
        pick_envelope(True,False)
        if pick_envelope(True,False) == True:
            count_sw = count_sw + 1
        pick_envelope(False,False)
        if pick_envelope(False,False) == True:
            count_no_sw = count_no_sw + 1
    sw_percentage = float(count_sw/n)
    no_sw_percentage = float(count_no_sw/n)
    print("After "+ str(n)+ " simulations:")
    print("  Switch successful: {:.2%}".format(sw_percentage))
    print("  No-switch successful: {:.2%}".format(no_sw_percentage))
    
    
    
    