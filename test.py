import unittest
import json
from Tweet import buildtweet
from DeleteTweet import builddeletetweet

#testing jonathan's API calls
class TestTweet(unittest.TestCase):
	#test cases for Tweet and Delete Tweet 
	def test_1_empty_tweet(self):
		sample = {'parameters_tweet' : ''}
		res = json.loads(buildtweet(sample))
		self.assertTrue(res['errors'])

	#test tweeting a tweet and immediately deleting it to keep the id around
	def test_2_tweet_and_delete(self):
		sample = {'parameters_tweet' : 'UNIT TEST TWEET'}
		res = json.loads(buildtweet(sample))
		temp_id = res['id_str']
		self.assertEqual(res['text'], 'UNIT TEST TWEET')

		sample = {'parameters_id' : temp_id}
		res = json.loads(builddeletetweet(sample))
		self.assertEqual(res['text'], 'UNIT TEST TWEET')

	#test deleting a tweet that doesn't exist
	def test_3_bad_id_for_delete(self):
		sample = {'parameters_id' : '0'}
		res = json.loads(builddeletetweet(sample))
		self.assertTrue(res['errors'])




if __name__ == '__main__':
    unittest.main()