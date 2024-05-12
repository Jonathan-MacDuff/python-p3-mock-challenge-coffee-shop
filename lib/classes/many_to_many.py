class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3 <= len(name) and not hasattr(self, "name"):
            self._name = name
        
    def orders(self):
        orders = []
        for order in Order.all:
            if order.coffee == self:
                orders.append(order)
        return orders
    
    def customers(self):
        customers = []
        for order in Order.all:
            if order.coffee == self and not customers.__contains__(order.customer):
                customers.append(order.customer)
        return customers
    
    def num_orders(self):
        order_count = 0
        for order in Order.all:
            if order.coffee == self:
                order_count += 1
        return order_count
    
    def average_price(self):
        price_total = 0
        price_count = 0
        for order in Order.all:
            if order.coffee == self:
                price_total += order._price
                price_count += 1
        return price_total/price_count


class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        orders = []
        for order in Order.all:
            if order.customer == self:
                orders.append(order)
        return orders

    
    def coffees(self):
        coffees = []
        for order in Order.all:
            if order.customer == self and not coffees.__contains__(order.coffee):
                coffees.append(order.coffee)
        return coffees
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and not hasattr(self, "price"):
            self._price = price