import smtplib, ssl


def sendEmail(Message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "thariduniroshan232@gmail.com"
    password = "1777"
    receiver_email = "thariduniroshan232@gmail.com"


    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtplib_server,port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, Message)
    

    except Exception as e:
        print(e)

    finally:
        server.quit()