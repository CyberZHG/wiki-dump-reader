import re


class Cleaner(object):

    def __init__(self):
        self.text = ''
        self.links = []

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
