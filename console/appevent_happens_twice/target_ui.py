#!/usr/bin/env python

from usecase import applicationEvent
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print "Interrupted while sleeping for", length, "seconds."

sleep(0.5)
applicationEvent("the event")
applicationEvent("the event")
sleep(5)
