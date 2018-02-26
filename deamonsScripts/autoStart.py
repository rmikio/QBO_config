#!/usr/bin/env python2.7

import time
import fileinput
import sys
import os
import errno
import yaml
import subprocess

# read config file
config = yaml.safe_load(open("/home/pi/Documents/config.yml"))
print "CONFIG " + str(config)

text = "Hello"
speak = "espeak -ven+f3 \"" + text + "\" --stdout  | aplay -D convertQBO"
result = subprocess.call(speak, shell = True)
time.sleep(0.5)

if config["startWith"] == "Scratch":
	text = "I'm in scratch mode."
        speak = "espeak -s 140 -ven+f3 \"" + text + "\" --stdout  | aplay -D convertQBO"
        result = subprocess.call(speak, shell = True)

	result = subprocess.call("/home/pi/Documents/deamonsScripts/QBO_scratch start > /home/pi/scratchMode.log 2>&1", shell = True)

elif config["startWith"] == "Interactive":
	text = "I'm in interactive mode."
        speak = "espeak -s 140 -ven+f3 \"" + text + "\" --stdout  | aplay -D convertQBO"
        result = subprocess.call(speak, shell = True)

	result = subprocess.call("/home/pi/Documents/Python\ projects/PiFaceFast.py > /home/pi/PiFaceFastMode.log 2>&1 &", shell = True)

