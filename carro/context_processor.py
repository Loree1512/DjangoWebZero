def importe_total_carro(request):
    total = 0
    carro = request.session.get('carro', {})  # Obtener 'carro' de la sesión o un diccionario vacío si no existe
    for key, value in carro.items():
        total += value['precio'] * value['cantidad']
    return {'importe_total_carro': total}