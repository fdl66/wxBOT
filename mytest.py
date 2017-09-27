#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *
import re


keyword=u"@得良"
def record_into_database(url):
    print url+"**has into database"

urlregex = re.compile(
    r'(^(?:http|ftp)s?://)?' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 3 or msg['msg_type_id'] == 4:
            if msg['content']['type'] == 0 :
                if keyword in msg['content']['data']:
                    urlmatch=urlregex.match(msg['content']['data'].split()[-1])
                    if urlmatch:
                        record_into_database(urlmatch.group())
                        self.send_msg_by_uid(urlmatch.group()+u'已经加入工单', msg['user']['id'])
                    else :
                        print "nomatchurl"
                else :
                    print "nomatchmsg"

            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
