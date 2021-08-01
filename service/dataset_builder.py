import pickle
import glob
import random
from tqdm import tqdm
import os
import collections
import urllib
import urllib.request
from urllib.request import Request, urlopen
import json
import shutil

class DatasetBuilder:

    def __init__(self, name, data_type, classes, class_size):
        self.name = name
        self.data_type = data_type
        self.classes = classes
        self.class_size = class_size

    def download_page(self, url):
        headers = {}
        headers[
            'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        req = urllib.request.Request(url, headers=headers)
        return str(urllib.request.urlopen(req).read())

    def fetch_google_images(self, query, image_limit=10):
        search_url = 'https://www.google.com/search?q={}&tbm=isch'.format('+'.join(urllib.parse.quote(k) for k in query))
        raw_html = self.download_page(search_url)
        if raw_html is None:
            return []
        images = [img.replace("src=", "").split(';')[0][1:] for img in raw_html.split(" ") if "src=" in img and "https://" in img]
        return images[:image_limit]


    def get_text_vocab(self, prefix='train', pos='verb', topk=1000):
        pass

    def save_imgs(self, class_name, images):
        dir = f'test_images/{class_name}'
        if not os.path.exists(dir):
            os.makedirs(dir)

        for i, url in enumerate(images):
            urllib.request.urlretrieve(url, f'{dir}/{i}.jpg')

    def remove_folders(self, query):
        pass
            

    def get_data(self):
        dataset = {}
        for query in self.classes:
            dataset[query] = self.fetch_google_images(query, self.class_size)
        return dataset

if __name__ == "__main__":

    queries = ["strawberry", "the green knight", "tyler the creator", "pizza", "zurich"]

    builder = DatasetBuilder("movies", queries, 10)
    dataset = builder.get_data()
    for k in dataset:
        builder.save_imgs(k, dataset[k])
