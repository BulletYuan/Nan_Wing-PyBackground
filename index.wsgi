# -*- coding: UTF-8 -*-

import sae,sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib,urllib2,cookielib
import HTMLParser,json
#from multiprocessing.pool import Pool
import threading,time
from greenlet import greenlet

import getSearchResult as gsr
import publicParams as P
import reHTMLTags as rH

def app(environ, start_response):
    key=environ['QUERY_STRING']
    if key.count("&"):
        key=key.split("&")[0]
    if key:
        P.key=urllib.unquote(key)
        
        for surl in P.searchURLarr:
            t = threading.Thread(target=getURL,args=(surl,key))
            t.start()
            #g=greenlet(getURL)
            #g.switch(surl,key)
            #getURL(surl,key)
        
        jsarr=json.loads(json.dumps(P.list_data, indent=2))
        jsarr.sort(key = lambda x:x["weight"],reverse=True)
        response_body=json.dumps(jsarr, indent=2)
        #response_body=json.dumps(P.list_time, indent=2)
    else:
    	response_body=[]
    
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*')
        #('Content-Type', 'text/plain')
    ]
    
    start_response(status, response_headers)
    
    return response_body

application = sae.create_wsgi_app(app)

def getURL(surl,key):
	u=surl
	u+=key
	mu=u.split('/')[0]+'/'+u.split('/')[1]+'/'+u.split('/')[2]
	#P.list_time.append("1"+str(time.ctime()))
	h=gethtml(u)
	#P.list_time.append("2"+str(time.ctime()))
	#pool_getlinks=getlinks(h,mu)
	#getlinks(h,mu)
	#with Pool(8) as p:
	#	p.map_async(pool_getlinks,RAW_DATASET,1)
	#t = threading.Thread(target=getlinks,args=(h,mu))
	#t.start()
	g=greenlet(getlinks)
	g.switch(h,mu)
	#P.list_time.append("3"+str(time.ctime()))

def getlinks(html_code,addr):
    hp = gsr.getSearchResult(addr)
    hp.feed(html_code)
    hp.close()


def gethtml(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    req = urllib2.Request(url)
    try:
    	content = opener.open(req).read() #获取页面内容
    except urllib2.URLError,e:
        pass
    return content
