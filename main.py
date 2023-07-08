# Import class Transaction to run program
from transaction import Transaction

# Create object from class to begin
# example: t1 = Transaction()
t1 = Transaction()

t1.add_item('ayam goreng',2,20000)
t1.add_item('pasta gigi',3,15000)
t1.add_item('mainan mobil',1,200000)
t1.add_item('mie instan',5,3000)
t1.total_price()