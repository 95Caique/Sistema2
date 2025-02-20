import requests
import json
import traceback
from django.shortcuts import render
from django import forms
from .importacao_servidor import ClienteServidorAPI

class ClienteServidorAPI:
    def __init__(self, base_url: str, auth_token: str = None):
        self.base_url = base_url.rstrip('/')
        self.headers = {'Content-Type': 'application/json'}
        if auth_token:
            self.headers['Authorization'] = f'Bearer {auth_token}'

    def buscar_servidor(self, identificador: str):
        urls_para_tentar = [
            f"{self.base_url}/api/servidores/",
            f"{self.base_url}/api/api/servidores/",
            f"{self.base_url}/servidores/",
            f"{self.base_url}/api/",
        ]

        for url in urls_para_tentar:
            try:
                response = requests.get(url, headers=self.headers)
                if response.status_code == 200:
                    servidores = response.json()
                    for servidor in servidores:
                        if servidor['cpf'] == identificador or servidor['matricula'] == identificador:
                            return servidor
            except requests.RequestException:
                traceback.print_exc()

        return None


class ImportarServidorForm(forms.Form):
    identificador = forms.CharField(label="CPF ou Matrícula", max_length=20)


from django.shortcuts import render
from django.contrib import messages
from importador.importacao_servidor import ClienteServidorAPI

def importar_servidor_view(request):
    servidor = None
    error = None

    if request.method == "POST":
        identificador = request.POST.get("identificador")

        if identificador:
            api_client = ClienteServidorAPI(base_url="http://127.0.0.1:8000")
            servidor_dados = api_client.importar_servidor(identificador)

            if servidor_dados:
                servidor = servidor_dados
            else:
                error = "Servidor não encontrado."

    return render(request, "importar_servidor.html", {"servidor": servidor, "error": error})
