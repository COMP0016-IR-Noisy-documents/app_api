
import test.result.constance as const
import pytest
from source.model.searchModel import searchModel
import test.result.constance as const
import requests
from dotenv import load_dotenv

load_dotenv()

'''
search model unit test
'''

class TestMetadata:
    sm = searchModel()

    def test_format_metadata(self):
        assert TestMetadata.sm.format_metadata(requests.get("https://platform.x5gon.org/api/v1/oer_materials/1").text) == (const.metadata_desc, const.metadata_url)

    def test_format_metadata_nometadata(self):
        assert TestMetadata.sm.format_metadata(requests.get("https://platform.x5gon.org/api/v1/oer_materials/136127").text) == ("","")

class TestSearch:
    sm = searchModel()
    def test_search(self):
        assert len(TestSearch.sm.search("french", [])) != 0
    
    def test_search_with_missing_elem(self):
        assert len(TestSearch.sm.search("physics", [])) != 0