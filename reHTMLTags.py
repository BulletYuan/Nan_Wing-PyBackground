# -*- coding: UTF-8 -*-

import re

def getString(html):
    new=re.compile('\s+').sub('',html)
    new=re.compile('<\s*script[^>]*>.*?\<\s*/\s*script\s*>',re.S|re.M).sub('',new)
    new=re.compile('<\s*style[^>]*>.*?\<\s*/\s*style\s*>',re.S|re.M).sub('',new)
    new = re.compile(r'<[^>]+>',re.S|re.M).sub('',new)
    new=re.compile('\s+').sub('',new)
    return new

def getCount(hstr,k):
    rli=re.findall(k.upper(),hstr.upper())
    return len(rli)
    

'''    
def getString(htmlstr):
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I|re.M)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I|re.M)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('',htmlstr)#去掉换行
    s=re_cdata.sub('',s)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    s=blank_line.sub('',s)
    s=replaceCharEntity(s)#替换实体
    return s

def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}
   
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)
    
'''