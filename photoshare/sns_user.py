# ログインなどユーザーに関する処理をまとめた
from flask import Flask, session, redirect
from functools import wraps

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import pyrebase
import json, os

with open("./config/firebaseConfig.json") as f:
    firebaseConfig = json.loads(f.read())
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# ユーザー名とパスワードの一覧 --- (*1)

#DBから読み込むようにする
USER_LOGIN_LIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
    'siro': 'ddd',
    'goro': 'eee' }

# ログインしているかの確認 --- (*2)
def is_login():
    return 'login' in session

# ログインを試行する --- (*3)
#ftakahashidev@gmail.com
#testlogin

def try_login(form):
    email = form.get('user', '')
    password = form.get('pw', '')
    # 認証チェック
    try:
        user_auth = auth.sign_in_with_email_and_password(email, password)
        session['login'] = email
        return True
    except:
        return False



# ユーザー名を得る --- (*4)
def get_id():
    return session['login'] if is_login() else '未ログイン'

# 全ユーザーの情報を得る --- (*5)
def get_allusers():
    return [ u for u in USER_LOGIN_LIST ]

# ログアウトする --- (*6)
def try_logout():
    session.pop('login', None)

# ログイン必須を処理するデコレーターを定義 --- (*7)
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login():
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
