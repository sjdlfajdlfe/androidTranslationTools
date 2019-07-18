import os;
import re;
from collections import Counter
import xml.dom.minidom
import codecs
from xml.dom import minidom

# filename根据自己的文件路径替换
if __name__ == '__main__':
    oldxmldoc = xml.dom.minidom.parse('/Users/liuwenji/Desktop/format_strings.xml')
    oldcode = oldxmldoc.getElementsByTagName('string')
    doc = minidom.Document()
    resources = doc.createElement('resources')
    doc.appendChild(resources)    
    for node in oldcode:
        for item in node.childNodes:
            print('写入key= ' , node.getAttribute('name') , ' =value= ' , item.nodeValue)
            text_element = doc.createElement('string')
            text_element.setAttribute('name', node.getAttribute('name'))
            text_element.setAttribute('formatted', 'false')
            replace_string = item.nodeValue.replace('%@','%s')
            replace_string = replace_string.replace("'","\\'")
            replace_string = replace_string.replace("’","\\'")
            #item.nodeValue
            text_element.appendChild(doc.createTextNode(replace_string))
            resources.appendChild(text_element)
    f = codecs.open('new_format_strings.xml', 'w', encoding='utf-8')            
    f.write(doc.toprettyxml(''))      
    # doc.removeChild(resources)
    print ('完成')