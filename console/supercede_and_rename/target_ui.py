#!/usr/bin/env python

from usecase import applicationEvent, applicationEventRename
import time

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print "Interrupted while sleeping for", length, "seconds."

sleep(0.5)
applicationEvent("first sleep to complete", "old category", supercedeCategories=["new category"])
applicationEventRename("first sleep to complete", "silly name", "old category", "other category")
applicationEvent("something in other category", "other category")
applicationEvent("something else interesting", "new category")
sleep(5)
