from utils.helpers import get_all_humans, write_new_human, check_email, change_items, is_email_correct

while True:
    print("1. Add new person \n2. Get all persons \n3. Edit person")
    flag = int(input("Choose what youwant to do: "))
    if flag ==1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        
        while check_email(email) == False:  
            print("Invalid Email") 
            break

        while is_email_correct(email) == False:
            print("This Email already exist")
            email = input("Enter new Email: ")
        else:
            human = {'first_name': first_name, "last_name": last_name, "email": email}
        write_new_human(human)

    elif flag ==2:
        humans = get_all_humans()
        for human in humans:
            print(human ["first_name"])
            print(human ["last_name"])
            print(human ["email"])
            print("-----------------------------------------------")

    elif flag == 3:
        change_id = int(input("Enter id to change item:"))
        change_items(change_id)
    else:
        print("Don't have this item")
        break
