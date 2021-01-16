from django.core.exceptions import ValidationError
import re

def validatePenulis(value):
    if re.findall('otong', value):
        raise ValidationError('tolong Si Otong jangan ikut campur')