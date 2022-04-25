from connection import *
import unittest
import HtmlTestRunner


class MyTestSuit(unittest.TestCase):

    def data(self):
        function_name()
    # def setUp(self):
    #     unittest.TestCase.setUp(self)
    #     self.driver = webdriver.Firefox(executable_path="firefox webdriver path")
    #
    # def test_get_title(self):
    #     driver = self.driver
    #     driver.get("website url")
    #     print(driver.title)

    def tearDown(self):
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))


# example: https://docs.python.org/3/library/unittest.html
