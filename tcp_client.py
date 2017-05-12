#coding=utf-8
import getopt,socket,sys,string

opts, args = getopt.getopt(sys.argv[1:], "hi:p:",["help","ip=","port="])
#设置默认的ip地址和端口号，在没有使用命令传入参数的时候将使用默认的值
host="localhost"
port=8001
def usage():
    print """
    -h --help             print the help
    -i --ip               Enter the IP address to connect
    -p --port             Enter the port number to connect
    """
for op, value in opts:
    if op in ("-i","--ip"):
        host = value
    elif op in ("-p","--port"):
        port = string.atol(value)
    elif op in ("-h"):
        usage()
        sys.exit()

def main():
#创建socket对象。调用socket构造函数
#AF_INET为ip地址族，SOCK_STREAM为流套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置要连接的服务器的ip号和端口号
    sock.connect((host, port))
#客户端输入一个字符串给服务器
    while True:
        message = raw_input("inupt:")
    #pdb.set_trace()
        if message == 'exit':
            break
        sock.send(message)
        #print 'ServerOupt:'+ sock.recv(2048)
#关闭与服务器的连接
    sock.close()

if __name__ == '__main__':
    main()