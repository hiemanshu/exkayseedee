#!/usr/bin/env python

#
#
# exkayseedee.py
# Game Idea By : YuviPanda
# Author : Hiemanshu Sharma
#
#

from database import ComicsDB
import os
import random
import sys

DOCUMENTATION = ""

check = os.path.isfile('data.db')
if (check):
    cdb = ComicsDB('data.db')
    id = random.randrange(1,840,1) #fix
    alt = cdb.getAlt(id)
    title = cdb.getTitle(id)
    print "Alt Text : %s" %alt
    t = random.randrange(1,5,1) #fix
    ch = 1;
    for i in range(1,6):
        rand = random.randrange(1,840,1) #fix
        if (i != t):
            if (rand != id):
                print "%d %s" %(i, cdb.getTitle(rand))
        else:
            print "%d %s" %(ch, title)
    while True:
        ans = raw_input('Pick the correct answer : ')
        if (int(ans) == t) :
            print "Answer is correct"
            sys.exit(0)
        else:
            print "Try again"
                
else :
    print SCRAPER
