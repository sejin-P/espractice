from elasticsearch import Elasticsearch
import json

es = Elasticsearch()
DICT_DIR = ''

# 사전 형식으로 넣고,
es.indices.create(
    index='dictionary',
    body={
        'settings': {
            'index': {
                'analysis': {
                    'analyzer': {
                        'my_analyzer': {
                            'type': 'custom',
                            'tokenizer': 'nori_tokenizer'
                        }
                    }
                }
            }
        },
        'mappings': {
            'dictionary_datas': {
                'properties': {
                    'id': {
                        'type': 'long'
                    },
                    'title': {
                        'type': 'text',
                        'analyzer': 'my_analyzer'
                    }
                }
            }
        }
    }
)

# json file열어
with open(DICT_DIR, encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

# body에 dictionary 정보 뭉쳐놓기!!
body = ""
for i in json_data:
    body = body + json.dumps({'index': {'_index': 'dictionary', '_type': 'dictionary_datas'}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

es.bulk(body)
