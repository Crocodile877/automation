import requests

def test_resp100():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100