import unittest
from fastapi.testclient import TestClient
from main import app


class TestAPI(unittest.TestCase):
        def setUp(self):
            self.client = TestClient(app)  # Create an instance of the test client.

        def test_root(self):
            """ Check the endpoint /. """
            response = self.client.get("/", )  # GET request to an endpoint
        
            self.assertEqual(response.status_code, 200)  # Check the expected status code
            self.assertIn("Hello World", response.json()["message"])  # Check the expected JSON response

        def test_solution_created(self):
            """ Check the endpoint /solution for the "completed" criterion. """
            data = {
                "orders": [
                    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
                    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                    {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
                ],
                "criterion": "completed"
            }
            response = self.client.post("/solution", json=data)  # POST request to an endpoint
            
            self.assertEqual(response.status_code, 200)  # Check the expected status code
            self.assertEqual("1299.69", response.json()) # Check the expected JSON response

        def test_solution_error(self):
            """ Check that endpoint /solution validate the input parameters. """
            data = {
                "orders": [
                    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
                    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
                    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
                    {"id": 4, "item": "Mouse", "quantity": 4, "price": -24.99, "status": "canceled"}
                ],
                "criterion": "completed"
            }
            response = self.client.post("/solution", json=data)  # POST request to an endpoint
            
            self.assertEqual(response.status_code, 422)  # Check the expected status code
            self.assertEqual(-24.99, response.json()["detail"][0]["input"]) # Check the expected JSON response
            self.assertEqual("Input should be greater than 0", response.json()["detail"][0]["msg"]) # Check the expected JSON response
        

if __name__ == '__main__':
    unittest.main()