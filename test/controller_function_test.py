from sqlalchemy import null
import os
import jwt
import datetime as dt
from flask import jsonify
import pytest

from source.controller.security.password import EncPassword
from source.controller.security.token import genJWT, jwt_Token

from source.controller.modifyFormat import modifyFilter


import test.result.constance as const


'''
controller function unit test
'''

class TestAuthentication:
    
    def test_EncPassword_salt_is_generated(self):
        password = EncPassword(const.str_1)
        assert password.getSalt() != None
        assert type(password.getSalt()) == str

    def test_EncPassword_ran_salt_gen_is_not_equal(self):
        password = EncPassword(const.str_1)
        another_password = EncPassword(const.str_1)
        assert password.getSalt() != another_password.getSalt()

    def test_EncPassword_password_is_hashed(self):
        password = EncPassword(const.str_1)
        assert password.getPassword() != const.str_1

    def test_EncPassword_hashed_password_not_equal(self):
        password = EncPassword(const.str_1)
        another_password = EncPassword(const.str_1)
        assert password.getPassword() != another_password.getPassword()
   
    def test_token_enc_can_be_decrypt_by_our_key(self):
        token = genJWT(const.str_1, const.str_2)
        decoded = jwt.decode(token, const.str_2, "HS256")
        assert decoded['public_id'] == const.str_1

    



class TestModifyFilter:
    
    def test_modifyFilter_lang_and_type_null(self):
        modified = modifyFilter(const.filter_lang_null_type_null)
        assert modified == null

    def test_modifyFilter_lang_null(self):
        modified = modifyFilter(const.filter_lang_null)
        assert modified == const.mod_filter_lang_null

    def test_modifyFilter_type_null(self):
        modified = modifyFilter(const.filter_type_null)
        assert modified == const.mod_filter_type_null

    def test_modifyFilter_type_one_element(self):
        modified = modifyFilter(const.filter_type_one_element)
        assert modified == const.mod_filter_type_one_element

    def test_modifyFilter_lang_one_element(self):
        modified = modifyFilter(const.filter_lang_one_element)
        assert modified == const.mod_filter_lang_one_element

    def test_modifyFilter_general_case(self):
        modified = modifyFilter(const.filter_general)
        assert modified == const.mod_filter_general

    

 

        

