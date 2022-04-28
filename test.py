from my_hash_cash_app import app
import unittest
import json

class FlaskTest(unittest.TestCase):
    
    #check /find response for 200 status code with valid inputs provided
    def test_find_status_code_valid_inputs(self):
        tester = app.test_client()
        response = tester.get("/find?challenge=iBeat&zero_bits=16")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)    
    
    #check /verify response for 200 status code with valid inputs provided
    def test_verify_status_code_valid_inputs(self):
        tester = app.test_client()
        response = tester.get("/verify?challenge=iBeat&zero_bits=16&proof=62073")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check /find response for 400 status code with no inputs provided
    def test_find_status_code_no_inputs(self):
        tester = app.test_client()
        response = tester.get("/find")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    #check /find response for 400 status code with non-integer zero_bits value
    def test_find_status_code_non_integer(self):
        tester = app.test_client()
        response = tester.get("/find?challenge=iBeat&zero_bits=notanint")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)    
    
    #check /verify response for 400 status code with no inputs provided
    def test_verify_status_code_no_inputs(self):
        tester = app.test_client()
        response = tester.get("/verify")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
        
    #check /find response returns the correct proof
    def test_find_response_true(self):
        tester = app.test_client()
        response = tester.get("/find?challenge=iBeat&zero_bits=16")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['proof'], 62073)

    #check /verify response is True with correct proof as input
    def test_verify_response_true(self):
        tester = app.test_client()
        response = tester.get("/verify?challenge=iBeat&zero_bits=16&proof=62073")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], True)

    #check /verify response is False with incorrect proof as input
    def test_verify_response_false(self):
        tester = app.test_client()
        response = tester.get("/verify?challenge=iBeat&zero_bits=16&proof=12345")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['result'], False)
        
if __name__ == "__main__":
    unittest.main()
    