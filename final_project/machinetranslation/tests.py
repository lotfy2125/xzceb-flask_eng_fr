import unittest
from translator import englishToFrench , frenchToEnglish

class TestEnglish1(unittest.TestCase):  
    """ test for translate english to french """
    def test_englishToFrench(self):
        """ test for translate english to french """
        text_1 = englishToFrench('hello')
        self.assertEqual(text_1, 'Bonjour') # Test for  world 'Hello' and 'Bonjour
class TestEnglish2(unittest.TestCase):  
    """ test for translate english to french """
    def test_englishToFrench(self):
        """ test for translate english to french """
        text_2 = englishToFrench('good evening')
        self.assertEqual(text_2, 'Bonne soirée') # Test for  world 'good evening' and 'Bonne soirée'
class TestEnglish3(unittest.TestCase):
    """ test for translate english to french """
    def test_englishToFrench(self):
        """ test for translate english to french """
        text_3 = englishToFrench('good') 
        self.assertEqual(text_3, 'Bon') # Test for  world 'good' and 'Bon'
class TestEnglish4(unittest.TestCase):
    """ test for translate english to french """
    def test_englishToFrench(self):
        """ test for translate english to french """
        text_4 = englishToFrench('') 
        self.assertEqual(text_4, '')# Test for null input  english To French.
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")    
class TestFrench1(unittest.TestCase):
    """ test for translate french to english """
    def test_frenchToEnglish(self):
        """ test for translate french to english """
        text_1= frenchToEnglish('Bonjour') 
        self.assertEqual(text_1, 'Hello') # Test  world 'Bonjour' and 'hello
class TestFrench2(unittest.TestCase):
    """ test for translate french to english """        
    def test_frenchToEnglish(self):
        """ test for translate french to english """
        text_2 = frenchToEnglish('Bonne soirée')
        self.assertEqual(text_2, 'Good evening') # Test  'Bonne soirée' and 'good evening'
class TestFrench3(unittest.TestCase):
    """ test for translate french to english """
    def test_frenchToEnglish(self):
        """ test for translate french to english """
        text_3 = frenchToEnglish('Bon') 
        self.assertEqual(text_3, 'Good') # Test for  world 'Bon' and 'good'
class TestFrench4(unittest.TestCase):
    """ test for translate french to english """
    def test_frenchToEnglish(self):
        """ test for translate french to english """
        text_4 = frenchToEnglish('') 
        self.assertEqual(text_4, '')# Test for null input  english To French.

unittest.main()
