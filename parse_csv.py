import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('bank_loan.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS loanlist')
conn.execute('DROP TABLE IF EXISTS customerinfo')
print("table dropped successfully");

# create table again
conn.execute('CREATE TABLE loanlist (loan_ID TEXT PRIMARY KEY, customer_ID TEXT, current_Loan_amount INTEGER, term TEXT, FOREIGN KEY(customer_ID) REFERENCES customerinfo(customer_ID))')
conn.execute('CREATE TABLE customerinfo (customer_ID TEXT PRIMARY KEY, credit_score INTEGER, annual_income INTEGER,  current_credit_balance INTEGER)')
print("table created successfully");

try:
    # open the CSV file and establish an SQLite3 connection
    with open('Bank/bank_loan.csv', newline='')as f:
        reader = csv.reader(f, delimiter=",")
        next(reader) # skip the header line
        for row in reader:
            print(row)

            loan_ID = row[0]
            customer_ID = row[1]
            current_loan_amount = int(row[2])
            term = row[3]
            
            cur.execute('INSERT INTO loanlist VALUES (?,?,?,?)', (loan_ID, customer_ID, current_loan_amount, term))
        f.close()    
except:
    print("something went wrong when opening the file")
else:    
    print("data parsed successfully");
    conn.commit()

try:
    # open the CSV file and establish an SQLite3 connection
    with open('Bank/bank_loan.csv', newline='')as f:
        reader = csv.reader(f, delimiter=",")
        next(reader) # skip the header line
        for row in reader:
            print(row)
            

            customer_ID = row[1]
            credit_score = int(row[4])
            annual_income = int(row[5])
            current_credit_balance = int(row[14])
        
            cur.execute('INSERT INTO customerinfo VALUES (?,?,?,?)', (customer_ID, credit_score, annual_income, current_credit_balance))
        f.close()
except:
    print("something went wrong when opening the file")
else:
    print("data parsed successfully");
    conn.commit()
conn.close()