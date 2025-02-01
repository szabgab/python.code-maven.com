---
title: "Python - Elasticsearch - Consul"
timestamp: 2019-01-01T07:30:01
tags:
  - CodeMaven
published: false
books:
  - python
author: szabgab
archive: true
---


```
from elasticsearch import Elasticsearch
from datetime import datetime
import consul

# pip install elasticsearch

def get_hosts():
   con = consul.Consul()
   id, nodes = con.catalog.service('elastic')
   hosts = []
   for n in nodes:
       hosts.append(n['Address'])
   return hosts


def submit_to_es(doc):
   hosts = get_hosts()
   #print(hosts)
   now = datetime.now()
   es = Elasticsearch(hosts)
   doc['timestamp'] = now
   name = now.strftime('job-%Y-%m')
   #print(name)
   res = es.index(index = name, doc_type = 'job', body = doc)
   print(res)

def example():
   doc = {
       'job' : 'self-test',
       'text' : 'some text',
   }
   submit_to_es(doc)

if __name__ == '__main__':
   example()

```

```
from elasticsearch import Elasticsearch
from datetime import datetime
import consul

# pip install elasticsearch


def get_hosts():
   con = consul.Consul()
   id, nodes = con.catalog.service('elastic-metrics')
   hosts = []
   for n in nodes:
       hosts.append(n['Address'])
   return hosts


def submit_to_es(doc, hosts = None):
   if not hosts:
       hosts = get_hosts()
   if not hosts:
       print("WARN: Could not find the hosts for elastic. Skipping the reporting.")
       return

   #print(hosts)
   try:
       now = datetime.now()
       es = Elasticsearch(hosts)
       doc['timestamp'] = now
       name = now.strftime('jobs-%Y-%m')
       #print(name)
       res = es.index(index = name, doc_type = 'job', body = doc)
       print(res)
   except Exception as e:
       print("ERROR: Exception while trying to report to Elasticsearch.")
       print(e)


def get_load_from_es(hosts = None):
   if not hosts:
       hosts = get_hosts()
   if not hosts:
       print("WARN: Could not find the hosts for elastic. Skipping the reporting.")
       return

   #print(hosts)
   try:
       now = datetime.now()
       es = Elasticsearch(hosts)
       #return(es.search( size = 1, index = 'metricbeat-2018.10.11' ))
       #return(es.search( size = 1, index = 'metricbeat-2018.10.11', body = {"query": {"match": {"beat.hostname" : 'name-of-a-server' }}} ))
       return(es.search( size = 1, index = 'metricbeat-2018.10.11', body = {"query":            {
               "bool" :                    {
                       "must" : [
                           {"match": {"beat.hostname" : 'name-of-a-server' }},
                           {"match": {"metricset.name" : 'load' }}
                       ],
                   "filter": {
                       "range": {
                           "@timestamp": {
                                "gte": "2018-10-11T08:04:39.892Z"
                           }
                       }
                   }
               }
           },
       }))
   except Exception as e:
       print("ERROR: Exception while trying to retreive data from Elasticsearch.")
       print(e)
def example():
   doc = {
       'job' : 'self-test',
       'text' : 'some text',
   }
   submit_to_es(doc)

if __name__ == '__main__':
   #example()
   print(get_load_from_es(hosts = ['10.1.1.2']))
```
