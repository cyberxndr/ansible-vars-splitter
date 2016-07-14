# ansible-vars-splitter
Split a single json file with the host variables into the multiple files.

## The problem
Ansible is a great tool for managing servers. It allows to control multiple servers at once. Sometimes we need to use host variables for the maintance purposes. The [default scenario](http://docs.ansible.com/ansible/playbooks_variables.html) is to store this variables into the separate files inside the `host_vars` folder. It can be useful, but not really comfortable in cases when we have a lot of hosts with the same variables.We may want to store them in a one place instead. But Ansible expects to get an individual file for the each host.

## Solution
We can split a single json file by keys, and place them into the individual files.

`./script.py`

So the following file
##### vars.json
```json
{
  "host1": {
    "backup_dir": "/archives",
  },
  
  "host2": {
    "backup_dir": "/backups"
  }
}
```

will be splitted into the parts and placed into a `/etc/ansible/host_vars` folder:

##### /etc/ansible/host_vars/host1
```json
{
  "backup_dir": "/archives"
}
```

##### /etc/ansible/host_vars/host2
```json
{
  "backup_dir": "/backups"
}
```

### Conclusion
The script can be useful when we need to store a lot of similar variables for the multiple hosts. We can change them in a one place and run the script then to mirror changes. 
