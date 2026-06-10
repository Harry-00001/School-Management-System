import tkinter as tk 
from tkinter import  ttk 
import logic
from tkinter import messagebox

	
def new_admission():
	
	win = tk.Tk()
	win.geometry("400x550")
	win.title ("Add Student")

	win["bg"]="Blue"
	
	def back_func():
		win.destroy()
		show_menu()
		

	back_button = ttk.Button(win , text = "<-" , command = back_func)
	back_button.pack(anchor = "nw" )
	
	heading  = tk.Label(win , text = "New Admission" , font = ("Arial", 20 , "bold"), background = "blue", foreground = "white")
	heading.pack()
	#Name Entry
	name_var = tk.StringVar()
	name_frame= ttk.Frame(win)
	name_frame.pack(pady = 10)
	name_label = ttk.Label(name_frame , text = "Name").pack(side = "left" , padx=5)
	name_entry = ttk.Entry(name_frame, textvariable = name_var )
	name_entry.pack(side = "left")
	
	#roll no entry
	roll_no_var = tk.StringVar()
	roll_no_frame= ttk.Frame(win)
	roll_no_frame.pack(pady = 10)
	roll_no_label = ttk.Label(roll_no_frame , text = "Roll no.").pack(side = "left" , padx=5)
	roll_no_entry = ttk.Entry(roll_no_frame, textvariable = roll_no_var )
	roll_no_entry.pack(side = "left")

	#class Entry 
	class_var = tk.StringVar()
	class_frame= ttk.Frame(win)
	class_frame.pack(pady = 10)
	class_label = ttk.Label(class_frame , text = "class").pack(side = "left" , padx=5)
	class_entry =ttk.Entry(class_frame  , textvariable= class_var)
	class_entry.pack(side = "left")
	
	#section
	section_var = tk.StringVar() 
	section_frame= ttk.Frame(win)
	section_frame.pack(pady = 10)
	section_label = ttk.Label(section_frame , text = "section").pack(side = "left" , padx=5)
	section_entry =ttk.Entry(section_frame , textvariable = section_var)
	section_entry.pack(side = "left")
	
	#House
	house_var = tk.StringVar()
	house_frame= ttk.Frame(win)
	house_frame.pack(pady = 10)
	house_label = ttk.Label(house_frame , text = "house").pack(side = "left" , padx=5)
	house_entry =ttk.Entry(house_frame , textvariable=house_var )
	house_entry.pack(side = "left")
	#any_post
	any_post_var = tk.StringVar()
	any_post_frame= ttk.Frame(win)
	any_post_frame.pack(pady = 10)
	any_post_label = ttk.Label(any_post_frame , text = "Any post").pack(side = "left" , padx=5)
	any_post_entry =ttk.Entry(any_post_frame ,textvariable = any_post_var)
	any_post_entry.pack(side = "left")
	
	#bus no
	bus_var = tk.StringVar()
	bus_frame= ttk.Frame(win)
	bus_frame.pack(pady = 10)
	bus_label = ttk.Label(bus_frame , text = "bus").pack(side = "left" , padx=5)
	bus_entry =ttk.Entry(bus_frame, textvariable=bus_var )
	bus_entry.pack(side = "left")
	
	#address
	address_var = tk.StringVar()
	address_frame= ttk.Frame(win)
	address_frame.pack(pady = 10)
	address_label = ttk.Label(address_frame , text = "Address").pack(side = "left" , padx=5)
	address_entry =ttk.Entry(address_frame ,textvariable=address_var )
	address_entry.pack(side = "left")
	
	#phone number
	phn_var = tk.StringVar()
	phn_frame= ttk.Frame(win)
	phn_frame.pack(pady = 10)
	phn_label = ttk.Label(phn_frame , text = "phone no.").pack(side = "left" , padx=5)
	phn_entry =ttk.Entry(phn_frame, textvariable = phn_var )
	phn_entry.pack(side = "left")
	
	#Father Name
	fan_var = tk.StringVar()
	fan_frame= ttk.Frame(win)
	fan_frame.pack(pady = 10)
	fan_label = ttk.Label(fan_frame , text = "Father Name").pack(side = "left" , padx=5)
	fan_entry =ttk.Entry(fan_frame , textvariable = fan_var)
	fan_entry.pack(side = "left")
	
	#Mother Name 
	mon_var = tk.StringVar()
	mon_frame= ttk.Frame(win)
	mon_frame.pack(pady = 10)
	mon_label = ttk.Label(mon_frame , text = "Mother Name").pack(side = "left" , padx=5)
	mon_entry =ttk.Entry(mon_frame , textvariable = mon_var)
	mon_entry.pack(side = "left")
	
	
	
	
	#Function to convert into dict and add in databse 
	def add_in_database():
		name= name_var.get()
		roll_no = roll_no_var.get()
		class_va = class_var.get()
		section= section_var.get()
		house= house_var.get()
		any_post = any_post_var.get()
		bus= bus_var.get()
		address = address_var.get()
		phn= phn_var.get()
		fan = fan_var.get()
		mon = mon_var.get()
		
		data = {
		"name":name,
		"roll_no":roll_no,
		"class":class_va , 
		"section":section , 
		"house":house ,
		"any post":any_post, 
		"bus":bus,
		"address":address,
		"phone number":phn,
		"father name":fan,
		"mother name":mon
		}
		
		logic.add_student(data)
		messagebox.showinfo("Done","student successfully added!!")
		
	#Done
	done_button = ttk.Button(win , text = "Done" , command = add_in_database)
	done_button.pack()
	
	win.mainloop()



