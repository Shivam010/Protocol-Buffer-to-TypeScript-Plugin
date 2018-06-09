#!/usr/bin/env python
# tsPlugin.py is the plugin compiler to generate the TypeScript code for the corresponding protocol buffer code
import sys

from google.protobuf.compiler import plugin_pb2 as plugin
from google.protobuf.descriptor_pb2 import DescriptorProto, EnumDescriptorProto, ServiceDescriptorProto

# Data Types corresponding to the parsed numerical values for datatypes generated by google.protobuf.compiler
DataType = { 
    1: "number", 2: "number", 3: "number", 4: "number", 5: "number",
    6: "number", 7: "number", 8: "boolean", 9: "string", 10: "Group",
    11: "Message", 12: "string", 13: "number", 14: "Enum", 15: "number", 
    16: "number", 17: "number", 18: "number", 19: "number",
}

# Custom Types [ <first>: input_parameter, <second>: output_observable] translated in typesript format
CustomType = {
    "Empty": ["", "void"], 
    "Timestamp": ["number","number"], 
    "Duration": ["number","number"],
    "Any": ["any","any"],
}

# Ignored Imports are the imports for which we are providing custom types
ImportIgnore = [
    "GoogleProtobuf",
]

# Package stores all the package name of the provided files including the imported files corresponding to their file name
PackAge = {}

# dictPackage keys all the packages that are called in
dictPackage = {} 
# dictImports stores all the imports for a package
dictImports = {} 
# dictImports stores all the classes, enums, and interfaces for a package
dictDeclarations = {}

# Output File Name
def fileName(nameWithExt):
    seg = nameWithExt.split('.')
    no = len(seg)
    nameWithoutExt = seg[0]
    for i in range(1,no-1):
        nameWithoutExt+="."+seg[i]
    return nameWithoutExt

# imported variable name case handling 
def importVariable(name):
    seg = name.split('.')
    name = ""
    for i in seg:
        i = i[0].upper() + i[1:]
        name += i
    return name

# interface name case handling 
def interfaceName(full_name):
    seg = full_name.split('.')
    name = seg[len(seg)-1]
    package = seg[1]
    i = 2
    while (i < len(seg)-1):
        package += "." + seg[i]
        i = i + 1
    package = importVariable(package)
    return name, package

# variable name case handling
def variableName(name):
    seg = name.split('_')
    res = ""
    no = len(seg)
    for i in range(no):
        if i != 0:
            seg[i] = seg[i][0].upper() + seg[i][1:]
        res+=seg[i]
    return res

# function name case handling
def functionName(name):
    name = name[0].lower() + name[1:]
    return name

# fucntion parameter case handling
def functionParameter(name):
    name = name[0].lower()+name[1:]
    return name

# parametersTypes returns the Function input Parameters
def parametersTypes(proto_package, full_name):
    name, package = interfaceName(full_name)
    if name in CustomType:
        if CustomType[name][0] == "":
            return ""
        else:
            return functionParameter(name) + ": " + CustomType[name][0]
    else:
        inface = name
        if package != proto_package:
            inface = package + "." + inface
        return functionParameter(name) + ": " + inface

# returnTypes returns Function output Parameters
def returnTypes(proto_package, full_name):
    name, package = interfaceName(full_name)
    #return full_name
    if name in CustomType:
        return CustomType[name][1]
    else:
        if package != proto_package:
            name = package + "." + name
        return name


# nestedTypes returns the nested declarations of enums and message 
def nestedTypes(proto_file, proto_package):
    # Nested Enums
    Enums = ""
    for enm in proto_file.enum_type:
        Enums += "export enum " + enm.name + " {\n"
        for v in enm.value:
            Enums += "\t" + str(v.name) + " = " + str(v.number) + ",\n"
        Enums += "}\n\n"

    # Nested Inerfaces
    Interfaces = ""
    for msg in proto_file.nested_type:
        Interfaces += nestedTypes(msg, proto_package)
        Interfaces += "export interface " + msg.name + " {\n"
        for f in msg.field:
            dtype = DataType[f.type]
            if dtype == "Message" or dtype == "Enum":
                dtype, package = interfaceName(f.type_name)
                if dtype in CustomType:
                    dtype = CustomType[dtype][0]
                else:
                    if package != proto_package:
                        dtype = package + "." + dtype
            arr = ""
            if f.label == 3: # if Repeated
                arr = "[]"
            Interfaces += "\t" + variableName(f.name) + ": " + dtype + arr + ";\n"
        Interfaces += "}\n\n"

    return Enums + Interfaces


