"""
The search algorithm (currently only returns the id column, unranked)
"""

import pandas
import numpy
import requests
import json
import time
from requests_futures.sessions import FuturesSession
from source.controller.ElasticSearchEngine import ElasticSearchEngine

class searchModel():
    """
    data: the pandas dataframe where
        - id (numpy.int64)
        - title (str)
        - type (str)
        - language (str)
        - keywords (list(str))
        - concepts (list(str))
        
    """

    def __init__(self):
        # Initialise the search engine and the "x5gon database"
        self.searchEngine = ElasticSearchEngine()

    def search(self, query: str, filters: dict):
        # To search simply use the search() function of search engines.
        # Similar to interfaces in traditional OOP
        
        search_results =  self.searchEngine.search(query, filters)
        print("Search Done")
        
        return self.add_metadata_to_search_results(search_results)
    

    # get additional metadata (description, etc.) from the X5GON API
    # TODO make this safe: catch errors if the API call fails
    def get_metadata(self, material_id: numpy.int64) -> dict:
        # see https://www.askpython.com/python/examples/pull-data-from-an-api
        response_API = requests.get("https://platform.x5gon.org/api/v1/oer_materials/" + str(material_id))
        # print(response_API.status_code)
        data = response_API.text
        data_json = json.loads(data)
        return data_json["oer_materials"]
    
    def format_metadata(self, metadata: str):
        try:
            data_json = json.loads(metadata)
        except:
            return ("", "")
        return (data_json["oer_materials"]["description"], data_json["oer_materials"]["url"])
    
    def get_metadata_urls(search_results: pd.DataFrame):
        urls = []
        for index in search_results["id"]:
            urls.append("https://platform.x5gon.org/api/v1/oer_materials/" + str(index))
        return urls

    def add_metadata_to_search_results(self, search_results: pandas.DataFrame) -> pandas.DataFrame:
        """This function gets the metadata from the X5GON api and adds it to the search results. it uses parallelism to gain time

        Args:
            search_results (pandas.DataFrame): The search results

        Returns:
            pandas.DataFrame: The search results with the metadata for each document
        """
        
        print("started appending")
        
        # Run all of the get requests to add the metadata in parallel (for each document)
        metadata = []
        with FuturesSession() as session:
            futures = [session.get(url) for url in self.get_metadata_urls(search_results)]
            print(len(futures))
            for future in futures:
                metadata.append(self.format_metadata(future.result().content))
                
        print("finished appending")
        # Add the new columns wit hthe metadata
        search_results["description"] = [data[0] for data in metadata]
        search_results["url"] = [data[1] for data in metadata]

        search_results = search_results[search_results.url != ""]    
        print("Added metadata")
        return search_results

# test code
if __name__ == "__main__":
    m = searchModel()
    print(m.get_metadata(1)["url"])
