try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0: raise Exception("La edad no puede ser menor a 0")
    precio = int(input("Ingrese el precio de la entrada: "))
    if precio < 0: raise Exception("El precio no puede ser menor a 0")
    if edad < 5:
        print("No puede ingresar al teatro ya que es un menor de 5 años")
    else:
        if 5 <= edad <= 14:
            descuento = precio*0.35
            descuento = round(descuento)
            print(f"El cliente se encuentra en categoria 1, obtiene un descuendo del 35% que corresponde a ${descuento}")
        else:
            if 15 <= edad <= 19:
                descuento = precio*0.25
                descuento = round(descuento)
                print(f"El cliente se encuentra en categoria 2, obtiene un descuendo del 25% que corresponde a ${descuento}")
            else:
                if 20 <= edad <= 45:
                    descuento = precio*0.1
                    descuento = round(descuento)
                    print(f"El cliente se encuentra en categoria 3, obtiene un descuendo del 10% que corresponde a ${descuento}")
                else:
                    if 46 <= edad <= 65:
                        descuento = precio*0.25
                        descuento = round(descuento)
                        print(f"El cliente se encuentra en categoria 4, obtiene un descuendo del 25% que corresponde a ${descuento}")
                    else:
                        descuento = precio*0.35
                        descuento = round(descuento)
                        print(f"El cliente se encuentra en categoria 5, obtiene un descuendo del 35% que corresponde a ${descuento}")
except Exception as err:
    print(f"Ocurrio un error, {err}")
