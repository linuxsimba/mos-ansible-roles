#!/usr/bin/python

# Returns the external LMA alerting VIP IP address as an Ansible Fact
# Author: Stanley Karunditu
# LICENSE: MIT

import subprocess
import json

cmd = 'pcs resource show vip__public'.split()
output = subprocess.check_output(cmd)
entries = output.split('\n')
fact = {'ip': ''}
for entry in entries:
    splitentry = entry.split()
    for subentry in splitentry:
        if subentry.startswith('ip'):
            fact['ip'] = subentry.split('=')[1]
print json.dumps(fact)
