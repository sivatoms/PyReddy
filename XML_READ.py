import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    out = len(node.attrib)
    return out + sum((get_attr_number(child) for child in node))


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
#6
#<feed xml:lang='en'>
#<title>HackerRank</title>
#<subtitle lang='en'>Programming challenges</subtitle>
#<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#<updated>2013-12-25T12:00:00</updated>
#</feed>


# Xml file has tags and their attributes  <> -- This is a tag and <t lang = 'en>  here lang='en is a attribute