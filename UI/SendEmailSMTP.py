def send_Email(email_subject, email_message):
    import smtplib
    from settings import SMTP_Services

    server = smtplib.SMTP(SMTP_Services["HOST_NAME"])
#Send the mail
    message = """From: Ravi Akella <""" + SMTP_Services["SENDER"] +""">
To: Poorna Pemmasani <"""+SMTP_Services["RECEIVER"]+""">
Subject:"""+email_subject+"""

This mail is sent by Alpha to raise a case on behalf of the User. 
Please find the details below. 
Priority: High
Issues Description:"""+email_message+"""
"""# The /n separates the message from the headers
    server.sendmail(SMTP_Services["SENDER"], SMTP_Services["RECEIVER"], message)

#send_Email("Issue with Site of USer","The User is facing issue with the Site. The Site is missing in the list")