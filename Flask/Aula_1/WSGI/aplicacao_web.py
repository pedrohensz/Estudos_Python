from wsgiref.simple_server import make_server

def aplicacao(environ, start_response):
    produtos = [
        {'nome':'Notebook', 'valor': 7499},
        {'nome':'Mouse', 'valor': 125.99},
        {'nome':'Teclado', 'valor': 450},
        {'nome':'Monitor', 'valor': 2100}                       
    ]

    linhas_html = ''
    for produto in produtos:
        linhas_html += f'<li>{produto['nome']} - R${produto['valor']}</li>'
    start_response('200 Ok',[('Content-type', 'text/html;charset=utf-8')] )
    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()
        

    html_final = html.replace('{{produtos}}', linhas_html)
    return [html_final.encode("Utf-8")]
    
make_server("",5000, aplicacao).serve_forever()