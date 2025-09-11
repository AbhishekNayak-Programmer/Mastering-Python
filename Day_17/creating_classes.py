class User: 
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0
        print('New user is created!')
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("Abhishek Nayak", "001")
user_2 = User("Adarsh Nayak", "002")

print(user_1.username)
print(user_1.id)

print(user_2.username)
print(user_2.id)

print("Before Calling Function")
print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)
print("Before Calling Function")

user_1.follow(user_2)

print("After Calling Function")
print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)
print("After Calling Function")