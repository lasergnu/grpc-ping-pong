# coding=utf-8
""" Sends a ping to a PingPong gRPC service. """

import sys

import grpc

from ping_pb2 import Ping, PingPongStub


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')
    client = PingPongStub(channel)

    ping = Ping(message=sys.argv[1], delaySeconds=float(sys.argv[2]))
    pong = client.SendPing(ping)
    print(pong.message)
