import elasticsearch

es = elasticsearch.Elasticsearch(['http://docker.local:9200'])

print es.indices.create(index='test', ignore=400)
print es.indices.delete(index='test', ignore=[400, 404])
