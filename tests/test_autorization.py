import allure


@allure.title("Проверка токена на дееспособность")
def test_is_live_token(token):
    token.get_new_token()
    token.check_response_token_is_correct()


@allure.title("Проверка получени токена при имени  на кирилице")
def test_get_new_token_cyrilic_name(token):
    token.get_new_token(name="Иван")
    token.check_response_token_is_correct()


@allure.title("Проверка получени токена при имени спец символами")
def test_get_new_token_special_name(token):
    token.get_new_token(name="!@#$%^&*()_+")
    token.check_response_token_is_correct()


@allure.title("Получение токена с пустым именем")
def test_get_new_token_empty_name(token):
    token.get_new_token(name="")
    token.check_response_token_is_correct()
