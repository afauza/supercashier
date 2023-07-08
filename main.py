# Import class Transaction to run program
from transaction import Transaction
from transaction import tabulate

# Create object from class to begin
# Example could be observed through test cases

# test case 1
# t1 = Transaction()
# t1.add_item('ayam goreng',2,20000)
# t1.add_item('pasta gigi',3,15000)

# test case 2
# t1 = Transaction()
# t1.add_item('ayam goreng',2,20000)
# t1.add_item('pasta gigi',3,15000)
# t1.delete_item('pasta gigi')
# t1.check_order()

# test case 3
t1 = Transaction()
t1.add_item('ayam goreng',2,20000)
t1.add_item('pasta gigi',3,15000)
t1.reset_transaction()

# test case 4
# t1 = Transaction()
# t1.add_item('ayam goreng',2,20000)
# t1.add_item('pasta gigi',3,15000)
# t1.add_item('mainan mobil',1,200000)
# t1.add_item('mie instan',5,3000)
# t1.total_price()