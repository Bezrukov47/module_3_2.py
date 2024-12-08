# Создаю функцию, которая принимает два позиционных параметра и один именованный
def send_email (message, recipient, *, sender="university.help@gmail.com" ):
    if "@" not in sender or "@" not in  recipient or not (sender.endswith (".com"".ru"".net") and recipient.endswith(".com"".ru"".net")):
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>.")
        return
     # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print ("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")



