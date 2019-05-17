import unittest
from UnbabelChallenge.Services import db_connection, authentication_service
from UnbabelChallenge.Model import User

class TestDbConnection(unittest.TestCase):
	
	def setUp(self):
		self.def_name = 'David'
		self.def_email = 'test-user-email@test-unbabel'
		self.def_pw_hass = 'superSafeHash'

		self.def_translation_text = 'Lorem Ipsum' 
		self.def_olanguage = 'en' 
		self.def_tlanguage = 'es' 
		self.def_user_id = 2 
		self.def_status = 'new' 
		self.def_callback_url= '----UNIQUE----' 

	def tearDown(self):
		pass

	def test_add_user(self):
		self.assertIsNone(db_connection.add_user(self.def_name, self.def_email, self.def_pw_hass))

	def test_add_translation(self):
		result = db_connection.add_translation(self.def_translation_text, 
						self.def_olanguage, 
						self.def_tlanguage, 
						self.def_user_id, 
						self.def_status, 
						self.def_callback_url)
		self.assertIsNone(result)

	def test_delete_translation(self):
		result = db_connection.delete_translation_by_url(self.def_callback_url)
		self.assertIsNone(result)

	def test_delete_user(self):
		self.assertIsNone(db_connection.delete_user(self.def_email))

	if __name__ == '__main__':
		unittest.main()