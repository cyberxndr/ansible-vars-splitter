#!/usr/bin/env python2

import json

file = open('vars.json', 'r')
hosts = json.load(file)
file.close()

for host in hosts: 
   f = open("/etc/ansible/host_vars/%s" % host, 'w')
   f.write(json.dumps(hosts[host], indent=4)) 
   f.close()
   print("%s file created" % host)
