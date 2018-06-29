
# coding: utf-8

# In[1]:


#Importación de las clases que vamos a necesitar


# In[2]:


import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import copy


# In[3]:


#Estados Iniciales que vamos a utilizar, los numeros 7 indican las "paredes del tablero" 
#los numeros 3 indican las fichas que ya se han colocado,los numeros 0 las casillas vacias
#Los numeros 1 y 2 indican una ficha en movimiento, el 2 se utiliza para identificar el centro de la ficha.

#Explicación de los estados:

#Estado0: Tablero con fichas ya colocadas 

#Estado1: Tablero con fichas ya colocadas y una ficha en movimiento

#Estado2: Tablero con fichas colocadas y una ficha en movimiento a punto de llegar al final
#Tras realizar un ultimo "mover abajo se eliminaran las filas correspondientes y todos los 1 y 2 se harán 3

#Piezas que vamos a utilizar, en forma de matriz 5x5


# In[4]:


estadoVacio=   [[7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7]
            ]
estado0=   [[7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 7,7],
            [7,7,3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7]
            ]
   
estado1=   [[7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 7,7],
            [7,7,3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7]
            ]
   
estado2=    [[7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7],
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7],
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7],
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7],
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7],
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7], 
             [7, 7, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7, 7], 
             [7, 7, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 7, 7],
             [7, 7, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 7, 7],
             [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
             [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
            ]

estado3=   [[7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
            [7,7,3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 7,7],
            [7,7,3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7],
            [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7]
            ]
estadoConTrampa=   [[7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 7,7],
                    [7,7,0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 7,7],
                    [7,7,3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,7],
                    [7,7,3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 7,7],
                    [7,7,3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 7,7],
                    [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7],
                    [7,7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7]
                    ]
piezas=[
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,2,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],[
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,1,2,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],[
        [0,0,0,0,0],
        [0,0,0,1,0],
        [0,1,2,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],[
        [0,0,0,0,0],
        [0,0,1,1,0],
        [0,0,2,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],[
        [0,0,0,0,0],
        [0,0,1,1,0],
        [0,1,2,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],[
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,1,2,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],[
        [0,0,0,0,0],
        [0,1,1,0,0],
        [0,0,2,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
]


# In[5]:


#Acciones que vamos a utilizar


# In[6]:


class MoverIzquierda(probee.Acción):
    def __init__(self):
        nombre = 'muevo izquierda'
        super().__init__(nombre)
        
    def es_aplicable(self,estado):
        res=True
        for x, i in list(enumerate(estado)):
            for y, j in list(enumerate(i)):
                if j==2:
                    if(estado[x][y-1]==3 or estado[x][y-1]==7):
                        res=False
                if j==1:
                    if(estado[x][y-1]==3 or estado[x][y-1]==7):
                        res=False  
        return res
    def coste_de_aplicar(self,estado):    
        return 1             
        

    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        for y, i in list(enumerate(estado)):
            for x, j in list(enumerate(i)):
                if j==1:
                    nuevo_estado[y][x-1]=1
                    nuevo_estado[y][x]=0
                if j==2:
                    nuevo_estado[y][x-1]=2
                    nuevo_estado[y][x]=0
        return nuevo_estado  


# In[7]:


class MoverAbajo(probee.Acción):
    def __init__(self):
        nombre = 'muevo abajo'
        super().__init__(nombre)
        
    def es_aplicable(self,estado):
        return True
    
    
    def coste_de_aplicar(self,estado):    
        return 0
    
    def eliminar_filas_llenas(estado):
        sehacefija=False
        for x, i in list(enumerate(estado)):
            numerode3=0
            for y, j in list(enumerate(i)):
                if j==3:
                    numerode3=numerode3+1
            if numerode3==10:
                estado.pop(x)
                estado.insert(0,[7,7,0,0,0,0,0,0,0,0,0,0,7,7])
                
        return estado
    
    def se_hace_fija(estado):
        sehacefija=False
        for x, i in list(enumerate(estado)):
            for y, j in list(enumerate(i)):
                if j==2:
                    if(estado[x+1][y]==3 or estado[x+1][y]==7):
                        sehacefija=True
                if j==1:
                    if(estado[x+1][y]==3 or estado[x+1][y]==7):
                        sehacefija=True
                if sehacefija:
                    break
            if sehacefija:
                break
        return sehacefija
                
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        if MoverAbajo.se_hace_fija(estado):
            for y, i in reversed(list(enumerate(estado))):
                for x, j in list(enumerate(i)):
                    if j==1:
                        nuevo_estado[y][x]=3
                    if j==2:
                        nuevo_estado[y][x]=3
            nuevo_estado=MoverAbajo.eliminar_filas_llenas(nuevo_estado)
        else:
            for y, i in reversed(list(enumerate(estado))):
                for x, j in list(enumerate(i)):
                    if j==1:
                        nuevo_estado[y+1][x]=1
                        nuevo_estado[y][x]=0
                    if j==2:
                        nuevo_estado[y+1][x]=2
                        nuevo_estado[y][x]=0
        return nuevo_estado 


# In[8]:


class MoverDerecha(probee.Acción):
    def __init__(self):
        nombre = 'muevo derecha'
        super().__init__(nombre)
        
    def es_aplicable(self,estado):
        res=True
        for x, i in list(enumerate(estado)):
            for y, j in list(enumerate(i)):
                if j==2:
                    if(estado[x][y+1]==3 or estado[x][y+1]==7):
                        res=False
                if j==1:
                    if(estado[x][y+1]==3 or estado[x][y+1]==7):
                        res=False  
        return res
    def coste_de_aplicar(self,estado):    
        return 1           
        

    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        for y, i in list(enumerate(estado)):
            for x, j in reversed(list(enumerate(i))):
                if j==1:
                    nuevo_estado[y][x+1]=1
                    nuevo_estado[y][x]=0
                if j==2:
                    nuevo_estado[y][x+1]=2
                    nuevo_estado[y][x]=0
        return nuevo_estado


# In[9]:


class Rotar(probee.Acción):
    def __init__(self):
        nombre = 'Roto 90 grados'
        super().__init__(nombre)
        
    def es_de_cinco(estado):
        for x, i in list(enumerate(estado)):
            for y, j in list(enumerate(i)):
                if j==2:
                    return estado[x+2][y]==1 or estado[x-2][y]==1 or estado[x][y+2]==1 or estado[x][y-2]
        
    def coste_de_aplicar(self,estado):    
        return 1
    
    def es_aplicable(self,estado):
        for y, i in list(enumerate(estado)):
            for x, j in list(enumerate(i)):
                if j==2:
                    if estado[y][x+1]==1:
                        if estado[y-1][x]==3 or estado[y-1][x]==7:
                            return False
                    if estado[y][x-1]==1:
                        if estado[y+1][x]==3 or estado[y+1][x]==7:
                            return False
                    if estado[y+1][x]==1:
                        if estado[y][x+1]==3 or estado[y][x+1]==7:
                            return False
                    if estado[y-1][x]==1:
                         if estado[y][x-1]==3 or estado[y][x-1]==7:
                            return False
                    if estado[y-1][x-1]==1:
                         if estado[y+1][x]==3 or estado[y+1][x]==7:
                            return False
                    if estado[y+1][x-1]==1:
                        if estado[y+1][x+1]==3 or estado[y+1][x+1]==7:
                            return False
                    if estado[y+1][x+1]==1:
                        if estado[y-1][x+1]==3 or estado[y-1][x+1]==7:
                            return False
                    if estado[y-1][x+1]==1:
                        if estado[y-1][x-1]==3 or estado[y-1][x-1]==7:
                            return False                    
                    if Rotar.es_de_cinco(estado):
                        if estado[y][x+2]==1:
                            if estado[y-2][x]==3 or estado[y-2][x]==7:
                                return False     
                        if estado[y][x-2]==1:
                             if estado[y+2][x]==3 or estado[y+2][x]==7:
                                return False     
                        if estado[y+2][x]==1:
                            if estado[y][x+2]==3 or estado[y][x+2]==7:
                                return False     
                        if estado[y-2][x]==1:
                            if estado[y][x-2]==3 or estado[y][x-2]==7:
                                return False     
        return True                
        

    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        for y, i in list(enumerate(estado)):
            for x, j in list(enumerate(i)):
                if j==2:
                    if estado[y-1][x-1]==1:
                        nuevo_estado[y-1][x-1]=0
                    if estado[y+1][x-1]==1:
                        nuevo_estado[y+1][x-1]=0
                    if estado[y+1][x+1]==1:
                        nuevo_estado[y+1][x+1]=0
                    if estado[y-1][x+1]==1:
                        nuevo_estado[y-1][x+1]=0  
                    if estado[y][x+1]==1:
                        nuevo_estado[y][x+1]=0
                    if estado[y][x-1]==1:
                        nuevo_estado[y][x-1]=0
                    if estado[y+1][x]==1:
                        nuevo_estado[y+1][x]=0
                    if estado[y-1][x]==1:
                        nuevo_estado[y-1][x]=0
                    if estado[y][x+1]==1:
                        nuevo_estado[y-1][x]=1
                    if estado[y][x-1]==1:
                        nuevo_estado[y+1][x]=1
                    if estado[y+1][x]==1:
                        nuevo_estado[y][x+1]=1
                    if estado[y-1][x]==1:
                        nuevo_estado[y][x-1]=1
                    if estado[y-1][x-1]==1:
                        nuevo_estado[y+1][x-1]=1
                    if estado[y+1][x-1]==1:
                        nuevo_estado[y+1][x+1]=1
                    if estado[y+1][x+1]==1:
                        nuevo_estado[y-1][x+1]=1
                    if estado[y-1][x+1]==1:
                        nuevo_estado[y-1][x-1]=1                       
                    if Rotar.es_de_cinco(estado):
                        if estado[y][x+2]==1:
                            nuevo_estado[y][x+2]=0
                        if estado[y][x-2]==1:
                            nuevo_estado[y][x-2]=0
                        if estado[y+2][x]==1:
                            nuevo_estado[y+2][x]=0
                        if estado[y-2][x]==1:
                            nuevo_estado[y-2][x]=0

                        if estado[y][x+2]==1:
                            nuevo_estado[y-2][x]=1
                        if estado[y][x-2]==1:
                            nuevo_estado[y+2][x]=1
                        if estado[y+2][x]==1:
                            nuevo_estado[y][x+2]=1
                        if estado[y-2][x]==1:
                            nuevo_estado[y][x-2]=1      
        return nuevo_estado   
                


# In[10]:


class RotarInverso(probee.Acción):
    def __init__(self):
        nombre = 'Roto -90 grados'
        super().__init__(nombre)
        
    def es_de_cinco(estado):
        for x, i in list(enumerate(estado)):
            for y, j in list(enumerate(i)):
                if j==2:
                    return estado[x+2][y]==1 or estado[x-2][y]==1 or estado[x][y+2]==1 or estado[x][y-2]
        
    def coste_de_aplicar(self,estado):    
        return 1
    
    def es_aplicable(self,estado):
        for y, i in list(enumerate(estado)):
            for x, j in list(enumerate(i)):
                if j==2:
                    if estado[y][x+1]==1:
                        if estado[y+1][x]==3 or estado[y+1][x]==7:
                            return False
                    if estado[y][x-1]==1:
                        if estado[y-1][x]==3 or estado[y-1][x]==7:
                            return False
                    if estado[y+1][x]==1:
                        if estado[y][x-1]==3 or estado[y][x-1]==7:
                            return False
                    if estado[y-1][x]==1:
                         if estado[y][x+1]==3 or estado[y][x+1]==7:
                            return False
                    if estado[y-1][x-1]==1:
                         if estado[y-1][x+1]==3 or estado[y-1][x+1]==7:
                            return False
                    if estado[y+1][x-1]==1:
                        if estado[y-1][x-1]==3 or estado[y-1][x-1]==7:
                            return False
                    if estado[y+1][x+1]==1:
                        if estado[y+1][x-1]==3 or estado[y+1][x-1]==7:
                            return False
                    if estado[y-1][x+1]==1:
                        if estado[y+1][x+1]==3 or estado[y+1][x+1]==7:
                            return False                    
                    if Rotar.es_de_cinco(estado):
                        if estado[y][x+2]==1:
                            if estado[y+2][x]==3 or estado[y+2][x]==7:
                                return False     
                        if estado[y][x-2]==1:
                             if estado[y-2][x]==3 or estado[y-2][x]==7:
                                return False     
                        if estado[y+2][x]==1:
                            if estado[y][x-2]==3 or estado[y][x-2]==7:
                                return False     
                        if estado[y-2][x]==1:
                            if estado[y][x+2]==3 or estado[y][x+2]==7:
                                return False     
        return True                
        

    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        for y, i in list(enumerate(estado)):
            for x, j in list(enumerate(i)):
                if j==2:
                    if estado[y-1][x-1]==1:
                        nuevo_estado[y-1][x-1]=0
                    if estado[y+1][x-1]==1:
                        nuevo_estado[y+1][x-1]=0
                    if estado[y+1][x+1]==1:
                        nuevo_estado[y+1][x+1]=0
                    if estado[y-1][x+1]==1:
                        nuevo_estado[y-1][x+1]=0  
                    if estado[y][x+1]==1:
                        nuevo_estado[y][x+1]=0
                    if estado[y][x-1]==1:
                        nuevo_estado[y][x-1]=0
                    if estado[y+1][x]==1:
                        nuevo_estado[y+1][x]=0
                    if estado[y-1][x]==1:
                        nuevo_estado[y-1][x]=0
                    if estado[y][x+1]==1:
                        nuevo_estado[y+1][x]=1
                    if estado[y][x-1]==1:
                        nuevo_estado[y-1][x]=1
                    if estado[y+1][x]==1:
                        nuevo_estado[y][x-1]=1
                    if estado[y-1][x]==1:
                        nuevo_estado[y][x+1]=1
                    if estado[y-1][x-1]==1:
                        nuevo_estado[y-1][x+1]=1
                    if estado[y+1][x-1]==1:
                        nuevo_estado[y-1][x-1]=1
                    if estado[y+1][x+1]==1:
                        nuevo_estado[y+1][x-1]=1
                    if estado[y-1][x+1]==1:
                        nuevo_estado[y+1][x+1]=1                       
                    if Rotar.es_de_cinco(estado):
                        if estado[y][x+2]==1:
                            nuevo_estado[y][x+2]=0
                        if estado[y][x-2]==1:
                            nuevo_estado[y][x-2]=0
                        if estado[y+2][x]==1:
                            nuevo_estado[y+2][x]=0
                        if estado[y-2][x]==1:
                            nuevo_estado[y-2][x]=0

                        if estado[y][x+2]==1:
                            nuevo_estado[y+2][x]=1
                        if estado[y][x-2]==1:
                            nuevo_estado[y-2][x]=1
                        if estado[y+2][x]==1:
                            nuevo_estado[y][x-2]=1
                        if estado[y-2][x]==1:
                            nuevo_estado[y][x+2]=1      
        return nuevo_estado   


# In[11]:


#Funcion que utilizaremos para imprimir el tablero y que sea mas visual el resultado

from IPython.display import HTML, display
def printBonito(estado1):
    display(HTML(
        '<table><tr>{}</tr></table>'.format(
            '</tr><tr>'.join(
                '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in estado1)
            )))


# In[12]:


#ejemplo del tablero tras realizar un movimiento de moverAbajo al estado1
printBonito(MoverAbajo.aplicar(estado1,estado1))


# In[13]:


#Ejemplo de rotaciones -90 grados
estadoRotado=estado1
for i in range (0,5):
    printBonito(estadoRotado)
    estadoRotado=RotarInverso.aplicar(estadoRotado,estadoRotado)



# In[14]:


#Ejemplo de rotaciones 90 grados
estadoRotado=estado1
for i in range (0,5):
    printBonito(estadoRotado)
    estadoRotado=Rotar.aplicar(estadoRotado,estadoRotado)


# In[15]:


#Ejemplo de Rotacion Ficha "larga"
estadoRotado=estado3
for i in range (0,5):
    printBonito(estadoRotado)
    estadoRotado=RotarInverso.aplicar(estadoRotado,estadoRotado)


# In[16]:


#Inicializamos el problema de espacio de estados


# In[17]:


acciones =[MoverAbajo(),MoverIzquierda(),MoverDerecha(),Rotar(),RotarInverso()]
estado_inicial = estado1
estado_final = estado2
tetris=probee.ProblemaEspacioEstados(acciones,estado_inicial,[estado_final])


# In[18]:


#Resultado de una busqueda en Anchura
b_anchura = búsqee.BúsquedaEnAnchura(detallado=False)
b_anchura.buscar(tetris)


# In[19]:


#Resultado de una busqueda del tipo óptima
b_Optima = búsqee.BúsquedaÓptima(detallado=False)
b_Optima.buscar(tetris)


# In[20]:


# Como heurística para el A* ponemos que la ficha este más cerca del punto objetivo, calculamos el centro actual de la ficha y lo comparamos
# con el final

def heuristica(nodo):
    estado = nodo.estado
    hayEstado=0
    for x, i in list(enumerate(estado)):
        for y, j in list(enumerate(i)):
            if j==2:
                xFicha=x
                yFicha=y
                hayEstado=1
    for x2, i in list(enumerate(estado_final)):
        for y2, j in list(enumerate(i)):
            if j==2:
                xFinal=x2
                yFinal=y2
                hayEstado=hayEstado+1
    #en el caso de que la ficha se haya hecho final sin llegar al estado final, consideramos 1000 el coste
    puntuacion=1000
    if hayEstado==2:
        puntuacion= abs(xFicha-xFinal)+abs(yFicha-yFinal)
    return puntuacion
    


# In[21]:


#Resultado de una busqueda A*
b_Estrella = búsqee.BúsquedaAEstrella(heuristica,detallado=False)
b_Estrella.buscar(tetris)


# In[22]:


#Fase 2


# In[23]:


#Para averiguar el estado final óptimo utilizamos la acción "prueba a poner" que dado una pieza concreta una X y una Y permite
#principalmente calcular la puntuación de esa posicion y ver si es posible colocar ahi.

class PruebaPoner(probee.Acción):
    def __init__(self,x,y,pieza):
        nombre=[x+2,y+2]
        super().__init__(nombre)
        self.x = x
        self.y = y
        self.pieza=pieza
      
      
        
        
    def es_aplicable(self,estado):
        ans = PruebaPoner.comprobar(self,estado,self.pieza,self.x,self.y)
        return ans 
    
    #El coste de aplicar que sera menor si elimina una fila o cuanto mas abajo en el tablero se encuentre,si tapa un hueco sera penalizado
    def coste_de_aplicar(self,estado):
        res=10000
        valor_fila=0
        filaEliminada=0
        tapandoHueco=0
        for x, i in list(enumerate(estado)):
            numerodefichas=0
            for y, j in list(enumerate(i)):
                if j==1 or j==2:
                    valor_fila=valor_fila+x
                    numerodefichas=numerodefichas+1
                    if estado[x+1][y] ==0:
                        tapandoHueco=tapandoHueco+1
                if j==3:
                    numerodefichas=numerodefichas+1
            #lleno una fila
            if numerodefichas==10:
                filaEliminada=filaEliminada+1
           
        return res-valor_fila-(filaEliminada*10000)+(tapandoHueco*1000)
    
    def comprobar(self, estado, pieza, x, y):
        res=False
        for a,j in reversed(list(enumerate(pieza))):
            for b,k in list(enumerate(pieza)):
                if pieza[a][b]==1 or pieza[a][b]==2:
                    if estado[x+a][y+b]==3 or estado[x+a][y+b]==7:           #Comprobamos si choca con una pieza colocada en el tablero
                        return False
                    if estado[x+a+1][y+b]==3 or estado[x+a+1][y+b]==7:       #Comprobamos si la pieza está asentada sobre otra
                        res= True
                   
        return res
                
    def aplicar(self,estado):
        nuevo_estado = copy.deepcopy(estado)
        for a,j in reversed(list(enumerate(self.pieza))):
            for b,k in list(enumerate(self.pieza)):  #Adjudicamos valor a la casilla del nuevo estado
                if self.pieza[a][b]==1 :
                    nuevo_estado[self.x+a][self.y+b]=1
                if self.pieza[a][b]==2:
                     nuevo_estado[self.x+a][self.y+b]=2
     
        return nuevo_estado


# In[24]:


#Este ejemplo muestra todas las posibilidades dada una pieza y un tablero, en este caso el estado0 y escoje la mejor 
#mostrando por pantalla el resultado escogido, que es el de menor coste.


# In[25]:



pieza=[[0,0,0,0,0],[0,0,1,0,0],[0,1,2,1,0],[0,0,0,0,0],[0,0,0,0,0]]
pieza2=Rotar.aplicar(pieza,pieza)
pieza3=Rotar.aplicar(pieza2,pieza2)
pieza4=Rotar.aplicar(pieza3,pieza3)
piezasF=[pieza,pieza2,pieza3,pieza4]
acciones = [PruebaPoner(i, j,p) for i in range(0, 22) for j in range(0, 11) for p in piezasF]

estado_inicial = estado0
estados_finales=[]
posiblesSoluciones=set()
print("Resultado Escogido:")
for x in acciones:
    if(x.es_aplicable(estado_inicial)):
        estado_inicial = estado0
        estados_finales.append(x.aplicar(estado_inicial)) 
        
        listaacciones=[x]
             
        
        
      
        

estado_inicial = estado0
tetrih = probee.ProblemaEspacioEstados(
    acciones, estado_inicial,estados_finales )
    
mejor=100000000
for z in estados_finales:
    if(PruebaPoner.coste_de_aplicar(z,z)<mejor):
        mejor=PruebaPoner.coste_de_aplicar(z,z)
        solucion=z
        

printBonito(z)
print("coste del resutado escogido:")
print(PruebaPoner.coste_de_aplicar(z,z))




# In[26]:


#En forma de funcion recibiendo un estado y una pieza devuelve el estado final
def CalculoEstadoFinal(estado,pieza):
    pieza=pieza
    pieza2=Rotar.aplicar(pieza,pieza)
    pieza3=Rotar.aplicar(pieza2,pieza2)
    pieza4=Rotar.aplicar(pieza3,pieza3)
    piezasFF=[pieza,pieza2,pieza3,pieza4]
    acciones = [PruebaPoner(i, j,p) for i in range(0, 21) for j in range(0, 11) for p in piezasFF]
    estado_inicial = estado
    estados_finales=[]
    for x in acciones:
        if(x.es_aplicable(estado_inicial)):   
            estados_finales.append(x.aplicar(estado_inicial))
    mejor=10000000
    for z in estados_finales:
        if(PruebaPoner.coste_de_aplicar(z,z)<mejor):
            mejor=PruebaPoner.coste_de_aplicar(z,z)
            solucion=z
    return(z)




# In[27]:


#Ejemplo de su Uso en el estado0 que tiene un hueco claro para la ficha[5]
CalculoEstadoFinal(estado0,piezas[5])


# In[28]:


#En forma de funcion recibiendo un estado y una pieza devuelve una lista de estados ordenada de mejor a peor
def valora(estado):
    return PruebaPoner.coste_de_aplicar(estado,estado)

def CalculoEstadosFinalesOrdenados(estado,pieza):
    pieza=pieza
    pieza2=Rotar.aplicar(pieza,pieza)
    pieza3=Rotar.aplicar(pieza2,pieza2)
    pieza4=Rotar.aplicar(pieza3,pieza3)
    piezasFFF=[pieza,pieza2,pieza3,pieza4]
    acciones = [PruebaPoner(i, j,p) for i in range(0, 21) for j in range(0, 11) for p in piezasFFF]
    estado_inicial = estado
    estados_finales=[]
    for x in acciones:
        estado_inicial = estado     
        if(x.es_aplicable(estado_inicial)):
            estados_finales.append(x.aplicar(estado_inicial))
    return( sorted(estados_finales, key=valora))




# In[29]:


#Ejemplo de su Uso, devuelve una lista de los estados de mejor a peor
CalculoEstadosFinalesOrdenados(estado0,piezas[5])


# In[30]:


#Apartado 3


# In[31]:


#dado un estado y una ficha, la inserta en el tablero


# In[32]:



def pon_ficha_nueva(estado,pieza):
        x=0
        y=4
        nuevo_estado = copy.deepcopy(estado)
        for a,j in reversed(list(enumerate(pieza))):
            for b,k in list(enumerate(pieza)):
                if pieza[a][b]==1 or pieza[a][b]==2:
                    nuevo_estado[x+a][y+b]=pieza[a][b]                                     #Adjudicamos valor a la casilla del nuevo estado
        return nuevo_estado


# In[33]:


#Dado un estado inicial, y una pieza te calcula los movimientos para llegar al estado mas óptimo, en el caso de no encontrarlo 
#va probando los siguientes estados hasta llegar a uno


# In[34]:


#Dado un estado y una pieza (y un numero de intentos, inicializar a 0) devuelve un par de los movimientos que dar y el intento en el cual se consiguio

def CalculoMovimientos(estado0,pieza,intentos):
   
   
    if(intentos<len(CalculoEstadosFinalesOrdenados(estado0,pieza))-1):
        try:
            acciones =[MoverAbajo(),MoverIzquierda(),MoverDerecha(),Rotar(),RotarInverso()]
            estado_inicial = pon_ficha_nueva(estado0,pieza)
            estados_finales = CalculoEstadosFinalesOrdenados(estado0,pieza)
            estado_final = estados_finales[intentos]
            estadosFinales=[estado_final]
            tetris3=probee.ProblemaEspacioEstados(acciones,estado_inicial,estadosFinales)
            b_Estrella = búsqee.BúsquedaAEstrella(heuristica,detallado=False)
            res= b_Estrella.buscar(tetris3)
            return res,intentos
            
        except:
            print("no encontrada solucion, probando de nuevo con otro estado intento numero:"+ str(intentos+1)+ "de" + str(len(CalculoEstadosFinalesOrdenados(estado0,pieza))))
            return CalculoMovimientos(estado0,pieza,intentos+1)      

    else:
        print("No Encontrada Solucion")
        return 777
       


# In[35]:


#ejemplo en un tablero normal


# In[36]:


CalculoMovimientos(estado0,piezas[2],0)


# In[37]:


#Ejemplo en un tablero creado con malicia, los primeros 29 posibles estados son imposibles de alcanzar


# In[38]:


res=CalculoMovimientos(estadoConTrampa,piezas[2],0)
print(res)


# In[39]:


#Dado un estado inicial vacio, inserta la ficha 5, calcula sus movimientos, la mueve al objetivo e inserta la ficha 0


# In[40]:


printBonito(estado0)
print("")
printBonito(pon_ficha_nueva(estado0,piezas[5]))
print(CalculoMovimientos(estado0,piezas[5],0))
nuevoEstado=CalculoEstadoFinal(estado0,piezas[5])
printBonito(nuevoEstado)
nuevoEstado=MoverAbajo.aplicar(nuevoEstado,nuevoEstado)
printBonito(nuevoEstado)
nuevoEstadoSinFicha=nuevoEstado
printBonito(pon_ficha_nueva(nuevoEstado,piezas[0]))
print(CalculoMovimientos(nuevoEstadoSinFicha,piezas[0],0))


# In[ ]:


def TetrisApartado3Visual(estado,listaFichas):
    nuevoEstado=estado
    for i in listaFichas:
        printBonito(pon_ficha_nueva(nuevoEstado,i))
        print(CalculoMovimientos(nuevoEstado,i,0))
        nuevoEstado=CalculoEstadoFinal(nuevoEstado,i)
        printBonito(nuevoEstado)
        nuevoEstado=MoverAbajo.aplicar(nuevoEstado,nuevoEstado)
        printBonito(nuevoEstado)
        


# In[ ]:


#Muestra paso por paso lo que va pasando, con 4 piezas
TetrisApartado3Visual(estado0,[piezas[5],piezas[0],piezas[3],piezas[4],piezas[2]])


# In[ ]:


#muestra solo los estados finales y las apariciones de fichas, contempla que las soluciones no sean posibles y prueba con 
#las siguientes alternativas, si se queda sin soluciones posibles da por terminada la partida
def TetrisLargoConFin(estado,listaFichas):
    nuevoEstado=estado
    fichaNumero=0
    for i in listaFichas:
        fichaNumero=fichaNumero+1
        print("ficha numero "+ str(fichaNumero))
        printBonito(i)
        pon_ficha_nueva(nuevoEstado,i)
        res=CalculoMovimientos(nuevoEstado,i,0)
        if(res==777):
            return ("fin de la partida")
        nuevoEstados=CalculoEstadosFinalesOrdenados(nuevoEstado,i)
        nuevoEstado=nuevoEstados[res[1]]
        nuevoEstado=MoverAbajo.aplicar(nuevoEstado,nuevoEstado)
        printBonito(nuevoEstado)
        


# In[ ]:


fichas=[piezas[5]]

#generamos una lista de muchas fichas 
for repeticiones in range (50):
    for i in range (0,6): 
        fichas.append(piezas[i])
TetrisLargoConFin(estado0,fichas)
print("fichas acabadas o partida perdida")
#Jugara una partida hasta que no pueda continuar o acabe la lista de fichas


# In[ ]:


#esta version simula la funcion anterior sin los print(ya que reducen el rendimiento), para ver si en algun momento pierde la partida, dandole una lista de fichas enorme

def TetrisLargoOptimizado(estado,listaFichas):
    nuevoEstado=estado
    fichaNumero=0
    for i in listaFichas:
        fichaNumero=fichaNumero+1
        print("iteracion numero "+ str(fichaNumero)+ " Conseguida")
        pon_ficha_nueva(nuevoEstado,i)
        res=CalculoMovimientos(nuevoEstado,i,0)
        if(res==777):
            return ("fin de la partida")
        nuevoEstados=CalculoEstadosFinalesOrdenados(nuevoEstado,i)
        nuevoEstado=nuevoEstados[res[1]]
        nuevoEstado=MoverAbajo.aplicar(nuevoEstado,nuevoEstado)   

fichas=[piezas[5]]

#generamos una lista de muchas fichas 
for repeticiones in range (5000):
    for i in range (0,6): 
        fichas.append(piezas[i])


# In[ ]:


#Con una lista de fichas No aleatoria y el estado inicial 0, llega a 1510 iteraciones
TetrisLargoOptimizado(estado0,fichas)


# In[ ]:


#Con la lista de fichas aleatorias y el tablero vacio


# In[46]:


#esta version simula la funcion anterior sin los print(ya que reducen el rendimiento), para ver si en algun momento pierde la partida, dandole una lista de fichas enorme
import random
def TetrisLargoAleatorio(estado,listaFichas):
    nuevoEstado=estado
    fichaNumero=0
    for i in listaFichas:
        print("ficha aleatoria:")
        printBonito(i)
        fichaNumero=fichaNumero+1
        print("iteracion numero "+ str(fichaNumero)+ " Conseguida")
        pon_ficha_nueva(nuevoEstado,i)
        res=CalculoMovimientos(nuevoEstado,i,0)
        if(res==777):
            return ("fin de la partida")
        nuevoEstados=CalculoEstadosFinalesOrdenados(nuevoEstado,i)
        nuevoEstado=nuevoEstados[res[1]]
        nuevoEstado=MoverAbajo.aplicar(nuevoEstado,nuevoEstado)   

fichas=[piezas[5]]

#generamos una lista de muchas fichas 
for repeticiones in range (5000):
    pieza=piezas[random.randint(0, 6)]
    fichas.append(pieza)


# In[48]:


TetrisLargoAleatorio(estadoVacio,fichas)

