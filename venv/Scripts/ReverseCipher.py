text = input()
cipher = ""
for i in range(len(text)-1,-1,-1):
    cipher = cipher + text[i]
print(cipher)