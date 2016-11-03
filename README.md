# gRPC Ping Pong

[gRPC](http://www.grpc.io/) is a high performance, open-source universal RPC framework that can help make your 
Python services blazing fast.  This is a bare bones example of creating and using a gRPC 
ping-pong service and client.

## Running

- `pip install -r requirements.txt --user`
- `python -m grpc.tools.protoc --python_out=. --grpc_python_out=. --proto_path=. ping.proto`
- `python main.py`
- In anonther terminal: `python send_ping.py 'hello, grpc!' 0.3`
