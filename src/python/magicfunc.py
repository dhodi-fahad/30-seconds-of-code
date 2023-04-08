class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2

print(v3.x)
print(v3.y)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle of Length: {self.length} and Width: {self.width}"

    def __eq__(self, other):
        return True if self.area() == other.area() else False

    def __lt__(self, other):
        return True if self.area() < other.area() else False


r1 = Rectangle(10, 5)
r2 = Rectangle(5, 10)
print(r1 == r2)
print(r1 < r2)

rect1 = Rectangle(4, 5)
rect2 = Rectangle(2, 10)

print(rect1 == rect2)  # False
print(rect1 < rect2)  # True


# ------ More About Magic Methods ------

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __getitem__(self, item):
        if self.id == item:
            return {'id': self.id,'username': self.username, 'password': self.password}
        else:
            return None

    def __eq__(self, other):
        if isinstance(other, User):
            return self.id == other.id and self.username == other.username and self.password == other.password
        return False


class Authenticator:
    def __init__(self, users):
        self.users = users

    def authenticate(self, id, username, password):
        user = User(id, username, password)
        if user in self.users:
            return True
        return False


u1 = User(1, 'john', 'password1')
u2 = User(2, 'doe', 'password2')
u3 = User(3, 'mark', 'password3')
u4 = User(4, 'james', 'password4')
u5 = User(5, 'peter', 'password5')
u6 = User(6, 'fahad', 'password6')
users = [u1, u2, u3, u4, u5, u6]

auth = Authenticator(users)
user_to_authenticate = u6[6]
result = auth.authenticate(user_to_authenticate['id'], user_to_authenticate['username'], user_to_authenticate['password'])
print(result)

