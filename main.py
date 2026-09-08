class Product:
    def __init__(self, id, name, price):
        self.id = self._validate_id(id)
        self.name = self._validate_name(name)
        self.price = self._validate_price(price)

    @staticmethod
    def _validate_id(value):
        if type(value) is not int or value <= 0:
            raise ValueError("id must be positive integer")
        return value

    @staticmethod
    def _validate_name(value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name cannot be empty")
        return value.strip()

    @staticmethod
    def _validate_price(value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("price must be positive")
        return value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return NotImplemented

    def __hash__(self):
        return hash(self.id)


class User:
    def __init__(self, id, name, email):
        self.id = self._validate_id(id)
        self.name = self._validate_name(name)
        self.email = self._validate_email(email)

    @staticmethod
    def _validate_id(value):
        if type(value) is not int or value <= 0:
            raise ValueError("id must be positive integer")
        return value

    @staticmethod
    def _validate_name(value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name cannot be empty")
        return value.strip()

    @staticmethod
    def _validate_email(value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("email cannot be empty")
        return value.strip()


class Order:
    def __init__(self, id, user):
        self.id = self._validate_id(id)
        self.user = self._validate_user(user)
        self._items = {}
        self._status = "new"

    def add_product(self, product, quantity):
        if self.status != "new":
            raise InvalidOrderStatus(f"Нельзя изменить заказ.\nid:{self.id}")
        self._validate_product(product)
        self._validate_quantity(quantity)
        self._items[product] = self._items.get(product, 0) + quantity

    @property
    def total(self):
        total_sum = 0
        for item, quantity in self._items.items():
            total_sum += item.price * quantity
        return total_sum

    @property
    def status(self):
        return self._status

    def pay(self):
        if self.status != "new":
            raise InvalidOrderStatus(f"Оплата закрытого или отмененного заказа невозможна\nid:{self.id}")
        self._status = "paid"

    def cancel(self):
        if self.status != "new":
            raise InvalidOrderStatus(f"Отмена оплаченного или закрытого заказа невозможна.\nid:{self.id}")
        self._status = "cancelled"

    @staticmethod
    def _validate_id(value):
        if type(value) is not int or value <= 0:
            raise ValueError("id must be positive integer")
        return value

    @staticmethod
    def _validate_user(value):
        if not isinstance(value, User):
            raise TypeError("Argument should belong to class User")
        return value

    @staticmethod
    def _validate_product(value):
        if not isinstance(value, Product):
            raise TypeError("Item should belong to class Product")
        return value

    @staticmethod
    def _validate_quantity(value):
        if type(value) is not int or value <= 0:
            raise ValueError("Quantity must be positive integer")
        return value


class StoreError(Exception):
    pass


class InvalidOrderStatus(StoreError):
    pass
