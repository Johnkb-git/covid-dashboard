import flask
import database

app = flask.Flask(__name__)


# @app.route('/')
# def hello_world():
#    return 'Hello World'
@app.route('/')
def index():
    return flask.redirect(flask.url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        if database.verify_user(username,password):
            return flask.redirect(flask.url_for('main_page'))
        else:
            error = 'Invalid username or password. Please try again!'
            return flask.render_template("login.html", error = error)
        # some code contact with database

    return flask.render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if flask.request.method == 'POST':
        print("get post request")
        username = flask.request.form['username']
        password = flask.request.form['password']
        print(username)
        print(password)

        # some code contact with database

    return flask.render_template("create-account.html")


@app.route('/mainpage', methods=['GET'])
def main_page():
    # some code contact with database

    # some code reform the main page html based on the user id
    userid = "1"
    return flask.render_template("mainpage.html", userid=userid)


@app.route('/list/medicine/<user_id>', methods=['GET'])
def medicine(user_id):
    # some code contact with database

    # some code reform the main page html based on the user id
    table_name = "Medicine records"
    return flask.render_template("medicine_table.html", table_name=table_name)


@app.route('/list/takeout/<user_id>', methods=['GET'])
def takeout(user_id):
    # some code contact with database

    # some code reform the main page html based on the user id
    table_name = "Takeout"
    return flask.render_template("takeout_table.html", table_name=table_name)


@app.route('/list/news/<user_id>', methods=['GET'])
def news(user_id):
    # some code contact with database

    # some code reform the main page html based on the user id
    table_name = "News"
    return flask.render_template("news_table.html", table_name=table_name)


@app.route('/list/trips/<user_id>', methods=['GET'])
def trips(user_id):
    # some code contact with database

    # some code reform the main page html based on the user id
    table_name = "Trips"
    return flask.render_template("trip_table.html", table_name=table_name)


if __name__ == '__main__':
    app.run()
