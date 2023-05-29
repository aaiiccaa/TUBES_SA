def search_word(text, target_word):
    if len(text) < len(target_word):
        return False
    if target_word in text:
        return True
    else:
        mid = len(text) // 2
        left_found = search_word(text[:mid], target_word)
        right_found = search_word(text[mid:], target_word)
        return left_found or right_found

text = input("Masukkan kalimat: ")
word = input("Masukkan kata yang ingin dicari: ")

found = search_word(text, word)
print("Apakah kata ditemukan?", found)
