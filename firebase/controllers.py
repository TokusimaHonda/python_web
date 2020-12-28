import responder
from auth import _login

api = responder.API()


@api.route('/')  # ルートは index() に投げる
def index(req, resp):
    resp.html = api.template('index.html',title='')

firebase_error_massages = {
    'EMAIL_NOT_FOUND': 'メールアドレスが正しくありません',
    'INVALID_PASSWORD': 'パスワードが正しくありません',
}

@api.route('/login')
def login(req, resp):
    # エラーがあれば取得
    error = req.params.get('error','')
    if error in firebase_error_massages:
        error = firebase_error_massages[error]

    resp.html = api.template('login.html',
                             title='Login',
                             error=error
                             )


@api.route('/admin')
class Admin:
    async def on_get(self, req, resp):
        api.redirect(resp,'/login')

    async def on_post(self,req,resp):
        # POSTデータを取得
        data = await req.media()
        email = data['email']
        password = data['password']

        # 認証
        res, session = _login(email,password)

        if 'error' not in res:
            # 認証成功ならば管理者ページへ
            resp.html = api.template('admin.html',
                                    title='管理者ページ',
                                    token=res['idToken'],
                                    name=res['displayName'])
        else:
            # 認証失敗ならばエラーメッセージをログイン画面に渡してリダイレクト
            api.redirect(resp,'/login?error={}'.format(res['error']['errors'][0]['message']))