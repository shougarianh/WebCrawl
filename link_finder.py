# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:53:23 2018

@author: Haik Shougarian
"""
from html.parser import HTMLParser #for sifting through html code
from urllib import parse 

class LinkFinder(HTMLParser): #Keeping functionality of HTMLparser within LinkFinder class
    #Constructor function reserved for initializing the class
    def __init__(self,homepage_url,page_url):
        super().__init__()
        #Using self to access attributes and methods within the class
        self.homepage_url = homepage_url
        self.page_url = page_url
        self.links = set()
    def handle_starttag(self,tag,attrs):
        if tag == 'a': #if the starting tag is a link
            for(attribute,value) in attrs: #for atribute int all attributes
                if attribute == 'href': # if the attribute is a link.
                    #Makes sure that there is a full URL. If there isnt, 
                    #the hompage url is joined with the found value to make it
                    #into a full url
                    url = parse.urljoin(self.homepage_url,value) 
                    self.links.add(url)# Adds properly formated link to the set
                    
    #This function is used to return the set of links gathered in the LinkFinder class
    def page_links(self): 
        return self.links
        
    def error(self,message): #Used in case of error 
        pass

    