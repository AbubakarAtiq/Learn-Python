name='''You can define a bytes object using single quotes, double quotes or triple coated; with literal b prefixed.\nbytes with single quotes'''
bytesObj=b'52s3a6s1sxA$as2'
print(name,'\n',bytesObj)
'''
When using a single quotes to define, you can include double quote character in the bytes sequence. But if you would like include a single quote character, use escape character "\"back slash.
'''
bytesObj=b'52s3a6s1s\'xA$as2';print(bytesObj)
'''
bytes with double quotes
'''
bytesObj=b"52s3a6s1sxA$as2";print(bytesObj)
'''
Similar to the case with single quotes, when using double quotes to define a bytes object, you can include single quote character in the bytes sequence as is. But if you would like include a double quote character, use escape character back slash
'''
bytesObj=b"52s3a6s1s2'xA$as2";print(bytesObj)
bytesObj=b"52s3a6\"s1s2xA$as2";print(bytesObj)
'''
bytes with triple quotes
'''
bytesObj=b'''52s3a6s1s2xA$as2'''
bytesObj=b"""52s3a6s1s2'xA$as2"""
