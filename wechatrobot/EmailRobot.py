
# example
import smtplib
from email.header import Header
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', "plain", "utf-8")

# # 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入收件人地址:
# to_addr = input('To: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ') # e.g. smtp.163.com

# build a secure connection #
# 1. raw
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# 2. TLS
# server = smtplib.SMTP(smtp_server, 587)  # gmail SMTP协议TLS端口 587
# server.ehlo()
# server.starttls()
# 3. SSL
# server = smtplib.SMTP_SSL(smtp_server, 465)  # gmail SMTP协议SSL端口 465
# server.ehlo()

# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# 第三方 SMTP 服务
mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "chenyuhang55555"                  # 用户名
mail_pass = ""               # 授权密码，非登录密码

# 发件人邮箱(最好写全, 不然会失败)
sender = 'chenyuhang55555@163.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['475192566@qq.com', 'chenyuhang55555@163.com']

content = '你好xiaoming,我用Python'
title = "放假通知"  # 邮件主题


def sendEmail():

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    # message['From'] = "{}".format(sender)
    message['From'] = "Ruizhi<chenyuhang55555@163.com>"
    message['To'] = "Jelly<475192566@qq.com>"
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sendEmail()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
