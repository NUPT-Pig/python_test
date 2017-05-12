import daemon

#daemon 守护进程没有显示输出 可以打log看 反正下面的格式是对的
with daemon.DaemonContext():
    while True:
        print('******')
