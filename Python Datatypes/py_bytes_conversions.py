name='''You can convert a bytes object to other datatypes or other datatype objects to bytes object.\nFor example, in the following program, we shall convert a bytes object to string and string object to bytes.\nPython Program:'''
print(name)
#bytes to string
bytesObj=b'52s3a6s1s2xA$as2'
strObj=bytesObj.decode("utf-8")
print(strObj)
#string to bytes
strObj='hello'
#string to bytes
strObj='hello'
bytesObj=bytes(strObj,"utf=8")
print(bytesObj)
end='''In the first part of the code, we hace taken a bytes object and converted it to string using decode() method.\nIn the second part of the code, we have taken a string and converted it to bytes object using bytes() builtin function.\nSimilar to this, we have a lot of conversions from and to bytes type, and following is the list of tutorials for converting bytes to and fro from other types.\n1.Convert Bytes to string\n2.Convert string to bytes\n3.Convert Bytes to int'''
print(end)