from db import connect 

def add_student (add):
	
	conn = connect ()
	cursor= conn.cursor()
	cursor.execute("""
	INSERT INTO student_info(name,roll_number , class,section , house , any_post , bus_no , address , phone_no , father_name , mother_name) VALUES(?, ?,? ,?,?,?,?,?,?,?,?)
	""",tuple(add.values()))
	
	conn.commit()
	conn.close()
	
def delete_student(adm_no):
	conn = connect()
	cursor = conn.cursor()
	cursor.execute('''
	DELETE FROM student_info WHERE admission_no  = ?
	''',(adm_no,))
	conn.commit()
	conn.close()
	
def find_student_by_adm (adm_no):
	conn=connect()
	cursor = conn.cursor()
	cursor.execute("""
	SELECT * FROM student_info WHERE admission_no=? 
	""" , (adm_no,))
	result = cursor.fetchall()
	conn.close()
	return result 
	
def find_student_by_n_c_fn(name , cls , f_name):
	conn = connect()
	cursor = conn.cursor()
	cursor.execute("""
	SELECT * FROM student_info  WHERE name = ? AND class = ? AND father_name = ?
	""",(name , cls , f_name))
	result = cursor.fetchall()
	conn.close()
	return result 
	
def change(adm_no , **kwargs ):
	conn = connect()
	cursor =conn.cursor()
	fields=[]
	values=[]
	for column , value in kwargs.items():
		fields.append(f"{column}= ?")
		values.append(value)
		
	query = f"""UPDATE student_info SET {',  '.join(fields)}
	WHERE admission_no =?"""
	
	values.append(adm_no)
	cursor.execute(query , values )
	conn.commit ()
	conn.close()

def show_all():
	pass 



def main():
	pass
	
if __name__== "__main__":
	main()


