# -*- coding: utf-8 -*-
'''Work with Open AI - all options'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.2'
__status__     =  'Development'

import sources.fn as fn
import sources.txt as txt
import sources.ask as ask
import sources.option as option

if __name__ == '__main__':
    try:
        fn.console(txt.intro_api, True)
        while True:
            # Get a menu option
            opt = ask.integer(
                t = txt.menu, 
                pre='', 
                post='', 
                default='', 
                lst_allowed=[1,2,3], 
                i_min=1, i_max=3,
                menu=False
            )

            if opt == 1:
                option.ai_txt(menu=True)

            elif opt == 2:
                option.ai_img(menu=True)

            elif opt == 3:
                option.ai_yt_txt(menu=True)

            fn.ln()

    except KeyboardInterrupt: # User interrupt quit the program with ctrl+c
        pass

    fn.console(f'\n\n{txt.goodbye}', True)