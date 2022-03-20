import pytest
import requests
import jwt

import test.result.constance as const

app_url = 'http://127.0.0.1:5000/'

class TestCallback:

    route_url = app_url + 'callback'

    def test_callback(self):
        res = requests.get(TestCallback.route_url, params={const.str_1: const.str_1, const.str_2:const.str_2})
        assert res.status_code == 200
        assert res.json() == {const.str_1: const.str_1, const.str_2:const.str_2}

# class TestSearch:

#     route_url = app_url + 'search'

#     def test_search(self):
#         res = requests.post(TestSearch.route_url, json=const.search_req_no_filter)
#         assert res.status_code == 200
#         assert len(res.json()['result']) > 0

class TestLogin:

    route_url = app_url + 'login'

    def test_login_correct(self):
        res = requests.post(TestLogin.route_url, json=const.mock_user_data_correct)
        assert res.status_code == 200
        assert jwt.get_unverified_header(res.json()['token']) == {  "typ": "JWT","alg": "HS256" }

    def test_login_wrong_password(self):
        res = requests.post(TestLogin.route_url, json=const.mock_user_data_wrong_pass)
        assert res.status_code == 401
        assert res.text == 'wrong password'

    def test_login_no_user(self):
        res = requests.post(TestLogin.route_url, json=const.mock_user_data_no_user)
        assert res.status_code == 401
        assert res.text == 'wrong username'

class TestUserdetails:

    route_login_url = app_url + 'login'
    route_url = app_url + 'login'

    def test_user_detail_no_token(self):
        res = requests.post(TestLogin.route_url, json=const.mock_user_data_correct)
        assert res.status_code == 200
        assert jwt.get_unverified_header(res.json()['token']) == {  "typ": "JWT","alg": "HS256" }

    def test_login_wrong_password(self):
        res = requests.post(TestLogin.route_url, json=const.mock_user_data_wrong_pass)
        assert res.status_code == 401
        assert res.text == 'wrong password'

    def test_login_no_user(self):
        res = requests.post(TestLogin.route_url, json=const.mock_user_data_no_user)
        assert res.status_code == 401
        assert res.text == 'wrong username'
