#!/usr/bin/env python

import os
import time
from sys import argv, stdout

script, filename = argv

border = '\n+++++++++++++++++++++++++++\n\n'
border1 = '\n<><><><><><><><><><><><><><><><>\n\n'

commands_to_run = [''] #type in commands as a list: 'command_1', 'command_2'
times_to_collect = int() #how many times this should be collected
time_interval = int() #in seconds

file = open(filename, 'w')
file.write('Below file is an output of commands: %r\n' % commands_to_run)
file.write(border)

for i in range(0,times_to_collect):
    run = i + 1
    current_time = time.ctime()
    universal_time = str(time.time())
    file.write('\tRun: %s' % run)
    file.write('\n\nCollected at: %s' % current_time)
    file.write('\nEpoch time: %s\n\n' % universal_time)
    for cmd in commands_to_run:
        c = os.popen('%s' % cmd)
	command = c.read()
	file.write(command)
	file.write(border1)
    if i < (times_to_collect - 1):
        time.sleep(time_interval)
	file.write(border)

file.close()
