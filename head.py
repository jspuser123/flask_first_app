import sqlite3

con = sqlite3.connect('main.db')
cur = con.cursor()

    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
tbl="select * from ProductMovement"

cur.execute(tbl)
for x in cur.description:
    
    print(x)

con.commit()
con.close()
  