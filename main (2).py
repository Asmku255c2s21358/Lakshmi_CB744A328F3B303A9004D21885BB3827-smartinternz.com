implement a class called
bank account that represent abs
bank account, the class should

have private attributes for account
number, account holder name, and
account balance, include

methods to deposit money, 
withdraw money, and diaplay the 
accoubalance,ensure that the 

account balance cannot be accessed 
directly a program to create an 

instance of the bank account 
class and test the deposit and 
withdrawal functionality, 
class bank account:
det__unit__(self,account_number
account_holder_name, initial_ba 
            lance_00) :
self__account_number=account_nu 
mber
self__account_holder_name=account 
unt_holder_name
self__account_balance=initial_bal 
ance 
def deposit(self,amount):
if ￼a￼amount>0:
  self__account_balance+=amount 
print("deposited$():new balance: 
$()".formot (amount,self__account unt_balance))
else:
print("invalid deposit
amount. please deposit a positive
amount")
def with draw (self, amount):
if amount>0 and
amount<=self._account_balance 
self. __account_balance==amount
print("withdraw$()new balance:$ 
()".format(amount,self.__accoun 
t. balance.") 
def display_balance (self):
else:
print("invalid with draw amount 
or insufficient balance.")
def display_balance (self):
print("account balance for {} 
(account #{}):$".format 
self. _account_holder_name.self.
_account_number,
self. __account_balance)}
#creat an instance of the bank 
account class 
account= bank account (account_nu 
mber=" 123456789"
account_ holder_name=" hari 
prabu"
initial_balance=5000,0
  def __init__(self, params):
      
