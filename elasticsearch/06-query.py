import elasticsearch

es = elasticsearch.Elasticsearch(['http://docker.local:9200'])

res = es.search(index='test-index', body={'query': {'match_all': {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
