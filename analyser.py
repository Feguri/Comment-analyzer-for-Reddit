from selenium import webdriver
from sorting import sort_dict
import time


class Analyse:
    def __init__(self, url, alist, wait_time, path):
        self.url = url
        self.path = path
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.get(url)
        time.sleep(wait_time)

        self.user_list = alist

        self.user_dict = {keyword: 0 for keyword in self.user_list}

        self.all_p = self.driver.find_elements_by_tag_name('p')

        self.all_comments = []
        for p in self.all_p:
            try:
                self.all_comments.append(p.text)
            except Exception:
                continue

        self.all_words = []
        for comment in self.all_comments:
            comment_words_list = comment.split()
            for word in comment_words_list:
                self.all_words.append(word.replace(",", ""))

        for word in self.all_words:
            for item in self.user_list:
                if type(item) != str:
                    raise TypeError('Make sure all your list items are strings.')
                if word.lower() == item.lower():
                    self.user_dict[item] += 1

        self.result = sort_dict(self.user_dict)
        self.percentage_dictionary = {}

    def calculate_percentage(self):
        sum_of_all = 0
        for key in self.result:
            sum_of_all += self.result[key]

        for key in self.result:
            try:
                my_result = round((self.result[key] / sum_of_all) * 100, 2)
                self.percentage_dictionary[key] = f'{round(my_result, 2)}%'
            except ZeroDivisionError:
                self.percentage_dictionary[key] = '0%'

    def get_result(self):
        return self.result

    def get_percentage(self):
        return self.percentage_dictionary

    def get_number_of_comments_analysed(self):
        return len(self.all_comments)
