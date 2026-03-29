class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self.sex = sex
        self.major = major
        self.diemTB = diemTB
        self._hocLuc = ""
    
    def get_hocLuc(self):
        return self._hocLuc

    def set_hocLuc(self, hocLuc):
        self._hocLuc = hocLuc
