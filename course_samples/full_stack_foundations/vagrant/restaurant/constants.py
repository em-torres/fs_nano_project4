import os


class Paths:
    ACTUAL_PATH = os.getcwd()
    TEMPLATES_PATH = "%s/templates" % ACTUAL_PATH

    TEMPLATE_RESTAURANT = "%s/restaurants.html" % TEMPLATES_PATH


# print(Paths.TEMPLATE_RESTAURANT)
