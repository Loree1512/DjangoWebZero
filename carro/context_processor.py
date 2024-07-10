def importe_total_carro(request):
    if 'carro' not in request.session:
        request.session['carro'] = {}

    total = sum(value['precio'] * value['cantidad'] for value in request.session['carro'].values())
    return {'importe_total_carro': total}