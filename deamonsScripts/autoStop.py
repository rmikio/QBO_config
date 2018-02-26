#!/usr/bin/env python2.7

import time
import fileinput
import sys
import os
import errno
import yaml
import subprocess

# fichero config, contiene languaje
config = yaml.safe_load(open("/home/pi/Documents/config.yml"))
print "CONFIG " + str(config)

text = "good bye"
speak = "espeak -ven+f3 \"" + text + "\" --stdout  | aplay -D convertQBO"
result = subprocess.call(speak, shell = True)

result = subprocess.call("/home/pi/Documents/deamonsScripts/QBO_scratch stop > /home/pi/sampleStop.log 2>&1", shell = True)

