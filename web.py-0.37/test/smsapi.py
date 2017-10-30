import sys, urllib, urllib2, json

tel="15639267512"
url = 'http://apis.baidu.com/txct/txct/tianxiachangtong?mobile='+tel+'&content=%E6%82%A8%E7%9A%84%E9%AA%8C%E8%AF%81%E7%A0%81%E6%98%AF1232333%E3%80%82%E8%AF%B7%E6%82%A8%E5%9C%A83%E5%88%86%E9%92%9F%E4%B9%8B%E5%86%85%E5%AE%8C%E6%88%90%E9%AA%8C%E8%AF%81%EF%BC%8C%E5%A6%82%E9%9D%9E%E6%9C%AC%E4%BA%BA%E6%93%8D%E4%BD%9C%EF%BC%8C%E8%AF%B7%E5%BF%BD%E7%95%A5%E6%9C%AC%E4%BF%A1%E6%81%AF%E3%80%82%E3%80%90%E4%BF%A1%E5%A4%A9%E4%B8%8B%E3%80%91'

req = urllib2.Request(url)
apikey="cbf671b7a18213b824e8e4774acb0982"
req.add_header("apikey",apikey)
resp = urllib2.urlopen(req)

content = resp.read()

if(content):
	print(content)
