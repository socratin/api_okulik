class PayloadNormal:
    payload = {'info': {'colors': ['blue', 'white'], 'objects': ['picture', 'text']}, 'tags': ['mosquito', 'spray'],
               'text': 'Loll', 'updated_by': 'new_1_name', 'url': 'ftp://example2134.com'}


class PayloadError:
    payload = {'info': {'colors': ['blue', 'white'], 'objects': ['picture', 'text']}, 'tags': ['mosquito', 'spray'],
               'text': None, 'updated_by': 'new_1_name', 'url': 'ftp://example2134.com'}
