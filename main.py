# -*- coding: utf-8 -*-
#"""
#Created on Tue Aug  7 15:39:30 2018

#Web Crawler Program
#@author: Haik Shougarian
#""
import threading
from Functions import file_to_set
from queue import Queue
from Spider import spider
from domain import get_domain_name

#Each itteration of the program is a new project
PROJECT_NAME = 'Web Crawler'  #Naming the current project
HOMEPAGE ='https://www.reuters.com/' #Gives starting page
DOMAIN_NAME = get_domain_name(HOMEPAGE) #Function is called that gets domain name
QUEUE_FILE = PROJECT_NAME + '/queue.txt' 
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)  # First spider is called 


# creating worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS): #itterates as many times as there are threads
        t = threading.Thread(target=work) 
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get() 
        spider.crawl_page(threading.current_thread().name, url) #crawls page in current thread
        queue.task_done() #finishes crawling


# Each queue link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE): #itterates for every link in the queue
        queue.put(link) #puts links in queue
    queue.join() #makes sure all items in queue are processed 
    crawl() # crawl function is called 


# Check if there are items in queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:  # If there are links in the queue
        print(str(len(queued_links)) + '  links in queue')  # Shows the user how many links are left in the queue
        create_jobs()


create_workers()
crawl()