Protocol Buffer to TypeScript Plugin
====================================
Protocol Buffer is copyright with Google Inc. https://developers.google.com/protocol-buffers/

Protocol Buffer to TypeScript Plugin is the extension of the Protocol Compiler to compile the proto files into corresponding TypeScript code.

Overview
========

Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data. You can find [protobuf's documentation on the Google Developers site](https://developers.google.com/protocol-buffers/).

This repository contains the TypeScript extension that implements Protocol Buffers functionality in TypeScript.

Consider file test.proto, 

```proto
    syntax = "proto3";

    package test;

    message Msg{
    string name = 1;
    }
```

Compiling the file into TypeScript code, 

```typescript
    import { Observable } from 'rxjs';

    export interface Msg {
        name: string;
    }
```

Installations
=============

1) Make sure you have Python 2.x.  If in doubt, run:
       
       $ python -V

2) If you don't have the protocol compiler, `protoc` installed, install a binary distribution of `protoc`, and the simplest way to install it is to download a [pre-built binary](https://github.com/google/protobuf/releases).
        
        $ protoc --version

3) Download or clone the [Python Protocol Buffers runtime library](https://github.com/google/protobuf/tree/master/python)

4) Build and run the tests:

       $ python setup.py build
       $ python setup.py test

5) And Install:

       $ python setup.py install

6) Now, clone our plugin and you are all done.

Setup and Run
=============

For Windows

1) Set the interpreter to the plugin by adding your Python 2.x path 'C:\Python27\python.exe' in the begining of the `tsPlugin.py` file
    `#!C:\Python27\python.exe`

2) Now, edit the `runPlugin.bat` file to make the python file executable.

3) Now, generate your TypeScript code using,
	
	`$ protoc -I <Project_Path> -I <Proto_File_Directory_Path> <Proto_Files_Path> --plugin=protoc-gen-custom=<Executable_File_Path> --custom_out=<Output_Directory_Path>`
    Like:

	`$ pwd
	`..\protobuf-to-typescript`
	`$ protoc -I . -I examples examples\test.proto --plugin=protoc-gen-custom=runPlugin.bat --custom_out=examples\output`

Fow Linux

1) Set the interpreter to the plugin by adding your Python 2.x path '/usr/bin/env python' in the begining of the `tsPlugin.py` file
    `#!/usr/bin/env python`

2) Now, generate your TypeScript code using,

	$ protoc -I <Python_Path> -I <Proto_File_Directory_Path> <Proto_Files_Path> --plugin=protoc-gen-custom=<Plugin_Path> --custom_out=<Output_Directory_Path>

    Like:
	
	$ protoc -I /usr/local/include -I examples examples\test.proto --plugin=protoc-gen-custom=tsPlugin.py --custom_out=examples\output

    or 

    Use the `generator.sh` script to compile all the proto files in a directory

Contributing
============
Changes and improvements are more than welcome! 
Feel free to fork and open a pull request. 
And Please make your changes in a specific branch and request to pull into master! If you can, please make sure the game fully works before sending the PR, as that will help speed up the process.

License
=======
Protocol Buffer to TypeScript Plugin is licensed under the [MIT license](https://github.com/Shivam010/Protocol-Buffer-to-TypeScript-Plugin/blob/master/LICENSE).
