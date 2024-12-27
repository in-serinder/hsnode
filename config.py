import os
import json
import os
import datetime


json_data={
    "creat_date":datetime.datetime.now().isoformat(),
    "log_use":True,
    "port":6000,
    "ipv4":"127.0.0.1",
    "scan_time":10,
}

config_file= "config.json"
file_data={}


def exist_config():
    if not os.path.exists(config_file):     #存在?
        with open("config.json", "w")as file:
            json.dump(json_data,file,indent=4)
    else:
        try:
            config_data=file_data
            #校验
            for key,value in json_data.items():
                if key not in config_data:
                    config_data[key]=value  #修复
        except FileNotFoundError:
            print("Json Config File Not Found")




def get_config():   #处理配置文件
    global file_data
    exist_config()
    with open(config_file,"r")as file:
        file_data=json.load(file)




def get_log_isuse():
    return file_data['log_use']

def get_ipv4():
    # print("sdsda",file_data)
    try:
        exist_config()
        return file_data['ipv4']
    except KeyError:
        print("JSON key value error---[ipv4]")



#get_port
    # "res_dir_port":6324,
    # "base_info_api_port":6325,
    # "log_api_port":6326,
    # "public_msg_api_port":6327,
    # "status_api":6328,
    # "webinfo_api":6329

def custom_port():
    if file_data['custom_port']:
        return True
    else:
        return False


def get_master_port():  #主端口
    return file_data['port']





def get_scan_time():
    return file_data['scan_time']

