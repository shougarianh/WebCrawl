# -*- coding: utf-8 -*-
#"""
#Created on Wed Aug  8 15:16:25 2018

#@author: Haik Shougarian
#"""

from urllib.parse import urlparse


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.') # Creates list of elements of the url
        return results[-2] + '.' + results[-1] #Returns 2nd to last and last elements of url
    except:
        return '' #in case of error endures something is returned 


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc #parses through url and returns network location
    except:
        return '' #If try function doesnt work, makes sure something is returned
