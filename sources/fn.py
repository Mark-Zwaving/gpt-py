# -*- coding: utf-8 -*-
'''Functions library'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.6'
__status__     =  'Development'

import config as cfg
import sources.txt as txt
import sys, datetime, subprocess, os, webbrowser, openai
import requests, shutil, re
import pytube, youtube_transcript_api

openai.organization = cfg.organization
openai.api_key = cfg.api_key  # os.getenv("OPENAI_API_KEY")

def console(
        s, # String to print on the screen
        verbose=cfg.verbose  # If set to True it always prints on a screen
    ):
    '''Function shows output string (s) on screen'''
    if verbose: 
        print(str(s))

def ln():
    console(' ', True)

def goto_main_menu(t):
    s = str(t).strip().replace('m^D', 'm').replace('m^Z', 'm').lower().strip()
    return True if s in txt.lst_menu else False

def check_input(t, menu=False):
    t = t.lower().strip()
    if t == txt.empthy:
        return False
    elif menu and goto_main_menu(t):
        return True
    elif len(t) < 2:
        return False

    return True

def cleanup_spaces(t):
    '''Remove unnecessary (double) whitespaces'''
    t = re.sub('\n\n+', '\n', t)
    t = re.sub('\s\s+', ' ',  t)
    t = t.replace('  ', ' ')
    return t

# Unused, maybe implement later
def clean_ai_txt(t):
    res = '' 
    fl_reg = r'[-+]?(?:\d*\.*\d+)'
    fl_lst = r'(\d*\. )'

    # Replace all floats with comma floats
    for el in re.findall(fl_reg, t): # Find all floats
        eln = el.replace('.', ',' )
        t = t.replace(el, eln)
    
    # Replace all lst nums with parenthesis )
    for el in re.findall(fl_lst, t): # Find all floats
        eln = el.replace('. ', ') ' )
        t = t.replace(el, eln) 

    for line in t.strip().split('. '):
        s, cnt = line.strip(), len(line)
        if s.isnumeric():
            s += '. '
        else:
            s += '.\n'
    
        if s.strip() != '.': 
            res += s 

    return res.replace('  ', ' ').strip()

def quit():
    answ = input(f'{txt.continu}\n{txt.quit}\n').lower()
    return True if answ in txt.lst_quit else False

def yyyy_mm_dd():
    return datetime.datetime.now().strftime('%Y-%m-%d') # Get current time

def hh_mm_ss():
    return datetime.datetime.now().strftime("%H-%M-%S")

def file_log():
    return cfg.path_log % yyyy_mm_dd()

def file_img():
    ymd, hms = yyyy_mm_dd(), hh_mm_ss()
    return cfg.path_img % f'{ymd}-{hms}'

def save_log(question, answer):
    os.makedirs(cfg.dir_log, exist_ok=True)  # Make map if not exists
    with open(file_log(), encoding=cfg.charset, mode='a') as f:
        t  = f'{txt.line_hash}\n{question}\n{txt.line_hash}\n'
        t += f'{answer}\n{txt.line_hash}\n\n'
        f.write(t)

def save_img(url): # Save image
    img_online = requests.get(url, stream = True)

    if img_online.status_code == 200:
        os.makedirs(cfg.dir_img, exist_ok=True)
        img_local = file_img()
        with open(img_local,'wb') as f:
            shutil.copyfileobj(img_online.raw, f)
        return img_local
        
    else:
        console(f'Image {url} could not be retrieved', True)
        return 'Error'

def is_int(s):
    try: i = int(s)
    except ValueError: return False  
    return True

def is_float(s):
    try: i = float(s)
    except ValueError: return False  
    return True

def process_question_txt( prompt, temp ):
    ok = True
    try:
        console('\nProcess question...\n', True)
        resp_json = openai.Completion.create(
            model  = cfg.model_txt, 
            prompt = prompt, 
            temperature = temp, 
            max_tokens = cfg.model_txt_max_words
        )
        answer = resp_json['choices'][0]['text'].strip()
        console(f'{txt.line_hash}\n{answer}\n{txt.line_hash}\n', True)

    except Exception as e:
        console(f'Error in process question for text from Open AI\n{e}\n', True)
        ok = False

    else:
        save_log(prompt, answer)

    return ok

def process_question_img( prompt, size ):
    ok, img_loc = True, ''
    try:
        console('\nProcess image...\n', True)
        resp_json = openai.Image.create(
            prompt=prompt,
            n=3, # ?
            size=f'{size}x{size}',
        )
        img_url = resp_json["data"][0]["url"]
        img_loc = save_img(img_url)
        t  = f'{txt.line_hash}\nLocal: {img_loc}\n'
        t += f'Url: {img_url}\n{txt.line_hash}\n'
        console(t, True)

    except Exception as e:
        console(f'Error in process question for image from Open AI\n{e}\n', True)
        ok = False

    else:
        t = f'Local image: {img_loc}\nOnline image: {img_url}'
        save_log(prompt, t)

    return ok, img_loc, img_url

def process_question_transcript( title, description, prompt, lang, max_words ):
    ok, output = True, ''
    try:
        t  = '\nProcess question...\n'
        console(t, True)

        resp_json = openai.Completion.create(
            model  = cfg.model_txt, 
            prompt = prompt, 
            temperature = 0, 
            max_tokens = cfg.model_txt_max_words
        )
        answer = resp_json['choices'][0]['text'].strip()

        output  = f'A summary in {lang} of maximum {max_words} words.\n'
        output += f'Video title: {title}\n'
        output += f'{txt.line_hash}\n'
        output += f'{answer}'
        console(f'{txt.line_hash}\n{output}\n{txt.line_hash}\n', True)

    except Exception as e:
        console(f'Error in process question for transcript from Open AI\n{e}\n', True)
        ok = False

    else:
        save_log(prompt, output)

    return ok

def open_with_app(path):
    '''Function opens a file with an default application'''
    ok, err, t = False, '', ''

    if os.path.exists(path):
        # Linux
        if sys.platform.startswith('linux'):
            try: subprocess.call( ['xdg-open', path] )
            except Exception as e:
                err += f'{e}\n'
                try: os.system(f'start {path}')
                except Exception as e: err += f'{e}\n'
                else: ok = True
            else: ok = True

        # OS X
        elif sys.platform.startswith('darwin'): # ?
            try: os.system( f'open "{path}"' )
            except Exception as e: err += f'{e}\n'
            else: ok = True

        # Windows
        elif sys.platform in ['cygwin', 'win32']:
            # Should work on Windows
            try: os.startfile(path)
            except Exception as e:
                err += f'{e}\n'
                try: os.system( f'start "{path}"' )
                except Exception as e: err += f'{e}\n'
                else: ok = True
            else: ok = True

        # Possible fallback, use the webbrowser
        if not ok:
            try: webbrowser.open_new_tab(path)
            except Exception as e: err += e
            else: ok = True

    else:
        t += 'File not found\n'

    t += f'Open {path} successful\n' if ok else \
         f'Error open {path}\n{err}\n'

    return ok, t

def yt_meta_info(id):
    ok, title, description = False, '', ''
    try: # Get meta info movie parameters
        url = f'{txt.yt_base_url}{id}'
        yt = pytube.YouTube(url)
    
    except Exception as e:
        console(f'Error in YouTube stream\n{url}\n{e}\n', True)

    else:
        # Print media info
        title = cleanup_spaces(yt.title)
        description = cleanup_spaces(yt.description)
        ok = True

    return ok, title, description

def yt_transcript(id):
    ok, trs_time, trs_txt = False, '', ''
    try:
        url      = f'{txt.yt_base_url}{id}'
        dict_trs = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(id)
        trs_txt  = '. '.join([d['text'] for d in dict_trs])

    except Exception as e:
        console(f'Error in YouTube Transscript\n{url}\n{e}\n', True)

    else:
        ok = True

    return ok, trs_time, trs_txt[:cfg.model_max_tokens]

# [
#     {
#         'text': 'Hey there',
#         'start': 7.58,
#         'duration': 6.13
#     },
#     {
#         'text': 'how are you',
#         'start': 14.08,
#         'duration': 7.58
#     },
#     # ...
# ]