#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII   FIND STUDENT  IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
def find_student  ():
	win = tk.Tk()
	win.geometry("400x400")
	win.title("Find Student")
	win["bg"]="Blue"
	
	def back_func():
		win.destroy()
		show_menu()
		

	back_button = ttk.Button(win , text = "<-" , command = back_func)
	back_button.pack(anchor = "nw" )
	
	heading  = tk.Label(win , text = "student detail" , font = ("Arial", 20 , "bold"), background = "blue", foreground = "white")
	heading.pack()
	
#_______________________________________________________ find student BY ADMISSION NUMBER _________________________________________________
	def by_adm():
		win.destroy()
		root= tk.Tk()
		root.title("Find STudent")
		root.geometry("400x450")
		root["bg"]="blue"
		def back_func():
			root.destroy()
			find_student()
		

		back_button = ttk.Button(root , text = "<-" , command = back_func)
		back_button.pack(anchor = "nw" )
		heading  = tk.Label(root , text = "Search Student " , font = ("Arial", 20 , "bold"), background = "blue", foreground = "white")
		heading.pack()
		
		adm_var = tk.StringVar()
		adm_frame= ttk.Frame(root)
		adm_frame.pack(pady = 10)
		adm_label = ttk.Label(adm_frame , text = "Enter Addmission Number:").pack(side = "left" , padx=5)
		adm_entry = ttk.Entry(adm_frame, textvariable = adm_var )
		adm_entry.pack(side = "left")
		
		def show_info ():
			argument = int(adm_var.get())
			data =logic.find_student_by_adm(argument)
			
			name_l= ttk.Label(root, text = f"Name :    {data[0][1]}           " , font = ("Arial" , 15 , "bold"))
			name_l.pack(padx = 10 ,  anchor = "w")
			
			roll_no_l = ttk.Label(root, text = f"roll no :       {data[0][2]}          " , font = ("Arial" , 15 , "bold"))
			roll_no_l.pack(padx = 10 ,  anchor = "w")
			
			section_l = ttk.Label(root, text =f"section:      {data[0][3]}            " , font = ("Arial" , 15 , "bold"))
			section_l.pack(padx = 10 , anchor = "w")
			
			clas_l = ttk.Label(root, text = f"class :          {data[0][4]}         " , font = ("Arial" , 15 , "bold"))
			clas_l.pack( padx = 10 ,   anchor = "w" )
			
			house_l = ttk.Label(root, text = f" house:      {data[0][5]}             " , font = ("Arial" , 15 , "bold"))
			house_l.pack( padx = 10 , anchor = "w")
			
			
			any_post_l = ttk.Label(root , text = f"any_post :        {data[0][6]}           " , font = ("Arial" , 15 , "bold"))
			any_post_l.pack( padx = 10 , anchor = "w")
			
			bus_l = ttk.Label(root , text = f"Bus :         {data[0][7]}          " , font = ("Arial" , 15 , "bold"))
			bus_l.pack(padx = 10 ,  anchor = "w")
			
			address_l = ttk.Label(root , text = f"address :      {data[0][8]}             " , font = ("Arial" , 15 , "bold"))
			address_l.pack( padx = 10 ,  anchor = "w")
			
			phn_l = ttk.Label(root , text = f"phone number :       {data[0][9]}            " , font = ("Arial" , 15 , "bold"))
			phn_l.pack(padx = 10 , anchor = "w")
			
			fan_l = ttk.Label(root , text = f"Father Name :         {data[0][10]}          " , font = ("Arial" , 15 , "bold"))
			fan_l.pack(padx = 10 , anchor = "w")
			
			mon_l = ttk.Label(root , text = f"Mother Name :         {data[0][11]}          " , font = ("Arial" , 15 , "bold"))
			mon_l.pack(padx = 10 , anchor = "w")
		
		done_button = ttk.Button(root, text = "Done" , command  = show_info )
		done_button.pack()
		
		
		
		win.mainloop()
		
