import sys
import unittest

sys.path.insert(0, "../../src")
from user import User


class TestUserOperationsClass(unittest.TestCase):

	def setUp(self):
		self._user = User()

	def test_User_init(self):
		self.assertEqual(self._user.friends, [])
		self.assertEqual(self._user.network, [])
		self.assertEqual(self._user.purchases, [])
		self.assertEqual(self._user.network_purchases, [])
		self.assertEqual(self._user.mean, 0.0)
		self.assertEqual(self._user.sd, 0.0)
		self.assertEqual(self._user.threshold, 0.0)

	def test_add_friend(self):
		self._user.add_friend('2')
		self.assertEqual(self._user.friends,['2'])
		self._user.add_friend('3')
		self.assertEqual(self._user.friends,['2','3'])

	def test_remove_friend(self):
		self._user.add_friend('4')
		self._user.add_friend('5')
		self._user.remove_friend('4')
		self.assertEqual(self._user.friends,['5'])
		self._user.remove_friend('5')
		self.assertEqual(self._user.friends,[])

	def tearDown(self):
		del self._user


class TestUserUpdateThresholdClass(unittest.TestCase):

	def test_update_threshold_1(self):
		user = User()
		user.network_purchases = [('',1.0), ('',2.0), ('',3.0), ('',5.0), ('',10.0), ('',6.0)]
		user.update_threshold()
		self.assertEqual(user.mean, 4.5)
		self.assertEqual('{0:.3f}'.format(user.sd), '2.986')
		self.assertEqual('{0:.3f}'.format(user.threshold), '13.458')

	def test_update_threshold_2(self):
		user = User()
		user.network_purchases = [('',1), ('',2), ('',3), ('',5), ('',10), ('',6)]
		user.update_threshold()
		self.assertEqual(user.mean, 4.5)
		self.assertEqual('{0:.3f}'.format(user.sd), '2.986')
		self.assertEqual('{0:.3f}'.format(user.threshold), '13.458')

	def test_update_threshold_3(self):
		user = User()
		user.network_purchases = []
		user.update_threshold()
		self.assertEqual(user.mean, 0.0)
		self.assertEqual(user.sd, 0.0)
		self.assertEqual(user.sd, 0.0)


if __name__ == '__main__':
    unittest.main()