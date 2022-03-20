# -*- coding:utf-8 -*-


str_1 = 'abc'
str_2 = 'def'
str_3 = 'ghi'

filter_lang_null_type_null = {"language": [], "type": []}
filter_type_null = {"language": ["sl"], "type": []}
filter_lang_null = {"language": [], "type": ["doc"]}
filter_type_one_element = {"type":["docx"],"language":["sl","de","es"]}
filter_lang_one_element = {"language": ["sl"], "type": []}
filter_general = {"type":["docx","odt","rtf","txt","docx","odt","rtf","txt"],"language":["sl","de","es"]}

mod_filter_type_null= {
                "bool":
                {
                    "must": {"term": {"language": "sl"}}
                }
            }
mod_filter_lang_null = {
                "bool":
                {
                    "must": {"term": {"type": "doc"}}
                }
            }
mod_filter_type_one_element = {
                "bool": {
                    "must": [
                        {"term": {"type": "docx"}},
                        {"terms": {"language": ["sl","de","es"]}}
                    ]
                }
            }
mod_filter_lang_one_element = {
                "bool":
                {
                    "must": {"term": {"language": "sl"}}
                }
            }
mod_filter_general = {
                "bool": {
                    "must": [
                        {"term": {"type": ["docx","odt","rtf","txt","docx","odt","rtf","txt"]}},
                        {"terms": {"language": ["sl","de","es"]}}
                    ]
                }
            }

search_req_no_filter = {
  "query": "bat",
  "filter": {
    "type": [],
    "language": []
  }
}

# for login route
mock_user_data_correct = {
    "username": "Admin",
    "password": "56789"
}

mock_user_data_wrong_pass = {
    "username": "Admin",
    "password": "567899"
}

mock_user_data_no_user = {
    "username": "Adminssssss",
    "password": "567899"
}

# for user detail
mock_user_detail_header_no_token = {
    'Content-Type': 'application/json',
}

mock_user_detail_header_invalid_token = {
    'Content-Type': 'application/json',
    'x-access-token': eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiJmMzE1ODQ1ZS1iZjlkLTQ1MGYtOGIxZi04YmY0NDgzODVjZGIiLCJleHAiOjE2MDc4MDA0ODZ9.0RL4RffEa5Pi3L918nTPZuPdmJD_weqMioXGDQVnXVA
}

mock_user_detail_header_expire_token = {
    'Content-Type': 'application/json',
    'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiJmMzE1ODQ1ZS1iZjlkLTQ1MGYtOGIxZi04YmY0NDgzODVjZGIiLCJleHAiOjE2MDc4MDA0ODZ9.AuWbw_Ko0OF9rPUy7yqv0eqZKdC0-F4eyB2b--WRG1Q'
}