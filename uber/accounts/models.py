from utils.models import BaseModel


class Account(BaseModel):
    name = None
    birth_date = None
    email = None
    password = None
    phone_number = None

    @classmethod
    def create(cls, name):
        acc = Account()
        acc.name = name
        return acc

    @property
    def name_in_ru(self):
        return self.name

class Driver(Account):
    has_driver_license = False
    actual_car = None
    salary = 0.00


class Car(BaseModel):
    owner = None  # Driver
    model = None
    color = None
    is_hybrid = False


class Client(Account):
    discount = 0


