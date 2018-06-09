#!/bin/sh
local_path=$(pwd)

generate() {
    protoc -I ${local_path} --plugin=protoc-gen-custom=./tsPlugin.py --custom_out=.\output ${local_path}/${1}*.proto
}

for d in */; do
    generate ${d}
done
