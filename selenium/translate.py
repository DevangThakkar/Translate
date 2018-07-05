#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import sys
import time

class element_has_lang(object):
	"""An expectation for checking that an element has a particular css class.

	locator - used to find the element
	returns the WebElement once it has the particular css class
	"""
	def __init__(self, locator, lang):
		self.locator = locator
		self.lang = lang

	def __call__(self, driver):
		element = driver.find_element(*self.locator)   # Finding the referenced element
		if self.lang in element.get_attribute("class"):
			return element
		else:
			return False


def open_browser():
	browserHTML = webdriver.Chrome("/mnt/e/Translate/chromedriver.exe")
	return browserHTML

def get_translate(browserHTML, lang, word):
	
	browserHTML.get("https://translate.google.co.in/#" + lang + "/" + word)

	# Wait until an element with id='myNewInput' has class 'myCSSClass'
	# wait = WebDriverWait(browserHTML, 10)
	# element = wait.until(element_has_lang((By.ID, "result_box"), lang.split("/")[1]))

	result = browserHTML.find_element_by_css_selector("#result_box>span")
	# print(result.text)
	print(browserHTML($0))

translated = []
lang = sys.argv[1]
lang_file = lang.replace("/", "")
browserHTML = open_browser()
with open("translate_sans_num.csv", "r") as f:
	i = 0
	for line in f:
		if i > 10:
			sys.exit(1)
		i += 1
		line = line.strip()
		# print(line)
		translated.append(get_translate(browserHTML, lang, line))
		time.sleep(0.5)

with open("translated_" + lang_file + ".csv", "w") as f:
	for word in translated:
		f.write(word + "\n")