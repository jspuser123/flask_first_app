from flask import Flask, render_template,redirect,request,flash
import sqlite3


app = Flask(__name__)

app.secret_key = 'super secret key'




@app.route('/' ,methods = ['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':

            return redirect('viewdata')
        elif request.form.get('action2') == 'VALUE2':

            return redirect('locatin')
        elif request.form.get('action3') == 'VALUE3':

            return redirect('product')
    
        
        

        else:
            print("not vlue data")
    
    return render_template('home.html')







@app.route('/viewdata')
def view():

    
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
    tbl="select * from ProductMovement"

    cur.execute(tbl)
    x =cur.fetchall()
    
        
    con.commit()
    con.close()
  
   
   

    return render_template('index.html',x=x)


@app.route('/addtable', methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        
        x2=request.form.get('date')
        x3=request.form.get('from_location')
        x4=request.form.get('to_location')
        x5=request.form.get('product_id')
        x6=request.form.get('product')
        x7=request.form.get('qty')

        if x2 and x3 and x4 and x5 and x6 and x7:



            con = sqlite3.connect('main.db')
            cur = con.cursor()

            tbl= """insert into  ProductMovement(date,from_location,to_location,product_id,product,'\u200bQty') values (?,?,?,?,?,?);"""
        
            sql=(x2,x3,x4,x5,x6,x7)
            cur.execute(tbl,sql)
        
                
            con.commit()
            con.close()
           
            print("insert data sucesfully")

            flash("Successfull  Prodect Add")
        else:
           
            flash("No move prodect add")
            
  
    return redirect('viewdata')
@app.route('/locatin')
def loc():
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
    tbl="select * from Location"

    cur.execute(tbl)
    x =cur.fetchall()

    print(x)
    
        
    con.commit()
    con.close()


   

    return render_template('loction.html',x=x)

@app.route('/locaddtable', methods = ['POST', 'GET'])
def addloc():
    if request.method == 'POST':
     
        
        x2=request.form.get('address')

        if x2:

            print(x2)
            con = sqlite3.connect('main.db')
            cur = con.cursor()
            

            
            cur.execute('insert into  Location(address) values (?)',(x2,))
                
            con.commit()
            con.close()
            print("insert data sucesfully")
            flash("Successfull  Location Add")
            

        else:
           
            flash("Location Not Successfull ADD")
           
        

    return redirect('/locatin')







@app.route('/product')
def product():
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
    tbl="select * from product"

    cur.execute(tbl)
    x1 =cur.fetchall()

    
        
    con.commit()
    con.close()
  
    return render_template('product.html',x1=x1)

@app.route('/locprotable', methods = ['POST', 'GET'])
def addpro():
    if request.method == 'POST':
     
       

        x2=request.form.get('produc')

        if x2:

           

            con = sqlite3.connect('main.db')
            cur = con.cursor()
           

            
            
            
            cur.execute('insert into  product(product) values (?)',(x2,))
        
                
            con.commit()
            con.close()
            print("insert data sucesfully")
            flash("Successfull  Product Add")
           
        else:
            print("not value product1")
            flash("Successfull  Product Add")


    return redirect('product')


@app.route('/<int:id>/editable/', methods = ['POST', 'GET'])
def editable(id):

   
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    print(id)
    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
    tbl="select * from ProductMovement where ​movement_id =?"

    cur.execute(tbl,str(id))
    for user in cur:
        print(user)
    
        
    con.commit()
    con.close()

  
    
    return render_template('edit.html' ,user=user)


@app.route("/update",methods=["POST","GET"])
def update():
    if request.method == 'POST':
        
        y1=request.form.get('id')
        y2=request.form.get('date')
        y3=request.form.get('from_location')
        y4=request.form.get('to_location')
        y5=request.form.get('product_id')
        y6=request.form.get('product')
        y7=request.form.get('qty')

        print(y1 +"this is id value")

        con = sqlite3.connect('main.db')
        cur = con.cursor()

        # tbl= """insert into  ProductMovement(​movement_id,date,from_location,​to_location,product_id,qty) values (?,?,?,?,?,?);"""
        tbl = """ UPDATE ProductMovement SET date=?,from_location=?,To_location=?,product_id=?,product=?,\u200bQty=? WHERE ​movement_id=?;"""
        sql=(y2,y3,y4,y5,y6,y7,y1)
        cur.execute(tbl,sql)

            
        con.commit()
        con.close()
        print("insert data sucesfully")
        return redirect ("/viewdata")
    
    
    

@app.route('/<int:id>/locedit1/', methods = ['POST', 'GET'])
def locedit1(id):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    print(id)
    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
    tbl="select * from Location where loction_id =?"

    cur.execute(tbl,str(id))
    for user in cur:
        print(user)
    
        
    con.commit()
    con.close()

  
    
    return render_template('locedit.html' ,user=user)

@app.route("/locupdate",methods=["POST","GET"])
def locupdate():
  

    if request.method == 'POST':
        y1=request.form.get('loction_id')
        y2=request.form.get('address')
       
        print(y1,y2)

        con = sqlite3.connect('main.db')
        cur = con.cursor()

        # tbl= """insert into  ProductMovement(​movement_id,date,from_location,​to_location,product_id,qty) values (?,?,?,?,?,?);"""
        tbl = """ UPDATE Location SET address=? WHERE loction_id=?;"""
        sql=(y2,y1)
        cur.execute(tbl,sql)

            
        con.commit()
        con.close()
        print("insert data sucesfully")

    return redirect ("/locatin")



@app.route('/proedit/<int:x>/', methods = ['POST', 'GET'])
def proedit(x):
    con = sqlite3.connect('main.db')
    cur = con.cursor()

 
    #tbl= """insert TABLE  ProductMovement(​movement_id,date,from_location,​to_location,product_id, ​qty);"""
    tbl="select * from product where product_id =?"

    cur.execute(tbl,str(x))
    for user in cur:
        print(user)
    
        
    con.commit()
    con.close()

  
   # return redirect ("/product")
    return render_template('product.html',user=user)

@app.route("/proupdate",methods=["POST","GET"])
def proupdate():
  

    if request.method == 'POST':
        y1=request.form.get('product_id')
        y2=request.form.get('product')
       
        print(y1,y2)

        con = sqlite3.connect('main.db')
        cur = con.cursor()

        # tbl= """insert into  ProductMovement(​movement_id,date,from_location,​to_location,product_id,qty) values (?,?,?,?,?,?);"""
        tbl = """ UPDATE product SET product=? WHERE product_id=?;"""
        sql=(y2,y1)
        cur.execute(tbl,sql)

            
        con.commit()
        con.close()
        print("insert data sucesfully")

    return redirect('product')