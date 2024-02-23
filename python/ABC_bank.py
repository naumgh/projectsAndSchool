
import myclasses

# Notice the import statement above. This statement imports a file
# that contains a class named "BankAccount" that is used in the code below.

# SECTION 01:
# Create the class “BankAccount” (as described below) and save it in file “myclasses.py” to be imported

# An object of the BankAccount class represents information about one individual and their one bank account:
#     - Name of account holder
#     - Address of account holder
#     - Account Number
#     - Balance of the account

# In addition, the class also KEEPS TRACK OF THE TOTAL NUMBER OF ACCOUNTS CURRENTLY OPEN
# AND THE TOTAL AMOUNT OF MONEY CURRENTLY HELD IN ALL THE ACCOUNTS.

# The BankAccount class must contain the following:
#     1) Class and data attributes
#     2) A constructor
#     3) A getter function "get_account_balance" to get account balance for a person
#     4) A setter function "set_account_balance" to set account balance for a person
#     5) A function "delete_account": When an account is deleted/ closed by a user, the delele_account function
#     is used to update the total number of accounts currently open and the total amount of money currently
#     held in all the accounts

# SECTIONs 02,03,04: Read and complete the code below, in the respective Sections.

import random

# NOTE:  You cannot import any other modules.

def main():

    information = {}

    for i in range(1,10000):
        temp = []
        temp.append("Name_%d" % (i))
        temp.append("AcNumber_%d" % (i))
        temp.append("Address_%d" % (i))
        temp.append(random.randint(0,50000))
        information[i] = temp

    list_of_accounts = []

    # When the code above is run, "information" will contain the following:
    #       keys: a number between 1 and 10000
    #       values: A list containing name, address, account number and account balance (integer)

    # An example of what "information" may look like is as follows:
            # {1:["Name_1", "AcNumber_1", "Address_1", 2512], 2:["Name_2", "AcNumber_2", "Address_2", 21012]..............}


    # SECTION 02:
    # Use the values inside the dictionary “information” to create objects of the class BankAccount, and store these objects in list_of_accounts

    Write your code for SECTION02 here.

    # SECTION 03
    # Person "Name_5" gives all their money to person "Name_8"
    # Using list_of_accounts, update the balances for both Name_5 and Name_8

    Write your code for SECTION03 here.

    # SECTION 04:
    # Using list_of_accounts, identify all accounts with balance less than 10000 and:
    #     - Print these accounts in a human-readable format by using the __repr()__ function
    #     - Delete all these accounts

    Write your code for SECTION04 here.


if __name__ == "__main__":
    main()
