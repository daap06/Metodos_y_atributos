from ingredientes import vegetales, masa, proteinas

class Pizza:
    precio = 10000
    tamanio = "Familiar"
    
    
    def __init__(self,i_proteico, vegetal_1, vegetal_2, t_masa, pizza_valida) -> None:
        self.i_proteico = i_proteico
        self.vegetal_1 = vegetal_1
        self.vegetal_2 = vegetal_2
        self.t_masa = t_masa
        self.pizza_valida = pizza_valida
        
        
    @staticmethod
    def casos_posibles(texto,lista: list):
        if texto in lista:
            # print("Lo logre")
            return True
        # print("Noooo")
        return False
    
    
    def realizar_pedido(self):
        self.i_proteico = input("Por favor ingrese el tipo de proteína: ")
        self.vegetal_1 =  input("Por favor ingrese el primer ingrediente vegetal: ")
        self.vegetal_2 =  input("Por favor ingrese el segundo ingrediente vegetal: ")
        self.t_masa =  input("Por favor ingrese el tipo de masa: ")
        
        v_1 = Pizza.casos_posibles(texto=self.i_proteico, lista=proteinas)
        v_2 = Pizza.casos_posibles(texto=self.vegetal_1, lista=vegetales)
        v_3 = Pizza.casos_posibles(texto=self.vegetal_2, lista=vegetales)
        v_4 = Pizza.casos_posibles(texto=self.t_masa, lista=masa)

        lista_respuesta = [v_1, v_2, v_3, v_4]

        if False in lista_respuesta:
            self.pizza_valida = False
            print("Existe al menos un false")
        else:
            self.pizza_valida = True
            print("Todo es True")
            
