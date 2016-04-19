import elasticsearch
import datetime

es = elasticsearch.Elasticsearch(['http://docker.local:9200'])

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.datetime.now(),
}

res = es.index(index='test', doc_type='tweet', id=1, body=doc)
print res
print "\n"

res = es.get(index='test', doc_type='tweet', id=1)
print res
print "\n"

res - es.delete(index='test', doc_type='tweet', id=1)
print res
print "\n"

es.indices.refresh(index='test')
