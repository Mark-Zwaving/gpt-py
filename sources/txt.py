# -*- coding: utf-8 -*-
'''Functions library'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.4'
__status__     =  'Development'

line_hash = '#' * 80 # Decoration line

ask = 'Your question is...'
continu = 'Press a key to continue...'
quit = 'Press <ctrl+c> to quit'
goodbye = 'Goodbye'
send_ai_linux = 'Send input text to AI on -  Linux  - with <ctrl+d> followed by <enter>'
send_ai_windows = 'Send input text to AI on - Windows - with <ctrl+z> followed by <enter>'
send_ai = f'{send_ai_linux}\n{send_ai_windows}'

intro_api_txt = f'\n{line_hash}\n## Application sends text-questions to OpenAI and answers in plain text\n{line_hash}\n'
intro_api_img = f'\n{line_hash}\n## Application sends text-questions to OpenAI and saves the generated image\n{line_hash}\n'

lst_quit = ['stop', 'q', 'quit']
