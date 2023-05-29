def search_word(text, target_word):
    words = text.split()
    for word in words:
        if word == target_word:
            return True
    return False

text = input("Masukkan kalimat: ")
word = input("Masukkan kata yang ingin dicari: ")

found = search_word(text, word)
print("Apakah kata ditemukan?", found)