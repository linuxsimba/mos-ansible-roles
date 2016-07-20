#!/usr/bin/python


# Returns the internal lma alerting VIP IP address as an Ansible Fact
# Author: Stanley Karunditu
# LICENSE: MIT

import subprocess
import json

cmd = 'pcs resource show vip__infrastructure_alerting_mgmt_vip'.split()
output = subprocess.check_output(cmd)
entries = output.split('\n')
fact = {'ip': '' }
for entry in entries:
    splitentry = entry.split()
    for subentry in splitentry:
        if subentry.startswith('ip'):
            fact['ip'] = subentry.split('=')[1]
print json.dumps(fact)
