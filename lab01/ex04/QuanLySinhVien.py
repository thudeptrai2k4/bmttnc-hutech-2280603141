from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xeploaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex  = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))

            sv._name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xeploaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại!")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse=False)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if(sv._id == ID):
                return sv
        return None

    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if(keyword.upper() in sv._name.upper()):
                listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            return True
        return False

    def xeploaiHocLuc(self, sv):
        if(sv.diemTB >= 8):
            sv.set_hocLuc("Giỏi")
        elif(sv.diemTB >= 6.5):
            sv.set_hocLuc("Khá")
        elif(sv.diemTB >= 5):
            sv.set_hocLuc("Trung Bình")
        else:
            sv.set_hocLuc("Yếu")

    def ShowSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if(listSV):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv.sex, sv.major, sv.diemTB, sv.get_hocLuc()))
        else:
            print("Không có sinh viên nào.")

    def getListSinhVien(self):
        return self.listSinhVien

    def soLuongSinhVien(self):
        return len(self.listSinhVien)
