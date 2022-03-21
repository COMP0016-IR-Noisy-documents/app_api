"""
The search algorithm (currently only returns the id column, unranked)
"""

import pandas
import numpy
import requests
import json

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
    

    def add_metadata_to_search_results(self, search_results: pandas.DataFrame) -> pandas.DataFrame:
        # initialise new columns as empty
        search_results["description"] = ""
        search_results["url"] = ""
        
        # for each result in the DataFrame, add the description and URL
        for index, result in search_results.iterrows():
            try:
                metadata = self.get_metadata(result["id"])
                search_results.at[index, "description"] = metadata["description"]
                search_results.at[index, "url"] = metadata["url"]
            #remove the object that have the issue retrieving url and description
            except:
                id = result["id"]
                print(f"cannot get document id: {id} from x5gon api" )

        search_results = search_results[search_results.url != ""]    
        print("______")
        return search_results

# test code
if __name__ == "__main__":
    m = searchModel()
    print(m.get_metadata(1)["url"])
