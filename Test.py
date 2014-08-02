import unittest
from XMLAnalyzer import *

class TestXMLAnalyzer(unittest.TestCase):
  def test_search(self):  
    xml = """<?xml version="1.0"?>
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <type>Class M</type>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <type>Class E</type>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>"""
    xml_analyzer = XMLAnalyzer(xml)
    self.assertEqual(xml_analyzer.search("data/country/rank", ret_type=int), [1, 4, 68])
    self.assertEqual(xml_analyzer.search("data/country/year", ret_type=int), [2008, 2011, 2011])
    self.assertEqual(xml_analyzer.search("data/country/type"), ["Class M", "Class E"])
      
if __name__ == "__main__":
  unittest.main()
