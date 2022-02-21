#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_count = 5

while pw != secret:
    count += 1
    if count > max_count: break
    pw = input("What's the secret word? ")
else:
    auth = True
print("Authorized" if auth else "Calling the FBI...")

