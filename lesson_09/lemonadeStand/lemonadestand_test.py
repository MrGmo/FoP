import unittest
from LemonadeStand import MenuItem, LemonadeStand, InvalidSalesItemError

class TestLemonadeStand(unittest.TestCase):
  '''Contains unit tests for Lemonade Stand class'''

  def test_total_profit_of_stand(self):
    '''Tests if total profit for the stand over its history is being calculated properly'''
    stand = LemonadeStand('LemonHead')
    item1 = MenuItem('lemonade', 1.75, 3.50)
    item2 = MenuItem('cupcake', .60, 1.50)
    stand.add_menu_item(item1)
    stand.add_menu_item(item2)
    day_0 = {
    'lemonade' : 3,
    'cupcake' : 5
    }
    day_1 = {
    'cupcake' : 2
    }
    day_2 = {
    'lemonade' : 5
    }
    stand.enter_sales_for_today(day_0)
    stand.enter_sales_for_today(day_1)
    stand.enter_sales_for_today(day_2)
    total_profit = stand.total_profit_for_stand()
    self.assertEqual(total_profit, 20.30)


  def test_total_profit_for_poptart(self):
    '''Tests if the total profit for the poptart menu item is correct to six decimal places'''
    stand = LemonadeStand('Lemon\s')
    item1 = MenuItem('lemon ice', 1.0, 1.85)
    item2 = MenuItem('poptart', 0.43, 1.59)
    stand.add_menu_item(item1)
    stand.add_menu_item(item2)
    day_0 = {
    'lemon ice' : 13,
    'poptart' : 2
    }
    day_1 = {
    'poptart' : 16
    }
    stand.enter_sales_for_today(day_0)
    stand.enter_sales_for_today(day_1)
    total_profit = stand.total_profit_for_menu_item('poptart')
    self.assertAlmostEqual(total_profit, 20.88, 6)


  def test_invalid_sales_error(self):
    '''Tests if the InvalidSalesItemError is raised if an item sold is not in the menu list'''
    stand = LemonadeStand('LemonKidz')
    item1 = MenuItem('lemonz', 0.5, 1.50)
    item2 = MenuItem('fudge', 0.30, 1.05)
    stand.add_menu_item(item1)
    stand.add_menu_item(item2)
    day_0 = {
    'fudge' : 8,
    'lemonz' : 2, 
    'cake': 10
    }
    with self.assertRaises(InvalidSalesItemError):
      stand.enter_sales_for_today(day_0)


  def test_sales_of_menu_item_for_day_that_doesnt_exist(self):
    '''Tests if the correct message is returned to the user if they query the sales for a day that does not exist'''
    stand = LemonadeStand('Lemon Arcade')
    item1 = MenuItem('lemon pops', 1.0, 2.00)
    item2 = MenuItem('chips', 1.00, 2.00)
    stand.add_menu_item(item1)
    stand.add_menu_item(item2)
    day_0 = {
    'lemon pops' : 10,
    'chips' : 20
    }
    stand.enter_sales_for_today(day_0)
    total_profit = stand.sales_of_menu_item_for_day(1, 'chips')
    self.assertEqual(total_profit, 'No information found for that day')


  def test_total_sales_for_menu_item(self):
    '''Tests the total sales for wallnuts to make sure it does not equal an incorrect number'''
    stand = LemonadeStand('Lemon House')
    item1 = MenuItem('lemon-flakes', 1.50, 2.75)
    item2 = MenuItem('wallnuts', 1.00, 3.00)
    stand.add_menu_item(item1)
    stand.add_menu_item(item2)
    day_0 = {
    'lemon-flakes' : 10,
    'wallnuts' : 20
    }
    day_1 = {
    'wallnuts' : 20
    }
    stand.enter_sales_for_today(day_0)
    stand.enter_sales_for_today(day_1)
    total_sales = stand.total_sales_for_menu_item('wallnuts')
    self.assertNotEqual(total_sales, 100) # should be 40


if __name__ == '__main__':    
  unittest.main()