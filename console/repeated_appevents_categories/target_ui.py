#!/usr/bin/env python

from storytext import applicationEvent
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print("Interrupted while sleeping for " + str(length) + " seconds.")

sleep(0.5)
applicationEvent("the event", "main")
applicationEvent("the other event", "other")
applicationEvent("the event", "main")
sleep(5)
