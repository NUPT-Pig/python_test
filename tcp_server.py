#coding=utf-8
import socket
import os
import threading,getopt,sys,string

opts, args = getopt.getopt(sys.argv[1:], "hp:l:",["help","port=","list="])
#设置默认的最大连接数和端口号，在没有使用命令传入参数的时候将使用默认的值
list=50
port=8001
def usage():
    print """
    -h --help             print the help
    -l --list             Maximum number of connections
    -p --port             To monitor the port number
    """
for op, value in opts:
    if op in ("-l","--list"):
        list = string.atol(value)
    elif op in ("-p","--port"):
        port = string.atol(value)
    elif op in ("-h"):
        usage()
        sys.exit()

def jonnyS(client, address):
    try:
    #设置超时时间
        client.settimeout(500)
    #接收数据的大小
        while True:
            print os.getpid() + '++wait recv data+++'
            buf = client.recv(2048)
            print (buf)
    #将接收到的信息原样的返回到客户端中
        #client.send(buf)
    #超时后显示退出
    except socket.timeout:
        print 'time out'
    #关闭与客户端的连接
    client.close()

def main():
    #创建socket对象。调用socket构造函数
    #AF_INET为ip地址族，SOCK_STREAM为流套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #将socket绑定到指定地址，第一个参数为ip地址，第二个参数为端口号
    sock.bind(('localhost', port))
    #设置最多连接数量
    sock.listen(list)
    while True:
    #服务器套接字通过socket的accept方法等待客户请求一个连接
        print '--wait new accept---'
        client,address = sock.accept()
        thread = threading.Thread(target=jonnyS, args=(client, address))
        thread.start()

if __name__ == '__main__':
    main()