from datetime import datetime
import uuid
import psutil

def get_uuid():
    return str(uuid.uuid4())

def dateTime():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y%l:%M:%S %p")
    return date

def memory():
    mem = psutil.disk_usage('/')
    usage = int(psutil.disk_usage('/')[1]/(10**6))
    total = int(psutil.disk_usage('/')[0]/(10**6))
    per = psutil.disk_usage('/')[3]
    str_mem = str(usage) + "/" + str(total) + " Mb (" + str(per) + "%)"
    return str_mem