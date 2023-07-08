# Super Cashier

## Background

A fictional supermarket wants to expand its services into online territory by providing a self-service checkout system for the customers. The customers would be asked to input the product name, qty, and price directly into the system to put the order. The system itself would be required to process the data, namely calculating total price and incorporating any discounts available.

## Requirements 
Based on the background, the system would need several features, namely:
1. A feature to add items to cart, with details such as item name, quantity, and price
2. A feature to update items that has been added, just in case there were errors with name, quantity, or price
3. A feature to check what’s in the cart
4. A feature to remove items in cart, whether individual items or the whole cart itself
5. A feature to display total price that must be paid, deducted by amount of discounts available

Considering the requirements above, the journey would be as follows:

![!\[Working flowchart\](<C:\Users\asus\Desktop\sc\images\Final Project Python.png>)](<images/Final Project Python.png>)

To begin, the customers would be asked to assign ID for the upcoming transaction by making an object from the class Transaction. Everytime the ID is assigned, the system would create an empty cart in which the items would be inputted. After the ID is assigned, customers could begin inputting items they intended to buy through the use of a function called add_items. Next, the customers could continue the transaction via several options with respective functions; update item details via update_item, remove particular item from cart via delete_item, or to discard all items in their cart via reset_transaction. While customers done with updating items or removing particular items might want to check their order to know what’s in their cart and its total price, they might do so by running check_order and total_price, respectively. On the other hand, customers discarding every item in their cart might want to start from scratch, hence the loop going into add_items, or to stop the transaction and quit the program altogether.

## Code explanation
To run the class Transaction, the customer could do so after installing the package requirements (listed in requirements.txt), importing Transaction from transaction.py and running main.py.

transaction.py contains class Transaction that provides all the functions needed in the program, while main.py was purposefully left blank except for necessary function and library as it would serve as an executable script for the customer.

To make sure that the functions in class Transaction could be understood clearly, here’s the explanation of each corresponding function inside the class Transaction and how to use them.
1. add_item(name, qty, price)\
   Add an item or multiple items in a single run. Name refers to item name (str), whereas qty and price refers to item quantity (int) and item price (int), respectively.
   Items added would occupy the empty dictionary called cart with the item name as key while quantity and price would form a list that would become the value.

2. update_item_name(item_name, new_item_name)\
   Through this function, the customer can update the name of the item on the cart. The parameter item_name (str) refers to the current item name, while new_item_name (str) refers to the correct item name.
   The function was designed with a nested if that would throw errors if one or both parameters were missing, item_name is not on the cart, or the parameters were inputted in the wrong format. In the case of success, this function will print a statement to confirm that the item name had been changed.

3. update_item_qty(item_name, new_qty)\
   Similar to update_item_name in design, however the details changed is the quantity of the item on the cart. The parameter item_name (str) refers to the item name, while new_qty (int) refers to the correct item quantity.
   The error handling is also similar, yet this function will print a statement to confirm the change in quantity in the case of success.

4. update_item_price(item_name, new_price)\
   Similar to update_item_name in design, however the details changed is the price of the item on the cart. The parameter item_name (str) refers to the item name, while new_price (int) refers to the correct item price.
   The error handling is also similar, yet this function will print a statement to confirm the change in item price in the case of success.

5. delete_item(item_name)\
   Can only delete a single item for every call. The corresponding information tied to the item, such as quantity and price, would also be removed from cart.
   The function was designed with a nested if that would throw errors if the parameter was missing, item_name is not on the cart, or the parameter was inputted in the wrong format. During success, this function will print a statement to confirm that the item has been deleted from cart.

6. reset_transaction()\
   Discard every item inside the cart. The function will print a statement to confirm if the process is successful.

7. check_order()\
   Display the list of items inside the cart in a tabular format, except when there are no items in the cart. If one of the items had blank string as name, this function will also print a statement to inform the customer.

8. total_price()\
   Returns the list of items inside the cart and their sum of price, with discount automatically deducted from total price if applicable. The conditions for discount are as follows:

       Purchase between 200,000 and 300,000 = 5% discount
       Purchase between 300,000 and 500,000 = 8% discount
       Purchase more than 500,000 = 10% discount

## Test case
To give examples on how to use the code, listed below were test codes and the following results:\
1. add_items()\
   input:\
   ![!\[Alt text\](<Question 1.png>)](<images/Question 1.png>)

   result:\
   ![!\[!\\[Alt text\\](<images/Test Case 1.png>)\](images/image-1.png)](<images/Testcase 1.png>)

2. delete_items(), check_order()\
   input:\
   ![!\[Alt text\](image-3.png)](<images/Question 2.png>)

   result:\
   ![!\[Alt text\](image-2.png)](<images/Testcase 2.png>)

3. reset_transaction()\
   input:\
   ![!\[Alt text\]\[\]](<images/Question 3.png>)

   result:\
   ![Alt text](<images/Testcase 3a.png>)

4. total_price()\
   input:\
   ![!\[Alt text\](image-6.png)](<images/Question 4.png>)
   
   result:\
   ![!\[Alt text\](<Test Case 4.png>)](<images/Testcase 4.png>)

## Future work
There are things to be explored to make this project more useful, such as listing every transaction inside a separate database to track transaction history. It is also feasible to record customers doing the transaction, so supermarket owners may reward loyal customers or to promote particular products popular with the customers.