#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    root = ET.Element('book')
    article = ET.SubElement(root, 'article')
    article.attrib['title'] = "卒業論文"
    novel = ET.SubElement(root, 'novel')

    chapters = []
    names = ["はじめに", "基礎理論", "実験方法", "結果と考察", "まとめ", "参考文献"]
    pages = [2, 8, 6, 2, 1, 2]
    for i in range(6):
        chapter = ET.SubElement(article, 'chapter')
        chapter.attrib['id'] = str(i+1)
        chapter.attrib['name'] = names[i]
        chapter.attrib['pages'] = str(pages[i])
        chapters.append(chapter)

    chapters = []
    names = ["1日のはじまり", "朝食", "仕事", "帰宅後", "新しい朝"]
    pages = [2, 8, 6, 2, 1]
    for i in range(5):
        chapter = ET.SubElement(novel, 'chapter')
        chapter.attrib['id'] = str(i+1)
        chapter.attrib['name'] = names[i]
        chapter.attrib['pages'] = str(pages[i])
        chapters.append(chapter)

    with open('lecture02_02_data.xml', 'wb') as f:
        import xml.dom.minidom as md
        f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))

if __name__ == '__main__':
    lecture02_02()