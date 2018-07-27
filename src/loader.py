import codecs
from xml.etree import ElementTree


def iterate(file_path):
    with codecs.open(file_path, 'r', 'utf8') as reader:
        content = None
        for line in reader:
            line = line.strip()
            if line == '<page>':
                content = [line]
            elif line == '</page>':
                content.append(line)
                content = '\n'.join(content)
                tree = ElementTree.fromstring(content)
                content = None
                ns_elem = tree.find('ns')
                if ns_elem is None:
                    continue
                if ns_elem.text.strip() != '0':
                    continue
                title_elem = tree.find('title')
                if title_elem is None:
                    continue
                title = title_elem.text
                text_elem = tree.find('revision/text')
                if text_elem is None:
                    continue
                text = text_elem.text
                if text is None:
                    continue
                yield title, text
            else:
                if type(content) is list:
                    content.append(line)
