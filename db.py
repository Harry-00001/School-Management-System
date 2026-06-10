import sqlite3 as sq

db_name="school.db"

def connect():
	return sq.connect(db_name)
	
def create_table ():
	conn = connect ()
	cursor = conn.cursor()
	
	cursor.execute("""
	CREATE TABLE IF NOT EXISTS student_info (
	admission_no INTEGER PRIMARY KEY AUTOINCREMENT ,
	name TEXT,
	roll_number TEXT,
	class TEXT,
	section TEXT,
	house TEXT,
	any_post TEXT , 
	bus_no TEXT,
	address TEXT,
	phone_no TEXT ,
	father_name TEXT,
	mother_name TEXT
	)""")
	conn.commit()
	conn.close ()
create_table()

def main():
	pass
	
if __name__== "__main__":
	main()

