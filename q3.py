
user_list = []
# takes 5 inputs from a user and stores them into the user_list array 
for i in range(0,5):
	list = str(raw_input('Please enter a list item: '))
	user_list.append(list)


def list(strings):
	# create variable to hold the list					
	string = "<ul><br>"
	# loop through the list of strings and apply list tag to each element. 				
	for s in strings:
		string += "<li>" + s + "</li>" + "<br>"
	string += "</ul>"
	return string

# calls list function and passes the user inputed list
print(list(user_list))