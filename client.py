from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os, time

abs_path = os.getcwd()
app = Flask(__name__)
URL, PORT = '0.0.0.0',6005


@app.route('/')
def home():
    db = DB_Connector()
    db.curse.execute("select date,count(*) from mds_env_survey group by date")
    fet = db.curse.fetchall()
    db.close()
    date = [i[0].replace('-', '/') for i in fet]
    data = [i[1] for i in fet]
    return render_template('home.html', data=data, date=date)


if __name__ == '__main__':
    app.run(URL,PORT)
    # thread = threading.Thread(target=app.run, args=[URL, PORT])
    # thread.daemon = True
    # thread.start()
    # qt_app = QApplication([])
    # w = QWebEngineView()
    # w.setWindowTitle('My Browser')
    #
    # w.load(QUrl('http://%s:%s' % (URL, PORT)))
    # # w.load(QUrl('http://www.baidu.com'))
    # w.showMaximized()
    # w.show()
    # qt_app.exec_()
