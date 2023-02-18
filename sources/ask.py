# -*- coding: utf-8 -*-
'''Functions for asking questions'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.3'
__status__     =  'Development'

import config as cfg
import sources.txt as txt
import sources.lang as lang
import sources.fn as fn
import sys

def q( 
        t='', pre='', post='', 
        default='', menu=False
    ):
    tt = ''
    if pre: 
        tt += f'{pre}\n'

    tt += f'{t}\n'


    if default: 
        tt += f'{txt.default % default}\n'

    if post: 
        tt += f'{post}\n'

    if menu:
        tt += f'{txt.go_back_to_menu}\n'

    tt += f'{txt.quit}\n'
    tt += ' ? '

    answ = input(tt).strip()
    fn.ln()

    return answ

def multiline(menu=False):
    ask_inp  = f'{txt.send_ai}\n'
    if menu: 
        ask_inp += f'{txt.go_back_to_menu}\n'
    ask_inp += f'{txt.quit}\n'
    ask_inp += f'{txt.ask_question}\n'
    ask_inp += ' ? '

    while True:
        fn.console(ask_inp, True)
        lst = sys.stdin.readlines()
        answ = " ".join(lst).strip().replace('  ', ' ')

        if menu and fn.goto_main_menu(answ):
            return txt.lst_menu[0]

        if fn.check_input(answ, menu): # Check response
            return answ 
        else:
            fn.console(f'Question empthy or too short...\n', True)

def integer(
        t, pre='', post='', 
        default='', lst_allowed=[], 
        i_min=-sys.maxsize-1, i_max=sys.maxsize,
        menu=False 
    ):

    while True:
        answ = q(t, pre, post, default, menu)
        if not answ:
            return default
        elif menu and fn.goto_main_menu(answ):
            return txt.lst_menu[0]
        elif fn.is_int(answ):
            i = int(answ)
            if i >= i_min and i <= i_max:
                if lst_allowed:
                    if i in lst_allowed or answ in lst_allowed:
                        return i
                    else:
                        allow = ", ".join(lst_allowed)
                        fn.console(f'Answer {i} must be of one of the following values {allow}\n', True)
                else:
                    return i
            else:
                fn.console(f'Integer value must be between {i_min} and {i_max}\n', True)
        else:
            fn.console(f'Answer {answ} is not an integer\n', True)


def double(
        t, pre='', post='', 
        default='', lst_allowed=[], 
        fl_min=sys.float_info.min, fl_max=sys.float_info.max, 
        menu=False
    ):

    while True:
        answ = q(t, pre, post, default, menu)
        if not answ:
            return default
        elif menu and fn.goto_main_menu(answ):
            return txt.lst_menu[0]
        elif fn.is_float(answ):
            fl = float(answ)
            if fl >= fl_min and fl <= fl_max:
                if lst_allowed:
                    if fl in lst_allowed or answ in lst_allowed:
                        return fl
                    else:
                        allow = ", ".join(lst_allowed)
                        fn.console(f'Answer {fl} must be of one of the following values {allow}\n', True)
                else:
                    return fl
            else:
                fn.console(f'Float value must be between {fl_min} and {fl_max}\n', True)
        else:
            fn.console(f'Answer {answ} is not a float\n', True)

def language(menu=False):
    while True:
        answ = q(
            t       = 'Give a language to answer in', 
            post    = 'See file - sources/lang.py - for the language codes or languages', 
            default = cfg.yt_summary_lang,
            menu    = menu
        )

        if not answ:
            return cfg.yt_summary_lang
        elif menu and fn.goto_main_menu(answ):
            answ = txt.lst_menu[0]
        elif lang.is_available(answ):
            break
        else:
            fn.console(f'Language - {answ} - not found\n', True)

    return answ

def max_words(menu=False):
    answ = integer( 
        t       = 'Set the maximum amount of words for the summary', 
        default = cfg.answ_words_words, 
        i_min   = cfg.answ_words_min,
        i_max   = cfg.answ_words_max,
        menu    = menu
    )

    if not answ:
        answ = cfg.answ_words
    elif menu and fn.goto_main_menu(answ):
        answ = txt.lst_menu[0]

    return answ

def yt_url(menu=False):
    while True:
        id, url = '', ''
        answ = q(
            t    = 'Give an url or an id of a YouTube video', 
            menu = menu
        )

        if not answ:
            fn.console(f'Url or id cannot be empthy\n', True)
            continue
        elif menu and fn.goto_main_menu(answ):
            id = txt.lst_menu[0]
        elif 'https://' in answ: 
            id, url = answ.split('=')[-1], answ 
        else:
            id, url = answ, f'{txt.yt_base_url}{answ}'

        break

    return id, url

def open_image_with_app(menu=False):
    return q(
        t    = f'Do you want to open the local image with the default app ?', 
        post = 'Press "y" for yess', 
        menu = menu
    ).lower()
