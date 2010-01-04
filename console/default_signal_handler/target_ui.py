#!/usr/bin/env python

from usecase import applicationEvent
import time

def sleep(length):
    time.sleep(length)
    
sleep(0.5)
applicationEvent("first sleep to complete")
sleep(5)
