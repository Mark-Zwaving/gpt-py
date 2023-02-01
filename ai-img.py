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
        question = fn.ask_multiline()
        if not fn.oke(question):
            continue

        fn.process_question_img(question)

        if fn.quit():
            break

except KeyboardInterrupt: # User interrupt quit the program with ctrl+c
    pass

fn.console(f'\n{txt.goodbye}', True)
