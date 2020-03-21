import pyperclip;

# message to be encrypted

message  = input()
mode = "e"
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
encrypted = ""
key = int(input())
for symbol in message:
    if symbol in S and (key <= 65 and key >= 0):
        symbol_index = S.find(symbol)
        if mode == "e":
            encrypted_index = symbol_index +  key
        elif mode == "d" :
            encrypted_index = symbol_index - key;

        if encrypted_index >= len(S):
            encrypted_index -= len(S)
        elif encrypted_index < 0 :
            encrypted_index += len(S)

        encrypted += S[encrypted_index]

    else:
        encrypted += symbol
print(encrypted)
pyperclip.copy(encrypted)

