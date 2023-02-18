from utils.helpers import get_all_humans, write_new_human

while True:
    print("1. Add new person \n2. Get all persons")
    flag = int(input("Choose what youwant to do: "))
    if flag ==1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        data=get_all_humans()
        human = {"first_name":first_name, "last_name":last_name,"email":email}
        write_new_human(human)

    elif flag ==2:
        humans = get_all_humans()
        for human in humans:
            print(human ["first_name"])
            print(human ["last_name"])
            print(human ["email"])
            print("-----------------------------------------------")
