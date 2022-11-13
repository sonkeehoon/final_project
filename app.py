# app.py
# flask

host_address = "0.0.0.0"
port_number = 5000

from flask import Flask, render_template, request, flash
from dbconnect import insert


app = Flask(__name__)
app.config['SECRET_KEY'] = "ABCD"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join.html')
def join():
    return render_template('join.html')

@app.route('/seat.html')
def seat():
    return render_template('seat.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    print('register page')
    if request.method == "GET":
        print('GET')
        return render_template('join.html')
    else:
        id = request.form.get('ID')
        password = request.form.get('password')
        re_password = request.form.get('password2')
        
        print(f"id is {id}, password is {password}")
        
        if id == "" or password == "":
            flash("[가입 실패] 아이디와 비밀번호를 입력하세요")
            
        elif password != re_password:
            flash("비밀번호를 확인하세요")
            
        else:
            sql = f"""INSERT INTO member(id, passwd)
                      VALUES("{id}","{password}");"""
            insert(sql)
            flash("회원가입 완료")
            
            return render_template('join.html')
            
            
        return render_template('join.html')
            
            

if __name__ == '__main__':
    app.run(host = host_address, port = port_number, debug = True)
    
    
