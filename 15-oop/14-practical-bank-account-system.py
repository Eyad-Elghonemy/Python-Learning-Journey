class BankAccount :
    
    def __init__(self, accountNumber, accountHolderName, balance):
        
        self.__accountNumber = accountNumber
        self.__accountHolderName = accountHolderName
        self.__balance = balance
        
        
    """
    Getter And Setter for BankAccount Private Attributes
        
    """
        
    def get_accountNumber(self):
            
        return self.__accountNumber
        
    def set_accountNumber(self, new_accountNumber):
            
        self.__accountNumber == new_accountNumber
            
    def get_accountHolderName(self):
            
        return self.__accountHolderName
        
    def set_accountHolderName(self, new_accountHolderName):
            
        self.__accountHolderName == new_accountHolderName
            
    def get_balance(self):
            
        return self.__balance
        
    def set_balance(self, new_balance):
            
        self.__balance == new_balance
            
        
    """
    BankAccount Methods
        
    """
        
    def deposit(self, amount):
        
        self.__balance += amount
        
    def Display(self):
        
        print(f"Account Number : {self.__accountNumber}, Holder's Name : {self.__accountHolderName}, Balance : {self.__balance}")
        
        
        

class SavingAccount(BankAccount) :
    
    def __init__(self, interestRate, accountNumber, accountHolderName, balance):
        
        self.__interestRate = interestRate
        
        super().__init__(accountNumber, accountHolderName, balance)
        
    