# -*- coding: utf-8 -*-
'''Options for AI'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.6'
__status__     =  'Development'

import config as cfg
import sources.fn as fn
import sources.txt as txt
import sources.ask as ask
import config as cfg

def ai_txt(menu=False):
    answ = ask.double(
        t       = 'Set the randomness (=temperature) for calculated output',
        post    = f'Set a value between {cfg.model_txt_temp_min} and {cfg.model_txt_temp_max}',
        default = cfg.model_txt_temp, 
        fl_min  = cfg.model_txt_temp_min, 
        fl_max  = cfg.model_txt_temp_max, 
        menu    = menu 
    )
    if menu and fn.goto_main_menu(answ):
        return txt.lst_menu[0]

    question = ask.multiline(menu)
    if menu and fn.goto_main_menu(question):
        return txt.lst_menu[0]

    ok = fn.process_question_txt(question, answ)

def ai_img(menu=False):
    size = ask.integer( 
        t       = 'Set the size (width and height are the same) of the image in px', 
        post    = f'Allowed values are: {", ".join(txt.lst_sizes)}', 
        default = cfg.model_img_size, 
        lst_allowed = txt.lst_sizes,
        i_min   = int(txt.lst_sizes[ 0]),
        i_max   = int(txt.lst_sizes[-1]),
        menu    = menu
    )
    if menu and fn.goto_main_menu(size):
        return txt.lst_menu[0]

    question = ask.multiline(menu)
    if menu and fn.goto_main_menu(question):
        return txt.lst_menu[0]

    ok, img, _ = fn.process_question_img(question, size)
    if ok and ask.open_image_with_app(menu) in txt.lst_yes:
        ok, t = fn.open_with_app(img)
        if not ok: 
            fn.console(t, True)

def ai_yt_trs(menu=False):
    id, url = ask.yt_url(menu)
    if menu and fn.goto_main_menu(id):
        return txt.lst_menu[0]

    lang = ask.language(menu)
    if menu and fn.goto_main_menu(lang):
        return txt.lst_menu[0]

    words = ask.max_words(menu)
    if menu and fn.goto_main_menu(words):
        return txt.lst_menu[0]

    # TODO 
    # Make own question
    # Not only summary 
    # But analyses too

    ok_inf, title, description = fn.yt_meta_info(id)
    ok_trs, trs_time, trs_txt = fn.yt_transcript(id)

    if ok_inf and ok_trs:
        t  = txt.ask_summary % (str(words), lang)
        t += f'Title: {title[:80]}'
        # t += f'Description: {description[:80]}'
        fn.console(t, True)

        prompt = f'{txt.ask_summary % (lang, words)}{trs_txt}'
        ok = fn.process_question_transcript( title, description, prompt, lang, words )

