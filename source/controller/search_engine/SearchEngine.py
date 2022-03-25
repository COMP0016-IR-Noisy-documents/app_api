
class SearchEngine():
    """The class defining the search engine objects that can be plugged-in the project. These objects should be children of this class."""
    def __init__(self):
        self.engine= True

    def search(self, query: str, filters: list):
        """This method uses the search engine to search for a query with  certain filters.

        Args:
            query (str): The query string which will be searched
            filters (list): The list of filters (in ElasticSearch format) which will be applied to the query

        
        """
        raise NotImplementedError