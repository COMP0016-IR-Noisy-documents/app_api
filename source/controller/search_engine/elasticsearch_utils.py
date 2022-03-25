import requests
from elasticsearch import Elasticsearch, helpers
import csv
import os



class Algorithm():
    """A class defining a search algorithm implemented in ElasticSearch.
    """

    def getJson(self): 
        raise NotImplementedError   


class BM25(Algorithm):
    """A class defining the BM25 algorithm in ElasticSearch.
    """
    def __init__(self, k1: int, b: int):
        """The constructor of the class defining the BM25 algorithm in ElasticSearch

        Args:
            k1 (int): A parameter of BM25.
            b (int): A parameter of BM25.
        """
        self.k1 = k1
        self.b = b
    
    def getJson(self):
        """Get the JSON object of the BM25 algorithm in ElasticSearch

        Returns:
            dict: The json object of the algorithm.
        """
        return {"type":"BM25", "k1": self.k1, "b": self.b}


class LMDirichlet(Algorithm):
               
    def __init__(self, mu: int):
        """The constructor of the class defining the LM Dirichlet algorithm in ElasticSearch

        Args:
            mu (int): A parameter of the algorithm.
        """
        self.mu = mu
    
    def getJson(self):
        """Get the JSON object of the LM Dirichlet algorithm in ElasticSearch

        Returns:
            dict: The json object of the algorithm.
        """
        return {"type":"LMDirichlet", "mu": self.mu}

def deleteData():
    requests.delete(ELASTICSEARCH_URI)
    
#TODO https verification
def createInstance(algorithm: Algorithm, stemming: bool):
    #TODO: Do for all fields
    #TODO: Might add transcript/résumé
    query = {"settings": {"index":{"similarity":{"my_similarity":algorithm.getJson()}}}, "mappings":{"properties": {"title": {"type": "text", "similarity": "my_similarity" }}}}
    if stemming == True: 
        query["mappings"]["properties"]["title"]["analyzer"] = "english"

    resp = requests.put(ELASTICSEARCH_URI, json=query)

def loadData(dataSet: str):
    
    with open(dataSet, encoding="utf8") as f:
        data= list(csv.DictReader(f, delimiter="\t", ))

        
        for row in data:
            if row["concepts"] is not None and row["keywords"] is not None:
                keywords = row["keywords"]
                concepts = row["concepts"]
                row["concepts"] = concepts.split("|||")
                row["keywords"] = keywords.split("|||")

        helpers.bulk(ES, data, index='x5gon')

def setSearchEngine(algorithm: Algorithm, stemming: bool, dataSet: str):
    # Delete previous data
    deleteData()
    print("Deleted previous data")
    createInstance(ALGORITHM, stemming)
    print("Created search instance")
    loadData(dataSet)
    print("Loaded data")


#########PARAMETERS############
ALGORITHM = LMDirichlet(mu=1000)
DATASET = "X5GON_content_metadata_dataset/datasets/v1/x5gon_metadata.tsv"
STEMMING = True
ELASTICSEARCH_URI = os.getenv('ELASTICSEARCH_URI')

ES_PASSWORD = os.getenv('ES_PASSWORD')
ES = Elasticsearch(
    ELASTICSEARCH_URI,
    basic_auth=("elastic",ES_PASSWORD)
    )
###############################


if __name__ == "__main__":
    setSearchEngine(ALGORITHM, STEMMING, DATASET)
