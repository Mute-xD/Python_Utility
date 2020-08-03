import unittest


def getFormattedName(first_name, last_name, mid_name=None):
    if mid_name is not None:
        return (first_name + ' ' + mid_name + ' ' + last_name).title()
    else:
        return (first_name + ' ' + last_name).title()


class NameTestCase(unittest.TestCase):
    def testFirstLastName(self):
        formatted_name = getFormattedName('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def testFirstMidLastName(self):
        formatted_name = getFormattedName('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
