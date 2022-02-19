#Ejercicio
 #Solicitar un verbo en infinitivo ar er ir
 #Tomar ese verbo y conjugarlo con las personas yo, 

'''
Yo
Tú
Él
Ella
Usted
Nosotros
'''
#Funcion para saber la cantidad de letras del string len()
verbo = input()
print(verbo)

len(verbo)

letrasVerbo = verbo[len(verbo)-1]
letrasVerbo2 = verbo[len(verbo)-2]


print(letrasVerbo)
print(letrasVerbo2)

letrasFinales = letrasVerbo2 + letrasVerbo

print(letrasFinales)

verboQuitado = verbo.replace(letrasFinales, '')

print(verboQuitado)


pronombres = {
    'Yo' : {
        'ar' : 'o',
        'er' : 'o',
        'ir' : 'o'
    },
    'Tú' : {
        'ar' : 'es',
        'er' : 'es',
        'ir' : 'es'
    },
    'Él' : {
    'ar' : 'a',
    'er' : 'a',
    'ir' : 'a'
    },
    'Élla' : {
    'ar' : 'o',
    'er' : 'o',
    'ir' : 'o'
    },
    'Nosotros' : {
    'ar' : 'o',
    'er' : 'o',
    'ir' : 'o'
    },
}

for recorre in pronombres:
    print(pronombres, verboQuitado , pronombres[letrasFinales])


print("Cambio GITHUB")