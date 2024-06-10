from abc import ABC, abstractmethod

#Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_expiry, cvv):
        self.card_number = card_number
        self.card_expiry = card_expiry
        self.cvv = cvv

    def pay(self, amount):
        return f"Paid {amount} using Credit Card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} using PayPal account {self.email}"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, bitcoin_address):
        self.bitcoin_address = bitcoin_address

    def pay(self, amount):
        return f"Paid {amount} using Bitcoin address {self.bitcoin_address}"


#Context
class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def pay(self, amount):
        return self._payment_strategy.pay(amount)


#Client Code
# Create payment strategies
credit_card = CreditCardPayment("1234567890123456", "12/23", "123")
paypal = PayPalPayment("user@example.com")
bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

# Create payment context
payment_context = PaymentContext(credit_card)
print(payment_context.pay(100))  # Output: Paid 100 using Credit Card ending in 3456

# Change strategy to PayPal
payment_context.set_payment_strategy(paypal)
print(payment_context.pay(200))  # Output: Paid 200 using PayPal account user@example.com

# Change strategy to Bitcoin
payment_context.set_payment_strategy(bitcoin)
print(payment_context.pay(300))  # Output: Paid 300 using Bitcoin address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
