from socket import *
from select import select

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 6868))
tcp_sock.listen(5)

file = open("my.log", "r+")

udp_sock = socket(AF_INET, SOCK_DGRAM)

print("开始监听IO")
rs, ws, xs = select([file, udp_sock], [file, udp_sock], [])
print("rlist", rs)
print("wlist", ws)
print("xlist", xs)