# Final TypeScript code generator
def generateCode(request, response):
    # Generate Package
    for proto_file in request.proto_file:
        PackAge[str(proto_file.name)] = str(proto_file.package)

    # Parse requests
    for proto_file in request.proto_file:
        # File Name and Package
        proto_file_name = fileName(str(proto_file.name))
        proto_package = importVariable(PackAge[str(proto_file.name)])

        # Stores Imports 
        Imports = ""
        for imp in proto_file.dependency:
            importName = importVariable(PackAge[imp])
            if importName not in ImportIgnore and importName != proto_package:
                Imports += "import * as " + importName + " from './" + PackAge[imp].lower() + ".service'\n"
        
        # Stores Enums
        Enums = ""
        for enm in proto_file.enum_type:
            Enums += "export enum " + enm.name + " {\n"
            for v in enm.value:
                Enums += "\t" + str(v.name) + " = " + str(v.number) + ",\n"
            Enums += "}\n\n"

        # Stores Interfaces
        Interfaces = ""
        for msg in proto_file.message_type:
            Interfaces += "export interface " + msg.name + " {\n"
            for f in msg.field:
                dtype = DataType[f.type]
                if dtype == "Message" or dtype == "Enum":
                    dtype, package = interfaceName(f.type_name)
                    if dtype in CustomType:
                        dtype = CustomType[dtype][0]
                    else:
                        if package != proto_package:
                            dtype = package + "." + dtype
                arr = ""
                if f.label == 3: # if Repeated
                    arr = "[]"
                Interfaces += "\t" + variableName(f.name) + ": " + dtype + arr + ";\n"
            Interfaces += "}\n\n"
            Interfaces += nestedTypes(msg, proto_package)

        # Stores Classes
        Classes = "" 
        for service in proto_file.service:
            Classes += "export abstract class Service" + service.name + " {\n"
            for m in service.method:
                Classes += "\tabstract " + functionName(m.name) + "(" + parametersTypes(proto_package, m.input_type) + "): Observable<" + returnTypes(proto_package, m.output_type) + ">;\n"
            Classes += "}\n\n"
    
        # proto_package will acts as the key to store all imports, classes, enums, and interfaces of all files with same package name
        key = proto_package
        if key not in dictPackage:
            dictPackage[key] = True
            dictImports[key] = Imports
            dictDeclarations[key] = Classes + Enums + Interfaces
        else:
            dictPackage[key] = True
            dictImports[key] += Imports
            dictDeclarations[key] += Classes + Enums + Interfaces

    # Fill responses in TypeScript corresponding to the proto::buffer
    for key in dictPackage.keys():
        if key in ImportIgnore:
            continue
        Imports =   "import { Observable } from 'rxjs';\n" + dictImports[key]
        Declarations = dictDeclarations[key]
        f = response.file.add()
        name = ""
        name += key[0].lower()
        for i in range(1,len(key)):
            if key[i].isupper():
                name += "."
            name += key[i].lower()
        f.name = name + ".service.ts"
        f.content = Imports + "\n" + Declarations


# Main CallBack
if __name__ == '__main__':
    # Read request message from stdin
    data = sys.stdin.read()

    # Parse request
    request = plugin.CodeGeneratorRequest()
    request.ParseFromString(data)

    # Create response
    response = plugin.CodeGeneratorResponse()

    # Generate code
    generateCode(request,response)

    # Serialise response message
    output = response.SerializeToString()

    # Write to stdout
    sys.stdout.write(output)

