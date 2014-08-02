import os, sys
import xml.etree.ElementTree as ElementTree

class XMLAnalyzer:
  def __init__(me, string):
    # parse XML into an ElementTree.
    if string.find('<') == -1: # string = path. 
      me.path = string
      me.tree = ElementTree.parse(me.path)
      me.root = me.tree.getroot()
    else:
      me.raw_text = string
      me.root = ElementTree.fromstring(string)

  """ pattern should be a path of tags.
   e.g. data/country/rank 
  """
  def search(me, pattern, ret_type=str): 
    pattern = pattern.split('/')
    pattern = [x for x in pattern if x != '']
    ret = me.__search__(pattern, me.root)
    return [ret_type(x) for x in ret]

  def __search__(me, pattern_list, node):
    text = list()
    if node.tag != pattern_list[0]:
      return text
    if len(pattern_list) == 1:
      return [node.text]
    else:
      for child in node:
        text = text + me.__search__(pattern_list[1:], child)
      return text

if __name__ == "__main__":
  xml = XMLAnalyzer('../wsj_simple3.xml')
  print xml.search('document/pass/score/')
