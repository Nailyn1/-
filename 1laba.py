message = 'СОВЕРШЕННО СЕКРЕТНО'
key = '3143143143143143143'
encryp = 'ФПЖИСЬИОССАХИЛФИУСС'
indexenc = []
finallyenc = []
a = ''
for i in range(len(message)):
    enc = ord(message[i]) + int(key[i])
    indexenc.append(enc)
for i in range(len(message)):
    encfin = chr(indexenc[i])
    finallyenc.append(encfin)
print(finallyenc)
print(''.join(finallyenc))