from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv
from tkinter import ttk




root = Tk()
root.title('crm')
root.geometry("400x600")

#connect to my sql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "hema",
    database = "crms",
    )

#create to see if connection to mysql was created
#print(mydb)

#create a cursor and initialize it
my_cursor  = mydb.cursor()

#create database
#my_cursor.execute("create database crms")
#test to see if databases was created

#my_cursor.execute("show databases")
#for db in my_cursor:
   # print(db)
#drop table
#my_cursor.execute("drop table custmor")

#create a table
my_cursor.execute("create table if not exists customers(first_name VARCHAR(255), \
        last_name VARCHAR(255),\
        zipcode INT(10), \
        price_paid DECIMAL(10, 2),\
        user_id INT AUTO_INCREMENT PRIMARY KEY)")
# Alter Table
'''
my_cursor.execute("ALTER TABLE custmores ADD(\
                  email VARCHAR(255),\
                  address_1 VARCHAR(255),\
                  address_2 VARCHAR(255),\
                  city VARCHAR(50),\
                  state VARCHAR(50),\
                  country VARCHAR(255),\
                  phone VARCHAR(255),\
                  payment_method VARCHAR(50),\
                  discount_code VARCHAR(255))")'''


#show tables
'''my_cursor.execute("SELECT * FROM customers")
print(my_cursor.description)
for thing in my_cursor.description:
    print(thing)'''

#clear text Fields

def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0,END)
    address1_box.delete(0,END)
    address2_box.delete(0,END)
    city_box.delete(0,END)
    state_box.delete(0,END)
    zipcode_box.delete(0,END)
    country_box.delete(0,END)
    phone_box.delete(0,END)
    email_box.delete(0,END)
    payment_method_box.delete(0,END)
    discount_code_box.delete(0,END)
    price_paid_box.delete(0,END)

# submit Custmor To Database

def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    #commit the changes to the database
    mydb.commit()
    clear_fields()

# write to csv to excel function
def write_to_csv(result):
    with open('E:/customers.csv', 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)


