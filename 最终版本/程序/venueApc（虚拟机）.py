from tkinter import *
import tkinter,os,logging
from tkinter import ttk
import tkinter.messagebox

#继承Frame类
class Venue(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        #设定变量
        self.obj = tkinter.StringVar()   #项目变量
        self.Object = ttk.Combobox(win, textvariable=self.obj)
        self.Object["value"] = (
            "APN", "ARC", "ATH", "BDM", "BKB", "BOX", "CRD", "DIV",
            "EQU", "FBL", "FEN", "GAR", "GEN", "GLF", "JUD", "LSA",
            "MIP", "MPN", "NPN", "OPW", "ORI", "PAR", "SAL", "SHO",
            "SWM", "TEN", "TKW", "TRI", "TTE", "VBV", "VVO", "WRE"
        )
        self.dict = {
            'APN':{'cl':'10.150.61.19',
                    'cm':'10.150.61.25'},
            'ARC':{'cl':'10.150.61.19',
                    'cm':'10.150.61.30'},
            'BDM': {'cl': '10.150.61.21',
                    'cm': '10.150.61.30'},
            'BKB': {'cl': '10.150.61.21',
                    'cm': '10.150.61.30'},
            'BOX': {'cl': '10.150.61.19',
                    'cm': '10.150.61.25'},
            'CRD': {'cl': '10.150.61.19',
                    'cm': '10.150.61.25'},
            'DIV': {'cl': '10.150.61.20',
                    'cm': '10.150.61.26'},
            'EQU': {'cl': '10.150.61.21',
                    'cm': '10.150.61.27'},
            'FBL': {'cl': '10.150.61.22',
                    'cm': '10.150.61.28'},
            'FEN': {'cl': '10.150.61.22',
                    'cm': '10.150.61.28'},
            'GLF': {'cl': '10.150.61.22',
                    'cm': '10.150.61.29'},
            'GAR': {'cl': '10.150.61.22',
                    'cm': '10.150.61.29'},
            'JUD': {'cl': '10.150.61.22',
                    'cm': '10.150.61.29'},
            'LSA': {'cl': '10.150.61.22',
                    'cm': '10.150.61.29'},
            'MIP': {'cl': '10.150.61.20',
                    'cm': '10.150.61.26'},
            'MPN': {'cl': '10.150.61.21',
                    'cm': '10.150.61.27'},
            'NPN': {'cl': '10.150.61.22',
                    'cm': '10.150.61.28'},
            'OPW': {'cl': '10.150.61.19',
                    'cm': '10.150.61.25'},
            'ORI': {'cl': '10.150.61.19',
                    'cm': '10.150.61.25'},
            'PAR': {'cl': '10.150.61.19',
                    'cm': '10.150.61.30'},
            'SAL': {'cl': '10.150.61.19',
                    'cm': '10.150.61.30'},
            'SHO': {'cl': '10.150.61.21',
                    'cm': '10.150.61.27'},
            'SWM': {'cl': '10.150.61.20',
                    'cm': '10.150.61.26'},
            'TEN': {'cl': '10.150.61.20',
                    'cm': '10.150.61.26'},
            'ATH': {'cl': '10.150.61.20',
                    'cm': '10.150.61.28'},
            'TKW': {'cl': '10.150.61.20',
                    'cm': '10.150.61.28'},
            'TRI': {'cl': '10.150.61.21',
                    'cm': '10.150.61.27'},
            'TTE': {'cl': '10.150.61.22',
                    'cm': '10.150.61.29'},
            'VBV': {'cl': '10.150.61.20',
                    'cm': '10.150.61.26'},
            'VVO': {'cl': '10.150.61.21',
                    'cm': '10.150.61.26'},
            'WRE': {'cl': '10.150.61.21',
                    'cm': '10.150.61.27'},
            'GEN': {'cl': '10.150.61.20',
                    'cm': '10.150.61.26'},
        }
        self.createFrame()

    def createFrame(self):
        tkinter.Label(win, text='第7届世界军人运动会场馆服务器', font=("楷体", 20), bg="#0A66CC").pack(anchor=CENTER)
        tkinter.Label(win, text='选择竞赛项目:', font=("Arial", 12), bg="#0A66CC").pack(padx=5, pady=5, side=LEFT)
        self.Object.current(0)
        self.Object["state"] = "readonly"
        self.Object.pack(padx=5, pady=5, side=LEFT)
        tkinter.Button(win,
                                text="文件生成",
                                command=self.mainDoc,
                                width=20,
                                height=1,
                                fg='white',
                                bg='black',
                                borderwidth=5,
                                font=("Arial", 14)
                       ).pack(padx=5, pady=5, side=RIGHT)

    def rtmpWrite(self, path, object):
        str1 = 'vl' + object + ".apc;"
        str2 = 'vm' + object + ".apc;"
        s1 = '\t\tinclude ' + str1 + '\n'
        s2 = '\t\tinclude ' + str2 + '\n'
        try:
            f = open(path, "r")
            list = f.readlines()
            j = 0
            k = 0
            for i in range(len(list)):
                if s1 == list[i]:
                    j = j + 1
                if s2 == list[i]:
                    k = k + 1
            if j == 0:
                with open(path, "a") as f2:
                    f2.write(s1)
            if k == 0:
                with open(path, "a") as f2:
                    f2.write(s2)
            f = open(path, "r")
            return f.read()
        except IOError as e:
            LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
            logging.basicConfig(filename=r'../rtmp-hls/ag2019/logs/errors.log',
                                level=logging.DEBUG,
                                format=LOG_FORMAT
                                )
            logging.debug('rtmpWrite_error:' + str(e))

    def mainDoc(self):
        a = tkinter.messagebox.askyesno('提示', '确定要执行此操作吗？')
        if a == True:
            try:
                path = r'../rtmp-hls/ag2019/conf'
                path1 = r'../rtmp-hls/ag2019/hls/v'
                path2 = r'../rtmp-hls/ag2019/record/v'
                open(r"../rtmp-hls/ag2019/conf/rtmp.apc", "a")  # 新建rtmp.apc文件
                path4 = r'../rtmp-hls/ag2019/conf/rtmp.apc'
                path5 = r'../rtmp-hls/ag2019/conf/nginx.conf'
                str1 = 'vl'
                str2 = 'vm'
                str3 = 'cl'
                str4 = 'cm'
                object = self.obj.get()
                pathJoin1 = self.docPath(path, self.joint(str1, object))
                pathJoin2 = self.docPath(path, self.joint(str2, object))
                fileAbsPath1 = os.path.join(path1, object)
                fileAbsPath2 = os.path.join(path2, object)
                handle3 = self.rtmpWrite(path4, object)
                nginx = self.nginxConf(handle3)
                with open(pathJoin1, 'w+') as handle1:
                    handle1.write(self.vlApc(self.joint(str1, object), self.dict[object]['cl'], self.joint(str2, object), self.joint(str3, object), object))
                with open(pathJoin2, 'w+') as handle2:
                    handle2.write(self.vmApc(self.joint(str2, object), self.dict[object]['cm'],self.joint(str4, object), object))
                with open(path5, "w+") as f2:
                    f2.write(nginx)

                if os.path.exists(fileAbsPath1) == False:
                    os.makedirs(fileAbsPath1)

                if os.path.exists(fileAbsPath2) == False:
                    os.makedirs(fileAbsPath2)
                tkinter.messagebox.showinfo("确认", "配置文件已生成")

            except IOError as e:
                LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
                logging.basicConfig(
                    filename=r'../rtmp-hls/ag2019/logs/errors.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT
                )
                logging.debug('mainDoc_error:' + str(e))

    # 在每个项目前面添加前缀名
    def joint(self, prefix, object):
        jointName = prefix + object
        return jointName

    # 给文件在后缀名
    def docPath(self, path, object):
        suffixName = object + ".apc"
        alterPath = os.path.join(path, suffixName)
        return alterPath

    # vlApc文件的生成
    def vlApc(self,vlobject, clObjIp, vmobject, clobject, object):
        nginx_conf = '''
            application {vlObject}{{
                    live on;

                    #以下三行需要修改
                    on_publish http://10.150.61.33/Inf/vssNotify.ashx;  
                    on_publish_done http://10.150.61.33/Inf/vssNotify.ashx;  
                    push rtmp://localhost:1935/{vmObject};

                    push rtmp://{clOBJIP}:1935/{clObject};
                    hls on;
                    hls_fragment 8s;
                    hls_path /media/sf_hls/ag2019/hls/v/{Object};
                }}
        '''
        nginx = nginx_conf.format(vlObject=vlobject, clOBJIP=clObjIp, vmObject=vmobject, clObject=clobject, Object=object)
        return nginx

    # vmApc文件的生成
    def vmApc(self,vmobject, cmObjIp, cmobject, object):
        nginx_conf = '''
            application {vmObject}{{
                live on;
                
                #以下三行需要修改
                on_publish http://10.150.61.33/Inf/vssNotify.ashx;
                on_publish_done http://10.150.61.33/Inf/vssNotify.ashx;  
                on_record_done http://10.150.61.33/Inf/vssNotify.ashx;  

                push rtmp://{cmOBJIP}:1935/{cmObject};
                record keyframes;
                recorder recFlag{{
                    record all manual;
                    exec_record_done bash /root/yamdi.sh $path $dirname $basename;
                    record_suffix .flv;
                    record_path /media/sf_hls/ag2019/record/v/{Object};
                    record_append on;
                    }}
                }}
        '''
        nginx = nginx_conf.format(vmObject=vmobject, cmOBJIP=cmObjIp,cmObject=cmobject, Object=object)
        return nginx

    def nginxConf(self, rtmp):
        try:
            nginx_conf = '''
            user www www;
            worker_processes 1;
            worker_cpu_affinity auto;

            error_log  /usr/local/nginx/logs/error.log crit;
            pid /var/run/nginx.pid;
            worker_rlimit_nofile 65535;

            events {{
              use epoll;
              worker_connections 65535;
              multi_accept on;
            }}

            rtmp {{
                server {{
                    listen 1935;
                    {rtmp}
                }}
            }}

            http {{
                include /usr/local/nginx/conf/mime.types;
                server {{
                    listen     8088;
                    server_name localhost;
                    location /stat {{
                        rtmp_stat all;
                        rtmp_stat_stylesheet stat.xsl;
                    }}

                    location /stat.xsl {{
                        root /usr/local/src/nginx-rtmp-module/;
                    }}

                    location /control {{
                        rtmp_control all;
                    }} 

                    location /hls{{
                        types{{
                                application/vnd.apple.mpegurl m3u8;
                                        video/mp2t ts;
                        }}       
                        alias /media/sf_hls/ag2019/hls;
                        add_header Cache-Control no-cache;
                        add_header Access-Control-Allow-Origin *;
                    }}
                    location /record {{
                        alias /media/sf_hls/ag2019/record;
                        add_header Cache-Control no-cache;
                        add_header Access-Control-Allow-Origin *;
                    }}                
            	}}
            }}
            '''
            nginxDoc = nginx_conf.format(rtmp=rtmp)
            return nginxDoc
        except IOError as e:
            LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
            logging.basicConfig(
                filename=r'../rtmp-hls/ag2019/logs/errors.log',
                level=logging.DEBUG,
                format=LOG_FORMAT
            )
            logging.debug('nginxConf_error:' + str(e))

if __name__ == '__main__':
    win = Tk()
    win.title("场馆配置文件生成")
    win.geometry("600x500+600+280")
    c = Venue()
    win.configure(background='#0066CC')
    win.minsize(600, 500)  # 窗口的最小缩放
    win.maxsize(600, 500)  # 窗口最大缩放
    win.mainloop()


