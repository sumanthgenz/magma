import matplotlib.pyplot as plt
import numpy as np
import requests
import collections
import os
import pandas as pd 
import time

import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def get_video_from_class(query, limit=-1, num_scrolls=0, sleep=1, pix_scroll=1000):
    driver = webdriver.Chrome() 
    vid_filter = "&sp=EgIQAQ%253D%253D" #want only videos
    url = f"https://www.youtube.com/results?search_query={query}{vid_filter}"
    driver.get(url)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    links = [i.get_attribute('href') for i in user_data]
    time.sleep(sleep) 
    for i in range(num_scrolls):
        driver.execute_script(f'window.scrollTo(0,(window.pageYOffset+{pix_scroll}))')
        user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
        links += [i.get_attribute('href') for i in user_data]
        time.sleep(sleep) 
    links = list(set(links))
    driver.close()
    return links[:limit]

def get_audio_from_class(query, qualtype=0, limit=-1, num_scrolls=0, sleep=1, pix_scroll=1000):
    qualifiers = ["sounds", "sound effect", "music", "stock music", "stock sounds"]
    qualifier = qualifiers[qualtype]
    driver = webdriver.Chrome() 
    vid_filter = "&sp=EgIQAQ%253D%253D" #want only videos
    url = f"https://www.youtube.com/results?search_query={query} {qualifier}{vid_filter}"
    driver.get(url)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    links = [i.get_attribute('href') for i in user_data]
    time.sleep(sleep) 
    for i in range(num_scrolls):
        driver.execute_script(f'window.scrollTo(0,(window.pageYOffset+{pix_scroll}))')
        user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
        links += [i.get_attribute('href') for i in user_data]
        time.sleep(sleep) 
    links = list(set(links))
    driver.close()
    return links

def get_image_from_class(query, limit=-1, num_scrolls=0, sleep=1, pix_scroll=2100):
    driver = webdriver.Chrome()
    query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjj9f6EkKrxAhUqQjABHUuVBOoQ_AUoAXoECAgQBA&biw=2793&bih=1154&dpr=0.75"
    driver.get(url)
    src_links, data_src_links = [], []
    
    for i in range(num_scrolls):
        image_links = driver.find_elements_by_css_selector("img.Q4LuWd")
        src_links += [image_links[i].get_attribute('src') for i in range(len(image_links))]
        data_src_links += [image_links[i].get_attribute('data-src') for i in range(len(image_links))]
        time.sleep(sleep) 
        driver.execute_script(f'window.scrollTo(0,(window.pageYOffset+{pix_scroll}))')

    links = list(set(src_links + data_src_links))
    links = [link for link in links if link and "https" in link]
    driver.close()
    return list(links)

def get_text_from_class(query, wiki=True, noisy=True):
    pass