#________________________find adm_____________________________		
	def find_adm ():
		win.destroy()
		root= tk.Tk()
		root.geometry("400x450")
		root.title("Find Admission Number")
		root["bg"]="blue"
		def back_func():
			root.destroy()
			find_student()
		

		back_button = ttk.Button(root , text = "<-" , command = back_func)
		back_button.pack(anchor = "nw" )
		
		heading  = tk.Label(root , text = "Find Admission number  " , font = ("Arial", 20 , "bold"), background = "blue", foreground = "white")
		heading.pack()
		
		#Name Entry
		nm_var = tk.StringVar()
		nm_frame= ttk.Frame(root)
		nm_frame.pack(pady = 10)
		nm_label = ttk.Label(nm_frame , text = "Enter Name:").pack(side = "left" , padx=5)
		nm_entry = ttk.Entry(nm_frame, textvariable = nm_var )
		nm_entry.pack(side = "left")
		# class
		cl_var = tk.StringVar()
		cl_frame= ttk.Frame(root)
		cl_frame.pack(pady = 10)
		cl_label = ttk.Label(cl_frame , text = "Enter class:").pack(side = "left" , padx=5)
		cl_entry = ttk.Entry(cl_frame, textvariable = cl_var )
		cl_entry.pack(side = "left")
		#Father Name
		fn_var = tk.StringVar()
		fn_frame= ttk.Frame(root)
		fn_frame.pack(pady = 10)
		fn_label = ttk.Label(fn_frame , text = "Enter Father Name:").pack(side = "left" , padx=5)
		fn_entry = ttk.Entry(fn_frame, textvariable = fn_var )
		fn_entry.pack(side = "left")
		
		def show_adm():
			nm = str(nm_var.get())
			cl = str(cl_var.get())
			fn = str(fn_var.get())
			
			data = logic.find_student_by_n_c_fn(nm , cl, fn)
			adm_label = ttk.Label(root , text = f" Admission Number :{data[0][0]}"  , font = ("Arial",10 , "bold"))
			adm_label.pack(pady =10)
		
		done_button = ttk.Button(root, text = "Done" , command  = show_adm )
		done_button.pack()
		
		root.mainloop()
		
		
	by_adm_button = ttk.Button(win , text = "Stu info by Addmission Number ", command = by_adm)
	by_adm_button.pack(pady=10, ipady = 20 , ipadx=20)
	
	find_adm_button = ttk.Button(win  , text = "Find Admission number" , command = find_adm)
	find_adm_button.pack(pady = 50 , ipady = 30 , ipadx=30)
	
	win.mainloop()


