studentList = list()

#%%
def add():
    while True:
        print("Öğrenci ekleme sistemine hoşgeldiniz\n*****************")
        
        
        fname = input("Öğrenci adı girin: ")
        lname = input("Öğrenci soyadı girin: ")
        
        studentList.append((fname+" "+lname))
        
        with open("./2.Hafta/students.txt","w+") as f:
            for student in studentList:
                
                f.writelines(student + "\n")
        f.close()
        
        print("\nBaşka Öğrenci eklemek istiyor musunuz?\nEvet veya Hayır yazın")
        
        cont = input(": ")
        
        
        if cont.title() == "Evet":
            continue
        elif cont.title() == "Hayır":
            break
            
        
        
        print("Oturum sonlandırıldı\n\n")
        
#%%

def remove_():
    
    print("Öğrenci çıkarma sistemine hoşgeldiniz\n*****************")
    
    fname = input("Öğrenci adı girin: ")
    lname = input("Öğrenci soyadı girin: ")
    student_name = fname + " " + lname
    studentList.remove((student_name))
    with open("./2.Hafta/students.txt",encoding="utf-8") as f:
        s = f.read()
        data = s.replace(student_name,"")
    with open("./2.Hafta/students.txt","w",encoding="utf-8") as f:
        f.write(data.strip())
        f.close()
    print("\rBaşka Öğrenci çıkarmak istiyor musunuz?\nEvet veya Hayır yazın")
    cont = input(": ")
    
    if cont.title() == "Evet": remove_()
        
    else:
        print("Oturum sonlandırıldı\n\n")
    
#%%     

def lister():
    for student in studentList:
        studentNumber = (studentList.index(student))
        print(f'Öğrenci Adı : {student}, Öğrenci numarası :  {str(studentNumber)}')
        

add()
remove_()
lister()
