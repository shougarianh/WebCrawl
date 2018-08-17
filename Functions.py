# -*- coding: utf-8 -*-

#Created on Tue Aug  7 15:39:30 2018

import os


# A directory is created in order to create prject folders. Every website is looked at as a seperate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project' + directory)
        os.makedirs(directory)


# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Appending to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:  # using 'a' to append
        file.write(data + '\n')


# Function is created for deleting contents of an existing file
def delete_file_contents(path):
    open(path, 'w').close()


# Reads file and converts each line to set items
# ensures that each item in the set is a unique element of that set making sure
# the same link is not repeated multiple times
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:  # itterates through file one line at a time
            results.add(line.replace('\n', ''))  # Each line is added to the set
            # New line character is replaced
        return results


# Itterate through a set, each item will be a new line in the file
def set_to_file(links, file_name):
    delete_file_contents(file_name) #Deleting all old data
    with open(file_name, "w") as f:
        for l in sorted(links): #Itterates for every link in links 
            f.write(l + "\n") #Adds links to the end of the file as well as new line character