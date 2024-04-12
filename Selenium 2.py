#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


# test the browser
import selenium
from time import sleep
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import pandas as pd


# In[24]:


#Question 1
driver = webdriver.Firefox()
driver.get('https://www.totaljobs.com/')
sleep(15)
job_title = driver.find_element(By.ID,"keywords")
job_title.send_keys('Data Scientist')

serach_button = driver.find_element(By.ID,"search-button")
serach_button.click()
sleep(10)

#select location
location = driver.find_element(By.CLASS_NAME,"res-44kvrv")
location.click()
sleep(5)

#select salary
salary = driver.find_element(By.CLASS_NAME,"res-44kvrv")
salary.click()
sleep(5)


# In[25]:


job_title=[]
location=[]


# In[27]:


#Scrapping the job title
title_tags=driver.find_elements(By.XPATH,"/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/article[1]/div[1]/h2/a")
for i in title_tags:
    title=i.text
    job_title.append(title)
    
#Scrapping the location
location_tags=driver.find_elements(By.XPATH,"/html/body/div[4]/div[1]/div/div/div[3]/div/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/div[2]/span")
for i in location_tags:
    location=i.text
    location.append(location)
    


# In[101]:


print(len(job_title),len(location))


# In[102]:


#dataframe
df=pd.DataFrame({'Title':job_title,'Location':location})
df


# In[ ]:





# In[20]:


#Question 2
driver = webdriver.Firefox()
driver.get('https://www.shine.com/')
sleep(30)

serach_button = driver.find_element(By.CLASS_NAME,"iconH-zoom-white")
serach_button.click()
sleep(10)

#select JobTitle
job_title = driver.find_element(By.ID,"id_q")
job_title.send_keys('Data Analyst')

#select location
location = driver.find_element(By.ID,"id_loc")
location.send_keys('Bangalore')

button = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div[1]/form/div/div[2]/div/button")
button.click()


# In[69]:


job_title=[0]
location=[0,15]


# In[70]:


#Scrapping the job title
title_tags=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/strong/a")
for i in title_tags:
    title=i.text
    job_title.append(title)
    
#Scrapping the location
location_tags=driver.find_elements(By.CLASS_NAME,"jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2")
for i in location_tags:
    location=i.text
    location.append(location)


# In[71]:


print(len(job_title),len(location))


# In[72]:


#dataframe
df=pd.DataFrame({'Title':job_title,'Location':location})
df


# In[2]:


#Question 4
driver = webdriver.Firefox()
driver.get('https://www.amazon.co.uk/')
sleep(5)
           
# search for product
product = driver.find_element(By.ID,"twotabsearchtextbox")
product.send_keys('sneakers')

serach_button = driver.find_element(By.ID,"nav-search-submit-button")
serach_button.click()
sleep(5)           


# In[18]:


#Brand,ProductDescription and Price
sneakers_brand=[]
sneakers_desc=[]
#sneakers_price=[]

brands = driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base"]')
for brand in brands:
    sneakers_brand.append(brand.text)

descrp = driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
for desc in descrp:
    sneakers_desc.append(desc.text)
    
# prices = driver.find_elements(By.XPATH,'//span[@class="a-offscreen"]')
#for price in prices:
#sneakers_price.append(price.text)

print(len(sneakers_brand),len(sneakers_desc))


# In[19]:


#dataframe
df=pd.DataFrame({'Brand':sneakers_brand,'Description':sneakers_desc})
df


# In[33]:


#Question 5
driver = webdriver.Firefox()
driver.get('https://www.amazon.co.uk/')
sleep(5)
           
# search for product
product = driver.find_element(By.ID,"twotabsearchtextbox")
product.send_keys('laptop')

serach_button = driver.find_element(By.ID,"nav-search-submit-button")
serach_button.click()
sleep(5)  

cpu_type = driver.find_element(By.ID,"p_n_feature_fifteen_browse-bin-title")
cpu_type.click()
sleep(5)

fliter_cpu_type = driver.find_element(By.LINK_TEXT,"Intel Core i7")
fliter_cpu_type.click()
sleep(5)


# In[38]:


#Brand,ratings and Price
laptop_brand=[]
laptop_ratings=[]
#laptop_price=[]

brands[0:30] = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for brand in brands[0:30]:
    laptop_brand.append(brand.text)

ratings[0:30] = driver.find_elements(By.XPATH,'//span[@class="a-size-base s-underline-text"]')
for rate in ratings[0:30]:
    laptop_ratings.append(rate.text)
    
#prices = driver.find_elements(By.XPATH,'//span[@class="a-price"]')
#for price in prices:
#laptop_price.append(price.text)

print(len(laptop_brand),len(laptop_ratings))


# In[39]:


#dataframe
df=pd.DataFrame({'Brand':laptop_brand,'Ratings':laptop_ratings})
df


# In[2]:


#Question 6
driver = webdriver.Firefox()
driver.get('https://www.azquotes.com/')
sleep(10)

top_quotes = driver.find_element(By.XPATH,'//*[@id="menu"]/div/div[3]/ul/li[5]/a')
top_quotes.click()
sleep(5)


# In[6]:


list_author=[]
list_quotes=[]
type_quotes=[]

authors[0:30] = driver.find_elements(By.XPATH,'//span[@class="author"]')
for author in authors[0:30]:
    list_author.append(author.text)

quotes[0:30] = driver.find_elements(By.XPATH,'//span[@class="title"]')
for quote in quotes[0:30]:
    list_quotes.append(quote.text)

tquotes[0:30] = driver.find_elements(By.XPATH,'//span[@class="tags"]')
for tquote in tquotes[0:30]:
    type_quotes.apend(tquote.text)

print(len(list_author),len(list_quotes),len(type_quotes))


# In[7]:


#Question 7
driver = webdriver.Firefox()
driver.get('https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1')
sleep(5)
# In this website there is no class or id and Xpath keep on change and there no parent path only text
#is given in each field not possiable do the dataframe


# In[15]:


#QUESTION 8
driver = webdriver.Firefox()
driver.get('https://www.motor1.com/')
sleep(8)
           
# search for product
product = driver.find_element(By.ID,"search_input")
product.send_keys('50 most expensive cars')
sleep(2)

serach_button = driver.find_element(By.CLASS_NAME,"m1-search-panel-button m1-search-form-button-animate icon-search-svg")
serach_button.click()
sleep(5)  

cpu_type = driver.find_element(By.XPATH,'//*[@id="page_index_articles_search"]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
cpu_type.click()
sleep(5)
# there is issue with search button not taking any Locators


# In[ ]:


#Question3 - There the website is access deneied in UK 


# In[ ]:




