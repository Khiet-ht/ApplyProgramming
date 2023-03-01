#%%
class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start_my_car(self):
        print("I am ready to drive!")
class Truck(Car):
    def __init__(self, brand, color, size):
        super().__init__(brand, color)
        self.size = size
    def start_my_car(self, key):
        if key == "truck_key":
            print("I am ready to drive!")
        else:
            print("Key is not right")
    def stop_my_car(self, brake):
        if brake:
            print("The engine is stopped!")
        else:
            print("I am still running!")

Xe_A = Car('Mercedes','Pink')
Xe_B = Truck('VinFast','Red','fgbhda')
truck1 = Truck("Toyota", "Silver", "Large")
truck1.start_my_car("truck_key")
truck1.stop_my_car(brake = False)

print(Xe_A.color)
Xe_A.start_my_car()
Xe_B.start_my_car('key')

# %%
class products:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def get_price(self, quantity):
        return self.price * quantity
    
    def make_purchase(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return True
        else:
            return False
A = products('áo', 50, 5000)
A.get_price(15)
A.make_purchase(15)
# %%
class products:
    def __init__(self,name,quanity,price):
        self.name = name
        self.quanity = quanity
        self.price = price
    def get_price(self,mount):
        
        while mount >=10:
            if mount <10 :
                return print(mount*self.price)
            elif 10<= mount < 99 :
                return print(0.9*mount*self.price)
            else :
                return print(0.8*mount*self.price)
    def make_purchase(self,mount):    
        return self.quanity - mount
A = products('áo',50,5000)

A.get_price(15)
A.make_purchase(15)
# %%
class Password_manager:
    def __init__(self):
        self.old_password =['khiet123','Khiet428626','Khiet428626@']
    def get_password(self):
        return print('pw hien tai: ',self.old_password[-1])
    def set_password(self,new_pass):
        if new_pass not in self.old_password:
            self.old_password.append(new_pass)
            return print('mat khau da duoc thay doi')
        else:
            return print('mat khau da duoc su dung')
    def is_correct(self,log_in):
        if log_in == self.old_password[-1]:
            return True
        else:
            return False
A = Password_manager()
A.get_password()
A.set_password(new_pass= input('nhap mat khau moi: '))
A.is_correct(log_in = input('nhap mat khau: '))

# %%
class Time:
    def __init__(self,second):
        self.second = second
    def convert_to_minutes(self):
        minutes = self.second//60
        seconds = self.second%60
        return print(f'{minutes}:{seconds}')
    def convert_to_hours(self):
        hours = self.second//3600
        munites = (self.second-hours*60)//60
        seconds = (self.second-hours*3600-munites*60)%60
        return print(f'{hours}:{munites}:{seconds}')
A = Time(3800)
A.convert_to_minutes()
A.convert_to_hours()
# %%
