
# creating a new list
clothes = ["socks", "shirt", "skirt", "scarf"]

def insert_element(new_cloth, index=0):
    """inserts a new element into a specified position"""
    global clothes
    clothes.insert(index, new_cloth)
    print (clothes)

# test calls
insert_element("pants", 3)
insert_element("hat", -2)
insert_element("coat")


employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]

def replace_employee(employees, old_employee, new_employee):
    """replaces an old employee by a new one by names"""
    #getting index of the old employee and saving it
    index = employees.index(old_employee)
    #deleting the old employee
    del employees[index] #yes, I remember about "pop" built-in function from the lecture, just like this one better :)
    #inserting the new employee to the position of the old one
    employees.insert(index, new_employee)

# test call
replace_employee(employee_shift,"Kelly", "Maria") # poor Kelly...
print(employee_shift)

