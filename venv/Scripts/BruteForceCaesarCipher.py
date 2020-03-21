import pyperclip;

# message to be encrypted

message  = input()

S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# it's just the decrypting algorithm with trying with every key possible in the encryption
for key in range(len(S)):
    decrypted = ""
    for symbol in message:
        if symbol in S and (key <= 65 and key >= 0):
            symbol_index = S.find(symbol)
            encrypted_index = symbol_index - key;

            if encrypted_index < 0 :
                encrypted_index += len(S)

            decrypted += S[encrypted_index]

        else:
            decrypted += symbol
    print(decrypted)
pyperclip.copy(decrypted)

