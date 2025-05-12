def tao_tuple_tu_list(lst):
    return tuple(lst)
in_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
nums = list(map(int,in_list.split(',')))
my_tuple = tao_tuple_tu_list(nums)
print("List: ", nums)
print("Tuple từ List: ",my_tuple)