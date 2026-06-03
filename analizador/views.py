
from django.shortcuts import render

def analizador_view(request):
    contexto = {}
    
   
    if request.method == 'POST':
        entrada_usuario = request.POST.get('numeros', '')
        
     
        if entrada_usuario.strip():
            try:

                lista_original = []
      
                pedazos_de_texto = entrada_usuario.split(',')
               
                for pedazo in pedazos_de_texto:
                    texto_limpio = pedazo.strip()
                    texto_sin_signo = texto_limpio.replace('-', '', 1)
                    
                   
                    if texto_sin_signo.isdigit() and texto_limpio != '-':
                        numero = int(texto_limpio)
                        lista_original.append(numero)

                if lista_original:
                    suma_total = sum(lista_original)
                    promedio = suma_total / len(lista_original)
                    numero_mayor = max(lista_original)
                    numero_menor = min(lista_original)
                    

                    pares = list(filter(lambda n: n % 2 == 0, lista_original))
                    impares = list(filter(lambda n: n % 2 != 0, lista_original))
                    
             
                    al_cuadrado = list(map(lambda n: n ** 2, lista_original))
                    
         
                    mayores_que_promedio = list(filter(lambda n: n > promedio, lista_original))

          
                    contexto = {
                        'entrada_usuario': entrada_usuario,
                        'lista_original': lista_original,
                        'resultados': {
                            'suma_total': suma_total,
                            'promedio': round(promedio, 2),
                            'numero_mayor': numero_mayor,
                            'numero_menor': numero_menor,
                            'pares': pares,
                            'impares': impares,
                            'al_cuadrado': al_cuadrado,
                            'mayores_que_promedio': mayores_que_promedio,
                        }
                    }
                else:
                    contexto['error'] = "Por favor, ingresa números válidos separados por comas."
                    
            except ValueError:
                contexto['error'] = "Asegúrate de ingresar únicamente números enteros."
        else:
            contexto['error'] = "El campo no puede estar vacío."

   
    return render(request, 'analizador/index.html', contexto)