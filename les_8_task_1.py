from hashlib import sha1


def num_sub_str(str_in):
    sub_hex = set()
    for i in range(len(str_in) - 1):
        for j in range(len(str_in) - i):
            sub_hex.add(sha1(str_in[j:j + i + 1].encode('utf-8')).hexdigest())
    return len(sub_hex)


print(num_sub_str(input('Введите строку: ')))
