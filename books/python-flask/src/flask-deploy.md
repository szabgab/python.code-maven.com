# Flask Deploy app

* [Linode](https://linode.com/)
* [Digital Ocean](https://www.digitalocean.com/)


* Setup server on Linode
* ssh to it root@IP
* Create user   adduser gabor
* ssh-copy-id gabor@IP
* scp * gabor@IP

* apt update
* apt upgrade -y
* reboot
* apt install -y uwsgi uwsgi-plugin-python3 nginx python3-virtualenv

* as gabor
* virtualenv .venv
* source .venv/bin/activate
* pip install pytest flask


{% embed include file="src/examples/flask/50/app.py" %}

[uwsgi](https://uwsgi-docs.readthedocs.io/)

{% embed include file="src/examples/flask/50/uwsgi.ini" %}

[nginx](https://nginx.org/)

{% embed include file="src/examples/flask/50/nginx.conf" %}

{% embed include file="src/examples/flask/50/test_app.py" %}

