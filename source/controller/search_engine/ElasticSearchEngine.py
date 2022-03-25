from source.controller.search_engine.SearchEngine import SearchEngine
import requests
from elasticsearch import Elasticsearch
import pandas as pd
import json
import os

class ElasticSearchEngine(SearchEngine):
    
    def search(self, query: str, filters: dict):
        
        # The json of the query that will be sent to the ES instance
        queryPaylod ={  "size": 25,
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

        session = requests.Session()
        session.auth = ("elastic",os.getenv('ES_PASSWORD'))

        results = session.get(os.getenv('ELASTICSEARCH_URI') + "/_search", json= queryPaylod)
        
        return self.getResultsAsDF(json.loads(results.text))
    
    def getResultsAsDF(self,res):

        columnNames = ['id', 'title', 'type', 'language', 'keywords', 'concepts']
        results = []
        resultDF = pd.DataFrame()
        # Parse the results json
        try:
            for hit in res['hits']['hits']:
                hit = hit['_source']
                row = [hit['id'], hit['title'], hit['type'], hit['language'], hit['keywords'], hit['concepts']]

                results.append(row)
                # Removed append as this method will be deprecated
        except KeyError:
            # If there is a KeyError, then it means there are no results: return an empty DataFrame
            return resultDF

        #Add all of the columns to the DataFrame   
        for i in range(len(columnNames)):
            
            resultDF[columnNames[i]] = [row[i] for row in results]
        
        return resultDF
