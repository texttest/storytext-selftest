#!/usr/bin/env python

from storytext import applicationEvent
import time, signal, sys

def handleSignal(signum, *args):
    sys.stderr.write("Got signal " + repr(signum) + "\n")

signal.signal(signal.SIGQUIT, handleSignal)
signal.signal(signal.SIGINT, handleSignal)

time.sleep(0.5)
applicationEvent("first sleep to complete", category="sleeps")
applicationEvent("nothing to happen", category="other")
time.sleep(5)
time.sleep(0.5)
applicationEvent("second sleep to complete", category="sleeps")
time.sleep(5)
