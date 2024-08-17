import pytest

from data.payloads import PayloadNormal
from endpoints.authorize import CreateToken
from endpoints.meme import Meme


@pytest.fixture(scope="function")
def token():
    return CreateToken()


@pytest.fixture(scope="function")
def new_token():
    token = CreateToken()
    token.get_new_token()
    return token.token


@pytest.fixture(scope="function")
def meme_page():
    return Meme()


@pytest.fixture(scope="function")
def create_meme_and_delete(new_token):
    meme_page = Meme()
    meme_page.add_new_meme(new_token, payload=PayloadNormal.payload)
    id_meme = meme_page.created_new_meme.json()['id']
    yield id_meme
    meme_page.delete_meme(new_token, id_meme)
