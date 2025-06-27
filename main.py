import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
import subprocess

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'autookx2nfk')

PASSWORD = '333333'

# 运行结果缓存
results = {
    'account': '',
    'order': '',
    'notify': ''
}

def run_script(script_name):
    try:
        output = subprocess.check_output(['python', script_name], stderr=subprocess.STDOUT, timeout=120)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')
    except Exception as e:
        return str(e)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('密码错误，请重试')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('已退出登录')
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html', results=results)

@app.route('/run/<task>')
def run_task(task):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if task == 'account':
        results['account'] = run_script('okx_account_balance.py')
        flash('账户查询已执行')
    elif task == 'order':
        results['order'] = run_script('okx_test_order.py')
        flash('测试下单已执行')
    elif task == 'notify':
        results['notify'] = run_script('notification_service.py')
        flash('通知服务已执行')
    else:
        flash('未知任务')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 