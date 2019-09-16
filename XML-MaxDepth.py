import xml.etree.ElementTree as etree

# here  getroot() returns root element for this tree
# here this code will find the number of nested roots in the give xml file

maxdepth = 0
def depth(elem, level):
    global maxdepth
    print("Start of Maxdepth and Level :", maxdepth, level)

    if (level == maxdepth):
        print("if level : ", level)
        maxdepth += 1
    for child in elem:
        print("for child : ", child)
        depth(child, level + 1)   # here the first time <feed> tag is root element and and second time <updated> tag becomes root element it has one child means levle = 1 of it plus <feed> has one level 1 so total = 2 nested levles

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


#input
#8
#<feed xml:lang='en'>
#    <title>HackerRank</title>
#    <subtitle lang='en'>Programming challenges</subtitle>
#    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
#    <updated>
#        <time>2013-12-25T12:00:00 </time>
#    </updated>
#</feed>