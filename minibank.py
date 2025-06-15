from typing import Union


# MiniBank – Oddiy Banking Simulyatori

# Global o'zgaruvchilar
name: Union[str, None] = None
balance: Union[float, None] = None

def open_account() -> None:
    """Bu funksiya yangi hisob yaratadi

    Foydalanuvchi ism kiritadi va hisob avtamatik 0.0 balans bilan payda bo'ladi
    """    
    global name, balance
    name = input("Ismingizni kiriting: ")
    balance = 0.0
    print(" --- Hisob Yaratildi ---")

def check_account() -> bool:
    """Bu funksiya hisob ochilgan-ochilmaganini tekshiradi.

    Returns:
        bool: Agar hisob ochilgan bo'lsa True, aks holda False qaytaradi.
            Ya'ni global o'zgaruvchilar (name va balance) None bo'lmasa, hisob mavjud deb hisoblanadi.
    """
   
    return name is not None and balance is not None

def deposit() -> None:
    """
    Foydalanuvchidan pul to'ldirish miqdorini so'raydi va balansga qo'shadi.

    To'ldirish shartlari:
    - Minimal to'ldirish miqdori: 5$
    - Maksimal to'ldirish miqdori: 10 000$

    Agar foydalanuvchi to'g'ri miqdor kiritsa, bu summa global `balance` o'zgaruvchisiga qo'shiladi.
    Aks holda, foydalanuvchiga xatolik haqida xabar beriladi.

    Returns:
        None
    """
    global balance
    amount = float(input("\nTo'ldirmoqchi bo'lgan summangizni kiriting: "))
    if amount <= 10_000 and amount >= 5:
        balance += amount
        print(f"\nPulingiz qo'shildi!\nBalansda jami: {balance}$")
    elif amount >= 10_000:
        print("Maksimal to'ldirish 10 ming $")
    elif amount >= 0  and amount <= 5:
        print("Minimal to'ldirish 5$")         
    else:
        print("Xato summa kiritingiz!")

def withdraw() -> None:
    """
    Foydalanuvchidan chiqariladigan pul miqdorini so'raydi va balansdan ayiradi.

    Shartlar:
    - Chiqariladigan summa 0 dan katta bo'lishi kerak
    - Balansdagi mavjud summadan ko'p bo'lmasligi kerak

    Agar kiritilgan summa to'g'ri bo'lsa, bu miqdor global `balance` o'zgaruvchisidan ayriladi.
    Aks holda, foydalanuvchiga xatolik haqida xabar beriladi.

    Returns:
        None
    """
    global balance
    amount = float(input("\nChiqarmoqchi bo'lgan summangizni kiriting: "))
    if amount < balance and amount > 0:
        balance -= amount
        print(f"\nPulingiz chiqarildi! \n Balansda qoldi: {balance}$")
    else:
        print("Xato summa kiritingiz yoki balansingizda buncha summa mavjud emas")

def check_balance() -> None:
    """Bu funksiya balansda qancha summa borligini tekshiradi"""
    print(f"Balansingiz: {balance}$")

def main() -> None:
    """
    Elektron hamyon dasturining bosh menyusini ishga tushiradi.

    Foydalanuvchiga quyidagi menyu orqali tanlov qilish imkonini beradi:
    0 - Yangi hisob yaratish
    1 - Balansni tekshirish
    2 - Pul chiqarish
    3 - Pul to'ldirish
    4 - Dasturdan chiqish

    Har bir tanlov mos funksiyani chaqiradi.
    Agar hisob yaratilmagan bo'lsa, foydalanuvchi hisob yaratishga yo'naltiriladi.

    Dastur foydalanuvchi `4` ni tanlaguncha doimiy ishlaydi. 
    0, 1, 2, 3, 4 sonlaridan tashqari boshqa hech qanday sonni tanlagani qo'ymaydi.

    Returns:
        None
    """

    while True:
        choice = int(input("\nMINI BANK - elektron hamyoni"
                        "\n 0. Hisob yaratish "
                        "\n 1. Balansni tekshirish "
                        "\n 2. Pul chiqarish "
                        "\n 3. Pul to'ldirish "
                        "\n 4. Dasturdan chiqish"
                        "\n Nima qilamiz: "))
        
        if choice == 0:
            open_account()

        elif choice == 1:
            if check_account():
                check_balance()
            else:
                print("Iltimos, avval account yarating.")
                open_account()

        elif choice == 2:
            if check_account():
                withdraw()
            else:
                print("Iltimos, avval account yarating.")
                open_account()

        elif choice == 3:
            if check_account():
                deposit()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
                
        elif choice == 4:
            print("Dasturdan chiqildi. Xayr!")
            break

        else:
            print("(0-4) dan birini tanlang: ")


main()