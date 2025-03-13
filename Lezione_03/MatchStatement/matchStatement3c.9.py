point_x:int=int(input("inserisci x: "))
point_y:int=int(input("inserisci y: "))

coordinate:tuple=(point_x,point_y)
match coordinate:
    case(0,0):
            print(f"Il punto{coordinate} si trova nell'origine.")
    case(point_y, 0):
            print(f"Il punto{coordinate}si trova sull'asse X.")
    case(point_x, 0):
            print(f"Il punto {coordinate} si trova sull'asse Y.")
    case(point_x,point_y) if point_x > 0 and point_y > 0:
              print(f"Il punto {coordinate} si trova nel primo quadrante.")
    case(point_x,point_y) if point_x < 0 and point_y > 0: 
                print(f"Il punto {coordinate} si trova nel secondo quadrante.")
    case(point_x,point_y) if point_x < 0 and point_y < 0: 
                print(f"Il punto {coordinate} si trova nel terzo quadrante.")
    case(point_x,point_y) if point_x > 0 and point_y < 0: 
                print(f"Il punto {coordinate} si trova nel quarto quadrante.")
    