#!/usr/bin/env python
import re
#s=re.sub("http://(.*)\.jrj\.com\.cn","https://\g<1>.jrj.com.cn",a)
s='''document.write('<script charset="utf-8" src="http://js.jrjimg.cn/common/foot/globalPopup-min.js"><\/script>');document.write('<script charset="utf-8" src="http://js.jrjimg.cn/common/foot/sidebar-min.js"><\/script>');document.write('<script charset="utf-8" src="http://js.jrjimg.cn/common/foot/copyright-min.js"><\/script>');document.write("<!--WebTCode Start-->");document.write('<script charset="utf-8" src="http://js.jrj.com.cn/common/foot/jrj_dcs_tag-min.js"><\/script>');document.write("<!--WebTCode End-->");'''
s1=re.sub("http://([^\.]*)\.jrj\.com\.cn","https://\g<1>.jrj.com.cn",s,0)
print(s1)
print("-"*100)
s2=re.sub("http://([^\.]*)\.jrjimg\.cn","https://\g<1>.jrjimg.cn",s1,0)
#print(s)


print(s2)

