#!/usr/bin/python
# -*- coding: ISO-8859-1 -*- 
blob = """ 
    �|���:A3/{�����W0HFC!�N(N�u��H�����T�=�v��m���'M�{t뼠�5o��䪟�+�m2$]m��k�h����� g�_h��["��G�Ux|T��ae�x�1"�{�e��=�"""
from hashlib import sha256
print(sha256(blob.encode()).hexdigest()) 
