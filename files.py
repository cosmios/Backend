file_path = "C:\\Users\\GC\\Desktop\\Cosmios\\1Week\\names.txt"

with open(file_path, 'a', encoding="utf-8") as file:


    while(True):


        name = input("Çıkış yapmak için q'ya basınız. \n İsim giriniz: ")

        if(name == 'q'):
            break

        line_name = name + '\n'

        file.write(name)

#     # dosyayı okur
# with open(file_path, 'r') as file:

#     lines = file.readlines()

#     print(lines)

# for line in lines:
#     print(line)

file.close()
