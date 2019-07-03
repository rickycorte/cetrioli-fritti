#!/usr/bin/env python
# -*- coding: ascii -*-

import random
import sys

def progressBar(value, endvalue, bar_length=20):

        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

size = 100000

random_del = False

entities = []

count = 0
print("Generating entries...")
while count < size:
    ln = random.randint(10, 100)
    
    i = 0
    s = ""
    while i < ln:
        s += chr(random.randint(65, 122))
        i += 1
    
    entities.append(s)
    count += 1
    progressBar(count, size)


size = 1000

print("Wrinting file...")
with open("test.txt", "w") as fd:
    i = 0
    while i < size:
        val = random.randint(0, 100)

        if val < 75 or not random_del:
            rsz = random.randint(0, len(entities)-1)
            st = "addent " + str(entities[rsz]) + "\n" 
            fd.write(st)
        else:
            rsz = random.randint(0, len(entities)-1)
            st = "delent " + str(entities[rsz]) + "\n"
            fd.write(st)

        i += 1    
        progressBar(i, size)
    
    fd.write("end")

print("Done")