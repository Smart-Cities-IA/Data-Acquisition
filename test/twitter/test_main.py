from src.twitter.main import make_url

BASE_URL = "https://api.twitter.com/2/tweets/" 

def test_make_url_no_space():
    keyword = "environment"
    actual_url = make_url(BASE_URL, keyword)
    expected_url = "https://api.twitter.com/2/tweets/counts/recent?query=environment"
    assert actual_url == expected_url

def test_make_url_with_space():
    keyword = "smart lighting"
    actual_url = make_url(BASE_URL, keyword)
    expected_url = "https://api.twitter.com/2/tweets/counts/recent?query=smart lighting OR smartlighting"
    assert actual_url == expected_url

