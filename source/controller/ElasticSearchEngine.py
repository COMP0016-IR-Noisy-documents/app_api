from source.controller.SearchEngine import SearchEngine
import requests
from elasticsearch import Elasticsearch
import pandas as pd
import json

class ElasticSearchEngine(SearchEngine):
    
    def search(self, query: str, filters: dict):
        
        # The json of the query that will be sent to the ES instance
        queryPaylod ={  "size": 50,
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
        # Get the results
        results = requests.get("http://localhost:9200/_search", json= queryPaylod)
        print(queryPaylod)
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
        print(len(resultDF.index))
        return resultDF