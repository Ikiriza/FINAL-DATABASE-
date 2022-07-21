import csv

from cs50 import SQL

open("computerbrands.db","w").close()

db = SQL("sqlite:///computerbrands.db")

db.execute("CREATE TABLE customer(customer_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,address TEXT,contact TEXT ,age INTEGER)" )
db.execute("CREATE TABLE ram(ram_id INTEGER PRIMARY KEY AUTOINCREMENT, ram_number INTEGER)")

db.execute("CREATE TABLE brand(brand_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,year_of_manufacture INTEGER, hard_disk_type TEXT, customer_id INTEGER, ram_id, FOREIGN KEY(customer_id) REFERENCES customer(customer_id),FOREIGN KEY (ram_id) REFERENCES ram(ram_id))")


with open("computerbrands.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["NAME"]
        address=row["RESIDENCE"]
        age=row["AGE"]
        contact=row["CONTACT"]

        cust=db.execute("INSERT INTO customer(name,address,age,contact) VALUES(?,?,?,?)",name,address,age,contact)
        
        ram=row["COMPUTER RAM"]
        ram_id=id
        #ram_number=row["RamID"]
        ids = db.execute("INSERT INTO ram( ram_number) VALUES(?)", ram)

        brand_id=id
        name = row["NAME"]
        year_of_manufacture=row["YEAR OF MANUFACTURE"]
        hard_disk = ["HARD DISK TYPE"]
        db.execute("INSERT INTO brand(name,year_of_manufacture,hard_disk_type,customer_id,ram_id) VALUES(?,?,?,(SELECT customer_id FROM customer WHERE customer_id=?),(SELECT ram_id FROM ram WHERE ram_id=?));",name,year_of_manufacture,hard_disk,cust,ids)