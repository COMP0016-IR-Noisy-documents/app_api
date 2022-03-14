import numpy as np
import pandas as pd

from x5gon_content_metadata_dataset.io import load_dataset

K1 = 2
B = 0.75


class SimpleSearchEngine():
    # Simple search engine algorithm implementation using the BM25 search model
    # See https://en.wikipedia.org/wiki/Okapi_BM25 

    def __init__(self):
        # Initialise the dataFrame
        self.documentList = load_dataset("X5GON_content_metadata_dataset/datasets/v1/x5gon_metadata.tsv")\
        .filter(["id","title","type","language","keywords","concepts"])

        # Calculate the avgdl (Average document length) for both rows in advance
        self.titleAvgdl = self.getAvgDl(self.documentList['title']) 
        self.keywordsAvgdl = self.getAvgDl(self.documentList['keywords']) 
        
    def getAvgDl(self, documentList: pd.Series) -> int:

        """
        Get the average length(in words) of a pandas series object

        documentList : Series
        returns : int

        """

        sumNbWords = 0
        # Get row lengh

        for document in documentList:

                if isinstance(document, str):
                        document = document.split()

                sumNbWords += len(document)
        
        nbOfDocs = len(documentList)

        return sumNbWords / nbOfDocs
    def search(self, query: str):

        """
        The search method takes a query string and return a dataframe corresponding to the search result
        query: the query input to the search engine
        """

        # BM25 Score for the title and concept columns
        titleScores = DocumentListScorer(query, self.documentList['title'], self.titleAvgdl).scoreDocumentList()
        conceptScores = DocumentListScorer(query, self.documentList['keywords'], self.keywordsAvgdl).scoreDocumentList()

        # Create a global score array
        # Score = 1.75* score_title + score_concept (for each row)
        score = [(1.75*titleScores[i]) + conceptScores[i] for i in range(len(titleScores))]

        self.documentList['score'] = score

        result = self.documentList[self.documentList['score'] != 0]
        
        return result.sort_values(by=['score'], ascending=False)




class DocumentListScorer():
    """
    Object to create a list of scores for document with a query using the Okapi BM25 algorithm
    """

    def __init__(self, query: str, documentList: pd.Series, avgdl: int):
        self.query = query

        self.documentList = documentList
        
        self.avgdl = avgdl

        # Dictionnary containing the number of documents in which each query term appears
        self.nbContainingPerQueryTerm = {}
        self.genNbContainingArray()
    
    

    def genNbContainingArray(self):
        """
        Generate the dictionnary containing the number of documents in which each query term appears
        """
        for queryTerm in self.query.split():
            nbContaining = 0
            for document in self.documentList:
                if isinstance(document, str):
                        document = document.split()
                
                for word in document:
                    
                    if queryTerm.lower() == word.lower():
                        nbContaining +=1
                        break

            self.nbContainingPerQueryTerm[queryTerm] = nbContaining

        

    def scoreDocumentList(self) -> list:
        """
        Give a score to all of the document in the list
        """

        scores = []
        for document in self.documentList:
            if len(document) == 0 or document == ['nan']:
                score = 0
            score = self.scoreDoc(document)
            
            scores.append(score)

        return scores
    
    def scoreDoc(self, document) -> float:
        """
        Score a document with the query : Add the score for all the lexemes in  the query string.
        """

        score = 0

        for queryTerm in self.query.split():
            score += self.scoreQueryTerm(queryTerm, document)
        return score
    
    def scoreQueryTerm(self, queryTerm: str, document) -> float:
        """
        Give a score to a document under a query term according to the BM25 algorithm formula.
        """
        fracTop = self.termFrequency(queryTerm, document) * (K1 + 1)
        #Small optimisation : if the term frequency is zero return 0
        if fracTop == 0:
            return 0

        fracBottom = (self.termFrequency(queryTerm, document) + K1 * (1 - B + B * (self.lengthOfDoc(document) / self.avgdl)))

        IDF = self.inverseDocumentFrequency(queryTerm)

        frac = fracTop / fracBottom

        return IDF * frac

    def inverseDocumentFrequency(self, queryTerm: str) -> float:
        """
        Inverse document frequency 
        """
        # IDF
        idf = np.log((len(self.documentList) - self.nbContaining(queryTerm) + 0.5)/(self.nbContaining(queryTerm) + 0.5) + 1)

        return idf
     
     
    def nbContaining(self, queryterm: str) -> int:
        # Number of Docs containing term
        return self.nbContainingPerQueryTerm[queryterm]


    def lengthOfDoc(self, document) -> int:

        if isinstance(document, str):
                        document = document.split()

        return len(document)

        
    def termFrequency(self, queryTerm : str, document) -> int:

        """
        returns how much a query term appears in a certain document
        """
        freq = 0

        if isinstance(document, str):
                        document = document.split()

        for term in document:
            if queryTerm.lower() == term.lower():
                freq +=1
        
        return freq

