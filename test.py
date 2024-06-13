def analizar_frase(frase):
    total_caracteres = len(frase)
    
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vocales = "aeiouAEIOU"
    numeros = "0123456789"
    especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
    
    total_consonantes = sum(1 for char in frase if char in consonantes)
    total_consonantes_mayuscula = sum(1 for char in frase if char in consonantes and char.isupper())
    total_consonantes_minuscula = sum(1 for char in frase if char in consonantes and char.islower())
    
    total_vocales = sum(1 for char in frase if char in vocales)
    total_vocales_mayuscula = sum(1 for char in frase if char in vocales and char.isupper())
    total_vocales_minuscula = sum(1 for char in frase if char in vocales and char.islower())
    
    total_numeros = sum(1 for char in frase if char in numeros)
    
    total_espacios = frase.count(' ')
    
    total_caracteres_especiales = sum(1 for char in frase if char in especiales)
    total_caracteres_especiales += total_espacios  
    
    total_palabras = len(frase.split())
    
    resultados = {
        'Total de caracteres': total_caracteres,
        'Total de consonantes': total_consonantes,
        'Total de consonantes mayúsculas': total_consonantes_mayuscula,
        'Total de consonantes minúsculas': total_consonantes_minuscula,
        'Total de vocales': total_vocales,
        'Total de vocales mayúsculas': total_vocales_mayuscula,
        'Total de vocales minúsculas': total_vocales_minuscula,
        'Total de números': total_numeros,
        'Total de caracteres especiales (incluyendo espacios)': total_caracteres_especiales,
        'Total de espacios': total_espacios,
        'Total de caracteres especiales (excluyendo espacios)': total_caracteres_especiales - total_espacios,
        'Total de palabras': total_palabras
    }
    

    caracteres_especificos = ['A', 'B', 'l', 't', '@', '1', 'v', 'a', 'L', 'T']
    resumen_caracteres = {char: frase.count(char) for char in caracteres_especificos}
    
    return resultados, resumen_caracteres

frase = input("Ingrese una frase: ")

resultados, resumen_caracteres = analizar_frase(frase)

print("\nResultados del análisis de la frase:")
for clave, valor in resultados.items():
    print(f"{clave}: {valor}")

print("\nResumen de caracteres específicos encontrados:")
for char, count in resumen_caracteres.items():
    print(f"Carácter encontrado: {char} = {count}")