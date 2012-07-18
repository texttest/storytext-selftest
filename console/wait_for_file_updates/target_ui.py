#!/usr/bin/env python

import time, os

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print("Interrupted while sleeping for " + str(length) + " seconds.")
        if os.path.isfile("file.txt"):
            print("File contains " + open("file.txt").read())

sleep(0.5)
f = open("file.txt", "w")
f.write("Message\n")
f.close()
sleep(5)
