from store.exceptions import StoreOperationError
from store.models import Product, User
from store.services import Store


def main() -> None:
    user = User(id=1, name="Michael Bekker", email="brumaldreamer@gmail.com")

    product_1 = Product(id=1, name="Headphones 7HZ x Crinacle Zero:2", price=10000)
    product_2 = Product(id=2, name="Winx Club Cards One Box", price=4500)

    global_store = Store()
    global_store.add_user(user)
    global_store.add_product(product_1)
    global_store.add_product(product_2)

    global_store.create_order(1, user.id)
    global_store.add_product_to_order(1, product_1.id, 1)
    global_store.add_product_to_order(1, product_2.id, 2)

    print(global_store.get_order(1).total)

    try:
        global_store.get_product(3)

    except StoreOperationError as error:
        print(error)

    try:
        global_store.create_order(2, 2)

    except StoreOperationError as error:
        print(error)

    try:
        global_store.add_user(user)

    except StoreOperationError as error:
        print(error)

    try:
        global_store.add_product(product_1)

    except StoreOperationError as error:
        print(error)

    try:
        global_store.create_order(1, user.id)

    except StoreOperationError as error:
        print(error)

    try:
        global_store.create_order(3, 999)

    except StoreOperationError as error:
        print(error)

    try:
        global_store.get_order(3)

    except StoreOperationError as error:
        print(error)


if __name__ == "__main__":
    main()
