#!/usr/bin/env python

from usecase import applicationEvent
import time, signal
signal.signal(signal.SIGURG, signal.SIG_DFL)

def sleep(length):
    time.sleep(length)
    
sleep(0.5)
applicationEvent("first sleep to complete")
sleep(5)
