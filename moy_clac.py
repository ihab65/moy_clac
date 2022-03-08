
les_modules = ["ana", "chimie", "physique", "algebre", "stat", "info", "dst", "eco", "ing", "fr", "eng"]
  
def calcule_moy():
    moy = []
    for i in les_modules:
        
        if i == "ana":
            print(f"entre votre note de cc , ds et es d' {i}: ")
            cc, ds, es = input(), input(), input()
            moy0 = float(cc)*0.2 + float(ds)*0.3 + float(es)*0.5  
            moy0 *= 6
            moy.append(moy0)
            print(f"votre moy d'{i}", moy0/6)
            
        if i == "chimie" or i == "physique":
            print(f"entre votre note de cc , ds et es d' {i}: ")
            cc, ds, es = input(), input(), input()
            moy1 = float(cc)*0.3 + float(ds)*0.2 + float(es)*0.5
            moy1 *= 5
            moy.append(moy1)
            print(f"votre moy d'{i}", moy1/5)
            
            
        if i == "stat" or i == "algebre":
            print(f"entre votre note de cc , ds et es d' {i}: ")
            cc, ds, es = input(), input(), input()
            moy2 = float(cc)*0.2 + float(ds)*0.3 + float(es)*0.5
            moy2 *= 3
            moy.append(moy2)
            print(f"votre moy d'{i}", moy2/3)
            
        if i == "info":
            print(f"entre votre note de cc , ds et es d' {i}: ")
            cc, ds, es = input(), input(), input()
            moy3 = float(cc)*0.3 + float(ds)*0.2 + float(es)*0.5
            moy3 *= 3
            moy.append(moy3)
            print(f"votre moy d'{i}", moy3/3)
            
        if i == "dst" or i == "eco" or i == "ing" or i == "fr" or i == "eng":
            print(f"entre votre note de cc , ds et es d' {i}: ")
            cc, ds, es = input(), input(), input()
            moy4 = float(cc)*0.2 + float(ds)*0.3 + float(es)*0.5
            moy.append(moy4)
            print(f"votre moy d'{i}", moy4)
            
           
    MOY = (moy[0]+moy[1]+moy[2]+moy[3]+moy[4]+moy[5]+moy[6]+moy[7]+moy[8]+moy[9]+moy[10])/30
    print(MOY)    
        

calcule_moy()        
            
        
