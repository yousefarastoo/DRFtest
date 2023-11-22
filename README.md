
DRFtest
https://www.caktusgroup.com/blog/2018/02/26/basics-django-rest-framework/
Django logo and REST API logo

Introduction
DRFtest is a Django REST framework (DRF) project that provides a simple way to create and manage APIs. The library includes utilities for testing DRF views, serializers, and viewsets. It also provides a simple Django project that demonstrates how to use the library.

Features
Simple and easy-to-use library for creating and testing DRF APIs
Provides a number of useful features, such as the ability to create mock objects and assert that views and serializers are called correctly
Well-documented and easy to understand
Installation
To install DRFtest, you can use the following command:

Bash
pip install drftest
Use code with caution. Learn more
Usage
To use DRFtest, you will first need to create a Django project and install the DRFtest library. Once you have done that, you can use the library to create and test your DRF APIs.

Here is an example of how to test a DRF view:

Python
from drftest import api_test, TestClient

@api_test
class MyViewTest(TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_get_view(self):
        response = self.client.get('/my-view/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello, world!'})
Use code with caution. Learn more
This code will create a test case for the MyView view. The test case will first create a test client, which is a mock object that can be used to make requests to the view. The test case will then make a GET request to the view and assert that the response status code is 200 and that the response data is a dictionary with a key of message and a value of Hello, world!.

Examples
The DRFtest library includes a simple Django project that demonstrates how to use the library. You can find the project in the examples/ directory of the repository.

Documentation
For more information on how to use DRFtest, please refer to the documentation at https://github.com/readthedocs/readthedocs.org/blob/main/pytest.ini.

Contributing
DRFtest is an open-source project and we welcome contributions from the community. If you are interested in contributing, please read the contributing guidelines at https://gist.github.com/MarcDiethelm/7303312.

License
DRFtest is licensed under the MIT License.
