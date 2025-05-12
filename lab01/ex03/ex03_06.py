def del_element(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a': 1, 'b' : 2,'c' : 3, 'd' : 4}
key_to_del = 'b'
result = del_element(my_dict,key_to_del)
if result:
    print("Phần tử đã được xoá từ dictionary: ",my_dict)
else:
    print("không tìm thấy phần tử cần xoá trong dictionary.")