"""


"""
import sys
sys.path.insert(0, "../../src")

import unittest


from user import User
from universe import Universe
from flagger import Flagger


class TestUniverseOperationsClass(unittest.TestCase):

	def test_universe_init(self):
		univ = Universe(2,3)
		self.assertEqual(univ.T, 2)
		self.assertEqual(univ.D, 3)
		self.assertEqual(univ.users, {})

	def test_universe_create_user(self):
		univ = Universe(2,3)
		univ.create_user('1')
		self.assertTrue('1' in univ.users)
		univ.create_user('2')
		self.assertTrue('1' in univ.users)
		self.assertTrue('2' in univ.users)


class TestUniverserDetermineNetworkClass(unittest.TestCase):

	def test_determine_network_1(self):
		"""
		Test case 1:
		Friends of '1' : ['2','3']
		Friends of '2' : ['1','4']
		Friends of '3' : ['1']
		Friends of '4' : ['2']

		Network of '1' to degree 1 : ['2','3']
		Network of '1' to degree 2 : ['2','3','4']
		Network of '2' to degree 1 : ['1','4']
		Network of '2' to degree 2 : ['1','3','4']
		Network of '3' to degree 1 : ['1']
		Network of '3' to degree 2 : ['1','2']
		Network of '3' to degree 3 : ['1','2','4']
		Network of '4' to degree 1 : ['2']
		Network of '4' to degree 2 : ['2','1']
		Network of '4' to degree 3 : ['2','1','3']

		"""

		results = [
		{'user_id':'1', 'D':1, 'network':['2','3']},
		{'user_id':'1', 'D':2, 'network':['2','3','4']},
		{'user_id':'2', 'D':1, 'network':['1','4']},
		{'user_id':'2', 'D':2, 'network':['1','3','4']},
		{'user_id':'3', 'D':1, 'network':['1']},
		{'user_id':'3', 'D':2, 'network':['1','2']},
		{'user_id':'3', 'D':3, 'network':['1','2','4']},
		{'user_id':'4', 'D':1, 'network':['2']},
		{'user_id':'4', 'D':2, 'network':['1','2']},
		{'user_id':'4', 'D':3, 'network':['1','2','3']},
		]
		T = 5
		for r in results:
			univ = Universe(T, r['D'])
			univ.create_user('1')
			univ.create_user('2')
			univ.create_user('3')
			univ.create_user('4')
			univ.users['1'].add_friend('2')
			univ.users['1'].add_friend('3')
			univ.users['2'].add_friend('1')
			univ.users['2'].add_friend('4')
			univ.users['3'].add_friend('1')
			univ.users['4'].add_friend('2')
			nw = univ.determine_network(r['user_id'], avoid=[], level=1)
			self.assertEqual(len(nw), len(r['network']))
			for member in r['network']:
				self.assertTrue(member in nw)

	def test_determine_network_2(self):
		"""
		Test case 1:
		Friends of '1' : ['2','3']
		Friends of '2' : ['1']
		Friends of '3' : ['1','5']
		Friends of '4' : []
		Friends of '5' : ['3','6']
		Friends of '6' : ['5','7']
		Friends of '7' : ['6']



		Network of '1' to degree 1 : ['2','3']
		Network of '1' to degree 2 : ['2','3','5']
		Network of '1' to degree 3 : ['2','3','5','6']
		Network of '1' to degree 4 : ['2','3','5','6','7']
		Network of '1' to degree 5 : ['2','3','5','6','7']
		Network of '2' to degree 1 : ['1']
		Network of '2' to degree 2 : ['1','3']
		Network of '2' to degree 3 : ['1','3','5']
		Network of '2' to degree 4 : ['1','3','5','6']
		Network of '2' to degree 5 : ['1','3','5','6','7']
		Network of '3' to degree 1 : ['1','5']
		Network of '3' to degree 2 : ['1','5','2','6']
		Network of '3' to degree 3 : ['1','5','2','6','7']
		Network of '3' to degree 4 : ['1','5','2','6','7']
		Network of '3' to degree 5 : ['1','5','2','6','7']
		Network of '4' to degree 1 : []
		Network of '4' to degree 2 : []
		Network of '4' to degree 3 : []
		Network of '4' to degree 4 : []
		Network of '4' to degree 5 : []
		Network of '5' to degree 1 : ['3','6']
		Network of '5' to degree 2 : ['3','6','7','1']
		Network of '5' to degree 3 : ['3','6','7','1','2']
		Network of '5' to degree 4 : ['3','6','7','1','2']
		Network of '5' to degree 5 : ['3','6','7','1','2']
		Network of '6' to degree 1 : ['5','7']
		Network of '6' to degree 2 : ['5','7','3']
		Network of '6' to degree 3 : ['5','7','3','1']
		Network of '6' to degree 4 : ['5','7','3','1','2']
		Network of '6' to degree 5 : ['5','7','3','1','2']
		Network of '7' to degree 1 : ['6']
		Network of '7' to degree 2 : ['6','5']
		Network of '7' to degree 3 : ['6','5','3']
		Network of '7' to degree 4 : ['6','5','3','1']
		Network of '7' to degree 5 : ['6','5','3','1','2']


		"""

		results = [
		{'user_id':'1', 'D':1, 'network':['2','3']},
		{'user_id':'1', 'D':2, 'network':['2','3','5']},
		{'user_id':'1', 'D':3, 'network':['2','3','5','6']},
		{'user_id':'1', 'D':4, 'network':['2','3','5','6','7']},
		{'user_id':'1', 'D':5, 'network':['2','3','5','6','7']},
		{'user_id':'2', 'D':1, 'network':['1']},
		{'user_id':'2', 'D':2, 'network':['1','3']},
		{'user_id':'2', 'D':3, 'network':['1','3','5']},
		{'user_id':'2', 'D':4, 'network':['1','3','5','6']},
		{'user_id':'2', 'D':5, 'network':['1','3','5','6','7']},
		{'user_id':'3', 'D':1, 'network':['1','5']},
		{'user_id':'3', 'D':2, 'network':['1','5','2','6']},
		{'user_id':'3', 'D':3, 'network':['1','5','2','6','7']},
		{'user_id':'3', 'D':4, 'network':['1','5','2','6','7']},
		{'user_id':'3', 'D':5, 'network':['1','5','2','6','7']},
		{'user_id':'4', 'D':1, 'network':[]},
		{'user_id':'4', 'D':2, 'network':[]},
		{'user_id':'4', 'D':3, 'network':[]},
		{'user_id':'4', 'D':4, 'network':[]},
		{'user_id':'4', 'D':5, 'network':[]},
		{'user_id':'5', 'D':1, 'network':['3','6']},
		{'user_id':'5', 'D':2, 'network':['3','6','7','1']},
		{'user_id':'5', 'D':3, 'network':['3','6','7','1','2']},
		{'user_id':'5', 'D':4, 'network':['3','6','7','1','2']},
		{'user_id':'5', 'D':5, 'network':['3','6','7','1','2']},
		{'user_id':'6', 'D':1, 'network':['5','7']},
		{'user_id':'6', 'D':2, 'network':['5','7','3']},
		{'user_id':'6', 'D':3, 'network':['5','7','3','1']},
		{'user_id':'6', 'D':4, 'network':['5','7','3','1','2']},
		{'user_id':'6', 'D':5, 'network':['5','7','3','1','2']},
		{'user_id':'7', 'D':1, 'network':['6']},
		{'user_id':'7', 'D':2, 'network':['6','5']},
		{'user_id':'7', 'D':3, 'network':['6','5','3']},
		{'user_id':'7', 'D':4, 'network':['6','5','3','1']},
		{'user_id':'7', 'D':5, 'network':['6','5','3','1','2']},		

		]
		T = 5
		for r in results:
			univ = Universe(T, r['D'])
			univ.create_user('1')
			univ.create_user('2')
			univ.create_user('3')
			univ.create_user('4')
			univ.create_user('5')
			univ.create_user('6')
			univ.create_user('7')
			univ.users['1'].add_friend('2')
			univ.users['1'].add_friend('3')
			univ.users['2'].add_friend('1')
			univ.users['3'].add_friend('1')
			univ.users['3'].add_friend('5')
			univ.users['5'].add_friend('3')
			univ.users['5'].add_friend('6')
			univ.users['6'].add_friend('5')
			univ.users['6'].add_friend('7')
			univ.users['7'].add_friend('6')
			nw = univ.determine_network(r['user_id'], avoid=[], level=1)
			self.assertEqual(len(nw), len(r['network']))
			for member in r['network']:
				self.assertTrue(member in nw)


