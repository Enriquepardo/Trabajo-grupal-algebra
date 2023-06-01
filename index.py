import webbrowser

print('--> Lo primero que hay que hace es activar el entorno virtual de Python. Para ello, en la consola de Python, escribe lo siguiente:')
print('virtualenv venv')
print('--> Ahora lo segundo que tienes que hacer es instalar los requirements:')
print(r'pip install -r ".\requirements.txt" ')


def abrir_localhost():
    url = 'http://127.0.0.1:5500/templates/index.html'  # Cambia el número de puerto si es necesario
    webbrowser.open(url)


abrir_localhost()
