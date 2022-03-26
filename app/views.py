from app import app
from app.functions import instagram, snapchat, tiktok, twitter, gmail, outlook, hotmail, reddit
from flask import request, jsonify
import smtplib
from app.settings import PASSWORD, SENDER, RECEIVER
from email.message import EmailMessage


dispatcher = {'instagram': instagram, 'snapchat': snapchat, 'tiktok': tiktok, 'twitter': twitter,
              'gmail': gmail, 'outlook': outlook, 'hotmail': hotmail, 'reddit': reddit}


@app.route('/check/<path:u_path>', methods=['POST'])
def check_usernames(u_path):
    data = request.form.to_dict()
    username = data['username']
    restrictions = data['restrictions']

    if len(username.split()) > 1:
        return {'status': False, 'reason': 'اسم المستخدم لا يجب ان يحتوي على مساحات', 'function': u_path}

    username = username.replace(" ", "").lower()
    restrictions = restrictions.split(',')

    args = []
    for i in restrictions:
        args.append(i)

    try:
        func = dispatcher[u_path](username, *args)
        return jsonify(func)
    except:
        return {'status': False, 'reason': 'حدث خطأ، الرجاء المحاولة مرة اخرى', 'function': u_path}


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.form.to_dict()
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    msg.set_content(f'''
    <html>
        <body style='direction:rtl'>
            <div style="background-color:#eee;padding:10px 20px">
                <h4 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"> 
                 من: {name}  <br><br/> ايميل: {email}
                </h4>
            </div>
            <div style="padding:20px 20px">
                <div style="height: 400px;width:400px">
                    {message}
                </div>
            </div>
        </body>
    </html>
    ''', subtype='html')

    # try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(SENDER, PASSWORD)
        smtp.sendmail(SENDER, RECEIVER, msg.as_string())
        return 'تم إرسال الرسالة بنجاح'
    # except:
    #     return 'عذراً، الرجاء المحاولة مرة اخرى', 400

