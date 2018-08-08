def send_Email():
    import smtplib
    from settings import SMTP_Services

    server = smtplib.SMTP(SMTP_Services["HOST_NAME"])
#Send the mail
    message = """From: CDK Chatter Services <""" + SMTP_Services["SENDER"] +""">
To: Poorna Pemmasani <"""+SMTP_Services["RECEIVER"]+""">
Subject: SMTP e-mail test

This is a test e-mail message.
Priority:
Issues Description: 
"""# The /n separates the message from the headers
    server.sendmail(SMTP_Services["SENDER"], SMTP_Services["RECEIVER"], message)

send_Email()