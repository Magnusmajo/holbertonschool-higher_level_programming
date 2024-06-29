#!/usr/bin/python3

import requests
import csv

def fetch_and_save_posts():
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {req.status_code}")

    if req.status_code == 200:
        data = req.json()
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            w.writeheader()
            w.writerows([{'id': d['id'], 'title': d['title'], 'body': d['body']} for d in data])
    else:
        print("Fail to fetch")

fetch_and_save_posts()