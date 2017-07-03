#_*_ coding:utf-8 _*_
import urllib2
import urllib
import cookielib

url = 'http://blog.kamidox.com'
def urlopen():
    try:
        s = urllib2.urlopen(url,timeout=3)
    except urllib2.HTTPError ,e:
        print e
    else:
        print s.read(111)
        s.close()

def request():
    headers = {'UserAgent':'Mozilla/5.0','x-my-header':'myvalue'}
    req = urllib2.Request(url,headers = headers)
    s = urllib2.urlopen(req)
    print s.read(111)
    print s.headers.items()

def request_post_debug():
    data = {'username':'hongcy','password':'q1q1q1'}
    headers = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request('http://www.douban.com',data=urllib.urlencode(data),headers=headers)
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    s = opener.open(req)
    print s.read(111)

def handle_cookie():
    cookiejar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
    opener = urllib2.build_opener(handler,urllib2.HTTPHandler(debuglevel= 1))
    s = opener.open('http://www.douban.com')
    print s.read(111)

if __name__ == '__main__':
    handle_cookie()
