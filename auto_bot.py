import json
import requests
import random

with open("info.json") as f:
    data = json.load(f)


def create_users():
    for user in range(data['user']):
        info = {
            "email": f"user_{user + 1}@gmail.com",
            "new_password": f"{user + 1}" * 5,
            "new_password_confirm": f"{user + 1}" * 5
        }
        requests.post('http://127.0.0.1:8000/api/v1/account/signup/', data=info)
        create_post(user)


def login(user):
    info = {
        "email": f"user_{user + 1}@gmail.com",
        "password": f"{user + 1}" * 5,
    }
    res = requests.post('http://127.0.0.1:8000/api/v1/account/login/', data=info).json()
    return res['token']


def create_post(user):
    token = login(user)
    headers = {
        'content-type': 'application/json',
        "authorization": f"Bearer {token}"
    }
    for i in range(random.randint(1, data['post'])):
        post = {
            "title": f"title_{user+1}_{i+1}",
            "content": f"content_{user+1}_{i+1}",
        }
        requests.post('http://127.0.0.1:8000/api/v1/posts/', data=json.dumps(post), headers=headers)


def get_posts(user):
    token = login(user)
    headers = {
        'content-type': 'application/json',
        "authorization": f"Bearer {token}"
    }
    return requests.get('http://127.0.0.1:8000/api/v1/posts/', headers=headers).json()


def like():
    for i in range(data['user']):
        token = login(i)
        count_like = random.randint(1, data['like'])
        headers = {
            'content-type': 'application/json',
            "authorization": f"Bearer {token}"
        }
        posts = get_posts(i)
        for j in range(count_like):
            index_post = random.randint(0, len(posts)-1)
            post = posts[index_post]
            requests.post(f'http://127.0.0.1:8000/api/v1/posts/{post["id"]}/like/', headers=headers)


if __name__ == "__main__":
    create_users()
    like()
