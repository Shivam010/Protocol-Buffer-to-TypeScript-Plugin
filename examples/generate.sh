#!/bin/sh
local_path=$(pwd)

generate() {
    $HOME/protobuf/bin/protoc -I ${local_path} ${local_path}/${1}*.proto --plugin=protoc-gen-custom=../tsPlugin.py --custom_out=${local_path}/new_outputs
}

if [ ! -d "new_outputs" ]; then
    mkdir new_outputs
else 
    rm -rf new_outputs/*
fi
for d in */; do
    generate ${d}
done
