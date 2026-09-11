from .exceptions import InvalidOrderStatus, ValidationError


class Product:
    def __init__(self, id: int, name: str, price: float) -> None:
        self._id = self._validate_id(id)
        self.name = self._validate_name(name)
        self.price = self._validate_price(price)

    @property
    def id(self) -> int:
        return self._id

    @staticmethod
    def _validate_id(value: int) -> int:
        if type(value) is not int or value <= 0:
            raise ValidationError("id must be positive integer")
        return value

    @staticmethod
    def _validate_name(value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValidationError("name cannot be empty")
        return value.strip()

    @staticmethod
    def _validate_price(value: float) -> float:
        if type(value) not in (int, float) or value <= 0:
            raise ValidationError("price must be positive number")
        return float(value)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id)


class User:
    def __init__(self, id: int, name: str, email: str) -> None:
        self._id = self._validate_id(id)
        self.name = self._validate_name(name)
        self.email = self._validate_email(email)

    @property
    def id(self) -> int:
        return self._id

    @staticmethod
    def _validate_id(value: int) -> int:
        if type(value) is not int or value <= 0:
            raise ValidationError("id must be positive integer")
        return value

    @staticmethod
    def _validate_name(value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValidationError("name cannot be empty")
        return value.strip()

    @staticmethod
    def _validate_email(value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValidationError("email cannot be empty")
        return value.strip()


class Order:
    def __init__(self, id: int, user: User) -> None:
        self._id = self._validate_id(id)
        self.user = self._validate_user(user)
        self._items: dict[Product, int] = {}
        self._status: str = "new"

    @property
    def id(self) -> int:
        return self._id

    def add_product(self, product: Product, quantity: int) -> None:
        if self.status != "new":
            raise InvalidOrderStatus(f"The order cannot be modified.\nid:{self.id}")
        self._validate_product(product)
        self._validate_quantity(quantity)
        self._items[product] = self._items.get(product, 0) + quantity

    @property
    def total(self) -> float:
        total_sum = 0.0
        for item, quantity in self._items.items():
            total_sum += item.price * quantity
        return total_sum

    @property
    def status(self) -> str:
        return self._status

    def pay(self) -> None:
        if self.status != "new":
            raise InvalidOrderStatus(f"Payment for a closed or cancelled order is not possible.\nid:{self.id}")
        self._status = "paid"

    def cancel(self) -> None:
        if self.status != "new":
            raise InvalidOrderStatus(f"It is not possible to cancel a closed or cancelled order.\nid:{self.id}")
        self._status = "cancelled"

    @staticmethod
    def _validate_id(value: int) -> int:
        if type(value) is not int or value <= 0:
            raise ValidationError("id must be positive integer")
        return value

    @staticmethod
    def _validate_user(value: object) -> User:
        if not isinstance(value, User):
            raise ValidationError("Argument should belong to class User")
        return value

    @staticmethod
    def _validate_product(value: object) -> Product:
        if not isinstance(value, Product):
            raise ValidationError("Item should belong to class Product")
        return value

    @staticmethod
    def _validate_quantity(value: int) -> int:
        if type(value) is not int or value <= 0:
            raise ValidationError("Quantity must be positive integer")
        return value
