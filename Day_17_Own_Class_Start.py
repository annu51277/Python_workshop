class User:

    def __init__(self,user_id,user_name,add):
        self.id = user_id
        self.name = user_name
        self.add = add
        self.followers= 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following +=1



user_1 = User("512","Ansar","Hyderabad")
user_2 = User("513","Arshia","Kokapet")

user_1.follow(user_2)

print(f"{user_1.name} following is {user_1.following} and followers are {user_1.followers}")
print(f"{user_2.name} following is {user_2.following} and followers are {user_2.followers}")