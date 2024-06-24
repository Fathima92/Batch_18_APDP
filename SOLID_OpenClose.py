from abc import ABC, abstractmethod

class Order:
    item =[]
    quantities =[]
    price =[]
    status ="open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0;
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total



class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        order.status = "paid"
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        order.status = "paid"
        
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "123495")







