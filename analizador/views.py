# analizador/views.py
from django.shortcuts import render

def analizador_view(request):
    contexto = {}
    
    # 1. Si el usuario presionó el botón "Calcular"
    if request.method == 'POST':
        entrada_usuario = request.POST.get('numeros', '')
        
        # Validamos que no esté vacío
        if entrada_usuario.strip():
            try:
                # LISTA BASE DONDE ENTRARÁN LOS NÚMEROS LIMPIOS
                lista_original = []
                
                # Separamos el texto largo por cada coma
                pedazos_de_texto = entrada_usuario.split(',')
                
                # BUCLE PARA LIMPIAR TEXTO Y VALIDAR SEGURIDAD
                for pedazo in pedazos_de_texto:
                    texto_limpio = pedazo.strip()
                    texto_sin_signo = texto_limpio.replace('-', '', 1)
                    
                    # Filtro de seguridad (si es un número entero válido)
                    if texto_sin_signo.isdigit() and texto_limpio != '-':
                        numero = int(texto_limpio)
                        lista_original.append(numero)

                # 2. CÁLCULOS AVANZADOS CON PROGRAMACIÓN FUNCIONAL (Solo si hay números)
                if lista_original:
                    suma_total = sum(lista_original)
                    promedio = suma_total / len(lista_original)
                    numero_mayor = max(lista_original)
                    numero_menor = min(lista_original)
                    
                    # --- AQUÍ ENTRA LA MAGIA FUNCIONAL ---
                    
                    # A. PARES E IMPARES: Filtramos la lista original con una condición lambda
                    pares = list(filter(lambda n: n % 2 == 0, lista_original))
                    impares = list(filter(lambda n: n % 2 != 0, lista_original))
                    
                    # B. AL CUADRADO: Mapeamos o transformamos cada número elevándolo al cuadrado
                    al_cuadrado = list(map(lambda n: n ** 2, lista_original))
                    
                    # C. MAYORES QUE EL PROMEDIO: Filtramos los que superan el promedio
                    mayores_que_promedio = list(filter(lambda n: n > promedio, lista_original))

                    # 3. ENVIAMOS TODOS LOS PLATOS LISTOS AL HTML
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

    # 4. Mostramos la página en la pantalla
    return render(request, 'analizador/index.html', contexto)