#search customers
def search_customer():
    search_customers = Tk()
    search_customers.title("Search Customer")
    search_customers.geometry("1100x800")

    def update():
        sql_command = """UPDATE customers SET first_name = %s, last_name = %s, zipcode = %s, price_paid = %s, email = %s, address_1 = %s, address_2 = %s, city = %s, state = %s, country = %s, phone = %s, payment_method = %s, discount_code = %s WHERE user_id = %s"""
        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        zipcode = zipcode_box2.get()
        price_paid = price_paid_box2.get()
        email = email_box2.get()
        address_1 = address1_box2.get()
        address_2 = address2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_code_box2.get()
        
        id_value = id_box2.get()
        inputs = (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, id_value)

        my_cursor.execute(sql_command, inputs)
        mydb.commit()

        search_customers.destroy()
    
    def edit_now(id, index):
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id, )
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        print(result2)
        
        index +=1
        first_name_label = Label(search_customers, text="First Name").grid(row=index+1, column=0,sticky=W,  padx=10)
        last_name_label = Label(search_customers, text="Last Name").grid(row=index+2, column=0, sticky=W, padx=10)
        address1_label = Label(search_customers, text="Address 1").grid(row=index+3, column=0,sticky=W , padx=10)
        address2_label = Label(search_customers, text="Address 2").grid(row=index+4, column=0,sticky=W, padx=10)
        city_label = Label(search_customers, text="City").grid(row=index+5, column=0, sticky=W, padx=10)
        state_label = Label(search_customers, text="State").grid(row=index+6, column=0, sticky=W, padx=10)
        zipcode_label = Label(search_customers, text="Zipcode").grid(row=index+7, column=0,sticky=W, padx=10)
        country_label = Label(search_customers, text="Country").grid(row=index+8, column=0,sticky=W, padx=10)
        phone_name_label = Label(search_customers, text="phone").grid(row=index+9, column=0,sticky=W, padx=10)
        email_label = Label(search_customers, text="Email Address").grid(row=index+10, column=0,sticky=W,  padx=10)
        payment_method_label = Label(search_customers, text="Payment Method").grid(row=index+11, column=0,sticky=W, padx=10)
        discount_code_label = Label(search_customers, text="Discount Code").grid(row=index+12, column=0,sticky=W, padx=10)
        price_paid_label = Label(search_customers, text="Price Paid").grid(row=index+13, column=0, sticky=W, padx=10)
        id_label = Label(search_customers, text="User ID").grid(row=index+14, column=0, sticky=W, padx=10)

        #create entry boxes
        global first_name_box2
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row=index+1, column=1, pady=10)
        first_name_box2.insert(0, result2[0][0])

        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row=index+2, column=1, pady=5)
        last_name_box2.insert(0, result2[0][1])

        global address1_box2
        address1_box2 = Entry(search_customers)
        address1_box2.grid(row=index+3, column=1, pady=5)
        address1_box2.insert(0, result2[0][6])

        global address2_box2
        address2_box2 = Entry(search_customers)
        address2_box2.grid(row=index+4, column=1, pady=5)
        address2_box2.insert(0, result2[0][7])

        global city_box2
        city_box2 = Entry(search_customers)
        city_box2.grid(row=index+5, column=1, pady = 5)
        city_box2.insert(0, result2[0][8])
    
        global state_box2 
        state_box2 = Entry(search_customers)
        state_box2.grid(row=index+6, column=1, pady=5)
        state_box2.insert(0, result2[0][9])

        global zipcode_box2
        zipcode_box2 = Entry(search_customers)
        zipcode_box2.grid(row=index+7, column=1, pady=5)
        zipcode_box2.insert(0, result2[0][2])
        
        global country_box2 
        country_box2 = Entry(search_customers)
        country_box2.grid(row=index+8, column=1, pady=5)
        country_box2.insert(0, result2[0][10])

        global phone_box2 
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row=index+9, column=1, pady=5)
        phone_box2.insert(0, result2[0][11])

        global email_box2
        email_box2 = Entry(search_customers)
        email_box2.grid(row=index+10, column=1, pady=5)
        email_box2.insert(0, result2[0][5])

        global payment_method_box2 
        payment_method_box2 = Entry(search_customers)
        payment_method_box2.grid(row=index+11, column=1, pady=5)
        payment_method_box2.insert(0, result2[0][12])

        global discount_code_box2
        discount_code_box2 = Entry(search_customers)
        discount_code_box2.grid(row=index+12, column=1, pady=5)
        discount_code_box2.insert(0, result2[0][13])

        global price_paid_box2
        price_paid_box2 = Entry(search_customers)
        price_paid_box2.grid(row=index+13, column=1, pady=5)
        price_paid_box2.insert(0, result2[0][3])

        global id_box2
        id_box2 = Entry(search_customers)
        id_box2.grid(row=index+14, column=1, pady=5)
        id_box2.insert(0, result2[0][4])

        save_record = Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=index+15, column=0, padx=10)

        
        

    def seach_now():
        selected = drop.get()
        sql = ""
        
        if selected == "search by ...":
            test=Label(search_customers, text="hey! you forgot to pick a drop down selection")
            test.grid(row=3, column=0)
            #test.grid(row=2, column=0)
            
        if selected == "Last Name":
            #test = Label(search_customers, text = "you picked last Name")
            #test.grid(row=3, column =0)
            #test.grid(row=2, column=0)
            sql = "SELECT * FROM customers WHERE last_name = %s"

        if selected == "Email Address":
            #test = Label(search_customers, text = "you picked Email Address")
            #test.grid(row=3, column=0)
            #test.grid(row=2, column=0)
            sql = "SELECT * FROM customers WHERE email = %s"

        if selected == "Customer ID":
            #test = Label(search_customers, text = "you picked Customer ID")
            #test.grid(row=3, column=0)
            #test.grid(row=2, column=0)
            sql = "SELECT * FROM customers WHERE user_id = %s"
        
       
        searched = search_box.get()
        #sql = "SELECT * FROM customers WHERE last_name = %s"
        name= (searched,)
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record not found..."
            searched_label = Label(search_customers, text=result)
            searched_label.grid(row = 2, column=0)
            
        else:
            for index,x in enumerate(result):
                num=0
                index +=2
                id_reference = str(x[4])
                edit_button = Button(search_customers, text="Edit", command=lambda: edit_now(id_reference, index))
                edit_button.grid(row=index, column=num)
                for y in x:
                    searched_label = Label(search_customers, text=y)
                    searched_label.grid(row = index, column=num+1)
                    num +=1
                    csv_button = Button(search_customers, text = "Save to Excel", command = lambda:write_to_csv(result))
                    csv_button.grid(row= index+1, column=0)

         

        #searched_label = Label(search_customers, text=result)
        #searched_label.grid(row=2, column=0, padx=10, columnspan=2)
        

    #Entry Boxes to search for customer
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)

    
    #Entry box label search customer
    search_box_label = Label(search_customers, text="Search Customers ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    # Entry box search  Button for customer
    search_button = Button(search_customers, text="Search Customers",command=seach_now)
    search_button.grid(row=1, column=0, padx=10)

    #Dropdown box
    drop = ttk.Combobox(search_customers, values = ["Search by...", "Last Name", "Email Address", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2)
     
    

#List Customers
def list_customers():
    list_customer_query = Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.geometry("800x600")
    # Query The Database
    #my_cursor.execute("SELECT * FROM customers")
    #result = my_cursor.fetchall()
    my_cursor.execute("select * from customers")
    result = my_cursor.fetchall()
    
    for index, x in enumerate(result):
        num = 0
        for y in x:
            #lookup_label = Label(list_customer_query,text=x[0]+ ' ' + x[1]+ '' +x[5])lookup_label = Label(list_customer_query,text=y)
            lookup_label = Label(list_customer_query,text=y)
            lookup_label.grid(row=index, column=num)
            num += 1
        #print(x)
    csv_button = Button(list_customer_query, text = "Save to Excel", command = lambda:write_to_csv(result))
    csv_button.grid(row= index+1, column=0)

#crea main form to enter customrt data
first_name_label = Label(root, text="First Name").grid(row=1, column=0,sticky=W,  padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1").grid(row=3, column=0,sticky=W , padx=10)
address2_label = Label(root, text="Address 2").grid(row=4, column=0,sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0,sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0,sticky=W, padx=10)
phone_name_label = Label(root, text="phone").grid(row=9, column=0,sticky=W, padx=10)
email_label = Label(root, text="Email Address").grid(row=10, column=0,sticky=W,  padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0,sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=12, column=0,sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

#create entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady = 5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

#create buttons

add_customer_button = Button(root, text = "Add Custmoer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields",command=clear_fields)
clear_fields_button.grid(row=14, column=1)

#list customer buttons

list_customers_button = Button(root, text = "List Customer",command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=W, padx=10)

# Search Customers
search_customers_button = Button(root, text="Search/Edit Customers", command=search_customer)
search_customers_button.grid(row=15, column=1, sticky=W, padx=10)


'''my_cursor.execute("select * from customers")
result = my_cursor.fetchall()
for x in result:
    print(x)'''

root.mainloop()
