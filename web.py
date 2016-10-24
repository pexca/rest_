from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/users/<userid>')
def api_user(userid):
    users = {'1': {'responseType': 'userInfo',
                   'name': 'John',
                   'lastname': 'Smith',
                    'middlename': 'J.'},
             '2': {'responseType': 'userInfo',
                   'name': 'John',
                   'lastname': 'Doe',
                   'middlename': 'Smith'},
             '3': {'responseType': 'userInfo',
                   'name': 'Jane',
                   'middlename': 'Smith',
                   'lastname': 'Doe'}
             }
    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return


if __name__ == '__main__':
    app.run()
