

class Customer:
    def __init__(self,customer_id: str, personal_nbr: str, name: str):
        self._name = name
        self._customer_id = customer_id
        self._personal_nbr = personal_nbr

    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def personal_nbr(self):
        return self._personal_nbr
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    def __str__(self):
        return f"Kund: {self.customer_id} Namn (personnummer) : {self.name} ({self.personal_nbr})"
    
class Account:
    def __init__(self,customer_id: str, account_nbr: int):
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance = 0

    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def account_nbr(self):
        return self._account_nbr
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance and amount > 0:
            self._balance -= amount
            return True
        return False
    def __str__(self):
        return f"kontonummer: {self.account_nbr}, saldo: {self.balance} ({self.customer_id})"

class Bank:
    def __init__(self):
        # customer_id: Customer
        self.customers: dict[str,Customer] = {}
        # kontonummer: Account
        self.accounts: dict[int,Account] = {}

        #self.customers: list[Customer] = []
        #self.accounts: list[Account] = []

    def add_customer(self,name: str, personal_nbr: str) -> str | None:
        customer_id = f"C{str(len(self.customers)+10)}"
        c = Customer(customer_id,personal_nbr,name)

        if personal_nbr not in [customer.personal_nbr for customer in self.customers.values()]:
            self.customers[customer_id] = c
            return customer_id
        return None
    
    def get_customer(self,customer_id: str) -> Customer | None:
        return self.customers.get(customer_id,None)
    
    def find_customer_by_part_of_name(self,name_part: str) -> list[Customer]:
        return [customer for customer in self.customers.values() if name_part.lower() in customer.name.lower()]
    
    def create_account(self,customer_id: str) -> int:
        if customer_id in self.customers:
            account_nbr = (1000+len(self.accounts))
            account = Account(customer_id,account_nbr)
            self.accounts[account_nbr] = account
            return account_nbr
        return -1
        
    def get_account(self,account_nbr: int) -> Account | None:
        return self.accounts.get(account_nbr,None)
    
    def remove_account(self,account_nbr: int) -> bool:
        acc = self.accounts.get(account_nbr,False)
        if acc and acc.balance == 0:
            del self.accounts[account_nbr]
            return True
        return False
    
    def transfer(self,from_acc_nbr: int, to_acc_nbr: int, amount: float) -> bool:
        from_acc = self.accounts[from_acc_nbr]
        to_acc = self.accounts[to_acc_nbr]
        if from_acc and to_acc and from_acc.withdraw(amount):
            to_acc.deposit(amount)
            return True
        return False
    
    def all_accounts(self) -> list[Account]:
        return list(self.accounts.values())
    
    def accounts_by_customer(self,customer_id: str) -> list[Account] | None:
        #customer = next((c for c in self.customers if c.customer_id == customer_id),False)¨
        customer = self.customers.get(customer_id,False)
        if customer:
            return [account for account in self.all_accounts() if customer.customer_id == account.customer_id]
        return None

    def all_customers_sorted_by_name(self) -> list[Customer]:
        return sorted(self.customers.values(), key=lambda customer: customer.name.lower())
                     
if __name__ == '__main__':
    e = Bank()
    cust1 = e.add_customer('Anders Andersson',10)
    cust2 = e.add_customer('Anders Svensson',20)
    cust3 = e.add_customer('AA',30)

    print(e.get_customer('C11'))
    print(e.find_customer_by_part_of_name('Anders')[0])
    print(cust1)
    acc1 = e.create_account(cust1)
    acc2 = e.create_account(cust1)
    acc3 = e.create_account(cust2)
    print(acc1)
    print(acc2)
    print(acc3)

    e.get_account(acc1).deposit(100)

    e.transfer(acc1,acc2,100)

    print(e.get_account(acc1))
    print(e.get_account(acc2))
    print(e.get_account(acc3))

    e.remove_account(acc1)
    print(e.get_account(acc1))

    print("Konton: ", e.accounts_by_customer(cust1))
    print('Sorterad by namn: ', e.all_customers_sorted_by_name()[0])
    accs = e.all_accounts()
    print(accs)

    print(e.customers)
    print(e.accounts)