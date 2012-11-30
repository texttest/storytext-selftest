#!/usr/bin/env python

from storytext import applicationEvent
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print("Interrupted while sleeping for " + str(length) + " seconds.")

sleep(0.5)
applicationEvent("something interesting", "new category")
applicationEvent("first sleep to complete", "old category", supercedeCategories=["new category"])
applicationEvent("something interesting", "new category")
sleep(5)
