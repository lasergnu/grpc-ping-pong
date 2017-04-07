import sys
import grpc
from ping_pb2 import Ping, PingPongStub

client = PingPongStub(grpc.insecure_channel('localhost:50051'))
ping = Ping(message=sys.argv[1], delaySeconds=float(sys.argv[2]))
print(client.SendPing(ping).message)
