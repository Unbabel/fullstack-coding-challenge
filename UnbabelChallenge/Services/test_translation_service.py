import unittest
from UnbabelChallenge.Services import translation_service
from UnbabelChallenge.Exceptions import UnExc
class TestTranslationService(unittest.TestCase):
	
	def setUp(self):
		self.def_translation_text = 'Lorem Ipsum' 
		self.def_olanguage = 'en' 
		self.def_tlanguage = 'es' 
		self.def_callback_url= '----UNIQUE----' 

	def tearDown(self):
		pass

	def test_request_translation(self):

		result = translation_service.request_translation(self.def_olanguage, self.def_tlanguage, self.def_translation_text, self.def_callback_url)
		
		self.assertNotEqual(result, UnExc.API_ERROR)

	if __name__ == '__main__':
		unittest.main()