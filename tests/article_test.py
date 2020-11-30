import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
         self.new_article = Articles("business-insider","Business Insider","snagarajan@businessinsider.com(Shalini Nagarajan","'Dr.Doom' economist Nouriel Roubini trashes Bitcoin for being heavily manipulated-and blames retail investor FOMO for its recent pump-and-dump","/Retail suckers with massive FOMO have been jumping again into BTC as they did in late 2017 when price went from 10K to 19K,\"he said.","https://www.businessinsider.com/economist-nouriel-roubini-trashes-bitcon-manipulation-retail-investor-fomo-2020-11","https://images2.markets.businessinsider.com/5fc0c25b50e71a0011557995? format=jpeg","2020-11-27T11:02:52Z","REUTERS/Fred Prouser\r\nNouriel Roubini,an economist nicknamed \"Dr Doom\"for his pessimistic predictions, trashed the world's most popular digital currency for being heavily manipulated in a series o...[+2682 chars]")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        


    def test_init(self):
        self.assertEqual(self.new_article.id,("business-insider")
        self.assertEqual(self.new_article.name,("Business Insider")
        self.assertEqual(self.new_article.author,("snagarajan@businessinsider.com(Shalini Nagarajan")
        self.assertEqual(self.new_article.title,("Dr.Doom' economist Nouriel Roubini trashes Bitcoin for being heavily manipulated-and blames retail investor FOMO for its recent pump-and-dump")
        self.assertEqual(self.new_article.description,("/Retail suckers with massive FOMO have been jumping again into BTC as they did in late 2017 when price went from 10K to 19K,\"he said.")
        self.assertEqual(self.new_article.url,("https://www.businessinsider.com/economist-nouriel-roubini-trashes-bitcon-manipulation-retail-investor-fomo-2020-11")
        self.assertEqual(self.new_article.urlToImage,"https://images2.markets.businessinsider.com/5fc0c25b50e71a0011557995? format=jpeg")
        self.assertEqual(self.new_article.publishedAt,"2020-11-27T11:02:52Z")
        self.assertEqual(self.new_article.content,("REUTERS/Fred Prouser\r\nNouriel Roubini,an economist nicknamed \"Dr Doom\"for his pessimistic predictions, trashed the world's most popular digital currency for being heavily manipulated in a series o...[+2682 chars]")




if __name__ == '__main__':
    unittest.main()
