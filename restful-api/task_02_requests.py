#!/usr/bin/python3
import requests
import csv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    def fetch_and_print_posts():
        response = requests.get(f'{url}/posts')
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post['title'])

    def fetch_and_save_posts():
        response = requests.get(f'{url}/posts')
        if response.status_code == 200:
            posts = response.json()
            with open('posts.csv', 'w') as file:
                writer = csv.DictWriter(file, fieldnames=['userId', 'id', 'title', 'body'])
                writer.writeheader()
                for post in posts:
                    writer.writerow(post)
