#!/usr/bin/env python

from usecase import ScriptEngine
import logging, time, sys

def sleep(length):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        print "Interrupted while sleeping for", length, "seconds."

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(message)s")
engine = ScriptEngine()
sleep(0.5)
engine.applicationEvent("first sleep to complete")
sleep(5)
