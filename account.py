class Account:
    '''
    Class for creating an account holder.
    '''
    def __init__(self, name: str) -> None:
        '''
        Method to initialize account holder.
        name: name of account holder.
        '''
        self.__account_name = name
        self.__account_balance = 0
    

    def deposit(self, amount: float) -> bool:
        '''
        Method to deposit funds into account.
        amount: amount deposited.
        return: value validation checker.
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    

    def withdraw(self, amount: float) -> bool:
        '''
        Method to withdraw funds from account.
        amount: amount withdrawn.
        return: value validation checker.
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        '''
        Method to retrieve current account balance.
        return: account balance.
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to retrieve account holder name.
        return: account holder name.
        '''
        return self.__account_name
    

            