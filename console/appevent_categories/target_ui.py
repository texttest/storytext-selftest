#!/usr/bin/env python

from storytext import applicationEvent
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print "Interrupted while sleeping for", length, "seconds."

sleep(0.5)
applicationEvent("first sleep to complete", "old category")
applicationEvent("something else interesting", "new category")
sleep(5)
