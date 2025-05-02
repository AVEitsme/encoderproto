## Generation
### Golang
```bash
protoc -I protos protos/encoder.proto --go_out=./go/gen --go_opt=paths=source_relative --go-grpc_out=./go/gen --go-grpc_opt=paths=source_relative
```
### Python
```
python -m grpc_tools.protoc -I protos/ ./protos/encoder.proto --python_out=./python/gen --pyi_out=./python/gen --grpc_python_out=./python/gen 
```
