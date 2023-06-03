import unittest
from Library import LibraryItem, Patron, Library, Book, Album, Movie

class TestLibrary(unittest.TestCase):
  '''Contains unit tests for Library class'''

  def setUp(self):
    '''Sets up test vars'''
    self._book = Book("345", "Phantom Tollbooth", "Juster")
    self._book2 = Book("111", "Some Book", "FamousAuthor")
    self._album = Album("456", "...And His Orchestra", "The Fastbacks")
    self._movie = Movie("789", "The Dark Knight", "Some Dude")
    self._Felicity = Patron("abc", "Felicity")
    self._Waldo = Patron("bcd", "Waldo")
    self._Guermo = Patron("xyz", "Guermo")
    self._lib = Library()
    self._lib.add_library_item(self._book)
    self._lib.add_library_item(self._book2)
    self._lib.add_library_item(self._album)
    self._lib.add_library_item(self._movie)
    self._lib.add_patron(self._Felicity)
    self._lib.add_patron(self._Waldo)
    self._lib.add_patron(self._Guermo)

  def test_location_of_lib_item(self):
    '''Test location of library item'''
    location_of_movie = self._lib.lookup_library_item_from_id('789').get_location()
    self.assertEqual(location_of_movie, 'ON_SHELF')

  def test_movie_late_fee(self):
    '''Test location of library item'''
    self._lib.check_out_library_item('xyz', '789')
    for _ in range(10):
        self._lib.increment_current_date()
    amount_owed = self._Guermo.get_fine_amount()
    self.assertAlmostEqual(amount_owed, 0.30, 6)

  def test_check_out_item_not_on_shelf(self):
    '''Test location of library item'''
    self._lib.check_out_library_item('xyz', '789')
    already_checked_out = self._lib.check_out_library_item('xyz', '789')
    self.assertEqual(already_checked_out, 'item already checked out')

  def test_return_item(self):
    '''Test location of library item'''
    self._lib.check_out_library_item('xyz', '789')
    self._lib.request_library_item('bcd', '789')
    self._lib.return_library_item('789')
    location_message = self._lib.lookup_library_item_from_id('789').get_location()
    self.assertEqual(location_message, 'ON_HOLD_SHELF')

  def test_autgrader_results(self):
    '''Test location of library item'''
    self._lib.check_out_library_item('xyz', '456')
    self._lib.check_out_library_item('xyz', '789')
    for _ in range(15):
        self._lib.increment_current_date()
    self._lib.pay_fine('xyz', 0.70)
    new_amount = self._Guermo.get_fine_amount()
    self.assertAlmostEqual(new_amount, 0.20, 6)


if __name__ == '__main__':    
  unittest.main()
