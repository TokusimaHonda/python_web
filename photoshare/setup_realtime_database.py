import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd

# realtime database接続情報
cred = credentials.Certificate('./config/realtime_database.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python-work-be99f.firebaseio.com',
})

ref_hinatazaka = db.reference('/hinatazaka')

dic_initial_data = {
        '1': {
            'name': '小坂菜緒',
            'email': 'kosaka@gr8-bizhack.com'
        },
        '2': {
            'name': '東村芽衣',
            'email': 'higashimura@gr8-bizhack.com'
        },
        '3': {
            'name': '佐々木久美',
            'email': 'ksasaki@gr8-bizhack.com'
        },
        '4': {
            'name': '丹生明里',
            'email': 'nibu@gr8-bizhack.com'
        }
    }

dic_insert_data = {
        '0': {
            'name': '高橋冬樹',
            'email': 'ftakahashi@gr8-bizhack.com'
        },
        '5': {
            'name': '高本彩花',
            'email': 'takamoto@gr8-bizhack.com'
        },
        '6': {
            'name': '金村美久',
            'email': 'kanemura@gr8-bizhack.com'
        }
    }




def initial_data_registration(ref,dic_initial_data):
    # 初期データ書き込み
    ref.set(dic_initial_data)

def db_insert(ref,dic_insert_data):
    # データ追加
    for insert_key, insert_value in dic_insert_data.items():
        ref.child(insert_key).set(insert_value)

def db_update(ref,dic_update_data):
    # データ更新
    for update_key, update_value in dic_update_data.items():
        ref.child(update_key).update(update_value)

def db_remove(ref,child):
    # データ削除
    ref.child(child).remove()

def db_select(ref):
    # データ取得
    return ref.get()

def main():
    # DBへ書き込み
    
    ##データを取得する
    #db_insert(ref_hinatazaka)
    #print(pd.DataFrame(db_select(ref_hinatazaka)))
    #print(db_select(ref_hinatazaka))
    db_update(ref_hinatazaka,dic_insert_data)
    


if __name__ == '__main__':
    main()