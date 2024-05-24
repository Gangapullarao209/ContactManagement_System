def displayContacts():
    f=open("contacts.txt","r")
    print(f.read())
    f.close()
def addContacts():
    f=open("contacts.txt","a")
    name=input("Enetr Name : ")
    no=input("Enter mobile no : ")
    f.write(name+" : "+no+"\n")
    f.close()
def delete():
    # Open the contacts file in read mode
    f = open("contacts.txt", "r")
    contacts = f.readlines()
    f.close()
    
    # Open the contacts file in write mode
    f = open("contacts.txt", "w")
    
    # Get the name to delete from the user
    keyName = input("Enter name you want to delete: ")
    
    # Initialize a flag to track if the contact was found and deleted
    found = False
    
    # Iterate over each contact
    for person in contacts:
        # Split each line into name and number
        name, no = person.strip().split(" : ")
        
        # If the name does not match the keyName, write it back to the file
        if name != keyName:
            f.write(person)
        else:
            # If a match is found, set the flag to True
            found = True
    
    # Close the file after writing
    f.close()
    
    # Print appropriate message based on whether the contact was found
    if found:
        print("Contact deleted")
    else:
        print("Contact not found")

# Call the delete function
delete()
