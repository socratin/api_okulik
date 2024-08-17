import allure
import requests

from endpoints.base_endpoint import Endpoint


class CreateToken(Endpoint):
    token = None
    name = "name_for_tests"

    @allure.step('Получение нового токена')
    def get_new_token(self, headers=None, name=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}/authorize',
            json={"name": name if name else self.name},
            headers=headers
        )
        self.json = self.response.json()
        self.token = self.json["token"]
        return self.token

    @allure.step('Проверка получения токена')
    def check_response_token_is_correct(self):
        assert len(self.token) > 14
