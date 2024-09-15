class Cookie:
    def __init__(self, color):
        self.color = color
        type = None

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

cookie_one.type = "Gingerbread"
cookie_two.type = "Chocolate Chip"

print('Cookie one is', cookie_one.type)
print('Cookie two is', cookie_two.type)
