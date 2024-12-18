from datetime import datetime
user_info={
    'username':"Xaydarov ALijon",
    'password':1308,
    'card_number':"9860160127859561",
    'balance':40000,
    'sms':True,
    'phone_number':""

}

bankomat={'pul':2000000}

def uzb_karta_tuldirish():
    print("<<<<<Karta to'ldirish bo'limi>>>>")
    money=input("""
    Summani kiriting:
    1.50000
    2.100000
    3.150000
    4.200000
    5.Boshqa summa
    
    
    
    """)

    if money=='1':
        if bankomat['pul']>=50000:
            user_info['balance']+=50000
            return uzbek_services()
        else:
            print("Uzur lekin bankomatda buncha pul yo'q.")
            return uzbek_services()

    elif money=='2':
        if bankomat['pul']>=100000:
            user_info['balance']+=100000
            return uzbek_services()
        else:
            print("Uzur lekin bizda buncha pul yo'q.")
            return uzbek_services()

    elif money=='3':
        if bankomat['pul']>=150000:
            user_info['balance']+=150000
            return uzbek_services()
        else:
            print("Uzur lekin bizda buncha pul yo'q.")
            return uzbek_services()


    elif money=='4':
        if bankomat['pul']>=200000:
            user_info['balance']+=200000
            return uzbek_services()

        else:
            print("Uzur lekin bizda buncha pul yo'q.")
            return uzbek_services()

    elif money=='5':
        summa=int(input("summani kiriting:"))
        if bankomat['pul']>=summa:
            user_info['balance']+=summa
            return uzbek_services()
        else:
            print("Uzur bizda buncha pul yo'q.")
            return uzbek_services()

    else:
        print("bizda bunday funksiya yo'q.ERROR")
        return uzbek_services()




def check_balance(money):
    m=money*1.01
    if user_info['balance'] >=m and bankomat['pul']>=money:
            user_info['balance'] -= m
            bankomat['pul'] += money
            return uzbek_services()

    else:
        print("Error ")
        return uzbek_services()


















def uzbek_pul_yechish():
    print("<<<<Pul yechish bo'limi>>>>")




    money=input("""
    Siz kartangizdan qancha pul yechib olmoqchisiz ?
    Summani tanlang:
    1.50000
    2.100000
    3.150000
    4.200000
    5.Boshqa summa
    """)


    if money=='1':
        return check_balance(50000)
    elif money=='2':
        return check_balance(100000)
    elif money=='3':
        return check_balance(150000)

    elif money=='4':
        return check_balance(200000)
    elif money=='5':
        summa=int(input("summani kiriting:"))
        return check_balance(summa)

    else:
        print("bizda bunay funksiya yo'q.ERROR")

















def uzb_sms_xabarnoma():
    print("siz sms xabarnoma bo'limidasiz !!")

    if user_info['sms'] is False:
        user_info['phone_number']=input("enter your phone number")
        user_info['sms']=True

        print(f"""Siz {user_info['phone_number']} telefoniga sms xabarnomani uladingiz.
        {user_info['sms']}
        """)
    else:
        print("siz allaqachon sms xabarnomani yoqtirgansiz !!!!")





def uzb_pin_code_change():
    print("Siz pin kodeni o'zgartirish bo'limidasiz !")
    new_code=input("yangi pin kodeni kiriting:")

    if new_code.isnumeric() and len(new_code)==4:
        while new_code==str(user_info["password"]):
            print("sizning parolingiz eskisidan farq qilishi kerak !!!!!")
            new_code=input("yangi pin kodeni kiriting:")

        user_info['password']=int(new_code)
        option=input(f"""siz parolingizni muvaffaqiyatli yangiladingiz !!!
        Sizning yangi parolingiz:{user_info['password']}
        
        
        Yana biror xizmatdan foydalanishni xohlaysizmi ?
        1.Ha
        2.yo'q
        """)

        if option=='1':
            return uzbek_services()

        elif option=='2':
            return main()

    else:
        print("parol raqamlarda berilish va 4 ta raqamdan iborat bo'lishi lozim!!!")
        return uzb_pin_code_change()









def uzb_balance_ekran():
    option=input(f"""
    Sizning balansingizda {user_info['balance']} so'm pul bor.
    
    Boshqa xizmatdan foydalanishni xohlaysizmi ?
    1.Ha
    2.Yo'q
    """)

    if option=='1':
        return uzbek_services()
    elif option=='2':
        print("Bizni tanlaganingiz uchun raxmat !")
        return main()




def uzb_balance_check():
    option=input(f"""
    Sizning balansingizda {user_info['balance']} so'm pul bor.
    Sana:{datetime.now()}
    Karta_raqami:{12*'*'}{user_info['card_number'][-4:]}
    Foydalanuvchi:{user_info['username']}
    
    
    
    Boshqa xizmat turidan foydalanishni xohlaysizmi ?
    1.Ha
    2.yo'q
    """)
    if option=='1':
        return uzbek_services()

    elif option=='2':
        print("bizni tanlaganingiz uchun raxmat !")
        return main()



def uzb_balance():
    print("Balans bo'limi.")
    option=input("""
    siz kartadaning balansini qay usulda ko'rmoqchisiz ?
    1.Ekranda
    2.Check holatida
    3.back
    
    
    """)
    if option=='1':
        return uzb_balance_ekran()

    elif option=='2':
        return uzb_balance_check()

    elif option=='3':
        return uzbek_services()




def uzbek_services():
    print("<<<Uzbek Service Menu>>>")

    services=input("""
    1.Balance ni ko'rish
    2.Kartani to'ldirish
    3.Kartadan pul yechish
    4.Sms xabarnoma
    5.Kartani pin codeni o'zgartirish
    """)


    if services=='1':
        return uzb_balance()

    elif services=='2':
        return uzb_karta_tuldirish()



    elif services=='3':
        return uzbek_pul_yechish()
    elif services=='4':
        return uzb_sms_xabarnoma()

    elif services=='5':
        return uzb_pin_code_change()


def english_services():
    pass


def russian_services():
    pass


def english():
    print("You chose english language,so the operations are going to be carried out in this language !")

def russian():
    print("Rus tili menyusiga xush kelibsiz !")
def uzbek():
    print("Siz o'zbek tilini tanladingiz,operatsiyalar o'zbek tilida amalga oshiriladi !")

    password=int(input("passwordni kiriting:"))
    count=2
    while password!=user_info['password'] and count!=0:
        print("Wrong password")
        password = int(input("passwordni kiriting:"))
        count=count-1

    if password==user_info['password']:
        return uzbek_services()
    if count==0:
        print("sizning kartangiz bloklandi !")





def main():
    language=input("""
    1.Uzbek tili
    2.Ingliz tili
    3.Rus tili
    
    TIlni tanlang:
    """)

    if language=='1':
        return uzbek()
    elif language=='2':
        return russian()
    elif language=='3':
        return english()
    else:
        print("Wrong command,We only have three languages.")


if __name__=='__main__':
     main()

































