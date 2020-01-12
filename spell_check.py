# coding: utf-8
"""
The spell check is checking word spelling correct in project
"""
import sys
import os
import enchant

from utils import camel2underscore, find_word


WORD_CHECK = {}
WORD_IGNORE = []


def check_file(ent, file_path):
    with open(file_path, 'rb') as f_p:
        for line in f_p:
            words_line = line.strip()
            if words_line:
                check_words_each_line(ent, words_line)

def check_words_each_line(ent, words_line):
    """

    :param ent:
    :param words_line:
    :return:
    """
    words_english = find_word(words_line)
    for word in words_english:
        if word_is_need_check(word):
            # Convert AbcDefGo value to abc_def_go, is used for split Camel-Case word
            # Split GetClientOutOfClusterOrDie to [get client out of cluster or die]
            word_split = camel2underscore(word).split('_')
            for w_d_p in word_split:
                if w_d_p and word_is_need_check(w_d_p):
                    WORD_CHECK[word] = 1 if check_word_typo(ent, w_d_p) else 0

def word_is_need_check(w_d):
    """Skip check if False"""
    return w_d.lower() not in [w_c.lower() for w_c in (list(WORD_CHECK.keys()) + WORD_IGNORE)]

def check_word_typo(ent, word):
    """
    spell check word
    """
    return not ent.check(word)

def walk_file(pathname):
    """
    :param pathname:
    :return:Wal all files in path
    """
    all_files = []
    for root, _, files in os.walk(pathname):
        for f_s in files:
            all_files.append(os.path.join(root, f_s))
    return all_files

def check_spell(ent, full_pathname):
    """
    check all spell word in path_name
    """
    if os.path.isfile(full_pathname):
        check_file(ent, full_pathname)
    elif os.path.isdir(full_pathname):
        all_files = walk_file(full_pathname)
        for f_i in all_files:
            check_file(ent, f_i)

def write_word_to_file(words):
    """
    Write words to file
    """
    with open('spell_check_wrong.txt', 'w+') as s_p:
        for word in words:
            s_p.writelines(word)
            s_p.writelines('\n')

def set_word_ignore():
    """Skip check word in ignore file"""
    with open('spell_check_ignore.txt', 'r+') as s_p:
        global WORD_IGNORE
        WORD_IGNORE = [str(w_i.replace('\n', '')).lower() for w_i in s_p.readlines()]

def main():
    """main start"""
    path_name = sys.argv[1]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_pathname = current_dir + '/' + path_name

    if not os.path.exists(full_pathname):
        print('The path {} is invalid'.format(full_pathname))
        return

    ent = enchant.Dict("en_US")
    set_word_ignore()
    check_spell(ent, full_pathname)

    write_word_to_file([k for k, v in WORD_CHECK.items() if v == 1])

main()
