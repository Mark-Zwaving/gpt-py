# -*- coding: utf-8 -*-
'''Functions library'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.5'
__status__     =  'Development'

import config as cfg
import sources.txt as txt
import sys, datetime, subprocess, os, webbrowser, openai
import requests, shutil

openai.organization = cfg.organization
openai.api_key = cfg.api_key  # os.getenv("OPENAI_API_KEY")

def console(
        s, # String to print on the screen
        verbose=cfg.verbose  # If set to True it always prints on a screen
    ):
    '''Function shows output string (s) on screen'''
    s = str(s)
    if verbose: 
        print(s)

def oke(resp):
    if not resp:
        return False
    elif len(resp) < 2:
        return False

    return True

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

def ask_multiline():
    console(f'{txt.send_ai}\n{txt.quit}\n{txt.ask}\n ? ', True)
    lst = sys.stdin.readlines()
    t = " ".join(lst).strip()

    return t

def is_int(s):
    try: i = int(s)
    except ValueError:
        return False  
    return True

def is_float(s):
    try: i = float(s)
    except ValueError:
        return False  
    return True

def ask( t='', pre='', post='', default='' ):
    tt = ''
    if pre: 
        tt += f'{pre}\n'

    tt += f'{t}\n'

    if default: 
        tt += f'{txt.default % default}\n'

    if post: 
        tt += f'{post}\n'

    tt += f'{txt.quit}\n'
    tt += ' ? '

    answ = input(tt).strip()
    return answ

def ask_int(t, pre='', post='', default='', lst_allowed=[], i_min=-sys.maxsize-1, i_max=sys.maxsize):
    while True:
        answ = ask(t, pre, post, default)
        if not answ:
            return default
        elif is_int(answ):
            i = int(answ)
            if i >= i_min and i <= i_max:
                if lst_allowed:
                    if i in lst_allowed or answ in lst_allowed:
                        return i
                    else:
                        allow = ", ".join(lst_allowed)
                        console(f'Answer {i} must be of one of the following values {allow}', True)
                else:
                    return i
            else:
                console(f'Integer value must be between {i_min} and {i_max}', True)
        else:
            console(f'Answer {answ} is not an integer', True)

        print(' ')

def ask_float(t, pre='', post='', default='', lst_allowed=[], fl_min=sys.float_info.min, fl_max=sys.float_info.max):
    while True:
        answ = ask(t, pre, post, default)
        if not answ:
            return default
        elif is_float(answ):
            fl = float(answ)
            if fl >= fl_min and fl <= fl_max:
                if lst_allowed:
                    if fl in lst_allowed or answ in lst_allowed:
                        return fl
                    else:
                        allow = ", ".join(lst_allowed)
                        console(f'Answer {fl} must be of one of the following values {allow}', True)
                else:
                    return fl
            else:
                console(f'Float value must be between {fl_min} and {fl_max}', True)
        else:
            console(f'Answer {answ} is not an float', True)

        print(' ')

def ask_img_size():
    cfg.model_img_size = ask_int( 
        'Set the size (width and height are the same) of the image in px', 
        pre = '', 
        post = f'Allowed values are: {", ".join(txt.lst_sizes)}', 
        default = cfg.model_img_size, 
        lst_allowed = txt.lst_sizes,
        i_min = int(txt.lst_sizes[ 0]),
        i_max = int(txt.lst_sizes[-1])
    )

def ask_model_temp():
    temp, fl_min, fl_max = cfg.model_txt_temp, cfg.model_txt_temp_min, cfg.model_txt_temp_max
    cfg.model_txt_temperature = ask_float(
        'Set the randomness (=temperature) for calculated output',
        pre = '',
        post = f'Set a value between {fl_min} and {fl_max}',
        default = temp,
        fl_min = fl_min,
        fl_max = fl_max
    )

def process_question_txt( prompt ):
    console('\nProcess question...\n', True)

    resp_json = openai.Completion.create(
        model  = cfg.model_txt, 
        prompt = prompt, 
        temperature = cfg.model_txt_temperature, 
        max_tokens = cfg.model_txt_max_words
    )

    answer = resp_json['choices'][0]['text'].strip().replace('. ', '.\n') # euhm ok
    console(f'{txt.line_hash}\n{answer}\n{txt.line_hash}\n', True)
    save_log(prompt, answer)

def process_question_img( prompt ):
    console('\nProcess image...\n', True)

    resp_json = openai.Image.create(
        prompt=prompt,
        n=3, # ?
        size=f'{cfg.model_img_size}x{cfg.model_img_size}',
    )

    img_url = resp_json["data"][0]["url"]
    img_loc = save_img(img_url)
    console(f'{txt.line_hash}\nLocal image saved at:\n{img_loc}\n{txt.line_hash}\n', True)
    save_log(prompt, f'Local image: {img_loc}\nOnline image: {img_url}')

def open_with_app(path): # Not implemented (yet)
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

    t += 'Open file successful' if ok else f'Error open file\n{err}'
    console(t)

    return ok