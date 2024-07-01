from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    price = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total

class Authorizer(ABC):
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):

    authorizer = False

    def verify_code(self, code):
        print(f"verifying code {code}")
        self.authorizer = True

    def is_authorized(self) -> bool:
         return self.authorizer

class NotRobot(Authorizer):
    authorizer = False
    def not_robot(self):
        print("Are yot a robot?")
        self.authorizer = True

    def is_authorized(self) -> bool:
        return self.authorizer

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSAuth()
processor = DebitPaymentProcessor("123455",authorizer)
authorizer.verify_code(123456)
processor.pay(order)








