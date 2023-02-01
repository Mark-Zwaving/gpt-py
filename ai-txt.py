# -*- coding: utf-8 -*-
'''Send question to open AI and recieve an answer'''
__author__     =  'Mark Zwaving'
__email__      =  'markzwaving@gmail.com'
__license__    =  'GNU General Public License (GPLv3)'
__copyright__  =  'Copyright (C) Mark Zwaving. All rights reserved.'
__version__    =  '0.0.4'
__status__     =  'Development'

import sources.fn as fn
import sources.txt as txt

try:
    fn.console(txt.intro_api_txt, True)
    while True:
        question = fn.ask_multiline()
        if not fn.oke(question):
            continue

        fn.process_question_txt(question)

        if fn.quit():
            break

except KeyboardInterrupt: # User interrupt quit the program with ctrl+c
    pass

fn.console(f'\n{txt.goodbye}', True)

# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nNew York is the most populous city in the United States and is located in the Northeastern region of the country. It is home to the iconic Statue of Liberty, the Empire State Building, and Times Square. It is also home to many world-renowned museums, galleries, and performing arts venues."
#     }
#   ],
#   "created": 1674507958,
#   "id": "cmpl-6byIowFMC8VuDSLFvKv8Fuod4mtjS",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 63,
#     "prompt_tokens": 6,
#     "total_tokens": 69
#   }
# }



