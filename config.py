# -*- coding: utf-8 -*-
'''File with the configurations options'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.4'
__status__     =  'Development'

import os

# Note: usage of the openai api is not free
organization = '<your organization key>' # Your organization key
api_key = '<your api key>' # Your Api key

# https://platform.openai.com/docs/models/overview
# For example: gpt-3.5-turbo, gpt-3.5-turbo-0301, text-davinci-003, 
# text-davinci-002, code-davinci-002
model_txt = 'gpt-3.5-turbo' # Which text model to use
model_txt_max_words = 1024 # How many (maximum) words to return
# The temperature controls the randomness in the output -> 0 - 1.0 
# 0 = no randomness, higher is more arbitrare, ie 0.7-0.9 
model_txt_temp     = 0.0
model_txt_temp_min = 0.0
model_txt_temp_max = 1.0

# model_img = '' # Which image model to use
model_img_size = 256 # Image size (width and height) options are 256, 512, 1024
model_img_ext = 'png' # Extension of image

# Maximum input of words for the AI model
model_max_tokens = 4097 

log_file = 'log-%s.txt' # Filename for the log
img_file = f'img-%s.{model_img_ext}' # Filename for the output image

dir_root = os.path.dirname(os.path.abspath(__file__)) # App dir
dir_log  = os.path.join(dir_root, 'log') # Log dir
path_log = os.path.join(dir_log, log_file) # Path log file
dir_img  = os.path.join(dir_root, 'img') # Image dir
path_img = os.path.join(dir_img, img_file) # Path image file

charset = 'utf-8' # Charset for log file
verbose = False # More verbose

# Minimum length of questions 
min_question_len = 2 

# Answer language for a YouTube video
# See file sources/lang.py for the available languages
answ_lang      = 'English' # Set language summary
answ_words     = 300 # Summary of X words
answ_words_min =  50 # Minimum of X words
answ_words_max = 600 # Maximum of X words
