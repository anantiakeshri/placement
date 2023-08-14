#Fun-ction with output.

fname = input("What is your first name?  ")
lname = input("What is your last name?  ")
    
def format_name(fname, lname):
    first_name = fname.title()
    last_name = lname.title()
    return f"{first_name} {last_name}"
    
print(format_name(fname, lname))