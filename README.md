## Generation
### Golang
```bash
protoc -I protos protos/encoder.proto --go_out=./gen/go/ --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative
```
### Python
```
python -m grpc_tools.protoc -I protos/ ./protos/encoder.proto --python_out=./gen/python --pyi_out=./gen/python --grpc_python_out=./gen/python
```
