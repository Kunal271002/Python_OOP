class Account:
    def __init__(self,Acc_no,Pass):
        self.account_no = Acc_no
        self.__password = Pass  # To make it private just write two Underscore infront of the Variable to make it private

    def print_pass(self):
        print(self.__password)  # Other Methods can be easity accessed because it is in the same class

Account1 = Account("12345","ABCD")

print(Account1.print_pass()) # Cannot be accessed outsite the class