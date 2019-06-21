#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):

    def test_true(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)


        name = browser.find_element_by_css_selector('.first[required=""]')
        name.send_keys('fhxm')
        surname = browser.find_element_by_css_selector('.second[required=""]')
        surname.send_keys('ghmc')
        mail = browser.find_element_by_css_selector('.third[required=""]')
        mail.send_keys('test@gmail.com')


        button = browser.find_element_by_css_selector("button.btn")
        button.click()


        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Should have successfull message")


    def test_false(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)


        name = browser.find_element_by_css_selector('.first[required=""]')
        name.send_keys('fdnza')
        surname = browser.find_element_by_css_selector('.second[required=""]')
        surname.send_keys('zdfnmn')
        mail = browser.find_element_by_css_selector('.third[required=""]')
        mail.send_keys('test@gmail.com')


        button = browser.find_element_by_css_selector("button.btn")
        button.click()


        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Should have successfull message")


if __name__ == "__main__":
    unittest.main()

