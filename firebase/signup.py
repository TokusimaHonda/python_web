import requests
import json


def _sign_up(email, password, displayName):
    # Api key取得
    with open('private/apikey.txt') as f:
        api_key = f.read()

    # 管理者ユーザ追加
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}'.format(api_key)
    headers = {'Content-type': 'application/json'}
    data = json.dumps({'email': email,
                       'password': password,
                       'returnSecureToken': True})

    result = requests.post(url=url,
                           headers=headers,
                           data=data,
                           )

    if 'error' in result.json():
        print('error: {}'.format(result.json()['error']['errors'][0]['message']))
        return result.json()

    # DisplayNameを更新
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:update?key={}'.format(api_key)
    data = json.dumps({
        'idToken': result.json()['idToken'],
        'displayName': displayName
    })

    result = requests.post(url=url,
                           headers=headers,
                           data=data,
                           )

    if 'error' in result.json():
        print('error: {}'.format(result.json()['error']['errors'][0]['message']))
        return result.json()

    return result.json()


if __name__ == '__main__':
    _sign_up('contact@sample.com', 'password', 'rightcode')