class User:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return (
            """
        -----------------------------------
        - Name: """
            + self.name
            + """  
        - Message: """
            + self.message
            + """
        -----------------------------------
        """
        )


POSTS: User = []
MENU: str = """
    1- Create a post:
    2- Print posts:
    0- Exit
"""


def add_post():
    while True:
        name = input("Enter your name: ")
        message = input("Enter a message: ")
        if not name or not message:
            print("Sorry, your name/message should contain at least one character!")
            continue
        else:
            POSTS.append(User(name, message))
            break


def print_posts():
    if not POSTS:
        return print("No posts available!")
    for post in POSTS:
        print(post)


while True:
    choice = input(MENU)
    if int(choice) == 1:
        add_post()
    elif int(choice) == 2:
        print_posts()
    elif int(choice) == 0:
        print("Thank you for using our program.")
        break
