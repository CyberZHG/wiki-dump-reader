import re


class Cleaner(object):

    def __init__(self):
        pass

    def clean_text(self, text):
        text = self._remove_file_links(text)
        text = self._remove_image_links(text)
        text = self._remove_refs(text)
        text = self._remove_emphasises(text)
        text = self._remove_comments(text)
        text = self._remove_langs(text)
        return text

    def _remove_file_links(self, text):
        """Remove links like `[[File:*]]`"""
        return self._remove_resource_links(text, 'File')

    def _remove_image_links(self, text):
        """Remove links like `[[File:*]]`"""
        return self._remove_resource_links(text, 'Image')

    def _remove_resource_links(self, text, resource):
        """Remove links likes `[[*:*]]`"""
        pattern = '[[' + resource + ':'
        pattern_begin = text.find(pattern)
        if pattern_begin == -1:
            return text
        begin, removed = 0, ''
        while begin < len(text):
            if pattern_begin > begin:
                removed += text[begin:pattern_begin]
            pattern_end, depth = pattern_begin + 2, 2
            while pattern_end < len(text):
                ch = text[pattern_end]
                pattern_end += 1
                if ch == '[':
                    depth += 1
                elif ch == ']':
                    depth -= 1
                    if depth == 0:
                        break
            if depth == 0:
                begin = pattern_end
            else:
                removed += text[begin]
                begin += 1
            pattern_begin = text.find(pattern, begin)
            if pattern_begin == -1:
                break
        if len(text) > begin:
            removed += text[begin:]
        return removed

    def _remove_refs(self, text):
        """Remove patterns like <ref*>*</ref>"""
        text = re.sub(r'<ref.*?</ref>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'<ref.*?/>', '', text, flags=re.IGNORECASE)
        return text

    def _remove_emphasises(self, text):
        """Remove patterns like '''*'''"""
        text = re.sub(r"'''(.*?)'''", r'\1', text)
        text = re.sub(r"''(.*?)''", r'\1', text)
        return text

    def _remove_comments(self, text):
        """Remove patterns like <!--*-->"""
        return re.sub(r'<!--.*?-->', '', text)

    def _remove_langs(self, text):
        """Remove pattenrs like {{lang-*|*}}}"""
        return re.sub(r'{{lang(-|\|).*?\|(.*?)}}', r'\2', text, flags=re.IGNORECASE)

    def build_links(self, text):
        begin, removed, links = 0, '', []
        while begin < len(text):
            pattern_begin = text.find('[[', begin)
            if pattern_begin == -1:
                if begin == 0:
                    removed = text
                else:
                    removed += text[begin:]
                break
            if pattern_begin > begin:
                removed += text[begin:pattern_begin]
            pattern_end, depth = pattern_begin + 2, 2
            while pattern_end < len(text):
                ch = text[pattern_end]
                pattern_end += 1
                if ch == '[':
                    depth += 1
                elif ch == ']':
                    depth -= 1
                    if depth == 0:
                        link = text[pattern_begin + 2:pattern_end - 2]
                        parts = link.split('|')
                        if len(parts) == 1:
                            if ':' in link:
                                pure = link.split(':')[-1]
                                links.append({
                                    'begin': len(removed),
                                    'end': len(removed) + len(pure),
                                    'link': link,
                                    'text': pure
                                })
                                removed += pure
                            else:
                                links.append({
                                    'begin': len(removed),
                                    'end': len(removed) + len(text),
                                    'link': link,
                                    'text': link
                                })
                                removed += link
                        elif len(parts) == 2:
                            links.append({
                                'begin': len(removed),
                                'end': len(removed) + len(parts[1]),
                                'link': parts[0],
                                'text': parts[1]
                            })
                            removed += parts[1]
                        break
            begin = pattern_end
        return removed, links
