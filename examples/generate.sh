#!/bin/sh
local_path=$(pwd)

generate() {
    $HOME/protobuf/bin/protoc -I /usr/local/include -I ${local_path} ${local_path}/${1}*.proto --plugin=protoc-gen-custom=../tsPlugin.py --custom_out=${local_path}/new_outputs
}

mkdir new_outputs
for d in */; do
    generate ${d}
done
