You will be writing code for recording the menu items and daily sales of a lemonade stand. It will have these classes: MenuItem, SalesForDay, and LemonadeStand. All data members of each class should be marked as **private** (a leading underscore in the name). Since they're private, if you need to access them from outside the class, you should do so via get or set methods.

Here are the method descriptions for the three classes:

**MenuItem:**

A MenuItem object represents a menu item to be offered for sale at the lemonade stand, which has three data members:
* a string for the item's name
* a float for the item's wholesale cost (how much the stand pays for the item)
* a float for the item's selling price (how much the stand sells the item for)

The Menu Item methods are:
* init method - takes three parameters (name, wholesale cost, selling price) and uses them to initialize the data members
* get methods for each of the data members: get_name(), get_wholesale_cost(), and get_selling_price()

**SalesForDay:**

A SalesForDay object represents the sales for a particular day, which has two data members:
* an integer for the number of days the stand has been open so far
* a dictionary whose keys are the names of the items sold and whose values are the numbers of those items sold that day

The SalesForDay methods are:
* init method - takes two parameters (number of days, sales dictionary) and uses them to initialize the data members
* get methods for each of the data members: get_day() and get_sales_dict()

**LemonadeStand:**
**Remember that the LemonadeStand class must not directly access the private data members of MenuItem and SalesForDay objects, but instead must call the appropriate get methods**

A LemonadeStand object represents a lemonade stand, which has four data members: 
* a string for the name of the stand
* an integer representing the current day
* a dictionary of MenuItem objects, where the keys are the names of the items and the values are the corresponding MenuItem objects
* a list of SalesForDay objects

The Lemonade Stand methods are:
* init method - takes one parameter, the name of the stand; initializes the name to that value, initializes current day to zero, initializes the menu to an empty dictionary, and initializes the sales record to an empty list
* a get method for the name: get_name()
* add_menu_item - takes as a parameter a MenuItem object and adds it to the menu dictionary. New items can be added to the menu on any day
* enter_sales_for_today - takes as a parameter a dictionary where the keys are names of items sold and the corresponding values are how many of the item were sold (see the example at the end of the readme). If an item in the menu doesn't appear in the dictionary, then there were no sales of that item on that day. If the name of any item sold doesn't match the name of any MenuItem in the dictionary of MenuItem objects, this method should do nothing except raise an **InvalidSalesItemError** (you'll need to define this exception class). Otherwise, it should create a new SalesForDay object using the current day and the dictionary that was passed in, add that object to the list of SalesForDay objects, and then increment the current day by 1
* sales_of_menu_item_for_day - takes as a parameter an integer representing a particular day and the name of a menu item. It returns the number of that item sold on that day. This method will use the given day to find the corresponding SalesForDay object in the list and then call its get_sales_dict method to get the dictionary of sales for that day. It will then look for the item name in the dictionary, taking into account that if an item in the menu doesn't appear in the dictionary, then there were no sales of that item on that day
* total_sales_for_menu_item - takes as a parameter the name of a menu item and returns the total number of that item sold over the history of the stand. This method can make use of sales_of_menu_item_for_day
* total_profit_for_menu_item - takes as a parameter the name of a menu item and returns the total profit on that item over the history of the stand. The profit for any item sold is the selling price of the item minus the wholesale cost of the item. This method can make use of total_sales_for_menu_item
* total_profit_for_stand - takes no parameters and returns the total profit on all items sold over the history of the stand. This method can make use of total_profit_for_menu_item

**Your LemonadeStand.py file must include a main function** that runs if the file is run as a script, but not if it's imported to another file.  Your main function should:
1. create a LemonadeStand object
2. create one or more MenuItem objects and add them to the LemonadeStand's menu
3. create a dictionary of sales for the day that includes sales of at least one item that isn't in the menu
4. try calling enter_sales_for_today(), passing that sales dictionary as the argument
5. If an InvalidSalesItem is raised, it should be caught with a try/except that prints an explanatory message for the user (otherwise the function should proceed normally)

In addition to your file containing the code for the above classes, **you must also submit a file that contains unit tests for your classes. It must have at least five unit tests and use at least two different assert functions.

Here's a very simple example of how your classes could be used:

stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
item2 = MenuItem('nori'), 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
item3 = MenuItem('cookie', 0.2, 1  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
day_0_sales = {
    'lemonade' : 5,
    'cookie'   : 2
}

stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}"  # print the total profit for lemonade so far
