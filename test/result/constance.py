# -*- coding:utf-8 -*-


str_1 = 'abc'
str_2 = 'def'
str_3 = 'ghi'

filter_lang_null_type_null = {"language": [], "type": []}
filter_lang_null = {"type": [], "language": ["sl"]}
filter_type_null = {"type": ["pdf"], "language": []}
filter_lang_one_element = {"language":["sl","de","es"],"type":["docx"]}
filter_type_one_element = {"ltype": [], "language": ["sl"]}
filter_general = {"language":["sl","de","es"],"type":["docx","odt","rtf","txt","docx","odt","rtf","txt"]}

mod_filter_type_null= [{"terms": {"language": ["pdf"]}}]

mod_filter_lang_null = [{"terms": {"type": ["sl"]}}]
            
mod_filter_lang_one_element =  [{"terms": {"type": ["sl", "de", "es"]}}, {"terms": {"language": ["docx"]}}]

mod_filter_type_one_element = [{"terms": {"type": ["sl"]}}]

mod_filter_general = [{"terms": {"type": ["sl","de","es"]}}, {"terms": {"language": ["docx","odt","rtf","txt","docx","odt","rtf","txt"]}}]

search_filter_one = [{"terms": {"type": ["fr"]}}, {"terms": {"language": ["mp4"]}}]
search_filter_two = [{"terms": {"type": ["fr", "en"]}}]
search_filter_three = [{"terms": {"type": ["fr", "en"]}}, {"terms": {"language": ["mp4"]}}]

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
    'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiJmMzE1ODQ1ZS1iZjlkLTQ1MGYtOGIxZi04YmY0NDgzODVjZGIiLCJleHAiOjE2MDc4MDA0ODZ9.0RL4RffEa5Pi3L918nTPZuPdmJD_weqMioXGDQVnXVA'
}

mock_user_detail_header_expire_token = {
    'Content-Type': 'application/json',
    'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiJmMzE1ODQ1ZS1iZjlkLTQ1MGYtOGIxZi04YmY0NDgzODVjZGIiLCJleHAiOjE2MDc4MDA0ODZ9.AuWbw_Ko0OF9rPUy7yqv0eqZKdC0-F4eyB2b--WRG1Q'
}

metadata_desc = "“Cinema is the art of moving image destruction,” says Paolo Cherchi Usai. Although he claims that a\r\nfilm is condemned to degradation due to the damage acquired during each projection, this judgement\r\ncould also refer to the low sustainability of film, caused by its material form.\r\n\r\nThis appeared in various historical ruptures, which have proved short life-span to be an immanent\r\ncharacteristic of the filmic base because of its chemical structure. After a big number of archives\r\nburned in devastating fires due to the high inflammability of the nitrate base, the latter was replaced by\r\nthe triacetate celluloid carrier as a more sustainable medium. However, shortly after the discovery, the\r\ntriacetate base started showing signs of rapid degradation accompanied by emissions of acid fumes\r\ninto the air that surrounds the degraded material. The resulting distinctive smell contributed to terming\r\nthis process of decay vinegar syndrome or the illness of triacetate film. The process is irreversible and\r\ninevitable – at best, it can only be decelerated by maintaining the proper storage conditions in climate\r\ncontrolled vaults. The main action that can be taken is the timely evaluation of the state of the\r\ncollection, which can be performed with pH indicator strips and followed by the optimization of storage\r\nconditions. Nowadays, when celluloid film on triacetate base represents the large-scale portion of\r\nmoving image collections, the vinegar syndrome is a critical issue that is affecting a great deal of\r\naudiovisual heritage institutions. One of the solutions for the preservation of elements in precarious\r\nstate lies in scanning and migration to the digital medium. However, this action should not be taken\r\nwithout being preceded by the appropriate conservation strategies. The long-term preservation of\r\ndegraded materials can only be assured by the assessment of the degradation state and prioritization\r\nof elements based on their condition."
metadata_url = "http://hydro.ijs.si/v014/6e/nzbynfzw3umn4kkfclqyu6jeuhhxu2vf.pdf"
