#!/bin/sh
set -e
# check to see if protobuf folder is empty
if [ 1 ]; then
  wget https://github.com/google/protobuf/releases/download/v3.6.1/protobuf-python-3.6.1.tar.gz
  ls -la
  tar -xzvf protobuf-python-3.6.1.tar.gz
  ls -la
  pushd protobuf-3.6.1 && ./configure --prefix=$HOME/protobuf && make && sudo make install && popd
  pwd
  ls -la
  cd python
  python setup.py build
  python setup.py test
  pwd 
  ls -la 
  echo "Downloading protobuf and caching."
else
  echo "Using cached directory."
fi