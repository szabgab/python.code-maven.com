---
title: "Compile Python from source code"
timestamp: 2019-12-20T18:30:01
tags:
  - Python
published: true
books:
  - python
author: szabgab
archive: true
---


## Download the Source code

Use <b>wget</b>:

```
wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz
```

or your borwser: [python.org](https://www.python.org/downloads/).

```
tar -xf Python-3.8.1.tar.xz
```

```
cd Python-3.8.1
```

```
./configure  --prefix /opt/python-3-8-1
```

```
make -j 4
```

```
make install
```

## Compile python on old Centos

```
yum install -y wget
yum install -y gcc
yum install -y libffi-devel
yum install -y zlib-devel
yum install -y openssl-devel
yum install -y readline-devel
yum install -y sqlite-devel
yum install -y bzip2-devel
yum install -y xz-devel
yum install -y uuid-devel
yum install -y make net-snmp net-snmp-utils net-snmp-libs net-snmp-devel
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
```


Install:

```
tar xzf Python-3.7.2.tgz
cd Python-3.7.2
./configure --prefix=/opt/python372
make
make install
```


Update ~/.bashrc:

```
export PATH=/opt/python372/bin:$PATH
```

reload bashrc:

```
source .bashrc
```

Verify:

```
/opt/python372/bin/python3 --version
which python3
```


Check if pip3 is installed (this should print /opt/python372/bin/pip3):

```
which pip3
```

If pip3 is not installed, then install pip:

```
wget https://bootstrap.pypa.io/get-pip.py
/opt/python372/bin/python3 get-pip.py
rm get-pip.py
```

