class College:
    college_name = "Old KHC"
    
    @classmethod
    def change_name(cls, new_name):
        cls.college_name = new_name
    
    def show(self):
        print(f"College: {College.college_name}")

c1 = College()
c1.show()  
College.change_name("New KHC")
c1.show()  