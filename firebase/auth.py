# auth.py内
import requests
import json
from firebase_admin import auth
from datetime import timedelta


def _login(email,password,expires=5):
    with open('private/apikey.txt') as f:
        api_key = f.read()

    url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={}'.format(api_key)
    headers = {'Content-type': 'application/json'}
    data = json.dumps({'email':email,
                       'password':password,
                       'returnSecureToken':True})

    result = requests.post(url=url,
                           headers=headers,
                           data=data,
                           )

    result = result.json()

    print(result)

    # エラーがある場合
    if 'error' in result:
        return result, None

    # セッションクッキーの作成
    session_cookie = auth.create_session_cookie(result['idToken'],timedelta(days=expires))

    return result, session_cookie