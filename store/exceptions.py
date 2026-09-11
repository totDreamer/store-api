class StoreError(Exception):
    pass


class ValidationError(StoreError):
    pass


class OrderOperationError(StoreError):
    pass


class InvalidOrderStatus(OrderOperationError):
    pass
