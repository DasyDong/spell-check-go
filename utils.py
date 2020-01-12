# coding: utf-8
import re

def camel2underscore(camelized_str):
    """
    Convert AbcDefGo value to abc_def_go, is used for split Camel-Case word
    """
    first_cap_re = re.compile('(.)([A-Z][a-z]+)')
    all_cap_re = re.compile('([a-z0-9])([A-Z])')

    sub1 = first_cap_re.sub(r'\1_\2', camelized_str)
    return all_cap_re.sub(r'\1_\2', sub1).lower()

def find_word(content):
    pat = '[a-zA-Z]+'
    words_english = re.findall(pat, content.decode('utf-8'))
    return words_english