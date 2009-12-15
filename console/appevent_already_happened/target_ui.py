#!/usr/bin/env python

from usecase import applicationEvent
import time, signal

def handleSignal(signum, *args):
    print "Got signal", signum

signal.signal(signal.SIGQUIT, handleSignal)
signal.signal(signal.SIGINT, handleSignal)

applicationEvent("nothing to happen")
time.sleep(0.5)
applicationEvent("first sleep to complete")
time.sleep(5)
time.sleep(0.5)
applicationEvent("second sleep to complete")
time.sleep(5)