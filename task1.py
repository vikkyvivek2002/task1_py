# student results in a order of fail or pass ::
hin = int(input("Enter your Hindi marks"))
eng = int(input("Enter your English marks"))
tel = int(input("Enter your Telugu marks"))
mat = int(input("Enter your Maths marks"))
sci = int(input("Enter your Science marks"))
soc = int(input("Enter your Social marks"))

if(hin >= 35):
    if(hin >= 90 ):
        print("Hindi   ",hin, " / 100", "A*",'p' )
    elif(hin >=80 ):
        print("Hindi   ",hin, " / 100", "A ",'p' )
    elif(hin >=70):
        print("Hindi   ",hin, " / 100", "B ",'p' )
    elif(hin >= 60):
        print("Hindi   ",hin, " / 100", "C ",'p' )
    elif(hin >=50):
        print("Hindi   ",hin, " / 100", "D ",'p' )
    elif(hin >= 35):
        print("Hindi   ",hin, " / 100", "E ","p" )
else:
    print("Hindi   ",hin, " / 100", "F ","F" )
if(eng >= 35):
    if(eng >= 90 ):
        print("English ",eng, " / 100", "A*","p" )
    elif(eng >=80 ):
        print("English ",eng, " / 100", "A ","p" )
    elif(eng >=70):
        print("English ",eng, " / 100", "B ","p" )
    elif(eng >= 60):
        print("English ",eng, " / 100", "C ","p" )
    elif(eng >=50):
        print("English ",eng, " / 100", "D ","p" )
    elif(eng >= 35):
        print("English ",eng, " / 100", "E ","p" )
else:
    print("English ",eng, " / 100", "F ","F" )
if(tel >= 35):
    if(tel >= 90 ):
         print("Telugu  ",tel, " / 100", "A*","p" )
    elif(tel >=80 ):
         print("Telugu  ",tel, " / 100", "A ","p" )
    elif(tel >=70):
         print("Telugu  ",tel, " / 100", "B ","p" )
    elif(tel >= 60):
         print("Telugu  ",tel, " / 100", "C ","p" )
    elif(tel >=50):
         print("Telugu  ",tel, " / 100", "D ","p" )
    elif(tel >= 35):
         print("Telugu  ",tel, " / 100", "E ","p" )
else:
    print("Telugu  ",tel, " / 100", "F ","F" )
if(mat >= 35):
    if(mat >= 90 ):
        print("Maths   ",mat, " / 100", "A*","p" )
    elif(mat >=80 ):
        print("Maths   ",mat, " / 100", "A ","p" )
    elif(mat >=70):
        print("Maths   ",mat, " / 100", "B ","p" )
    elif(mat >= 60):
        print("Maths   ",mat, " / 100", "C ","p" )
    elif(mat >=50):
        print("Maths   ",mat, " / 100", "D ","p" )
    elif(mat >= 35):
        print("Maths   ",mat, " / 100", "E ","p" )
else:
    print("Maths   ",mat, " / 100", "F ","F" )
if(sci >= 35):
    if("Science ",sci >= 90 ):
        print("Science ",sci, " / 100", "A*","p" )
    elif(sci >=80 ):
        print("Science ",sci, " / 100", "A ","p" )
    elif(sci >=70):
        print("Science ",sci, " / 100", "B ","p" )
    elif(sci >= 60):
        print("Science ",sci, " / 100", "C ","p" )
    elif(sci >=50):
        print("Science ",sci, " / 100", "D ","p" )
    elif(sci >= 35):
        print("Science ",sci, " / 100", "E ","p" )
else:
    print("Science ",sci, " / 100", "F ","F" )
if(soc >= 35):
    if(soc >= 90 ):
         print("Social  ",soc, " / 100", "A*","p" )
    elif(soc >=80 ):
         print("Social  ",soc, " / 100", "A ","p" )
    elif(soc >=70):
         print("Social  ",soc, " / 100", "B ","p" )
    elif(soc >= 60):
         print("Social  ",soc, " / 100", "C ","p" )
    elif(soc >=50):
         print("Social  ",soc, " / 100", "D ","p" )
    elif(soc >= 35):
         print("Social  ",soc, " / 100", "E ","p" )
else:
    print("Social  ",soc, " / 100", "F ","F" )
