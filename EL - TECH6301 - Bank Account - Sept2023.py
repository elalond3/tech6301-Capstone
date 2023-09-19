# Define Bank Account Class
class BankAccount:
    
    currentIdNum=152064 # aribitrary number for sake of exercise
    masterDict={} # initialize dictionary used to store all account objects
    
    def __init__(self,name,accountType,balance=0):
        
        # Assign specified username
        self.name = name
        
        
        # Check for saving or checking, assign if correct
        if (accountType!="Saving" and accountType!="Checking"):
            raise Exception('ERROR: Account Type must be \"Saving\" or \"Checking\"')
        else:
            self.accountType = accountType    
    
    
        # Check that balance is a positive number in usable format, convert to float
        if (type(balance).__name__ == 'str' and balance.isnumeric() and float(balance) >= 0):
            self.balance = float(balance)
        elif type(balance).__name__ == 'int' and balance >= 0:
            self.balance = float(balance)
        elif type(balance).__name__ == 'float' and balance >= 0:
            self.balance = balance
        else:
            raise Exception('ERROR: Balance must be a positive number entered as an int, float, or string')
        
        
        # Automatically assign an incrementing ID number
        BankAccount.currentIdNum += 1
        self.id = BankAccount.currentIdNum
        
        
        # Create file name, then file, then starting balance
        self.filename=str(self.id)+"_"+self.accountType+"_"+self.name+".txt"
        file=open(self.filename,"w")
        file.write("Starting Balance: $"+"{0:.2f}".format(self.balance)) # {0:.2f} restricts number of decimal places
        file.close()
        
        


# Create Bank Account Function
def createBankAccount(name,accountType,balance=0):
    
    # Username will be used as key for object in dictionary, so must be unique
    # Add an underscore at the end if it is already in use
    if name in BankAccount.masterDict.keys():
        print("Specified username is already in use. Username has been adjusted to "+name+"_")
        name+="_"
    
    # Create object, adding it to master dictionary with name as the key
    BankAccount.masterDict[name]=BankAccount(name,accountType,balance)
    
    # Return ID to user
    print("Account ID = "+str(BankAccount.masterDict[name].id)+" was assigned to "+name)
    



# Retreive User ID Function
def retrieveUserID(name):
    print("Account ID = "+str(BankAccount.masterDict[name].id))




# Retreive Username Function (redundant)
def retrieveUsername(name):
    print("Username = "+BankAccount.masterDict[name].name)




# Retreive Account Type Function
def retrieveAccountType(name):
    print("Account Type = "+BankAccount.masterDict[name].accountType)





# Check Balance Function
def checkBalance(name):
    print("Current Balance = $"+"{0:.2f}".format(BankAccount.masterDict[name].balance))




# Withdrawal Function
def withdrawFunds(name,withdrawAmount):
    
    # Access file to be appended
    file=open(BankAccount.masterDict[name].filename,"a+")
    
    # Count number of lines to determine which transaction number this is
    file.seek(0) # Point to first line
    transactionNumber=len(file.readlines())
    
    # Check if account has sufficient funds
    if withdrawAmount > BankAccount.masterDict[name].balance:
        
        # If withdrawal would exceed balance, create transaction line
        transactionLine="Transaction "+str(transactionNumber)+": Attempted withdrawal of $"+\
                   "{0:.2f}".format(withdrawAmount)+" rejected. Current balance = $"+\
                   "{0:.2f}".format(BankAccount.masterDict[name].balance)
                   
        # Add and print transaction line
        file.write("\n"+transactionLine)
        print(transactionLine)
        
    else:
            
        # Adjust balance
        BankAccount.masterDict[name].balance-=withdrawAmount
        
        # Create transaction line
        transactionLine="Transaction "+str(transactionNumber)+": Withdrew $"+\
                   "{0:.2f}".format(withdrawAmount)+". Current balance = $"+\
                   "{0:.2f}".format(BankAccount.masterDict[name].balance)
        
        # Add and print transaction line
        file.write("\n"+transactionLine)
        print(transactionLine)
        
    # Close file
    file.close()




# Deposit Function
def depositFunds(name,depositAmount):
    
    # Access file to be appended
    file=open(BankAccount.masterDict[name].filename,"a+")
    
    # Count number of lines to determine which transaction number this is
    file.seek(0) # Point to first line
    transactionNumber=len(file.readlines())
            
    # Adjust balance
    BankAccount.masterDict[name].balance+=depositAmount
    
    # Create transaction line
    transactionLine="Transaction "+str(transactionNumber)+": Deposited $"+\
               "{0:.2f}".format(depositAmount)+". Current balance = $"+\
               "{0:.2f}".format(BankAccount.masterDict[name].balance)
    
    # Add and print transaction line
    file.write("\n"+transactionLine)
    print(transactionLine)
        
    # Close file
    file.close()




# Access Transaction History
def checkHistory(name):
    
    # Access file to be read
    file=open(BankAccount.masterDict[name].filename,"r")
    
    print("\nAccount Transaction History:")
    
    # For each line in the file, print that linePrint entire file
    for lines in file.readlines():
        print(lines.rstrip()) # rstrip() removes trailing newlines
    print("\n")
    
    # Close file
    file.close()




## TEST CASES

# Full test case
createBankAccount("Jeff","Checking",1000)
retrieveUserID("Jeff")
retrieveUsername("Jeff")
retrieveAccountType("Jeff")

checkBalance("Jeff")

withdrawFunds("Jeff",1500)
withdrawFunds("Jeff",150)
depositFunds("Jeff",226.78)

checkHistory("Jeff")


# Create second account with more realistic account name
createBankAccount("elalonde22","Saving",10000)
checkHistory("jsawyer22")

# Create third account with same username and no balance
createBankAccount("Jeff","Saving",0)
checkBalance("Jeff_")
