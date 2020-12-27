travelling = input("Are you travelling: ")
passengers = {}


def user_data(passengers):
    n = int(input("How many passengers are travelling: "))
    pass_id = 1
    for n in range(n):
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        sex = input("Male or Female: ")
        passengers[pass_id] = {}
        passengers[pass_id]["Name"] = name
        passengers[pass_id]["Age"] = age
        passengers[pass_id]["Sex"] = sex
        pass_id += 1
    return passengers


def reservation_train(travelling):
    while travelling == 'yes':
        user_data(passengers)
        travelling = input("Oops! Did you forget someone? ")
        print(passengers)


reservation_train(travelling)
