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