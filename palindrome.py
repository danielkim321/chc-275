word = input("Enter a word: ")


clean_word = ""
for ch in word:
    if ch != " ":
        if ch >= "A" and ch <= "Z":
            ch = chr(ord(ch) + 32)  
        clean_word = clean_word + ch


backward = ""
for ch in clean_word:
    backward = ch + backward


if clean_word == backward:
    print("That is a palindrome!")
else:
    print("That is not a palindrome.")
