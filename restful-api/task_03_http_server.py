import requests
import csv

def fetch_and_print_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        """ Parse the fetched data into a JSON object"""
        posts = response.json()

        # Print titles of all posts
        for post in posts:
            print(post["title"])

        # Structure data into a list of dictionaries
        post_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        """Write data to a CSV file"""
        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(post_data)

fetch_and_print_and_save_posts()
