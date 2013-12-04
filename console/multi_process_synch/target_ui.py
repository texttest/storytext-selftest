#!/usr/bin/env python

""" We submit a second copy of ourselves (with the StoryText arguments hardcoded), which runs simultaneously.
    The idea is to test mutual synchronisation by each process writing a file for the other to read."""

import signal

def handleSignal(signum, *args):
    pass # Just a way to break the sleeps...

def handleSignals():
    signal.signal(signal.SIGQUIT, handleSignal)
    signal.signal(signal.SIGINT, handleSignal)

handleSignals()

from storytext import applicationEvent
import time, sys, os, subprocess

otherProc = None

if len(sys.argv) == 1:
    storytext = os.path.expandvars("${TEXTTEST_CHECKOUT}/python2.6.current/bin/storytext")
    #secondCommands = [ storytext, "-i", "console", "-t", "5", "target_ui.py", "file2", "file", "Hello First UseCase" ]
    secondCommands = ["sh", "-c", storytext + " -i console -t 5 target_ui.py file2 file 'Hello First UseCase' &"]
    env = { "USECASE_REPLAY_SCRIPT" : os.getenv("USECASE_REPLAY_SCRIPT"), "USECASE_RECORD_SCRIPT" : "recorded_usecase2.storytext" }
    otherProc = subprocess.Popen(secondCommands, stdout=open("output2.storytext", "w"), stderr=open("errors2.storytext", "w"), env=env, preexec_fn=handleSignals)

if otherProc is None:
    writeFile = sys.argv[1]
    readFile = sys.argv[2]
    contents = sys.argv[3]
    sleepLength = 3
else:
    writeFile = "file"
    readFile = "file2"
    contents = "Hello Second UseCase"
    sleepLength = 1

# Not broken, to ensure the test doesn't work if the synchronisation doesn't (different in both processes)
time.sleep(sleepLength)
with open(writeFile, "w") as f:
    f.write(contents + "\n")
applicationEvent("first sleep to complete")
# Broken by SIGQUIT
time.sleep(5)
# Broken by SIGINT
time.sleep(5)
if os.path.isfile(readFile):
    print open(readFile).read()
    sys.stdout.flush()
if otherProc:
    otherProc.wait()
