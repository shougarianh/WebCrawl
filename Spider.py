# -*- coding: utf-8 -*-
#"""
#Created on Wed Aug  8 14:20:50 2018

#@author: Haik Shougarian
#"""
from urllib.request import urlopen
from link_finder import LinkFinder
#Importing functions that are needed
from Functions import create_project_dir
from Functions import create_data_files
from Functions import file_to_set
from Functions import set_to_file
from domain import get_domain_name


class spider:
    # class variables. Shared among all instances
    #Preallocating all variables and sets
    project_name = ''
    homepage_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, homepage_url, domain_name):
        spider.project_name = project_name 
        spider.homepage_url = homepage_url
        spider.domain_name = domain_name
        spider.queue_file = spider.project_name + '/queue.txt'
        spider.crawled_file = spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider ', spider.homepage_url)

    @staticmethod
    def boot():
        create_project_dir(spider.project_name) #Creates a new project directory
        create_data_files(spider.project_name, spider.homepage_url) #Creates crawled and queue files
        spider.queue = file_to_set(spider.queue_file) # converts everything in the file to a set
        spider.crawled = file_to_set(spider.crawled_file) # converts everythign in the file to a set

    @staticmethod
    def crawl_page(thread_name, page_url): 
        if page_url not in spider.crawled:#if the link has not already been crawled 
            print(thread_name + 'Now crawling ' + page_url) #Display message to user
            #Shows how many links are in queue and crawled files 
            print('Queue ' + str(len(spider.queue)) + ' | Crawled ' + str(len(spider.crawled)))
            #links to be crawled are added to the queue
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url) #remove link frok queue
            spider.crawled.add(page_url) #Add link to crawled
            spider.update_files() # Updating/converting sets to files

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url) #goes to page url 
            if 'text/html' in response.getheader('Content-Type'): #checks the content type
                html_bytes = response.read() #reads the html
                html_string = html_bytes.decode("utf-8") # decodes html
            finder = LinkFinder(spider.homepage_url, page_url) 
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in spider.queue) or (url in spider.crawled):
                continue
            if spider.domain_name != get_domain_name(url):
                continue
            spider.queue.add(url)

    @staticmethod
    def update_files():
         #Takes set of queued links and puts them in the queue file
        set_to_file(spider.queue, spider.queue_file) 
        # Takes set of crawled links and puts themm in the crawled file 
        set_to_file(spider.crawled, spider.crawled_file) 





















