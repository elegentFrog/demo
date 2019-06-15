from tkinter import *
import tkinter,os,logging,tkinter.messagebox
from tkinter import ttk

#继承Frame类
class Central(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        #设定变量
        self.obj = tkinter.StringVar()  # 项目变量
        self.ip = tkinter.StringVar()
        self.Object = ttk.Combobox(win, textvariable=self.obj)
        self.IP = ttk.Combobox(win,textvariable=self.ip)
        self.Object["value"] = (
            '10.150.61.19',
            '10.150.61.20',
            '10.150.61.21',
            '10.150.61.22',
            #################
            '10.150.61.25',
            '10.150.61.26',
            '10.150.61.27',
            '10.150.61.28',
            '10.150.61.29',
            '10.150.61.30'
        )
        self.live = {
            '10.150.61.19':['APN','ARC','BOX','CRD','OPW','ORI','PAR','SAL'],
            '10.150.61.20':['DIV','MIP','SWM','TEN','ATH','TKW','VBV','GEN'],
            '10.150.61.21':['BDM','BKB','EQU','MPN','SHO','TRI','VVO','WRE'],
            '10.150.61.22':['FBL','FEN','GLF','GAR','JUD','LSA','NPN','TTE']
        }
        self.record = {
            '10.150.61.25': ['APN', 'BOX', 'CRD', 'OPW', 'ORI'],
            '10.150.61.26': ['DIV', 'MIP', 'SWM', 'TEN', 'VBV', 'VVO', 'GEN'],
            '10.150.61.27': ['EQU', 'MPN', 'SHO', 'TRI', 'WRE'],
            '10.150.61.28': ['FBL', 'FEN', 'NPN', 'ATH', 'TWK'],
            '10.150.61.29': ['GLF', 'GAR', 'JUD', 'LSA', 'TTE'],
            '10.150.61.30': ['ARC', 'BDM', 'BKB', 'PAR', 'SAL']
        }
        self.createFrame()
    def createFrame(self):
        tkinter.Label(win, text='第7届世界军人运动会云服务器', font=("楷体", 20), bg="#0A66CC").pack(anchor=CENTER)
        tkinter.Label(win, text='选择云服务器:', font=("Arial", 15), bg="#0A66CC").pack(padx=5, pady=5, side=LEFT)
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

    def rtmpWrite(self,path,str):
        # str1 = 'cl' + object + ".apc;"
        # str2 = 'cm' + object + ".apc;"
        s = '\t\tinclude ' + str + '\n'
        #s2 = '\t\tinclude ' + str2 + '\n'
        try:
            f = open(path, "r")
            list = f.readlines()
            j = 0
            k = 0
            for i in range(len(list)):
                if s == list[i]:
                    j = j + 1
                # if s2 == list[i]:
                #     k = k + 1
            if j == 0:
                with open(path, "a") as f2:
                    f2.write(s)
            # if k == 0:
            #     with open(path, "a") as f2:
            #         f2.write(s2)
            f = open(path, "r")
            return f.read()
        except IOError as e:
            LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
            logging.basicConfig(filename=r'D:\rtmp-hls\ag2019\logs\rtmpWrite_error.log',
                                level=logging.DEBUG,
                                format=LOG_FORMAT
                                )
            logging.debug('File Error:' + str(e))

    def mainDoc(self):
        a = tkinter.messagebox.askyesno('提示', '确定要执行此操作吗？')
        if a == True:
            try:
                obj = self.obj.get()
                path = r'D:\rtmp-hls\ag2019\conf'
                path1 = r'D:\rtmp-hls\ag2019\hls\c'
                path2 = r'D:\rtmp-hls\ag2019\record\c'
                path3 = r'D:\rtmp-hls\ag2019\thumb'
                path4 = r'D:\rtmp-hls\ag2019\conf\{}\rtmp.apc'.format(obj)
                open(path4, "a")  # 新建rtmp.apc文件
                path5 = r'D:\rtmp-hls\ag2019\conf\{}\nginx.conf'.format(obj)

                str1 = 'cl'
                str2 = 'cm'
                path_ip = os.path.join(path, obj)
                if obj in self.live.keys():
                    for object in self.live[obj]:
                        pathJoin1 = self.docPath(path_ip, self.joint(str1, object))
                        pathJoin2 = self.docPath(path_ip, self.joint(str2, object))
                        fileAbsPath1 = os.path.join(path1, object)
                        fileAbsPath2 = os.path.join(path2, object)
                        fileAbsPath3 = os.path.join(path3, object)
                        handle3 = self.rtmpWrite(path4, str1 + object + ".apc;")
                        nginx = self.nginxConf(handle3)
                        with open(pathJoin1, 'w+') as handle1:
                            handle1.write(self.clApc(self.joint(str1, object), object))
                        # with open(pathJoin2, 'w+') as handle2:
                        #     handle2.write(self.cmApc(self.joint(str2, object), object))
                        with open(path5, "w+") as f2:
                            f2.write(nginx)

                        # 新建每个项目业务的文件夹
                        if os.path.exists(fileAbsPath1) == False:
                            os.makedirs(fileAbsPath1)

                        if os.path.exists(fileAbsPath2) == False:
                            os.makedirs(fileAbsPath2)

                        if os.path.exists(fileAbsPath3) == False:
                            os.makedirs(fileAbsPath3)
                elif obj in self.record.keys():
                    for object in self.record[obj]:
                        pathJoin1 = self.docPath(path_ip, self.joint(str1, object))
                        pathJoin2 = self.docPath(path_ip, self.joint(str2, object))
                        fileAbsPath1 = os.path.join(path1, object)
                        fileAbsPath2 = os.path.join(path2, object)
                        fileAbsPath3 = os.path.join(path3, object)
                        handle3 = self.rtmpWrite(path4, str2 + object + ".apc;")
                        nginx = self.nginxConf(handle3)
                        # with open(pathJoin1, 'w+') as handle1:
                        #     handle1.write(self.clApc(self.joint(str1, object), object))
                        with open(pathJoin2, 'w+') as handle2:
                            handle2.write(self.cmApc(self.joint(str2, object), object))
                        with open(path5, "w+") as f2:
                            f2.write(nginx)

                        # 新建每个项目业务的文件夹
                        if os.path.exists(fileAbsPath1) == False:
                            os.makedirs(fileAbsPath1)

                        if os.path.exists(fileAbsPath2) == False:
                            os.makedirs(fileAbsPath2)

                        if os.path.exists(fileAbsPath3) == False:
                            os.makedirs(fileAbsPath3)
                tkinter.messagebox.showinfo("确认", "配置文件已生成")

            except IOError as e:
                LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
                logging.basicConfig(
                    filename=r'D:\rtmp-hls\ag2019\mainDoc_error.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT
                )
                logging.debug('File Error:' + str(e))

    # 配置文件的前缀
    def joint(self, prefix, object):
        jointName = prefix + object
        return jointName

    # 给文件添加后缀名
    def docPath(self, path, object):
        suffixName = object + ".apc"
        alterPath = os.path.join(path, suffixName)
        return alterPath

    def nginxConf(self, rtmp):
        try:
            nginx_conf = '''
            user nfsnobody nfsnobody;
            worker_processes 1;
            worker_cpu_affinity auto;

            error_log  /usr/local/nginx/logs/error.log crit;
            pid /var/run/nginx.pid;
            worker_rlimit_nofile 65535;

            events {{
              use epoll;
              worker_connections 65535;
              #multi_accept on;
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
                    listen      8088;
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

                    location /record {{
                        alias /data/ag2019/record;
                        add_header Cache-Control no-cache;
                        add_header Access-Control-Allow-Origin *;
                    }}   

                    location /hls{{
                        types{{
                            application/vnd.apple.mpegurl m3u8;
                                    video/mp2t ts;
                        }}       
                        alias /data/ag2019/hls;
                        add_header Cache-Control no-cache;
                        add_header Access-Control-Allow-Origin *;
                    }}  

                    location ~ ^/thumb/.*/.*\.jpg{{   
                        root /data/ag2019/;
                        expires 7s;
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
                filename=r'D:\rtmp-hls\ag2019\nginxConf_error.log',
                level=logging.DEBUG,
                format=LOG_FORMAT
            )
            logging.debug('File Error:' + str(e))

    def clApc(self, clobject, object):
        nginx_conf = '''
            application {clObject}{{
    			live on;
    			on_publish http://10.150.61.33/Inf/vssNotify.ashx;
    			on_publish_done http://10.150.61.33/Inf/vssNotify.ashx;
            
    			hls on;
    			hls_fragment 8s;
    			hls_path /data/ag2019/hls/c/{Object};
    			hls_nested on;
    			hls_continuous on;
    			hls_cleanup on;
    			exec_push ffmpeg -i rtmp://localhost:1935/{clObject}/$name -y -f image2 -ss 7 -s 960*540 /data/ag2019/hls/c/{Object}/$name/$name.jpg;

    		}}
        '''
        nginx = nginx_conf.format(clObject=clobject, Object=object)
        return nginx

    # cl***.apc    文件的内容
    def cmApc(self, cmobject, object):
        nginx_conf = '''
            application {cmObject}{{
                live on;
                on_publish http://10.150.61.33/Inf/vssNotify.ashx;
                on_publish_done http://10.150.61.33/Inf/vssNotify.ashx;
                on_record_done http://10.150.61.33/Inf/vssNotify.ashx;

                record keyframes;
                recorder recFlag{{
                    record all manual;
                    record_suffix .flv;
                    exec_record_done bash /root/yamdi.sh $path $dirname $basename;
                    record_path /data/ag2019/record/c/{Object};
                    record_append on;
                }}
                exec_push ffmpeg -i rtmp://localhost:1935/{cmObject}/$name -y -f image2 -ss 7 -s 960*540 /data/ag2019/thumb/{Object}/$name.jpg;
            }}
        '''
        nginx = nginx_conf.format(cmObject=cmobject, Object=object)
        return nginx
if __name__ == '__main__':
    win = Tk()
    win.title("云服务配置文件生成")
    win.geometry("600x500+600+280")
    c = Central()
    win.configure(background='#0066CC')
    win.minsize(600, 500)  # 窗口的最小缩放
    win.maxsize(600, 500)  # 窗口最大缩放
    win.mainloop()


