import requests

URL = 'http://127.0.0.1:5000/users/'

# тест, который отправляет последовательно три запроса, содержащих валидный UserID;
# параметр expected означает ожидаемый ответ от веб-сервиса


def test_request(expected):
    received = []               # список значений, полученных от веб-сервиса
    response0 = requests.get('%s1' % URL).status_code
    response1 = requests.get('%s2' % URL).status_code
    response2 = requests.get('%s3' % URL).status_code
    received.append(response0)
    received.append(response1)
    received.append(response2)
    assert expected == received

# тест запрашивает данные о несуществующем ID


def test_userid_out_of_range(expected):
    response = requests.get('%s4' % URL).status_code
    assert expected == response


# тест пытается отправить PUT-request


def test_modify_user(expected):
    users = {'3': {
        'responseType': 'userInfo',
        'name': 'some_name'
    }}
    response = requests.put(URL, json=users).status_code
    assert expected == response

# тест пытается запросить данные о пользователе с ID, отличным от целочисленного


def test_wrong_userid(expected):
    response = requests.get('%s&)^' % URL).status_code
    assert response == expected


test_request([200, 200, 200])
test_modify_user(404)
test_userid_out_of_range(500)
test_wrong_userID(500)
