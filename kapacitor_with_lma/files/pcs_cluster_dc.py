#!/usr/bin/python

# Returns the IP address of the Pacemaker cluster DC
# Works with MOS8 and MOS9.
# Author: Stanley Karunditu
# LICENSE: MIT

import subprocess
import json

cmd = 'pcs status cluster'.split()
output = subprocess.check_output(cmd)
entries = output.split('\n')
fact = {'hostname': ''}
for entry in entries:
    if entry.strip().startswith('Current'):
      splitentry = entry.split()
      fact['hostname'] = splitentry[2]
print json.dumps(fact)
