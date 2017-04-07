## gRPC Ping Pong

[gRPC](http://www.grpc.io/) is a high performance, open-source universal RPC framework that can help make your 
Python services blazing fast.  This is a bare bones example of creating and using a gRPC 
ping-pong service and client.

## Installing

cd grpc-ping-pong/
sudo apt-get install pip
sudo apt-get install python-virtualenv
virtualenv venv
source venv/bin/activate
python -m pip install grpcio
python -m pip install grpcio-tools

## Running

# In one terminal:
python -m grpc.tools.protoc --python_out=. --grpc_python_out=. --proto_path=. ping.proto
python main.py

# In another terminal:
python send_ping.py 'hello, grpc!' 0.3

## Credits

Initial version from
https://gitlab.com/thoughtvector/grpc-ping-pong.git