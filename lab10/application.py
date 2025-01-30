from data import *
import time

menu_options = [
    "1. Skapa en ny kund",
    "2. Skapa ett nytt konto",
    "3. Ta bort konto",
    "4. Sätta in pengar",
    "5. Ta ut pengar",
    "6. Överför pengar",
    "7. Skriv ut alla konton",
    "8. Sök på kund på del av namn",
    "9. Skriv ut samtliga kunder (bokstavsordning) och dess konton",
    "10. Avsluta programmet"
]

bank = Bank()

while True:
    print('Välj ett av följande alternativ: ')
    for option in menu_options:
        print(option)
    i = int(input())

    match i:
        case 1:
            print("Du har valt att skapa en ny kund")
            name = input('Skriv in kundens namn: ')
            personal_nbr = int(input('Skriv in kundens personnummer: '))
            customer_id = bank.add_customer(name,personal_nbr)
            if customer_id != None:   
                print(f"Kunden tillagd med kundnummer {customer_id}")
            else:
                print('Finns redan en kund med detta personnummer')
            time.sleep(1)
        case 2:
            print("Du har valt att skapa ett nytt konto")
            customer_id = input("Ange kundnummer för kunden som ska ha kontot: ")
            account_nbr = bank.create_account(customer_id)
            if account_nbr != -1:
                print(f"Kontot skapades med kontonummer {account_nbr}")
            else:
                print(f"Kundnummret {customer_id} existerar ej så kunde ej skapa ett konto!")
            time.sleep(1)
        case 3:
            print("Du har valt att ta bort ett konto")
            account_nbr = int(input("Ange kontonummer för kontot som ska tas bort: "))
            if bank.remove_account(account_nbr):
                print("Kontot togs bort")
            else:
                print("Kontot kunde inte tas bort")
            time.sleep(1)
        case 4:
            print("Du har valt att sätta in pengar")
            account_nbr = int(input("Ange kontonummer: "))
            account = bank.get_account(account_nbr)
            if account == None:
                print('Kontot hittades inte')
                time.sleep(1)
                continue
            amount = float(input("Ange belopp: "))
            if account.deposit(amount):
                print(f"Insättning lyckades, saldot på kontot är nu {account.balance}")
            else:
                print('Ogiltigt belopp')
            time.sleep(1)
        case 5:
            print("Du har valt att ta ut pengar")
            account_nbr = int(input("Ange kontonummer: "))
            account = bank.get_account(account_nbr)
            if account == None:
                print('Kontot hittades inte')
                time.sleep(1)
                continue
            amount = float(input("Ange belopp: "))
            if account.withdraw(amount):
                print(f"Uttag lyckades, saldot på kontot är nu {account.balance}")
            else:
                print(f"Uttag misslyckades, saldot på kontot är {account.balance}")
            time.sleep(1)
        case 6:
            print("Du har valt att överföra pengar")
            from_acc_nbr = int(input("Ange kontonummer att överföra från: "))
            to_acc_nbr = int(input("Ange kontonummer att överföra till: "))
            amount = int(input("Ange belopp: "))
            if bank.transfer(from_acc_nbr,to_acc_nbr,amount):
                print("Överföring lyckades")
            else:
                print("Överföring misslyckats")
            time.sleep(1)
        case 7:
            print("Du har valt att skriva ut alla konton")
            accounts = bank.all_accounts()
            if len(accounts) == 0:
                print("Hittade inga konton")
                time.sleep(1)
                continue
            for account in accounts:
                print(account)
            time.sleep(1)
        case 8:
            print("Du har valt att söka på (del av) kundnamn")
            part_name = input("Skriv in (del av) namn att söka på: ")
            customers = bank.find_customer_by_part_of_name(part_name)
            if len(customers) == 0:
                print(f"Hittade inga kunder med {part_name} som del av kundnamn")
                time.sleep(1)
                continue
            print("Följande kunder hittades:")
            for customer in customers:
                print(customer)
            time.sleep(1)
        case 9:
            print("Du har valt att skriva ut alla kunder tillsammans med deras konton")
            customers = bank.all_customers_sorted_by_name()
            if len(customers) == 0:
                print(f"Hittade inga kunder")
                time.sleep(1)
                continue
            for customer in customers:
                accounts = bank.accounts_by_customer(customer.customer_id)
                print(customer)
                for i,account in enumerate(accounts):
                    print(f"    {i}: {account}")
            time.sleep(1)
        case 10:
            print("Du har valt att avsluta programmet, välkommen tillbaka")
            break
        case _:
            print("Felaktigt val, välj ett alternativ mellan 1 och 10")
            time.sleep(1)

            
            
                
