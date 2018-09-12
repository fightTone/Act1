import csv

def clear():
	f = open('names.csv', "w+")
	f.close()


def add():
	csvfile = open('names.csv', "a+")
	fieldnames = ['id_number','first_name', 'last_name']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	select = "yes"
	while(select == "yes"):
		arr = []
		arr.append(raw_input("enter ID no: ")+','+raw_input("enter First Name: ")+','+raw_input("enter Last Name: ")+'\n')
		#writer.writerow({'id_number': raw_input("enter ID no: "),'first_name': raw_input("enter First Name: "), 'last_name': raw_input("enter Last Name: ")})
		csvfile.writelines(arr)
		select = raw_input("do you want to add another student? (yes/no): ")

def edit():
	nput = raw_input("enter ID no: ")
	file = open('names.csv','r')
	arr = []
	for line in file:
		x = line.split(',')
		idnum = x[0]
		if idnum == nput:
			editwhat = raw_input("enter what you want to edit: \n-firstname\n-lastname\n\n>>>")
			if editwhat == "firstname":
				e_fname = raw_input("Enter changes: ")
				arr.append(x[0]+','+e_fname+','+x[2])
			elif editwhat == "lastname":
				e_lname = e_fname = raw_input("Enter changes: ")
				arr.append(x[0]+','+x[1]+','+e_lname+'\n')
					
		else:
			print "not"
			arr.append(line)
	file.close()
	opt_del = open('names.csv', 'w')
	opt_del.writelines(arr)
	opt_del.close()

def view():
	file = open('names.csv')
	for line in file:
		print line

def delete():
	arr = []
	nput = raw_input("enter ID no: ")
	file = open('names.csv', 'r')
	for line in file:
		x = line.split(',')
		idnum = x[0]
		if idnum == nput:
			print "DELETED"
		else:
			arr.append(x[0]+','+x[1]+','+x[2]+'\n')
			print line

	opt_del = open('names.csv', 'w')
	opt_del.writelines(arr)
	opt_del.close()


while(True):

    
    choice = raw_input("\nadd\nview\nedit\ndelete\nexit\n\n>>>")

    if choice == "view":
    	view()	

    elif choice == "edit":
    	edit()
    elif choice == "add":
    	add()

    elif choice == "delete":
    	delete()

    elif choice == "exit":
    	repeat = raw_input("are you sure you want to Exit? (yes/no): ")
    	if repeat == "no":
    		pass
    	elif repeat == "yes":
    		break

    else:
    	print "hmmm ... Wrong input !!!"