import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os
import pickle

driver = webdriver.Chrome()
url = 'https://www.naukri.com/machine-learning-jobs'
driver.get(url)
time.sleep(4)

parent_handle = driver.current_url
print(parent_handle)


dict_links = {}
count = 0
for k in range(1, 350):
    if k == 1:
        a = driver.find_elements_by_class_name("title.fw500.ellipsis")
        for i in a:
            if (str(i.get_attribute('href')) != 'None'):
                count += 1
                dict_links[count] = i.get_attribute('href')
    else:
        url = 'https://www.naukri.com/machine-learning-jobs-'+str(k)
        print(url)
        driver.get(url)
        time.sleep(3)
        a = driver.find_elements_by_class_name("title.fw500.ellipsis")
        for i in a:
            if (str(i.get_attribute('href')) != 'None'):
                count += 1
                dict_links[count] = i.get_attribute('href')
    print(k)


print(len(dict_links))

file_to_write = open("machine_learning.pickle", "wb")

pickle.dump(dict_links, file_to_write)

df = pd.read_pickle(r'machine_learning.pickle')
print(len(df))

d = {}
for i in df:
    if(df[i] in d):
        d[df[i]] += 1
    else:
        d[df[i]] = 0
print(len(d))
