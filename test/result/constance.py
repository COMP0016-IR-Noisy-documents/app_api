# -*- coding:utf-8 -*-


str_1 = 'abc'
str_2 = 'def'
str_3 = 'ghi'

filter_lang_null_type_null = {"Language": [], "Type": []}
filter_type_null = {"Language": ["sl"], "Type": []}
filter_lang_null = {"Language": [], "Type": ["doc"]}
filter_type_one_element = {"Type":["docx"],"Language":["sl","de","es"]}
filter_lang_one_element = {"Language": ["sl"], "Type": []}
filter_general = {"Type":["docx","odt","rtf","txt","docx","odt","rtf","txt"],"Language":["sl","de","es"]}

mod_filter_type_null= {
                "bool":
                {
                    "must": {"term": {"Language": "sl"}}
                }
            }
mod_filter_lang_null = {
                "bool":
                {
                    "must": {"term": {"Type": "doc"}}
                }
            }
mod_filter_type_one_element = {
                "bool": {
                    "must": [
                        {"term": {"Type": "docx"}},
                        {"terms": {"Language": ["sl","de","es"]}}
                    ]
                }
            }
mod_filter_lang_one_element = {
                "bool":
                {
                    "must": {"term": {"Language": "sl"}}
                }
            }
mod_filter_general = {
                "bool": {
                    "must": [
                        {"term": {"Type": ["docx","odt","rtf","txt","docx","odt","rtf","txt"]}},
                        {"terms": {"Language": ["sl","de","es"]}}
                    ]
                }
            }