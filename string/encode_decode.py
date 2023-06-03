str = input('Please enter string data:\n')

bytes_encoded = str.encode()

str_decoded = bytes_encoded.decode()

print('Encoded bytes =', bytes_encoded)
print('Decoded String =', str_decoded)

#you can try with "üŋíc0de"