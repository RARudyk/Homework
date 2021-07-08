class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def dict_from_class(self):
        _excluded_keys = set(AddressBook.__dict__.self())
        return dict(AddressBook(self)
                    for (key, value) in self.__dict__.AddressBook(self)
                    if key not in _excludet_keys)



a1 = AddressBook('23','Rom', '0962076022', 'Lviv', 'r.a.rudyk@gmail.com','23-09-1984','XX')


print(a1.name)
print(a1.key)
a1.key = 34
print(a1.key)