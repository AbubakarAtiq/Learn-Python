name='''You can include hexadecimal characters in the bytes sequence. You have to use \x prefix for each hexadecimal character you place in the bytes object.'''
print(name)
bytesObj=b'52s3a6s\xFD1s2xA$as2'
print(bytesObj)
#In the above object, \xFD is a single byte in hexadecimal format.#