"""
Account API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from tests.factories import AccountFactory
from service import talisman
from service import config
from service.routes import app

# DATABASE_URI = os.getenv(
#    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
#)

######################################################################
#  T E S T   C A S E S
######################################################################
class TestConfig(TestCase):
    """Config Tests"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False

    @classmethod
    def tearDownClass(cls):
        """Runs once before test suite"""

    def setUp(self):
        """Runs before each test"""

        self.client = app.test_client()

    def tearDown(self):
        """Runs once after each test case"""

    ######################################################################
    #  CONFIG  T E S T   C A S E S
    ######################################################################

    def test_env_variables(self):
        """It should all evironment variable to be set"""
        self.assertTrue(config.DATABASE_USER)
        self.assertTrue(config.DATABASE_PASSWORD)
        self.assertTrue(config.DATABASE_NAME) 
        self.assertTrue(config.DATABASE_HOST)
        self.assertTrue(config.DATABASE_URI)