# ~ IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII     DO CHANGES   IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII	

def do_changes():
	win = tk.Tk()
	win.geometry("400x400")
	win.title("Do Changes")
	win["bg"]="Blue"
	
	def back_func():
		win.destroy()
		show_menu()
		

	back_button = ttk.Button(win , text = "<-" , command = back_func)
	back_button.pack(anchor = "nw" )
	
	heading  = tk.Label(win , text = "student detail" , font = ("Arial", 20 , "bold"), background = "blue", foreground = "white")
	heading.pack()
	
	adm_var = tk.StringVar()
	adm_frame= ttk.Frame(win)
	adm_frame.pack(pady = 10)
	adm_label = ttk.Label(adm_frame , text = "Enter Addmission Number:").pack(side = "left" , padx=5)
	adm_entry = ttk.Entry(adm_frame, textvariable = adm_var )
	adm_entry.pack(side = "left")
	
	column = tk.StringVar()
	column_list = ["admission no" , "name" , "roll_number","section" , "class" , "house" , "any_post" , "bus_no" , "address" , "phone_no" , "father_name" , "mother_name"]
	
	column_name = ttk.Combobox(win , values = column_list , textvariable = column)
	column_name.pack(padx = 50 , pady = 5 , ipadx = 50)
	
	new_var = tk.StringVar()
	new_frame= ttk.Frame(win)
	new_frame.pack(pady = 10)
	new_label = ttk.Label(new_frame , text = f"Enter New {column.get()}:").pack(side = "left" , padx=5)
	new_entry = ttk.Entry(new_frame, textvariable = new_var )
	new_entry.pack(side = "left")
	
	def change_conform():
		adm_arg = str(adm_var.get())
		column_arg= str(column.get())
		new_arg =str(new_var.get())
		logic.change(adm_arg , **{column_arg : new_arg})
		messagebox.showinfo("Done","Change Done!!")
		
	
	done_button = ttk.Button(win , text = "Done" , command = change_conform)
	done_button.pack()
	
	
	
	win.mainloop()
	
# ~ IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIshow all IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
	
def show_all ():
	pass
	

# ~ IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII     MAIN MENU  IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
def show_menu ():
	win = tk.Tk()
	win.geometry("400x450")
	win.title("Menu")
	win["bg"]="Blue"
	
	heading = ttk.Label(win , text ="School Management" , font = ("Arial", 30 , "bold"), background = "blue", foreground = "white")
	heading.pack ()
	
	def new_adm_func():
		win.destroy()
		new_admission()
		
		
	new_admission_label = ttk.Button(win , text = "New Admission" , command = new_adm_func)
	new_admission_label.pack(pady=10 , ipady = 10 , ipadx = 20)
	
	def call_change_func():
		win.destroy()
		do_changes()
		
		
	change_detail = ttk.Button(win , text = "Do Change", command =call_change_func)
	change_detail.pack(pady= 10 , ipady = 10 , ipadx = 20)
	
	def find_student_func():
		win.destroy()
		find_student()
		
	find_students = ttk.Button(win , text = "Find Student" , command = find_student_func)
	find_students.pack(pady= 10 , ipady = 10 , ipadx = 20)
	
	def show_all_call():
		messagebox.showinfo("pending" , "Add Later !!")
	
	show_all = ttk.Button(win , text = "show all student " , command = show_all_call)
	show_all.pack(pady= 10 , ipady = 10 , ipadx = 20)
	
	win.mainloop()
	

show_menu()
