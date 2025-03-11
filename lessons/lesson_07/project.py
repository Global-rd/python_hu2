def register_user(users, name, age):
    """
    Registers a user to the users list.
    """
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered: {user}")

def update_user_age(users, name, new_age):
    "Updates user's age based on the given name"
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            print(f"User {name}'s age has been updated to {new_age}")
            return
    print(f"No user named {name} is present in the users list")

def display_user_info(users, name):
    "Displays all information of a specific user"
    for user in users:
        if user["name"] == name:
            print(f"User info - Name: {user['name']} Age: {user['age']}")
    
def display_all_users(users):
    """
    Displays all information for all users.
    """
    print("Registered users:")
    for id, user in enumerate(users, 1):
        print(f"{id} - Name: {user['name']} Age: {user['age']}")


def main():
    users = []
    register_user(users=users, name = "Alice", age = 15)
    register_user(users=users, name = "Bob", age = 16)
    register_user(users=users, name = "Kathlyn", age = 17)
    register_user(users=users, name = "Dexter", age = 19)
    print(users)
    update_user_age(users=users, name="Alice", new_age=99)
    print(users)
    display_user_info(users=users, name="Bob")
    display_all_users(users=users)


#[{"name": "John", "age": 15},
# {"name": "John2", "age": 30}]

main()