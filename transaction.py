# Import function tabulate from tabulate library to display data in table format
import tabulate

class Transaction():
    """
    Use to data the items to be bought, edit item details, and sum the price to
    be paid.

    Currently does not have the ability to store data inputted nor calculation
    results into a database; thus information would be wiped after every usage.
    """

    def __init__(self, cart = {}):
        """
        Contains empty dictionary named cart, in which the items would be
        stored and be used in function.
        """
        self._cart = cart

    def add_item(self, name: str, qty: int, price: int):
        """
        Add items to cart. After addition, the function will print the item
        being added previously.
        """
        try:
            name = name.title()           
            if isinstance(qty, int) and isinstance(price, int):
                self._cart.update({name: [qty, price]})
                print(f'{qty} of {name} each priced {price:,} has been added into the cart.')
            else:
                print('Please entry data in the correct type.')        
        except AttributeError:
            print('Please entry data in the correct type.')

    def update_item_name(self, item_name, new_item_name = None):
        """
        Updates the name of an item inside the cart. Would return an error if
        one of the parameters found missing.
        """
        if new_item_name is None:
            print('Incomplete parameter. Please input item name and its updated name.')

        else:
            if isinstance(item_name, str) and isinstance(new_item_name, str):
                item_name = item_name.title()
                new_item_name = new_item_name.title()
                if item_name in self._cart.keys():
                    self._cart[new_item_name] = self._cart.pop(item_name)
                    print(f'Item name "{item_name}" had been changed into "{new_item_name}".')
                else:
                    print(f'Item "{item_name}" is not in cart. Please try again.')
            else:
                print('Please input item name in string format.')

    def update_item_qty(self, item_name, new_qty = None):
        """
        Updates the quantity of an item inside the cart. Would return an error
        if one of the parameters found missing.
        """
        if new_qty is None:
            print('Incomplete parameter. Please input item name and its correct quantity.')

        else:
            if (isinstance(item_name, str) and isinstance(new_qty, int)):
                item_name = item_name.title()
                if item_name in self._cart.keys():
                    self._cart[item_name][0] = new_qty
                    print(f'The quantity of "{item_name}" had been changed to {self._cart.get(item_name)[0]}.')
                else:
                    print(f'Item "{item_name}" is not in cart. Please try again.')
            else:
                print('Please repeat function with the correct parameter.')

    def update_item_price(self, item_name, new_price = None):
        """
        Updates the price of an item inside the cart. Would return an error if
        one of the parameters found missing.
        """
        if new_price is None:
            print('Incomplete parameter. Please input item name and its correct price.')

        else:
            if (isinstance(item_name, str) and isinstance(new_price, int)):
                item_name = item_name.title()
                if item_name in self._cart.keys():
                    self._cart[item_name][1] = new_price
                    print(f'The price of "{item_name}" had been changed to {self._cart.get(item_name)[1]}.')
                else:
                    print(f'Item "{item_name}" is not in cart. Please try again.')
            else:
                print('Please repeat function with the correct parameter.')

    def delete_item(self, item_name = None):
        """
        Delete an item inside the cart. Repeat function to delete several items
        separately.
        """
        if item_name is None:
            print('Incomplete parameter. Please input item name you want to delete from the cart.')

        else:
            if isinstance(item_name, str):
                to_be_deleted = item_name.title()
                if to_be_deleted in self._cart.keys():
                    self._cart.pop(to_be_deleted)
                    print(f'Item "{to_be_deleted}" had been deleted from the cart.')
                else:
                    print(f'Item "{item_name}" is not in cart. Please try again.')
            else:
              print('Please input item name in string format.')

    def reset_transaction(self):
        """Empty the cart from any items."""
        self._cart.clear()
        print('Cart has been emptied successfully.')

    def check_order(self):
        """
        Return the items inside the cart in tabular format. Notify the user for
        blank item name.
        """
        if self._cart == {}:
            print('There are no items in the cart.')

        else:
            cart_data = [['No','Item name', 'Quantity', 'Price']]
            rownumber = 1
            for key, value in self._cart.items():
                cart_data.append([rownumber, key, value[0], value[1]])
                rownumber += 1
            print(tabulate(cart_data, headers = 'firstrow', tablefmt = 'github', numalign = 'center'))

            for i in cart_data:
                if i[1] == '':
                    print(f'There is a blank item name, please modify.')
                else:
                    pass

    def total_price(self):
        """
        Returns the list of items inside the cart and their sum of price.

        Discount would be given if the total price surpassed a certain amount,
        details as follows:
            Total price between 200,000 and 300,000 = 5%
            Total price between 300,000 and 500,000 = 8%
            Total price more than 500,000 = 10%

        Discount is automatically deducted from total price if applicable.
        """
        totals = 0

        for value in self._cart.values():
            price = value[0]*value[1]
            totals += price

        if totals > 500000:
            totals = totals * 0.9
        elif totals > 300000:
            totals = totals * 0.92
        elif totals > 200000:
            totals = totals * 0.95
        else:
            totals = totals
        
        print(f'Inside your cart:')
        for i in self._cart.items():
            print(f'{i[1][0]} of {i[0]} each priced {i[1][1]:,}.')
        print(f'The total price is {totals:,}.')