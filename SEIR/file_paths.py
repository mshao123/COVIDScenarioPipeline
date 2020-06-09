import os
import datetime

def create_file_name(run_id,prefix,index,type,extension):
    return("%s%09d.%s.%s.%s" % (prefix,index,run_id,type,extension))

def create_file_name_without_extension(run_id,prefix,index,type):
    return("%s%09d.%s.%s" % (prefix,index,run_id,type))

def run_id():
    return(datetime.datetime.strftime(datetime.datetime.now(),"%Y.%m.%d.%H:%M:%S.%Z"))

def create_dir_name(run_id,prefix,type):
    return(os.path.dirname(prefix))