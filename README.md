## Generation
### Golang
```bash
protoc -I protos protos/encoder.proto --go_out=./go/encoderproto --go_opt=paths=source_relative --go-grpc_out=./go/encoderproto --go-grpc_opt=paths=source_relative
```
### Python
```
python -m grpc_tools.protoc -I protos/ ./protos/encoder.proto --python_out=./python/encoderproto --pyi_out=./python/encoderproto --grpc_python_out=./python/encoderproto 
```
