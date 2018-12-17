#!/bin/sh
local_path=$(pwd)

generate() {
    $HOME/protobuf/bin/protoc -I ${local_path} ${local_path}/${1}*.proto --plugin=protoc-gen-custom=../tsPlugin.py --custom_out=${local_path}/test_output
}

if [ ! -d "test_output" ]; then
    mkdir test_output
else 
    rm -rf test_output/*
fi
for d in */; do
    generate ${d}
done