class TestUniverseUpdateNetworkPurchasesClass(unittest.TestCase):
	
	def test_update_network_purchases(self):
		"""
		Test Case:

		user '1' has network '2', '3', '4'

		user '1' purchases [('2017-06-13 11:33:01', 1.01),('2017-06-13 11:33:04', 1.02),('2017-06-13 11:33:07', 1.03)]
		user '2' purchases [('2017-06-13 11:33:00', 2.01),('2017-06-13 11:33:03', 2.02),('2017-06-13 11:33:04', 2.03)]
		user '3' purchases []
		user '4' purchases [('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)]

		"""

		# test T=2
		univ = Universe(T=2, D=2)
		univ.create_user('1')
		univ.create_user('2')
		univ.create_user('3')
		univ.create_user('4')
		univ.users['1'].purchases = [('2017-06-13 11:33:01', 1.01),('2017-06-13 11:33:04', 1.02),('2017-06-13 11:33:07', 1.03)]
		univ.users['2'].purchases = [('2017-06-13 11:33:00', 2.01),('2017-06-13 11:33:03', 2.02),('2017-06-13 11:33:04', 2.03)]
		univ.users['3'].purchases = []
		univ.users['4'].purchases = [('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)]
		univ.users['1'].network = ['2','3','4']
		univ.users['2'].network = ['1','3','4']
		univ.users['3'].network = ['2','1','4']
		univ.users['4'].network = ['2','3','1']

		univ.update_network_purchases('1')
		univ.update_network_purchases('2')
		univ.update_network_purchases('3')
		univ.update_network_purchases('4')

		self.assertEqual(univ.users['1'].network_purchases,[('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		self.assertEqual(univ.users['2'].network_purchases,[('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		self.assertEqual(univ.users['3'].network_purchases,[('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		#print('user 1 purchases: ', univ.users['1'].purchases)
		#print('nw: ', univ.users['4'].network_purchases)
		self.assertEqual(univ.users['4'].network_purchases[0][0],'2017-06-13 11:33:04')
		self.assertEqual(univ.users['4'].network_purchases[1][0],'2017-06-13 11:33:07')

		# test T=3
		univ = Universe(T=3, D=2)
		univ.create_user('1')
		univ.create_user('2')
		univ.create_user('3')
		univ.create_user('4')
		univ.users['1'].purchases = [('2017-06-13 11:33:01', 1.01),('2017-06-13 11:33:04', 1.02),('2017-06-13 11:33:07', 1.03)]
		univ.users['2'].purchases = [('2017-06-13 11:33:00', 2.01),('2017-06-13 11:33:03', 2.02),('2017-06-13 11:33:04', 2.03)]
		univ.users['3'].purchases = []
		univ.users['4'].purchases = [('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)]
		univ.users['1'].network = ['2','3','4']
		univ.users['2'].network = ['1','3','4']
		univ.users['3'].network = ['2','1','4']
		univ.users['4'].network = ['2','3','1']

		univ.update_network_purchases('1')
		univ.update_network_purchases('2')
		univ.update_network_purchases('3')
		univ.update_network_purchases('4')

		#print('network_purchases: ', univ.users['1'].network_purchases)
		self.assertEqual(univ.users['1'].network_purchases,[('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		self.assertEqual(univ.users['2'].network_purchases,[('2017-06-13 11:33:07', 1.03),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		self.assertEqual(univ.users['3'].network_purchases,[('2017-06-13 11:33:07', 1.03),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		#print('user 1 purchases: ', univ.users['1'].purchases)
		#print('nw: ', univ.users['4'].network_purchases)
		self.assertEqual(univ.users['4'].network_purchases[0][0],'2017-06-13 11:33:04')
		self.assertEqual(univ.users['4'].network_purchases[1][0],'2017-06-13 11:33:04')
		self.assertEqual(univ.users['4'].network_purchases[2][0],'2017-06-13 11:33:07')
		self.assertEqual(univ.users['1'].mean, 4.02)
		self.assertEqual('{0:.5f}'.format(univ.users['1'].threshold), '4.04449')



		# test T=30
		univ = Universe(T=30, D=2)
		univ.create_user('1')
		univ.create_user('2')
		univ.create_user('3')
		univ.create_user('4')
		univ.users['1'].purchases = [('2017-06-13 11:33:01', 1.01),('2017-06-13 11:33:04', 1.02),('2017-06-13 11:33:07', 1.03)]
		univ.users['2'].purchases = [('2017-06-13 11:33:00', 2.01),('2017-06-13 11:33:03', 2.02),('2017-06-13 11:33:04', 2.03)]
		univ.users['3'].purchases = []
		univ.users['4'].purchases = [('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)]
		univ.users['1'].network = ['2','3','4']
		univ.users['2'].network = ['1','3','4']
		univ.users['3'].network = ['2','1','4']
		univ.users['4'].network = ['2','3','1']

		univ.update_network_purchases('1')
		univ.update_network_purchases('2')
		univ.update_network_purchases('3')
		univ.update_network_purchases('4')

		#print('network_purchases: ', univ.users['2'].network_purchases)
		self.assertEqual(univ.users['1'].network_purchases,[('2017-06-13 11:33:00', 2.01),('2017-06-13 11:33:03', 2.02),('2017-06-13 11:33:04', 2.03),('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])
		self.assertEqual(univ.users['2'].network_purchases,[('2017-06-13 11:33:01', 1.01),('2017-06-13 11:33:04', 1.02),('2017-06-13 11:33:06', 4.01),('2017-06-13 11:33:07', 1.03),('2017-06-13 11:33:09', 4.02),('2017-06-13 11:33:10', 4.03)])


class TestUniverseAddPurchaseClass(unittest.TestCase):


	def test_add_purchase(self):

		flag_path = 'temp_flag.json'
		flagger = Flagger(flag_path)

		universe = Universe(T=2, D=2, flagger=flagger)

		universe.create_user('1')
		universe.create_user('2')
		universe.create_user('3')
		universe.create_user('4')

		universe.users['1'].network = ['2','4']
		universe.users['2'].network = ['1','4']
		universe.users['3'].network = []
		universe.users['4'].network = ['1','2']



		universe.add_purchase('1', '2017-06-13 11:33:04', 1)
		self.assertEqual(universe.users['1'].purchases, [('2017-06-13 11:33:04',1)])
		self.assertEqual(universe.users['2'].network_purchases, [('2017-06-13 11:33:04',1)])
		self.assertEqual(universe.users['2'].mean, 1.0)
		self.assertEqual(universe.users['2'].sd, 0.0)
		self.assertEqual(universe.users['2'].threshold, 1.0)
		self.assertEqual(universe.users['2'].purchases, [])
		self.assertEqual(universe.users['3'].network_purchases, [])
		self.assertEqual(universe.users['4'].network_purchases, [('2017-06-13 11:33:04',1)])

		universe.add_purchase('2', '2017-06-13 11:33:05', 1.5)
		self.assertEqual(universe.users['2'].purchases, [('2017-06-13 11:33:05', 1.5)])
		self.assertEqual(universe.users['2'].mean, 1.0)
		self.assertEqual(universe.users['2'].sd, 0.0)
		self.assertEqual(universe.users['2'].threshold, 1.0)
		self.assertEqual(universe.users['1'].network_purchases, [('2017-06-13 11:33:05', 1.5)])
		self.assertEqual(universe.users['4'].network_purchases, [('2017-06-13 11:33:04',1), ('2017-06-13 11:33:05', 1.5)])
		self.assertEqual(universe.users['4'].mean, 1.25)
		self.assertEqual(universe.users['3'].network_purchases, [])

		universe.add_purchase('3', '2017-06-13 11:33:06', 1.00)
		self.assertEqual(universe.users['2'].network_purchases, [('2017-06-13 11:33:04',1)])
		self.assertEqual(universe.users['1'].network_purchases, [('2017-06-13 11:33:05', 1.5)])
		self.assertEqual(universe.users['4'].network_purchases, [('2017-06-13 11:33:04',1), ('2017-06-13 11:33:05', 1.5)])

		universe.add_purchase('2', '2017-06-13 11:33:07', 2.0)
		self.assertEqual(universe.users['2'].purchases, [('2017-06-13 11:33:05', 1.5),('2017-06-13 11:33:07', 2.0)])
		self.assertEqual(universe.users['1'].network_purchases, [('2017-06-13 11:33:05', 1.5),('2017-06-13 11:33:07', 2.0)])
		self.assertEqual(universe.users['4'].network_purchases, [('2017-06-13 11:33:05', 1.5),('2017-06-13 11:33:07', 2.0)])

		universe.add_purchase('4', '2017-06-13 11:33:08', 10.0)
		universe.add_purchase('1', '2017-06-13 11:33:08', 19.0)
