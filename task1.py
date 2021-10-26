# student results in a order of fail or pass ::
hin = int(input("Enter your Hindi marks"))
eng = int(input("Enter your English marks"))
tel = int(input("Enter your Telugu marks"))
mat = int(input("Enter your Maths marks"))
sci = int(input("Enter your Science marks"))
soc = int(input("Enter your Social marks"))

if((hin or eng or tel or mat or sci or soc) <= 35):
    print("Fail")
else:
    if(hin >= 90 ):
        print(hin, " / 100", "A*" )
    elif(hin >=80 ):
        print(hin, " / 100", "A" )
    elif(hin >=70):
        print(hin, " / 100", "B" )
    elif(hin >= 60):
        print(hin, " / 100", "C" )
    elif(hin >=50):
        print(hin, " / 100", "D" )
    elif(hin >= 40):
        print(hin, " / 100", "E" )
if(eng >= 35):
    if(eng >= 90 ):
        print(eng, " / 100", "A*" )
    elif(eng >=80 ):
        print(eng, " / 100", "A" )
    elif(eng >=70):
        print(eng, " / 100", "B" )
    elif(eng >= 60):
        print(eng, " / 100", "C" )
    elif(eng >=50):
        print(eng, " / 100", "D" )
    elif(eng >= 40):
        print(eng, " / 100", "E" )
if(tel >= 35):
    if(tel >= 90 ):
         print(tel, " / 100", "A*" )
    elif(tel >=80 ):
         print(tel, " / 100", "A" )
    elif(tel >=70):
         print(tel, " / 100", "B" )
    elif(tel >= 60):
         print(tel, " / 100", "C" )
    elif(tel >=50):
         print(tel, " / 100", "D" )
    elif(tel >= 40):
         print(tel, " / 100", "E" )
if(mat >= 35):
    if(mat >= 90 ):
        print(mat, " / 100", "A*" )
    elif(mat >=80 ):
        print(mat, " / 100", "A" )
    elif(mat >=70):
        print(mat, " / 100", "B" )
    elif(mat >= 60):
        print(mat, " / 100", "C" )
    elif(mat >=50):
        print(mat, " / 100", "D" )
    elif(mat >= 40):
        print(mat, " / 100", "E" )
if(sci >= 35):
    if(sci >= 90 ):
        print(sci, " / 100", "A*" )
    elif(sci >=80 ):
        print(sci, " / 100", "A" )
    elif(sci >=70):
        print(sci, " / 100", "B" )
    elif(sci >= 60):
        print(sci, " / 100", "C" )
    elif(sci >=50):
        print(sci, " / 100", "D" )
    elif(sci >= 40):
        print(sci, " / 100", "E" )
if(soc >= 35):
    if(soc >= 90 ):
         print(soc, " / 100", "A*" )
    elif(soc >=80 ):
         print(soc, " / 100", "A" )
    elif(soc >=70):
         print(soc, " / 100", "B" )
    elif(soc >= 60):
         print(soc, " / 100", "C" )
    elif(soc >=50):
         print(soc, " / 100", "D" )
    elif(soc >= 40):
         print(soc, " / 100", "E" )
