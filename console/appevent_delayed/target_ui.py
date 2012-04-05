#!/usr/bin/env python

from storytext import applicationEvent
import time, signal, sys

def handleSignal(signum, *args):
    sys.stderr.write("Got signal " + repr(signum) + "\n")

signal.signal(signal.SIGQUIT, handleSignal)
signal.signal(signal.SIGINT, handleSignal)

time.sleep(0.5)
applicationEvent("nothing to happen")
applicationEvent("first sleep to complete", "first", delayLevel=1)
time.sleep(5)
time.sleep(0.5)
applicationEvent("second sleep to complete", "second")
time.sleep(5)
