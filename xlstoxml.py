from xml.dom import minidom
from xlrd import open_workbook
import codecs

# 打开excel
workbook = open_workbook('strings.xls')

# 新建xml
doc = minidom.Document()

def load():
    print ('start...')
    # 添加字符串
    for sheet in workbook.sheets():
        for col in range(1,sheet.ncols):
            # 添加根元素
            resources = doc.createElement('resources')
            doc.appendChild(resources)
            for row_index in range(1,sheet.nrows):
                result_placeholder = sheet.cell(row_index, 0).value
                result_content = sheet.cell(row_index, col).value
                # 新建一个文本元素
                text_element = doc.createElement('string')
                text_element.setAttribute('name', result_placeholder)
                text_element.appendChild(doc.createTextNode(formatString(result_content)))
                resources.appendChild(text_element)
            result_content = sheet.cell(0, col).value
            f = codecs.open(result_content+'_new_strings.xml', 'w', encoding='utf-8')
            f.write(doc.toprettyxml(indent='    '))
            doc.removeChild(resources)
            print ('完成')

def formatString(result_content):
    if "%@" in result_content:
        result_content = result_content.replace('%@','%s')
        print ('替换%@: ' + result_content)

    if "'" in result_content:
        result_content = result_content.replace("'","\\'")
        print ('替换单引号: ' + result_content)
    
    return result_content
    
load()