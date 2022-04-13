class Atm(object):
    def __init__(self, Card_number, pin_number):
        self.Card_number = Card_number
        self.pin_number = pin_number

    def CashWithdrawl(self):
        print("Cash With drawl in progress")

    def BalanceEnquiry(self):
        print("Checking balance !")


Card_number = input("Enter card number:-")
pin_number = input("Enter pin number:-")
Rupay = Atm(Card_number, pin_number)

Rupay.CashWithdrawl()
Rupay.BalanceEnquiry()
