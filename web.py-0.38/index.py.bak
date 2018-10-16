#encoding utf-8
import sys,os,web,os.path,urllib,urllib2,commands,time,json,hashlib


#define const name 
gpio_arr=["12","16","18","20","21","23","24","25"]
lightid_arr = ["keting","canting","chufang","yangtai","zhuwo","ciwo","xishouchi","cesuo"]
apiurl_arr = ["http://api.yeelink.net/v1.1/device/15910/sensor/397625/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398151/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398152/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398153/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398154/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398155/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398156/datapoints", \
"http://api.yeelink.net/v1.1/device/15910/sensor/398157/datapoints"]
apiheaders = {'U-ApiKey': 'fe3b6ea89db31d9fd53dc259cdd04c0d'}

reload(sys)
sys.setdefaultencoding("utf-8")

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/t', 't',
    '/light', 'light',
    '/setlight', 'setlight',
    '/checklight', 'checklight',
    '/irremote', 'irremote',
    '/keting','keting',
    '/zhuwo','zhuwo',
    '/ciwo','ciwo',
    '/switch', 'switch',
    '/login','login',
    '/xxyl','xxyl',
    '/kill','kill',
    '/demo','demo',
    '/xbmclive','xbmclive',
    '/voice','voice',
    '/modify_pwd','modify_pwd',
    '/s','dawning_ds',
    '/project_input','project_input',
    '/dawning_ds_dynamic','dawning_ds_dynamic',
    '/dawning_ds_tips','dawning_ds_tips'
)

class index:
    def GET(self):
	err = web.input()
	return render.index(err)

class t:
    def GET(self):
	return render.t()

class dawning_ds:
    def GET(self):
	return render.dawning_ds()

class dawning_ds_dynamic:
    def GET(self):
	return render.dawning_ds_dynamic()

class dawning_ds_tips:
    def GET(self):
	return render.dawning_ds_tips()

class irremote:
    def GET(self):
	return render.irremote()

class keting:
    def GET(self):
	return render.keting()

class zhuwo:
    def GET(self):
	return render.zhuwo()

class ciwo:
    def GET(self):
	return render.ciwo()

class light:
    def GET(self):
	data=web.input()
	light_stats=[]
	light_stats_0_1=''
	count = 0
	while ( count < len(gpio_arr)):
        	on_off=int(commands.getstatusoutput('gpio -g read '+gpio_arr[count])[1])
		light_stats_0_1 = light_stats_0_1 + str(on_off)
		if on_off :
			light_stats.append("on")
		else:
			light_stats.append("off")
			count = count + 1
			print lightid_arr,light_stats
		if len(data) ==0 :
			return render.light(lightid_arr[0:4],light_stats[0:4],lightid_arr[4:],light_stats[4:])
		else: 
			# transfer light_status to esp8266 wifi module
			ip = web.ctx.ip
			if (ip =='192.168.88.190'): 
				# request from ESP8266-12F 
				print "request From ESP8266-12F"	
			elif (ip =='192.168.88.186'):
				# request from ESP8266-12F-1 
				print "request From ESP8266-12F-1 "	
			else:
				print "not this ip"
			return render.light_status(light_stats_0_1)

class setlight:
    def GET(self):
        data = web.input()
        if len(data) == 0 :
        	raise web.seeother('/light')
        else:
        	on_off=data.stats
        	lightid=data.lightid
        if (lightid in lightid_arr):
        	apiurl=apiurl_arr[lightid_arr.index(lightid)]
        # 
        if on_off == '1' :
        		values={"value":1}
        		on_off="on"
        else:
        		values={"value":0}
        		on_off="off"
        jdata=json.dumps(values)
        req = urllib2.Request(apiurl,jdata,apiheaders)
        response = urllib2.urlopen(req)
        print response.read()
        response.close()
        return on_off 

class checklight:
    def GET(self):
	return getstatus()

