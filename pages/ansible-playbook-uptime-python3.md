---
title: "Ansible playbook listing uptime using python3"
timestamp: 2019-06-12T19:30:01
tags:
  - ansible_python_interpreter
published: true
books:
  - ansible
author: szabgab
archive: true
---


Simple example using Python3 in Ansible and declaring this inside the playbook.

Lising the uptime of the remote host.

Declaring localhost (127.0.0.1) as the remote host inside the playbook to make the example simpler.


{% include file="examples/ansible/uptime-playbook-python3.yml" %}



```
$ ansible-playbook uptime-playbook-python3.yml

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match
'all'


PLAY [127.0.0.1] ******************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************
ok: [127.0.0.1]

TASK [just display] ***************************************************************************************************
changed: [127.0.0.1]

TASK [debug] **********************************************************************************************************
ok: [127.0.0.1] => {
    "hostname": {
        "changed": true,
        "cmd": "uptime",
        "delta": "0:00:00.002913",
        "end": "2019-06-12 19:11:38.562227",
        "failed": false,
        "rc": 0,
        "start": "2019-06-12 19:11:38.559314",
        "stderr": "",
        "stderr_lines": [],
        "stdout": " 19:11:38 up 8 days, 14:05,  1 user,  load average: 0.61, 0.86, 1.04",
        "stdout_lines": [
            " 19:11:38 up 8 days, 14:05,  1 user,  load average: 0.61, 0.86, 1.04"
        ]
    }
}

PLAY RECAP ************************************************************************************************************
127.0.0.1                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 

```
