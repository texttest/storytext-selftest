#!/usr/bin/env python

from usecase import applicationEvent, applicationEventRename
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print "Interrupted while sleeping for", length, "seconds."

sleep(0.5)
try:
    applicationEvent("first sleep to complete", "old category")
    applicationEventRename("first sleep to complete", "a renamed sleep event", 
                           "old category", "new category")
    sleep(5)
except KeyboardInterrupt:
    print "Interrupted while sleeping for 5 seconds."
