from pytest_factoryboy import register

pytest_plugins = "tests.fixtures"

from tests.factories import *

register(CategoryFactory)
register(UserFactory)
register(AdFactory)