import unittest
from appium import webdriver


class calculator_test(unittest.TestCase):
    calcsession = None
    calresult = None

    def setUp(self):
        print("setup")
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.calcsession = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=desired_caps
        )

    def tearDown(self):
        print("teardown")
        self.calcsession.quit()

    def test_add(self):
        print("add")

    def test_subtraction(self):
        print("subtraction")

    def test_division(self):
        print("division")

    def test_multiplication(self):
        print("multiplication")
