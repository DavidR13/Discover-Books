import requests
from Flask_Directory import json_functions
import os


def request_key():
    abs_path = os.environ['ABS_PATH']
    api_key_file = json_functions.read_from_file(f'{abs_path}/keys.json')
    api_key = api_key_file["API_KEY"]
    return api_key


def request_best_sellers(date, name):
    best_sellers_url = "https://api.nytimes.com/svc/books/v3/lists/" + date + "/" + name + ".json?api-key=" + request_key()
    best_sellers_response = requests.get(best_sellers_url).json()

    return best_sellers_response


def request_book_reviews_isbn(isbn):
    reviews_isbn_url = "https://api.nytimes.com/svc/books/v3/reviews.json?isbn=" + str(isbn) + "&api-key=" + request_key()
    reviews_isbn_response = requests.get(reviews_isbn_url).json()

    return reviews_isbn_response


def request_book_reviews_title(title):
    reviews_title_url = "https://api.nytimes.com/svc/books/v3/reviews.json?title=" + title + "&api-key=" + request_key()
    reviews_title_response = requests.get(reviews_title_url).json()

    return reviews_title_response


def request_book_reviews_author(author):
    reviews_author_url = "https://api.nytimes.com/svc/books/v3/reviews.json?author=" + author + "&api-key=" + request_key()
    reviews_author_response = requests.get(reviews_author_url).json()

    return reviews_author_response
