def send_email(message, recipient, *, sender="university.help@gmail.com"):
    recipient_flag = False
    sender_flag = False
    ends = [".com", ".ru", ".net"]
    for end in ends:
        if end in recipient:
            recipient_flag = True
        if end in sender:
            sender_flag = True

    if "@" not in recipient or "@" not in sender or not recipient_flag or not sender_flag:
        print("Impossible to send email from: '" + str(sender) + "' to: '" + str(recipient) + "'")
    elif sender == recipient:
        print("You cannot send email to yourself")
    elif sender == "university.help@gmail.com":
        print("Mail succesffuly sended from: '" + str(sender) + "' to: '" + str(recipient) + "'")
    else:
        print("NON-STANDART STUDENT! Mail succesffuly sended from: '" + str(sender) + "' to: '" + str(recipient) + "'")


send_email("Message for check", "ese.worldworkshop@mail.ru")
send_email("Message for check", "ese.worldworkshop@mail.ru", sender = "urban.info@mail.ru")
send_email("Message for check", "ese.worldworkshop@mail.ru", sender = "urban.info@mail.nek")
send_email("message for check", "ese.worldworkshop@mail.ru", sender = "ese.worldworkshop@mail.ru")