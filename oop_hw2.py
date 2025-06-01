class Customer:
    def __init__(self, name, email, customer_id):
        self.name = name
        self.email = email
        self.__id = customer_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        if isinstance(new_id, int) and new_id > 0:
            self.__id = new_id
        else:
            raise ValueError("ID must be a positive integer")

    def __str__(self):
        return f"Customer {self.name} (ID: {self.__id}) - Email: {self.email}"

    def __repr__(self):
        return f"Customer(name='{self.name}', email='{self.email}', id={self.__id})"


c1 = Customer("Alice", "alice@example.com", 101)
c2 = Customer("Bob", "bob@example.com", 202)

print(c1)
print(repr(c2))

try:
    c1.id = -5
except ValueError as e:
    print("Caught error:", e)
