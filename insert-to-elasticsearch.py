import sys
import json
from pprint import pprint
from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['localhost'],
    port=9200

)

MyFile= open("result.json",'r').read()
docs = json.loads(MyFile)

for i, doc in enumerate(docs):
    es.index(index='hotels', doc_type='hotel', id=i, body=doc)
