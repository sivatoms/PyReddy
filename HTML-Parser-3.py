
from html.parser import *

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #if len(attrs)<1:
        print(tag)
        for attr in attrs:
            print(r'-->', attr[0],'>',attr[1])
    #def handle_endtag(self, tag):
        #print("End  :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(r'-->', attr[0],'>',attr[1])

    def handle_decl(self, data):
        pass
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())