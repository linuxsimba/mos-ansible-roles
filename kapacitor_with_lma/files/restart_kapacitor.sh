#!/bin/bash

PCS_HOSTNAME=`/usr/sbin/crm resource status kapacitor | awk -F" " '{print $NF}'`

if [ "$PCS_HOSTNAME" == `hostname` ]; then
  KAPACITOR_STATUS=`service kapacitor status | awk -F" " '{print $(NF-1)}'`
  if [ "$KAPACITOR_STATUS" == "FAILED" ]; then
     echo  "restarting kapacitor"
     service kapacitor restart
  else
     echo "kapacitor already started"
  fi
fi
