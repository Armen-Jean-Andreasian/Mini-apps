import smtplib, ssl


def send_email_wow(message):
    host = "smtp.gmail.com"
    port = 465

    username = "cyber.store.commerce@gmail.com"
    password = "ijyobnaeaidkbsfv"

    receiver = "cyber.store.commerce@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




