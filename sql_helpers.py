import pandas as pd

def run_sql_query(query, cursor):
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    return df

def create_lesson_8_db(cursor, connection):
    cursor.execute("CREATE DATABASE IF NOT EXISTS dataLesson8;")
    cursor.execute("USE dataLesson8;")
    drop_tables_query = """DROP TABLE IF EXISTS OrderContent, OnlineOrder, Product, Customer, Address;"""

    create_customer_table_query = """CREATE TABLE Customer
        (id INTEGER NOT NULL AUTO_INCREMENT,
         first_name VARCHAR(255) NOT NULL,
         last_name VARCHAR(255) NOT NULL,
         contact_number CHAR(15) NOT NULL,
         PRIMARY KEY (id)) AUTO_INCREMENT=1;"""

    create_address_table_query = """CREATE TABLE Address
        (id INTEGER NOT NULL AUTO_INCREMENT,
         house_name_number VARCHAR(255) NOT NULL,
         postcode VARCHAR(10) NOT NULL,
         customer_id INTEGER NOT NULL,
         is_default BOOL NOT NULL DEFAULT false,
         instructions TEXT,
         UNIQUE KEY (customer_id, is_default),
         PRIMARY KEY (id),
         FOREIGN KEY (customer_id) REFERENCES Customer(id)) AUTO_INCREMENT=1;"""

    create_product_table_query = """CREATE TABLE Product
        (id INTEGER NOT NULL AUTO_INCREMENT,
         title VARCHAR(255) NOT NULL,
         description TEXT NULL,
         price DECIMAL(5, 2) NOT NULL,
         category ENUM("Starters","Mains","Sides","Drinks"),
         PRIMARY KEY (id)) AUTO_INCREMENT=1;"""

    create_onlineOrder_table_query = """CREATE TABLE OnlineOrder
        (id INTEGER NOT NULL AUTO_INCREMENT,
         order_date DATETIME NOT NULL,
         customer_id INTEGER NOT NULL,
         delivery_address_id INTEGER NOT NULL,
         PRIMARY KEY (id),
         FOREIGN KEY (customer_id) REFERENCES Customer(id),
         FOREIGN KEY (delivery_address_id) REFERENCES Address(id)) AUTO_INCREMENT=1;"""

    create_orderContent_table_query = """CREATE TABLE OrderContent
        (order_id INTEGER NOT NULL,
         product_id INTEGER NOT NULL,
         amount INTEGER DEFAULT 1,
         PRIMARY KEY (order_id, product_id),
         FOREIGN KEY (order_id) REFERENCES OnlineOrder(id),
         FOREIGN KEY (product_id) REFERENCES Product(id)) AUTO_INCREMENT=1;"""

    insert_into_customer_table_query = """INSERT INTO Customer (first_name, last_name, contact_number) VALUES
        ("Ivor","Woodard","0800 407 6465"),
        ("Hakeem","Cross","0800 1111"),
        ("Leonard","Love","0800 947865"),
        ("Sal","Cobb","07064 474116"),
        ("Rhonda","Slater","0845 46 48"),
        ("Zeph","Mcknight","(016977) 5458"),
        ("Yoshio","French","0800 580161"),
        ("Darryl","Dillard","086 4778 6368"),
        ("Porter","Mcknight","01697 72332"),
        ("Maia","Logan","08 45 46 47");"""

    insert_into_address_table_query = """INSERT INTO Address (house_name_number, postcode, customer_id, is_default, instructions) VALUES
        ("53","X16 6UM",1,true,"Use side entrance"),
        ("65, Lodge House","BC01 7KJ",2,false,""),
        ("94","G2D 2QA",3,false,NULL),
        ("28","M2 1LE",4,true,""),
        ("5","OS7 6KB",5,false,NULL),
        ("122","I37 1QZ",6,false,""),
        ("17B","B8V 1LS",7,true,NULL),
        ("The Tower","XX44 2UW",1,false,"Ring doorbell twice"),
        ("18","H2M 9HM",9,true,NULL),
        ("88","C10 4LH",10,true,NULL);"""

    insert_into_product_table_query = """INSERT INTO Product (title, description, price, category) VALUES
        ("Mozzarela sticks (4)","Sticks of mozzarela cheese, coated in bread crumbs and fried",4.99,"Starters"),
        ("Garlic bread","Pizza dough with a garlic topping",3.50,"Starters"),
        ("BBQ ribs","A full rack of ribs covered in BBQ sauce",5.99,"Starters"),
        ("Garden salad","A mixed garden salad, including tomatoes, mixed peppers and crutons",1.50,"Starters"),
        ("Margherita pizza","The Italian classic, a thin crust and tomato-base, covered with mozzarela",9.99,"Mains"),
        ("Fried chicken (6 pieces)","Using 8 secret spices mixed in a breadcrumb coating",10.45,"Mains"),
        ("Coconut curry noodle bowl","A vegan noodle dish with cashews and pak choi",7.85,"Mains"),
        ("Onion rings","Covered in beer-infused batter and fried",2.00,"Sides"),
        ("Fries","Maris piper potatoes, thinly cut, and fried in sunflower oil",3.00,"Sides"),
        ("Vegan chocolate milkshake","Made with vegan chocolate ice 'cream' and oat m*lk",4.80,"Drinks");"""

    insert_into_OnlineOrder_table_query = """INSERT INTO OnlineOrder (order_date, customer_id, delivery_address_id) VALUES
        ("2021-01-23 01:41:50",10,1),
        ("2021-02-05 18:34:05",3,5),
        ("2021-02-28 19:15:30",5,9),
        ("2021-04-16 00:40:09",4,7),
        ("2021-04-21 20:29:11",8,1),
        ("2021-05-28 01:36:32",6,6),
        ("2021-06-30 23:36:46",8,3),
        ("2021-07-05 22:24:50",6,2),
        ("2021-07-14 17:25:12",8,7),
        ("2021-08-04 00:22:32",6,6),
        ("2021-08-22 19:33:49",1,3),
        ("2021-08-23 21:22:00",5,3),
        ("2021-09-09 18:41:56",7,6),
        ("2021-09-15 21:59:33",7,10),
        ("2021-09-16 22:44:37",4,5),
        ("2021-09-17 18:54:50",2,2),
        ("2021-10-11 22:39:26",7,5),
        ("2021-11-05 19:53:56",9,6),
        ("2021-12-24 20:04:18",2,5),
        ("2021-12-29 23:29:09",1,3);"""

    insert_into_OrderContent_table_query = """INSERT INTO OrderContent (order_id, product_id, amount) VALUES
        (1,4,2), (1,6,1), (1,10,3), (2,2,1), (2,7,4),
        (3,2,3), (3,6,1), (4,3,1), (4,5,1), (5,10,2),
        (6,5,2), (7,1,2), (7,2,2), (7,3,1), (7,4,2),
        (8,4,1), (8,8,1), (9,7,2), (10,1,2), (10,5,2),
        (10,8,1), (11,4,1), (12,2,2), (12,3,2), (13,5,3),
        (14,5,2), (15,1,1), (15,6,3), (15,7,2), (16,1,2),
        (16,3,2), (16,5,1), (16,8,3), (17,5,3), (18,6,2),
        (18,7,1), (19,2,3), (19,6,3), (19,8,3), (20,7,2);"""

    cursor.execute(drop_tables_query)
    cursor.execute(create_customer_table_query)
    cursor.execute(create_address_table_query)
    cursor.execute(create_product_table_query)
    cursor.execute(create_onlineOrder_table_query)
    cursor.execute(create_orderContent_table_query)
    cursor.execute(insert_into_customer_table_query)
    cursor.execute(insert_into_address_table_query)
    cursor.execute(insert_into_product_table_query)
    cursor.execute(insert_into_OnlineOrder_table_query)
    cursor.execute(insert_into_OrderContent_table_query)
    connection.commit()


