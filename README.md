# Application gpt-py  
---
**GPT-PY** is a **CLI** _(=Commandline Interface)_ application.  
  
It will output the text answers in the console and logs the answers in the - log - directory.
When creating images the images will be saved in the - img - directory.  

The software will connect to **_Open AI GPT3_** with **_Python3_**.  
  
>This software can:  
>1. Give AI answers on text questions  
>2. Create AI images  
>3. Make AI summaries of YouTube transcripts  
  
  
**License**: <a href="https://github.com/Mark-Zwaving/gpt-py/blob/main/LICENSE" target="_blank">GNU General Public License v3.0</a>  

**Software**: For this software to work, you need to install _Python3_ with the _Python3 dependencies_ and you need to get an _API KEY_ and an _organizational ID_ from the website _openai.com_  

**Trial**: after a trial - _of spending maximum $18,- or after three months_ - the usage of the _Open AI API_ is not free anymore  

---

### Install Python version >= 3.7
<a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>  

### Install dependencies 
#### In the directory of gpt-py run the following command
```python -m pip install -r requirements.txt```  

### AI Account, ID and KEY  
For this software you need to get an API KEY and an organizational ID from the website openai.com  

#### On the website Open AI create an account 
<a href="https://openai.com" target="_blank">https://openai.com</a>  

#### Login on Open AI and get or create an API KEY
Login -> personal -> <a href="https://platform.openai.com/account/api-keys" target="_blank">https://platform.openai.com/account/api-keys</a>  

#### Get your organization ID from the settings
<a href="https://platform.openai.com/account/org-settings" target="_blank">https://platform.openai.com/account/org-settings</a>  

#### Fill in your Organization ID and AI KEY in config.py
In the map of gpt-py in the config.py fill your organization ID and API KEY*   

### Run python apps
Three Python Apps are available  
>1. Get AI text questions  
>2. Create AI images  
>3. AI Summary of YouTube transcripts  

#### AI Apps
All available AI options in one.  
```python ai.py```  

#### AI for text answers
Get AI answers on text questions  
```python ai-txt.py```  

#### AI for creating images
Create AI images  
```python ai-img.py```  

#### AI Youtube transcript 
AI summary of a YouTube transcript  
```python ai-yt-trs.py```  

### Output Examples
Output result will be logged in the log directory  
Created images will be saved in the img directory  
>_See log/log-test.txt_  
>_See img/_  

### Configuration options  
>_See config.py_  
  