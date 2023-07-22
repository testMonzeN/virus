class Register():
    def register(name):
        SteamID = int(input("please, write your SteamID: "))
        SteamName = input("please, write your SteamName: ")
        SteamPassword = input("please, write your SteamPassword: ")

        try:
            with open(r'C:\MonzeN\log\LogRegistor.txt', "a", encoding="utf-8") as reg:
                reg.write("SteamID: " + str(SteamID) + "\n")
                reg.write("SteanName: " + SteamName + "\n")
                reg.write("SteamPassword: " + SteamPassword + "\n")
        except:
            pass    

        


