import requests
import pytest

URL = "http://api.zippopotam.us/us/90210"
FAIL_URL = "http://api.zippopotam.us/us/90211"


@pytest.fixture()
def get_res():
    response = requests.get(URL)
    yield response


@pytest.fixture()
def get_fail_res():
    response = requests.get(FAIL_URL)
    yield response


def test_oo1(get_res):
    response = get_res

    assert response.status_code == 200

    body = response.json()
    assert body["post code"] == '90210'
    assert body["country"] == 'United States'


def test_oo2(get_fail_res):
    response = get_fail_res
    assert response.status_code == 404
    body = response.json()


# if __name__ == '__main__':
#     test_oo1()


print(2 - 2)
