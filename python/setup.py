from setuptools import setup, find_packages

setup(
    name="encoderproto",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "protobuf>=5.0.0",
        "grpcio>=1.0.0",
    ],
)