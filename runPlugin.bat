@echo off
cd ..
REM Change the path in the chdir command with your tsPlugin residing directory
REM And Change the Python Interpreter Path to run the plugin
C:/Python27/python.exe -u tsPlugin.py
REM protoc -I . -I folder folder\file.proto --plugin=protoc-gen-custom=runPlugin.bat --custom_out=..\ts-proto
