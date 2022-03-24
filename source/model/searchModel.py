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
        # The search engine object can be any object which is a child of the SearchEngine class, and implements the search() method
        self.searchEngine = ElasticSearchEngine()

    def search(self, query: str, filters: dict) -> pandas.DataFrame:
        # To search simply use the search() function of search engines.
        # Similar to interfaces in traditional OOP
        search_results =  self.searchEngine.search(query, filters)

        return self.add_metadata_to_search_results(search_results)
    
    
    def format_metadata(self, metadata: str) -> tuple:
        """This method gets metadata from the X5GON API as Json and returns a tuple containing the description and the url
            from the object.
        Args:
            metadata (str): The json object containing metadata from the X5GON API

        Returns:
            (str, str): Tuple object containing the description and the url
        """
        try:
            data_json = json.loads(metadata)
        except json.JSONDecodeError:
            print("Could not get metadata from a document")
            return ("", "")

        return (data_json["oer_materials"]["description"], data_json["oer_materials"]["url"])
    
    def get_metadata_urls(self, search_results: pandas.DataFrame) -> list:
        """This method creates a list of url to send requests to (in the X5GON Dataset) to get all of the metadata.

        Args:
            search_results (pandas.DataFrame): All of the search results as a dataFrame

        Returns:
            list: the list of urls to send GET requests to
        """

        urls = []
        for index in search_results["id"]:
            urls.append("https://platform.x5gon.org/api/v1/oer_materials/" + str(index))
        return urls
    
    def appendToResults(self, results: pandas.DataFrame, metadata: list):
        results["description"] = [data[0] for data in metadata]
        results["url"] = [data[1] for data in metadata]


    def add_metadata_to_search_results(self, search_results: pandas.DataFrame) -> pandas.DataFrame:
        """This function gets the metadata from the X5GON api and adds it to the search results. it uses parallelism to gain time

        Args:
            search_results (pandas.DataFrame): The search results

        Returns:
            pandas.DataFrame: The search results with the metadata for each document
        """
        
        # Run all of the get requests to add the metadata in parallel (for each document)
        urls = self.get_metadata_urls(search_results)
        metadata = []
        with FuturesSession() as session:
            futures = [session.get(url) for url in urls]
            
            for future in futures:
                metadata.append(self.format_metadata(future.result().content))
                
        
        # Add the new columns with the metadata
        self.appendToResults(search_results, metadata)
        # Only get results where we could retrieve metadata
        search_results = search_results[search_results.url != ""]    

        
        return search_results

