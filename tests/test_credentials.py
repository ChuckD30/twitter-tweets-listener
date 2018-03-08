import unittest
from subprocess import call
try:
    from unittest import mock
except ImportError:
    import mock

from credentials import TwitterCredentials

class CredentialsTestCase(unittest.TestCase):

    def test_can_access_twitter_credentials(self):
        twitter_credentials = TwitterCredentials()
        self.assertTrue(twitter_credentials.consumer_key != "")
        self.assertTrue(twitter_credentials.consumer_secret != "")
        self.assertTrue(twitter_credentials.access_token != "")
        self.assertTrue(twitter_credentials.access_secret != "")
