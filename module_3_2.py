def send_email(message, recipient, *, sender="university.help@gmail.com"):

    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Привет!', 'vasyok1337@gmail.com')
send_email('Привет!', "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email('Привет!', "invalid-email", sender='urban.teacher@mail.uk')
send_email('Привет!', "university.help@gmail.com")