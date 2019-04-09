# A Class of Personal Info: Perfect for Honeypotting!
class Info:
    def __init__(self, address, age, phone_num):
        self.__address = address
        self.__age = age
        self.__phone_num = phone_num
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num
    def get_address(self):
        return self.__address
    def get_phone_num(self):
        return self.__phone_num
infos = []
for i in range(3):
    address = input("Input a dumb address lmao: ")
    age = input("Input a dumb age lmao: ")
    phone_num = input("Input a shitty phone number lmao: ")
    infos.append(Info(address, age, phone_num))
for stuff in infos:
    print(stuff.get_address())
    print(stuff.get_phone_num())
