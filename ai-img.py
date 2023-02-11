# -*- coding: utf-8 -*-
'''Send question to open AI and recieve a generated image'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.4'
__status__     =  'Development'

import sources.fn as fn
import sources.txt as txt

try:
    fn.console(txt.intro_api_img, True)
    while True:
        fn.ask_img_size()
        print(' ')

        ok, question = fn.ask_multiline()
        if not ok:
            continue

        ok, img = fn.process_question_img(question)

        if ok:
            if fn.ask_open_image_with_app(img) in txt.lst_yes:
                ok, t = fn.open_with_app(img)
                if not ok: fn.console(t, True)
            print(' ')

        if fn.quit():
            break

except KeyboardInterrupt: # User interrupt quit the program with ctrl+c
    pass

fn.console(f'\n\n{txt.goodbye}', True)
