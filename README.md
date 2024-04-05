# Electricity Calculator

*  **By**: Kaung Sithu

## Overview

This Python project aims to streamline electricity bill calculations and management for a barber shop (let's assume that two shops are using one electricity meter). It utilizes Pyrebase to integrate with a Firebase database, storing bill data, paid amounts, and facilitating the calculation of outstanding amounts.

## Features

- **Bill Input**: Users enter the billing period (start and end dates) and the fixed unit amount. The calculator stores individual daily consumption records in the Firebase database.
  
- **Paid Bill Recording**: Users input the month, year, total electricity usage for the period, and the amount paid. The system calculates a daily usage average and stores it in the database.
  
- **Outstanding Bill Calculation**: Leverages stored bill data and paid bill records. Calculates the total bill amount based on daily consumption and unit rates. Subtracts the paid amount and clearly displays the outstanding balance.

## Dependencies

- **Pyrebase**: (https://github.com/thisbejim/Pyrebase) - For interaction with the Firebase database.
  
- **Calendar**: - For handling date calculations and determining the number of days in a month.
  
- **Datetime**: - For date and time manipulations.

## Setup

1 **Firebase Configuration**:

***Create a Firebase project.***
* Set up a Realtime Database within your Firebase project.
* Obtain your Firebase API keys and project configuration details.
* Replace the placeholder firebaseConfig in the Python script with your actual credentials.

2 **Install Dependencies**:
`pip install pyrebase calendar datetime`

## Usage

1 **Run the Script**:
```
python electricity_calculator.py  # Replace with the actual name of your script
```

2 **Follow the Interactive Menu**:
- ***Option 1***: Input Bills
  
- ***Option 2***: Insert Bills Paid by Barber Shop
  
- ***Option 3***: Calculate Amount Barber Shop Still Needs to Pay
  
- ***Option 4***: Exit

## Database Structure (Firebase)

- **bills**:
***(year)*** / ***(month)*** /
  date, amount


- **paid_bills**:
***(year)*** / ***(month)*** /
  usage, amount


## Disclaimer

This project is intended for demonstration purposes. Actual electricity billing may involve additional factors and tariff structures.
