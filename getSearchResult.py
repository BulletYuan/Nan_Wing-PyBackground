# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import re
import urllib,urllib2,cookielib
import threading,time

import publicParams as P
import reHTMLTags as rH

class getSearchResult(HTMLParser):
    def __init__(self,addr):
        HTMLParser.__init__(self)
        self.data={}
        self.lstr=None
        self.a_text = None
        self.addr=addr

    def handle_starttag(self, tag, attr):
        if tag == "a":
            if len(attr) == 0:
                pass
            else:
                for (variable, value) in attr:
                    self.a_text = True
                    if variable == "href":
                        self.lstr=value

    def handle_endtag(self, tag):
        if tag == 'a':
            self.a_text = None

    def handle_data(self, data):
        #P.list_time.append("1.1"+str(time.ctime()))
        if self.a_text:
            re_s =re.search( P.key, data, re.M|re.I|re.U)
            if re_s:
                ts=self.lstr.split('/')[0]
                if len(ts) > 0 :
                    self.lstr=self.lstr
                else :
                    self.lstr=self.addr+self.lstr
                    
                #P.list_time.append("1.2"+str(time.ctime()))
                if P.list_links.count(self.lstr)==0:
                    P.list_links.append(self.lstr)
                    P.list_titles.append(data)
                    #P.list_time.append("1.3"+str(time.ctime()))
                    
                    h=getChtml(self.lstr)
                    #P.list_time.append("1.4"+str(time.ctime()))
                    if h:
                    	h=rH.getString(h)
                        sc=rH.getCount(h,P.key)
                        if sc == 0:
                            pass
                        else:
                            self.data['weight']=sc
                            self.data['title']=data.encode('utf-8')
                            self.data['link']=self.lstr.encode('utf-8')
                            P.list_data.append(self.data)
                    else:
                        pass
                    
                    #t = threading.Thread(target=self.thr)
                    #t.start()
                    #P.list_time.append("1.5"+str(time.ctime()))
                
                self.data={}


def getChtml(url):
    content=None
    req=urllib2.Request(url)
    if req:
        res=urllib2.urlopen(req)
        content=res.read()
    else:
        pass
    return content
