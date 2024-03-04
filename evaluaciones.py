from pizza import Pizza

##### Requerimiento A ############

print(f"""Los atributos de la clase son: 
    precio: {Pizza.precio}
    tamaño: {Pizza.tamanio}\n""")

##### Requerimiento B ############

lista_salsas = ["salsa de tomate", "salsa bbq"]

print(f" Requerimiento B: {Pizza.casos_posibles('salsa de tomate', lista=lista_salsas)}\n")

##### Requerimiento C ############

pedido = Pizza(i_proteico= str, vegetal_1= str, vegetal_2= str, t_masa= str, pizza_valida=None)

print(pedido.realizar_pedido())

##### Requerimiento D ############

print(f"""Usted eligió los siguientes ingredientes:
    
    Proteína: {pedido.i_proteico}
    Vegetal 1: {pedido.vegetal_1}
    Vegetal 2: {pedido.vegetal_2}
    Tipo de masa: {pedido.t_masa}
    
    ¿Esta instancia es una pizza valida?: {pedido.pizza_valida}
    """)

# ##### Requerimiento E ############

print(Pizza.pizza_valida)

