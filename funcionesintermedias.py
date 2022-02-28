#1 Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#--------------------
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]["last_name"]="Bryant"
print(estudiantes)
# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes["fútbol"][0]="Andrés"
print(directorio_deportes)
# Cambia el valor 20 en z a 30.
z[0]["y"]=30
print(z)

#2 Iterar a través de una lista de diccionarios

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in range (len(some_list)):
        rex=""
        for k in some_list[x]:
            rex+=f" {k} - {some_list[x][k]},"
        print(rex)

iterateDictionary(estudiantes)

#3 Obtener valores de una lista de diccionarios

def iterateDictionary2(key_name, some_list):
    for x in range (len(some_list)):
        for k in some_list[x]:
            if k==key_name:
                print(some_list[x][key_name])
        
iterateDictionary2("last_name", estudiantes)

#4Iterar a través de un diccionarios con valores de lista

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dic):
    for k in some_dic:
        print(len(some_dic[k]),k.upper())
        for y in some_dic[k]:
            print(y)
printInfo(dojo)