import csv

def clear():
	f = open('names.csv', "w+")
	f.close()
repeat = "yes"
while(repeat == "yes"):

    
    choice = raw_input("\nadd\nview\nedit\ndelete\n\n>>>")

    if choice == "view":
    	file = open('names.csv', 'r')
    	for line in file:
    		print line	

    elif choice == "edit":
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




    elif choice == "add":
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

    elif choice == "delete":
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

	repeat = raw_input("do you wish to repeat? (yes/no): ")

	