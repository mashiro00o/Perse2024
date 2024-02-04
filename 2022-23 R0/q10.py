last_line = "work hard at this!"

words = last_line.split()
first_letters = [word[0] for word in words]
result_word = ''.join(first_letters)

# main
print(result_word)
