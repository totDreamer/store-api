from .exceptions import StoreOperationError, ValidationError
from .models import Order, Product, User


class Store:
    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._products: dict[int, Product] = {}
        self._orders: dict[int, Order] = {}

    def add_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise ValidationError("Argument should belong to class User")

        if user.id in self._users:
            raise StoreOperationError(f"User with id={user.id} already exists.")

        self._users[user.id] = user

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise ValidationError("Argument should belong to class Product")

        if product.id in self._products:
            raise StoreOperationError(f"Product with id={product.id} already exists.")

        self._products[product.id] = product

    def get_user(self, user_id: int) -> User:
        self._validate_id(user_id)

        if user_id not in self._users:
            raise StoreOperationError(f"User with id={user_id} does not exist")

        return self._users[user_id]

    def get_product(self, product_id: int) -> Product:
        self._validate_id(product_id)

        if product_id not in self._products:
            raise StoreOperationError(f"Product with id={product_id} does not exist")

        return self._products[product_id]

    def create_order(self, order_id: int, user_id: int) -> Order:
        self._validate_id(order_id)

        if order_id in self._orders:
            raise StoreOperationError(f"Order with id={order_id} already exists.")

        user = self.get_user(user_id)
        order = Order(order_id, user)
        self._orders[order_id] = order
        return order

    def add_product_to_order(self, order_id: int, product_id: int, quantity: int) -> None:
        order = self.get_order(order_id)
        product = self.get_product(product_id)
        order.add_product(product, quantity)

    def get_order(self, order_id: int) -> Order:
        self._validate_id(order_id)

        if order_id not in self._orders:
            raise StoreOperationError(f"Order with id={order_id} does not exist")

        return self._orders[order_id]

    @staticmethod
    def _validate_id(value: int) -> int:
        if type(value) is not int or value <= 0:
            raise ValidationError("id must be positive integer")
        return value
