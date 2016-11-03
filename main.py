# coding=utf-8
""" Serves Pongs to SendPing's via gRPC """

from concurrent import futures
from time import sleep

import grpc

from ping_pb2 import PingPongServicer, Pong, add_PingPongServicer_to_server


class PingPong(PingPongServicer):
    """ Implementation of the PingPong interface defined in ping.proto """
    def SendPing(self, request, context):
        """ Fulfills SendPing RPC defined in ping.proto """
        print("Received message '{}', delaying {}s...".format(request.message, request.delaySeconds))
        if request.delaySeconds:
            sleep(request.delaySeconds)
        return Pong(message="Thanks, friend!")


if __name__ == '__main__':
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PingPongServicer_to_server(PingPong(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    while True:
        # Sleep forever, since `start` doesn't block
        sleep(1)
