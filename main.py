from flask import Flask, render_template, request, redirect, current_app

name = {}
password = []
account = []

app = Flask(__name__, template_folder='web')

@app.route('/',methods=['POST','GET'])

def getdata():
    if request.method == 'POST':
        if request.values['send'] == 'log in':
            if request.values['account'] in name:
                if request.values['password'] == name[request.values['account']]:
                    return render_template('sighin_s.html')
                else:
                    return render_template('sighin_f.html')
            else:
                return render_template('sighin_f.html')
        password.append(request.values['password'])
        account.append(request.values['account'])
        if request.values['send'] == 'sigh up':
            return redirect('check')
    return render_template('sighin.html')

@app.route('/check',methods=['POST','GET'])

def check():
    try:
        if request.values['send'] == 'check':
            if password[0] == request.values['password'] and account[0] not in name:
                name.setdefault(account[0], password[0])
                account.remove(account[0])
                password.remove(password[0])
                return render_template('sighup_s.html')
            else:
                return render_template('sighup_f.html')
    except:
        pass
    return render_template('check.html')


if __name__ == '__main__':
    app.run(debug=True)