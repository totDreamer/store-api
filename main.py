from store.exceptions import StoreError
from store.models import Order, Product, User


def main() -> None:
    user = User(id=1, name="Michael Bekker", email="brumaldreamer@gmail.com")
    product_1 = Product(id=1, name="Headphones 7HZ x Crinacle Zero:2", price=10000)
    product_2 = Product(id=2, name="Winx Club Cards One Box", price=4500)
    order_1 = Order(id=1, user=user)
    order_1.add_product(product=product_1, quantity=1)
    order_1.add_product(product=product_2, quantity=2)
    print(order_1.total)
    order_1.pay()
    print(order_1.status)
    try:
        order_1.add_product(product=product_1, quantity=1)
    except StoreError as error:
        print(error)


if __name__ == "__main__":
    main()
