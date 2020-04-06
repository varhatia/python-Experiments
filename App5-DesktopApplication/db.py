import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='testDb' user='postgres' password='sherlock' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

#create_table()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='testDb' user='postgres' password='sherlock' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

#insert("Wine Glass", 12, 10.5)
#insert('Coffee Cup', 12, 10.5)
#insert('Tea Cup', 12, 10.5)
#insert('Water Glass', 12, 10.5)

def view():
    conn = psycopg2.connect("dbname='testDb' user='postgres' password='sherlock' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * from store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='testDb' user='postgres' password='sherlock' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE from store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

delete("Wine Glass") 

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='testDb' user='postgres' password='sherlock' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

update(11, 6, "Water Glass")

#print(view())