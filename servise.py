from bank import users


def user_check_card(card_number):
    if card_number in users:
        return users[card_number]
    else:
        return None

    


def show_balance(user):
    return user['balance']


def withdraw(user):
    return user['balance']


def cheng_password(user, old_password, new_password, reset_password):
    if old_password == user["password"]:
        if new_password == reset_password:
            user["password"] = new_password
            print("Parolingiz muaffaqqiyatli o'zgartirildi")
        else:
            print("Parollar mos emas")
    else:
        print("Parol noto'g'ri")