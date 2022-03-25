
import test.result.constance as const
import pytest
from source.model.searchModel import searchModel
import test.result.constance as const
import requests

'''
search model unit test
'''
sm = searchModel()
class TestMetadata:

    def test_format_metadata(self):
        assert sm.format_metadata(requests.get("https://platform.x5gon.org/api/v1/oer_materials/1").text) == (const.metadata_desc, const.metadata_url)

    def test_format_metadata_nometadata(self):
        assert sm.format_metadata(requests.get("https://platform.x5gon.org/api/v1/oer_materials/136127").text) == ("","")

class TestSearch:
    def test_search(self):
        assert len(sm.search("french", [])) != 0
    
    def test_search_with_missing_elem(self):
        assert len(sm.search("physics", [])) != 0