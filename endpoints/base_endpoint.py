import allure


class Endpoint:
    url = 'http://167.172.172.115:52355/'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Проверка кода ответа 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверка имени товара')
    def check_that_name_is_correct(self, name):
        assert self.json['name'] == name
