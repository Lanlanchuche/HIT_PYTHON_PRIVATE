def remove_puctuation(s : str):
    dau_cau = ['!', '.', ',', '...', '(', ')', ':', ";", '?']
    for character in s :
        if character in dau_cau:
            s = s.replace(character, '')
    return s

def to_lower(s:str):
    s = s.lower()
    return s

def remove_stopwords(s, stopword):
    s = s.split()
    result = ''
    for word in s:
        if word not in stopword:
            result += word + " "
    return result.strip()

def count_words(s):
    s = s.split()
    count = {}
    for word in s:
        count[word] = s.count(word)

    return count

s = input("Nhap chuoi>>  ")
print("Chuoi sau khi loai bo dau cau: ")
print(remove_puctuation(s))
print("Chuoi sau khi chuyen ve chu thuong")
print(to_lower(s))
stopword = input("Nhap cac tu muon xoa trong chuoi: ")
print("Chuoi sau khi xoa la: ", remove_stopwords(s, stopword))
print("So tu xuat hien trong chuoi la: ", count_words(s))


