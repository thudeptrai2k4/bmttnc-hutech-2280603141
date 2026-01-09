from QuanLySinhVien import QuanLySinhVien

def main():
    qlsv = QuanLySinhVien()  # Tạo đối tượng quản lý sinh viên
    
    while True:
        print("\nChọn chức năng:")
        print("1. Nhập sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Sắp xếp sinh viên theo ID")
        print("4. Sắp xếp sinh viên theo tên")
        print("5. Sắp xếp sinh viên theo điểm trung bình")
        print("6. Tìm sinh viên theo ID")
        print("7. Tìm sinh viên theo tên")
        print("8. Xóa sinh viên theo ID")
        print("9. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            qlsv.nhapSinhVien()  # Nhập sinh viên mới
        elif choice == '2':
            sv_id = int(input("Nhập ID sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(sv_id)  # Cập nhật thông tin sinh viên
        elif choice == '3':
            qlsv.sortByID()  # Sắp xếp theo ID
            print("Danh sách sinh viên đã sắp xếp theo ID")
        elif choice == '4':
            qlsv.sortByName()  # Sắp xếp theo tên
            print("Danh sách sinh viên đã sắp xếp theo tên")
        elif choice == '5':
            qlsv.sortByDiemTB()  # Sắp xếp theo điểm trung bình
            print("Danh sách sinh viên đã sắp xếp theo điểm trung bình")
        elif choice == '6':
            sv_id = int(input("Nhập ID sinh viên cần tìm: "))
            sv = qlsv.findByID(sv_id)  # Tìm sinh viên theo ID
            if sv:
                print(f"Sinh viên tìm thấy: {sv._name}, {sv.sex}, {sv.major}, {sv.diemTB}, {sv.get_hocLuc()}")
            else:
                print(f"Sinh viên với ID {sv_id} không tồn tại.")
        elif choice == '7':
            keyword = input("Nhập tên sinh viên cần tìm: ")
            listSV = qlsv.findByName(keyword)  # Tìm sinh viên theo tên
            if listSV:
                for sv in listSV:
                    print(f"{sv._id}: {sv._name}, {sv.sex}, {sv.major}, {sv.diemTB}, {sv.get_hocLuc()}")
            else:
                print(f"Không tìm thấy sinh viên với tên {keyword}.")
        elif choice == '8':
            sv_id = int(input("Nhập ID sinh viên cần xóa: "))
            if qlsv.deleteById(sv_id):  # Xóa sinh viên theo ID
                print(f"Sinh viên với ID {sv_id} đã bị xóa.")
            else:
                print(f"Sinh viên với ID {sv_id} không tồn tại.")
        elif choice == '9':
            qlsv.ShowSinhVien(qlsv.getListSinhVien())  # Hiển thị danh sách sinh viên
        elif choice == '0':
            print("Thoát chương trình.")
            break  # Thoát khỏi vòng lặp và kết thúc chương trình
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
