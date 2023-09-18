encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

decrypted_message=list(encrypted_message[:])
a = 0
b = len(decrypted_message)-1
while a < b:
    decrypted_message[b], decrypted_message[a] = decrypted_message[a], decrypted_message[b]
    a += 2
    b -= 2
# for some reason it came out backwards?
real_decrypted_message = ''
for i in decrypted_message[-1::-1]:
    real_decrypted_message += i
print(real_decrypted_message)





