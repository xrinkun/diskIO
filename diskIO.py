import psutil
import time
import sys
import os
import platform

def getDiskInfo():
    sleepTime = 5

    pre_info = psutil.disk_io_counters()
    pre_read_bytes = pre_info[2]
    pre_write_bytes = pre_info[3]

    time.sleep(sleepTime)

    info = psutil.disk_io_counters()
    read_bytes = info[2]
    write_bytes = info[3]
    res_write_byte = (write_bytes - pre_write_bytes) / 1024 / sleepTime 
    res_read_byte = (read_bytes - pre_read_bytes) / 1024 / sleepTime

    return (res_read_byte,res_write_byte)

def printResult(r_bytes, w_bytes, argv="-k"):
    if argv == "-m":
        print("读取速度为: %.2f Mb/s" % (r_bytes / 1024))
        print("写入速度为: %.2f Mb/s" % (w_bytes / 1024))
    elif argv == "-k":
        print("读取速度为: %.2f Kb/s" % r_bytes)
        print("写入速度为: %.2f Kb/s" % w_bytes)

def terminalClear():
    systemName = platform.system()
    if systemName == "Windows":
        os.system("cls")
    elif systemName == "Linux":
        os.system("clear")
    elif "Darwin" in systemName:
         os.system("clear")
    else:
        return

def main():
    args = "-k"
    if len(sys.argv) > 1:
        if sys.argv[1] == "-m":
            args = "-m"
        elif sys.argv[1] == "-k":
            args = "-k"
        elif sys.argv[1] == "-h":
            print("diskIO -m 以Mb/s为单位显示")
            print("diskIO -k 以Kb/s为单位显示")
            print("diskIO -h 查看帮助")
            return
        else:
            print("输入-h参数获取帮助")
            return

    while True:
        temp = getDiskInfo()
        r = temp[0]
        w = temp[1]
        terminalClear()
        printResult(r,w,args)

if __name__ == "__main__":
    main()