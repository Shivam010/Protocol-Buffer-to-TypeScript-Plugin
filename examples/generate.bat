@echo off
Rem generates all the ts files corresponding to the proto files in the directory
for /f %%f in ('dir /b /s *.proto') do (
    for /f %%i in ('dir /ad /b') do protoc -I . -I %cd%\%%i %%f --plugin=protoc-gen-custom=..\runPlugin.bat --custom_out=output
)