def getstatus():
	status_arr = []
	count = 0 
	v = '{'
	while ( count < len(lightid_arr)):
		on_off=int(commands.getstatusoutput('gpio -g read '+gpio_arr[count])[1])
		if on_off :
			status_arr.append("on")
		else:
			status_arr.append("off")
		v = v +'"'+ lightid_arr[count]+'":"' + status_arr[count]+'",'
		count = count + 1 
	v = v[0:-1]+'}'
	print v 
	return json.dumps(v)

class switch:
    def GET(self):
	return render.switch()

class voice:
    def GET(self):
	return render.voice()
    def POST(self):
	data = web.input()
	txt = data.txt
	if len(txt) == 0 :
		raise web.seeother('/voice')
	else:				
		txt="".join(txt.split());
		speech_path = "/mnt/disks/backup/speech/ifly/Linux_voice_1.109/samples/tts_sample"
		shell = "/bin/echo "+txt+" > "+speech_path+"/speech.txt && cd "+speech_path+"; sh 32bit_make.sh"
		os.system(shell)
		return render.voice()

class login:
    def GET(self):
        raise web.seeother('/')
    def POST(self):
	data = web.input()
	username,password = data.username,data.password
        db = web.database(dbn='mysql', user='rock64', pw='iQQ', db='ha_ds')
	myvar = dict(username=username)
	re = db.select('webuser',myvar,where="username=$username")
        if re[0]['password']==hashlib.md5(password).hexdigest():
		rootdir="/mnt/disks/backup/mms_radio"
		lst=sorted(os.listdir(rootdir))
		#return render.ls(username,lst,rootdir)
		return render.all(username,lst,rootdir)
	else:
		raise web.seeother('/?err=pwderr') 
	
class project_input:
    def GET(self):
	return render.project_input()
    def POST(self):
        d = web.input()
        customer,pname,dt,city,count_sum,ds_sum,config,win_manu,partner,zbgs,isJoin,ps=d.customer,\
                d.pname,d.dt,d.city,d.count_sum,d.ds_sum,d.config,d.win_manu,d.partner,d.zbgs,d.isJoin,d.ps
        print customer,pname,dt,city,count_sum,ds_sum,config,win_manu,partner,zbgs,isJoin,ps
        db = web.database(dbn='mysql', user='rock64', pw='iQQ', db='ha_ds')
        db.insert('project',customer=customer,pname=pname,dt=dt,city=city,count_sum=count_sum,ds_sum=ds_sum,
                config=config,win_manu=win_manu,partner=partner,zbgs=zbgs,isJoin=isJoin,ps=ps)
        info='project'
        stats='success'
        return render.stats(info,stats)

class modify_pwd:
    def GET(self):
        username = web.input().username
        return render.modify_pwd(username)
    def POST(self):
	data = web.input()
	username,password = data.username,data.password
        print username,password
	modify_password(username,password)
	return web.seeother('/')

class xxyl:
    def get(self):
	data = web.input()
	rootdir="/mnt/disks/backup/mms_radio"
	if len(data)>0:
		## play it if >0 and is file 
		rootdir=data.rootdir
		if os.path.isfile(rootdir):
			os.system('/usr/bin/mplayer -ao alsa `cat '+rootdir+' ` &')
			return render.kill(rootdir)
		else:
			lst=sorted(os.listdir(rootdir))
			return render.ls("",lst,rootdir)
			
	else:
		raise web.seeother('/xxyl?rootdir='+rootdir)
		
class kill:
    def GET(self):
	data = web.input()
	if "mplayer"==data.pid:
		os.system('sudo killall -9 mplayer ; sudo killall -9 mplayer ;')
		rootdir=os.path.dirname(data.fpath)
                web.seeother('/xxyl?rootdir='+rootdir)

class xbmclive:
    def GET(self):
        return web.seeother('/static/liveSource.xml')

class demo:
    def GET(self):
        return render.all()

def modify_password(user, pwd):
    password=hashlib.md5(pwd).hexdigest()
    db = web.database(dbn='mysql', user='rock64', pw='iQQ', db='ha_ds')
    db.update('webuser',vars={'user':user},where="username=$user",password=password)
    return 0

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
