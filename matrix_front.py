from flask import Flask
from MatCal import MatCal
import numpy as np
from flask import render_template,url_for,request,redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('matrix.html')

@app.route('/cal', methods=['GET', 'POST'])
def cal():
    if request.method == 'POST':
        if request.form['key']== 'A x B':
            m1, m2 = getMat(request)
            matcal = MatCal(m1,m2)
            multi = matcal.multi()
            return render_template('matrix.html',mat=str(multi))
        elif request.form['key']== 'A + B':
            m1, m2 = getMat(request)
            matcal = MatCal(m1, m2)
            add = matcal.add()
            return render_template('matrix.html',mat=str(add))
        elif request.form['key']== 'A - B':
            m1, m2 = getMat(request)
            matcal = MatCal(m1, m2)
            minus = matcal.sub()
            return render_template('matrix.html',mat=str(minus))
def getMat(request):
    m1r1c1 = request.form['m1r1c1']
    m1r1c2 = request.form['m1r1c2']
    m1r1c3 = request.form['m1r1c3']
    m1r2c1 = request.form['m1r2c1']
    m1r2c2 = request.form['m1r2c2']
    m1r2c3 = request.form['m1r2c3']
    m1r3c1 = request.form['m1r3c1']
    m1r3c2 = request.form['m1r3c2']
    m1r3c3 = request.form['m1r3c3']
    m1 = np.matrix([[m1r1c1, m1r1c2,m1r1c3], [m1r2c1, m1r2c2,m1r2c3],[m1r3c1,m1r3c2,m1r3c3]], dtype='float')
    m2r1c1 = request.form['m2r1c1']
    m2r1c2 = request.form['m2r1c2']
    m2r1c3 = request.form['m2r1c3']
    m2r2c1 = request.form['m2r2c1']
    m2r2c2 = request.form['m2r2c2']
    m2r2c3 = request.form['m2r2c3']
    m2r3c1 = request.form['m2r3c1']
    m2r3c2 = request.form['m2r3c2']
    m2r3c3 = request.form['m2r3c3']
    m2 = np.matrix([[m2r1c1, m2r1c2, m2r1c3], [m2r2c1, m2r2c2, m2r2c3], [m2r3c1, m2r3c2, m2r3c3]], dtype='float')
    return m1,m2

if __name__ == '__main__':
    app.run(debug=True)