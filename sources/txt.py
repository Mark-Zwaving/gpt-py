# -*- coding: utf-8 -*-
'''Functions library'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.5'
__status__     =  'Development'

import shutil 

cli_colls, cli_rows = shutil.get_terminal_size()
line_hash = '#' * (cli_colls - 1) # Decoration line

ask_question = 'Your question is...'
continu = 'Press a key to continue...'
quit = 'Press <ctrl+c> to quit'
go_back_to_menu = 'Press "m" to go back to the main menu'
default = 'Press <enter> for default <%s>'
goodbye = 'Goodbye'
send_ai_linux = 'Send question text to AI on -  Linux  - with <ctrl+d>'
send_ai_windows = 'Send question text to AI on - Windows - with <ctrl+z> followed by <enter>'
send_ai = f'{send_ai_linux}\n{send_ai_windows}'

intro_api = f'''
{line_hash}
## Application connects to Open AI
{line_hash}
'''

intro_api_txt = f'''
{line_hash}
## Application sends text-questions to OpenAI and answers in plain text
{line_hash}
'''

intro_api_img = f'''
{line_hash}
## Application sends text-questions to OpenAI and saves the generated image
{line_hash}
'''

intro_api_yt_txt = f'''
{line_hash}
## Application gets a text summary of a YouTube video using Open AI
{line_hash}
'''

menu = f'''{line_hash}
## MAIN MENU
##   1) Ask a question
##   2) Make an image
##   3) Transcript summary YouTube video
{line_hash}
Choose option: 1, 2 or 3...'''

lst_yes   = ['y', 'yess', 'yes', 'ok', 'oke', 'j', 'yee']
lst_no    = ['n', 'no', 'nee', 'nope', 'nada']
lst_quit  = ['stop', 'q', 'quit', 'done']
lst_sizes = ['256', '512', '1024']
lst_menu  = ['m', 'menu']

ask_summary = '''
    Give a professional and in depth summary 
    in the language %s of no more than %s words 
    of the following text: 
'''

ask_analyse = '''
    Give a professional and in depth analyse 
    in the language %s of no more than %s words 
    of the following text: 
'''

yt_base_url = 'https://www.youtube.com/watch?v='
