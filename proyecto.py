class Automata:
    def __init__(self, transiciones, finales):
        self.transiciones = transiciones
        self.estados_finales = estados_finales
        self.estados = {i: {} for i in range(max(max(t[:2]) for t in transiciones) + 1)} 
        self.estado_inicial = 0
        self.transicionesC(transiciones)

    def transicionesC(self,transiciones):
        for x,y,z in transiciones:
            self.estados[x][z] = y

    def tokenizacion(self, t):
    
        tokens = []
        estado = self.estado_inicial
        rompecadenas = ""
        token_final = None
        i = 0
        n = len(t)

        while i < n:
            x = t[i]

            #Comprobamos estados que rompen el automata para indicar fin de un token
            es_simbolo = x in "+-*/=()"
            if es_simbolo and rompecadenas and estado in self.estados_finales:
                tokens.append('id' if estado == loop_id else 'num')
                token_final = tokens[-1]
                buffer = ""
                estado = self.estado_inicial
            
            #Primero vemos signos u operadores por ser los primeros que deben salir
            if x in "+-":
                siguiente = t[i+1] if i+1 < n else ""
                es_signo = token_final in (None, 'op', 'par_abierto') and siguiente.isdigit()
                if es_signo:
                    tipo_var = x
                else:
                    tokens.append(x)
                    token_final = 'op'
                    i += 1
                    continue 
            
            #Luegos vemos operadores que no pueden ser signos
            elif x in "*/=":
                tokens.append(x)
                token_final = 'op'
                i += 1
                continue 

            #Ahora parentesis
            elif x in "()":
                tokens.append(x)
                token_final = 'par_abierto' if x == '(' else 'par_cerrado'
                i += 1
                continue 

            #Checa por letras y digitos
            elif x >= 'a' and x <= 'z' or x >= 'A' and x <= 'Z':
                tipo_var = 'char'
            elif x >= '0' and x <= '9':
                tipo_var = 'num' 
            
            #Aqui ya hacemos las transiciones 
            if tipo_var in self.estados[estado]:
                estado = self.estados[estado][tipo_var]
                rompecadenas += x
                i += 1
            else:
                rompecadenas = ""
                estado = self.estado_inicial

        if rompecadenas and estado in self.estados_finales:
            tokens.append('id' if estado == loop_id else 'num')                
        return tokens
    
##class Sintac:
    ##def Pruebas(self, tokens):

        ##i = 0
        ##n = len(tokens)

        ##while i < n:
            
            

transiciones = [
    #Par izq
    (0,3,'('),
    #Par der
    (0,8,')'),
    #Par der rompecadena
    (8,9,'+'),
    (8,9,'-'),
    #Op
    (0,1,'/'),
    (0,1,'='),
    (0,1,'*'),
    #num simbolo
    (0,6,'+'),
    (0,6,'-'),
    #num
    (0,5,'num'),
    (6,5,'num'),
    #loopnum
    (5,5,'num'),
    #num rompecadenas
    (5,7,'+'),
    (5,7,'-'),
    #id
    (0,2,'char'),
    #loopid
    (2,2,'char'),
    #id rompecadenas
    (2,4,'+'),
    (2,4,'-')
]

#Estados de loop
loop_id = 2

#Aceptacion
estados_finales = {1,2,3,4,5,6,7,8,9}

automata = Automata(transiciones, estados_finales)

#Inicio del programa
t = input("Ingresa texto: ")
t = t.replace(" ","")

tokens = automata.tokenizacion(t)

if not tokens:
    exit(1)

##prueba = Sintac(tokens)


print("Lexico: ", tokens)