# gRPC Ping Pong

## Running

- `pip install -r requirements.txt --user`
- `python -m grpc.tools.protoc --python_out=. --grpc_python_out=. --proto_path=. ping.proto`
- `python main.py`
- In anonther terminal: `python send_ping.py 'hello, grpc!' 0.3`
