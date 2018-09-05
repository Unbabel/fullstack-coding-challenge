from com.translator.app.core import TranslationsService
import unittest
import time

class TranslationServiceTestSuite (unittest.TestCase):

    def test_submitRequest(self):
        # initializations
        testToTranslate = "Hello World!"
        insertSuccessful = False

        # Call the Translation Service
        TranslationsService.submitRequest(testToTranslate)

        # Assess successful request insertion
        requests = TranslationsService.queryRequests()
        for id, trans_id, src_lang, trg_lang, txt, trans_result, state in requests:
            if txt == testToTranslate:
                insertSuccessful = True

        self.assertTrue(insertSuccessful == True)

        # I'll assume testing on a dev database
        # otherwise:
        # Delete test data on successfull request insertion/submission

    def test_queryRequests(self):

        # Just assess data properly fetched from the DB
        requestData = TranslationsService.queryRequests()
        self.assertIsNotNone(requestData)


    def test_submitRequestPerformance(self):

        start_time = time.time()
        self.test_submitRequest(self)
        end_time = time.time()

        ## assess elapsed time
        self.assertTrue((end_time - start_time) < 1.0)


    def test_queryRequestsPerformance(self):

        list = [1,2,3,4,5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for element in list:
            # Call the Translation Service
            TranslationsService.submitRequest(element)

        start_time = time.time()
        result = TranslationsService.queryRequests()
        end_time = time.time()

        ## assess elapsed time
        self.assertIsNotNone(result);
        self.assertTrue((end_time - start_time) < 1.0)

        # I'll assume testing on a dev database
        # otherwise:
        # Delete test data on successfull request insertion/submission