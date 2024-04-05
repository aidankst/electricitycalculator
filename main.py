import pyrebase
import calendar
from datetime import datetime, timedelta

firebaseConfig = {
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

def save_bills():
    starting_date = input('Enter the starting date (YYYY-MM-DD) : ')
    ending_date = input('Enter the ending date (YYYY-MM-DD) : ')
    amount = input('Enter the unit amount : ')
    
    start_date = datetime.strptime(starting_date, "%Y-%m-%d")
    end_date = datetime.strptime(ending_date, "%Y-%m-%d")

    current_date = start_date
    while current_date <= end_date:
        bills = {
            'date' : current_date.day,
            'amount' : amount
        }
        db.child('bills').child(current_date.year).child(current_date.month).push(bills)
        current_date += timedelta(days=1)

def paid_bills():
    month = int(input('Enter the month : '))
    year = int(input('Enter the year : '))
    usage = float(input('Enter the usage : '))
    amount = float(input('Enter the amount : '))

    _, num_days = calendar.monthrange(year, month)

    usage_per_day = usage / num_days
    
    bills = {
        'usage': usage_per_day,
        'amount': amount
    }

    db.child('paid_bills').child(year).child(month).set(bills)

def new_bills():
    month = input('Enter the month : ')
    year = input('Enter the year : ')
    month = int(month)
    year = int(year)

    _, num_days = calendar.monthrange(year, month)

    bills = db.child('bills').child(year).child(month).get().val()
    paid_bills = db.child('paid_bills').child(year).child(month).get().val()
    # print (bills)
    # print (paid_bills)

    total_bills = 0
    if bills is None or paid_bills is None:
        print("No bills data or paid bills data found for the specified month and year.")
        return
    for key, value in bills.items():
        total_bills += (float(bills[key]['amount']) * float(paid_bills['usage']))
    
    left = round(total_bills - paid_bills['amount'], 2)
    bills = {
        'total amount': total_bills,
        'left amount': left
    }
    # db.child('bills').child(year).child(month).push(bills)
    # print (bills)
    print(f"Barber shop needs to pay {left} PLN in {month}, {year}.")
    

if __name__ == '__main__':
    running = True
    while running:
        temp = input("Choose the options below:\n(1) Input Bills\n(2) Insert Bills Paid by Barber Shop\n(3) Calculate amount barber shop still needs to pay\n(4) Exit\n -> ")
        match temp:
            case "1":
                save_bills()
            case "2":
                paid_bills()
            case "3":
                new_bills()
            case "4":
                running = False
            case _:
                db.child('credentials').set(firebaseConfig)
                print("Invalid option")
