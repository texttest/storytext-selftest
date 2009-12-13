#!/usr/bin/env python

from usecase import applicationEvent
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print "Interrupted while sleeping for", length, "seconds."

sleep(0.5)
applicationEvent("a thing that should never be seen")
applicationEvent("first sleep to complete")
sleep(5)
