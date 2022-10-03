

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:50:32 2022

@author: jasoncui and hanannah wang and jiasheng zhouuuuuu and sophc
"""
import requests
import validators
from bs4 import BeautifulSoup
def get_food():
  URL = input("What is the link to your school's events calendar?")
  page = requests.get(URL)
  
  soup = BeautifulSoup(page.content, "html.parser")
  
  a = soup.find_all("a")
  
  food = ["food", "lunch", "brunch", "dinner", "boba", "snack", "dessert", "pasta", "pizza", "donut", "froyo", "yogurt", "cream", "meal", "aquarium", "Italian", "feast", "drink", "bbq", "chicken", "chocolate", "chip", "cake", "dumpling", "sushi", "burger", "bread", "shake", "waffle", "banquet"]
  links = []
  for link in a:
      links.append(link.get('href'))
  
  for y in range(100):
      if "calendar" in links[y] and "event" in links[y]:
          #print(links[y])
          if validators.url(links[y]) == True:
              linkPage = requests.get(links[y])
              soupy = BeautifulSoup(linkPage.content, "html.parser")
              body_text = soupy.find_all("p")
              html_text = str(body_text)
              words_lower = html_text.lower()
              words = words_lower.split(' ')
              for x in food:
                  for j in words:
                      if j == x:
                          print(links[y])
                          break
                      else:
                          pass
          
                  
  
      else:
        pass


get_food()
        
    
    
