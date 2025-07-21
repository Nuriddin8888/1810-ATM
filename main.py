from servise import *
from getpass import getpass


print("******> Welcome ATM <******")



user_card = int(input("Bank kartani kiriting: "))
# user_lang = input("Foydalanish tilini tanlang (uz, ru, en): ")
user_password = getpass("Parol kiriting: ")

user = user_check_card(user_card)

if user:
    card_password = user['password']
    if card_password == user_password:
        while True:
            print("""
        1.Balance
        2.Pul Yechish
        3.Pul o'tkazish
        4.Parolni o'zgartirish
        5.Chiqish
""")
            
            user_choose = input("Bo'limni tanlang: ")
            if user_choose == "1":
                card_balance = show_balance(user)
                print(f"Sizning hisobingizda {card_balance} sum bor")
                
            elif user_choose == "2":
                show_user_money = withdraw(user)
                user_money = int(input("Yechmoqchi bo'lgan summani kiriting: "))
                withdraw_money = user['balance']
                if user_money > withdraw_money:
                    print("Hisobingizda bunday summa yo'q")
                elif user_money <= withdraw_money:
                    withdraw_money = user['balance'] - user_money
                    user["balance"] = withdraw_money
                    print(f"Hisobingizda qolgan summa {user['balance']}")