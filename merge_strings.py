import os;
import re;
from collections import Counter
import xml.dom.minidom
import codecs
from xml.dom import minidom
 
def clear_null_bytes(string):
    return string.replace('\0', '')

#read file key
def read_file(file_path):
    xmldoc = xml.dom.minidom.parse(file_path)
    code = xmldoc.getElementsByTagName('string')
    array = []
    for node in code:
        for item in node.childNodes:
        # sheet.write(row, 0, node.getAttribute('name'))
        # sheet.write(row, 1, item.nodeValue)
            array.append(clear_null_bytes(node.getAttribute('name')).lower())
    return dict(Counter(array))
 
module_path = '/Users/liuwenji/Desktop'
filename = module_path + '/strings.xml'
oldFileName = module_path + '/old_strings.xml'

# merge old and new strings file
if __name__ == '__main__':
    dic = read_file(filename)
    oldxmldoc = xml.dom.minidom.parse(oldFileName)
    oldcode = oldxmldoc.getElementsByTagName('string')
    doc = minidom.Document()
    resources = doc.createElement('resources')
    doc.appendChild(resources)
    new_array = [] 
    for key in dic:
        if dic[key] > 1:
            print(key,' : ',dic[key])
            new_array.append(key)
    
    for node in oldcode:
        for item in node.childNodes:
            if node.getAttribute('name') in new_array:
                print('重复key')
            else:
                print('写入key= ' , node.getAttribute('name') , ' =value= ' , item.nodeValue)
                text_element = doc.createElement('string')
                text_element.setAttribute('name', node.getAttribute('name'))
                text_element.setAttribute('formatted', 'false')
                text_element.appendChild(doc.createTextNode(item.nodeValue))
                resources.appendChild(text_element)
    f = codecs.open('new_strings.xml', 'w', encoding='utf-8')            
    f.write(doc.toprettyxml(''))      
    # doc.removeChild(resources)
    print ('完成')