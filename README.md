# Application gpt-py  
---
Access Open AI GPT3 with Python3 for texts, creating images and a summary of Youtube transcripts  
  
Note: after a trial - *of maximum $18,- and/or after three months* - the usage of the openai api is not free anymore  

---

### Install Python version >= 3.7
<a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>  

### Install dependencies 
#### In the directory of gpt-py run the following command
```python -m pip install -r requirements.txt```  

### AI Account and KEY
#### On the website Open AI create an account 
<a href="https://openai.com" target="_blank">https://openai.com</a>  

#### Login on Open AI and get or create an api key
Login -> personal -> <a href="https://platform.openai.com/account/api-keys" target="_blank">https://platform.openai.com/account/api-keys</a>  

#### Get your organization ID from the settings
<a href="https://platform.openai.com/account/org-settings" target="_blank">https://platform.openai.com/account/org-settings</a>  

#### Fill in your Organization ID and Api Key in config.py
*In the map of gpt-py in the config.py fill your organization ID and API KEY*   

### Run python apps
*Three Python Apps are available*  
*1. AI text questions*  
*2. AI image*  
*3. YouTube transcripts (summary)*  

#### AI Apps
*All AI options*  
```python ai.py```  

#### AI for text answers
*AI answers on questions*  
```python ai-txt.py```  

#### AI for creating images
*AI images on questions*  
```python ai-img.py```  

#### AI Youtube transcript 
*AI images answers on questions*  
```python ai-yt-trs.py```  

### Output Examples
See log/log-test.txt  
See img/  

### Configuration options
See config.py  

