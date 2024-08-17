import random

import allure
import requests

from endpoints.base_endpoint import Endpoint


class Meme(Endpoint):
    all_list_meme = None
    list_id_of_meme = []
    meme_for_id = None
    created_new_meme = None
    updated_meme = None

    @allure.step("Получение списка всех мемов")
    def get_list_all_meme(self, token):
        response = requests.get(f'{self.url}/meme', headers={'Authorization': f'{token}'})
        self.all_list_meme = response.json()['data']
        for item in self.all_list_meme:
            self.list_id_of_meme.append(item['id'])

    @allure.step("Проверка фактического получения списка всех мемов")
    def check_get_leist_meme(self):
        assert len(self.all_list_meme) > 0

    @allure.step("Получение одного meme по id")
    def get_one_meme(self, token):
        self.get_list_all_meme(token)
        response = requests.get(f'{self.url}/meme/{random.choice(self.list_id_of_meme)}',
                                headers={'Authorization': f'{token}'})
        self.meme_for_id = response.json()

    @allure.step("Проверка фактического получения одного meme по id")
    def check_info_about_meme_for_id(self):
        fact_keys = set(self.meme_for_id.keys())
        expected_keys = {'id', 'info', "tags", 'text', 'updated_by', 'url'}
        assert fact_keys == expected_keys

    @allure.step("Создание нового мема")
    def add_new_meme(self, token, payload):
        expected_keys = {'id', 'info', "tags", 'text', 'updated_by', 'url'}
        self.created_new_meme = requests.post(f'{self.url}/meme', headers={'Authorization': f'{token}'}, json=payload)
        assert expected_keys == set(self.created_new_meme.json().keys())

    @allure.step("Отправка Put запроса для обновления данных мема")
    def update_data_meme(self, token, create_meme_and_delete):
        id_meme = create_meme_and_delete
        payload = {'id': id_meme, 'info': {'colors': ['blerthue', 'wegtrhhite'], 'objects': ['picture', 'text']},
                   'tags': ['mosquito', 'spray'],
                   'text': 'Loll', 'updated_by': 'new_1_name', 'url': 'ftp://example2134.com'}
        self.updated_meme = requests.put(f'{self.url}/meme/{id_meme}', headers={'Authorization': f'{token}'},
                                         json=payload)
        assert payload['info'] == self.updated_meme.json()['info']

    @allure.step("Удаление мема")
    def delete_meme(self, token, id_meme):
        response = requests.delete(f'{self.url}/meme/{id_meme}', headers={'Authorization': f'{token}'})
        assert response.status_code == 200

    @allure.step('Получение мема по ID')
    def get_meme_by_id(self, token, id_meme):
        response = requests.get(f'{self.url}/meme/{id_meme}', headers={'Authorization': f'{token}'})
        assert response.status_code == 404

    @allure.title("Создание мема с незаполненным полем Text")
    def add_new_meme_with_empty_text(self, token, payload):
        self.created_new_meme = requests.post(f'{self.url}/meme', headers={'Authorization': f'{token}'}, json=payload)
        assert self.created_new_meme.status_code == 400
