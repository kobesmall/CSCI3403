#!/usr/bin/python
# -*- coding: ISO-8859-1 -*- 
blob = """ 
    �|���:A3/{������0HFC!�N(N�u��H�����TϽ�v��m���'M�{�뼠�5o��䪟�+�m2$]m��kh����� g�_h��["��G�Ux|Td�ae�x�1"�{�e�=�"""
from hashlib import sha256
print(sha256(blob.encode()).hexdigest()) 
