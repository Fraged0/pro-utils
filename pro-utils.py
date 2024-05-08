import time as t
import requests


class Utils:

    def delayed_run(self, time='1s', toRun=str()):
        """
        Runs command with delay of selected like this: time='2m'

        :param time:
        :param toRun:
        :return:
        """
        if self.extract_unit(string=time) == 's':
            t.sleep(int(time[:-1]))
            toRun()
        elif self.extract_unit(string=time) == 'm':
            sec = int(time[:-1]) * 60
            t.sleep(sec)
            toRun()

        elif self.extract_unit(string=time) == 'h':
            sec = int(time[:-1]) * 3600
            t.sleep(sec)
            toRun()

    def extract_unit(self, string):
        """
        Gets first non-alpha character from string

        :param string:
        :return:
        """
        for char in string:
            if char.isalpha():
                return char

    def get_html(self, url=str()):
        """
        Gets HTML code from url

        :param url:
        :return:
        """
        req = requests.get(url)
        html = req.text
        return html
