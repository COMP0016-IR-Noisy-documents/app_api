from source.controller.SearchEngine import SearchEngine
import requests
from elasticsearch import Elasticsearch
import pandas as pd
import json

class ElasticSearchEngine(SearchEngine):
    
    def search(self, query: str, filters: dict):
        
        
        queryPaylod ={
                        "query":{
                            "bool": {
                                "filter":filters,
                                "must": {
                                    "multi_match": {
                                        "query": query, # To add parameters simply add var name without quotes
                                        "type": "most_fields",
                                        "fields": [
                                            "title",
                                            "keywords"
                                        ]
                                    }
                                }
                            }
                         }
                    }       
        print(queryPaylod)
        results = requests.get("http://localhost:9200/_search", json= queryPaylod)
        
        return self.getResultsAsDF(json.loads(results.text))
    
    def getResultsAsDF(self,res):

        columnNames = ['id', 'title', 'type', 'language', 'keywords', 'concepts']
        results = []
        resultDF = pd.DataFrame()

        for hit in res['hits']['hits']:
            hit = hit['_source']
            row = [hit['id'], hit['title'], hit['type'], hit['language'], hit['keywords'], hit['concepts']]

            results.append(row)
            # Removed append as this method will be deprecated
            
        for i in range(len(columnNames)):
            resultDF[columnNames[i]] = [row[i] for row in results]
        print("---")
        return resultDF