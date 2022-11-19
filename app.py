# app.py
# flask

host_address = "0.0.0.0"
port_number = 5000

from flask import Flask, render_template, request
from flask import flash, session
from dbconnect import insert_func, read_func


app = Flask(__name__)
app.config['SECRET_KEY'] = "ABCD"

def get_id_list():
    query = "SELECT ID FROM info;"
    id_lst = []
    for q in read_func(query):
        id_lst.append(q[0])
    return id_lst


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join.html')
def join():
    return render_template('join.html')

@app.route('/seat.html')
def seat():
    return render_template('seat.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    print('register')
    msg = None
    if request.method == "GET":
        print('GET')
        return render_template('join.html')
    else:
        id = request.form.get('ID')
        password = request.form.get('password')
        re_password = request.form.get('password2')
        name = request.form.get('name')
        birthday = request.form.get('birth')
        contact = request.form.get('contact')
        email = request.form.get('email')
        
        
        if id == "" or password == "":
            msg = "[가입 실패] 아이디와 비밀번호를 입력하세요"
            
        elif password != re_password:
            msg = "[가입 실패] 비밀번호를 확인하세요"
            
        elif id in get_id_list():
            msg = "[가입 실패] 이미 가입된 계정입니다"
                
        else:
            query = f"""INSERT INTO info(ID, PW, name, birthday, contact, email)
                      VALUES("{id}","{password}","{name}","{birthday}","{contact}","{email}");"""
            insert_func(query)
            return render_template('login.html')
        
        flash(msg)       
        return render_template('join.html')
            
@app.route('/loginPage', methods = ['GET', 'POST'])
def loginPage():
    print('login')
    
    if request.method == "GET":
        return render_template('login.html')
    else:
        msg = None
        id = request.form.get('login_ID')
        password = request.form.get('login_password')
        
        if id == "" or password == "":
            msg = "[로그인 실패] 아이디와 비밀번호를 입력하세요"
            
        elif id in get_id_list():
            query = "SELECT * FROM info;"
            
            for i in read_func(query):
                info_id = i[0]
                info_pass = i[1]
                
                if info_id == id and info_pass == password:
                    return render_template('login_success.html')
                
                flash("정보가 올바르지 않습니다")
                return render_template('login.html') 
            
        flash(msg)
        return render_template('login.html')

if __name__ == '__main__':
    app.run(host = host_address, port = port_number, debug = True)
    
    
