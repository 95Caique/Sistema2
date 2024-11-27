import requests
from typing import Optional, Dict
import json
import sys
import traceback

class ClienteServidorAPI:
    def __init__(self, base_url: str, auth_token: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Content-Type': 'application/json'
        }
        if auth_token:
            self.headers['Authorization'] = f'Bearer {auth_token}'

    def buscar_servidor(self, identificador: str) -> Dict:
        """
        Busca um servidor por CPF ou matrícula
        """
        # Tente múltiplas variações de URL
        urls_para_tentar = [
            f"{self.base_url}/api/servidores/",
            f"{self.base_url}/api/api/servidores/",
            f"{self.base_url}/servidores/",
            f"{self.base_url}/api/",
        ]

        for url in urls_para_tentar:
            try:
                print(f"Tentando URL: {url}")

                # Busca todos os servidores
                response = requests.get(url, headers=self.headers)

                print(f"Status da requisição: {response.status_code}")
                print(f"Cabeçalhos da resposta: {response.headers}")

                if response.status_code == 200:
                    # Filtra o servidor pelo identificador (CPF ou matrícula)
                    servidores = response.json()
                    print(f"Servidores encontrados: {len(servidores)}")

                    for servidor in servidores:
                        if servidor['cpf'] == identificador or servidor['matricula'] == identificador:
                            return servidor

                    # Se nenhum servidor for encontrado
                    print(f"Nenhum servidor encontrado para o identificador: {identificador}")
                else:
                    print(f"Resposta do servidor: {response.text}")

            except requests.RequestException as e:
                print(f"Erro de conexão para {url}: {e}")
            except json.JSONDecodeError:
                print(f"Erro ao decodificar JSON da URL: {url}")
            except Exception as e:
                print(f"Erro inesperado na URL {url}: {e}")
                traceback.print_exc()

        raise ValueError("Servidor não encontrado em nenhuma das URLs testadas")

    def importar_servidor(self, identificador: str) -> Dict:
        """
        Importa os dados de um servidor usando CPF ou matrícula
        """
        try:
            dados_servidor = self.buscar_servidor(identificador)
            print(f"Dados do servidor importados com sucesso: {dados_servidor['nome']}")
            return dados_servidor
        except ValueError as e:
            print(f"Erro: {str(e)}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            traceback.print_exc()
            return None


# Exemplo de uso
if __name__ == "__main__":
    # Configuração do cliente
    urls_para_testar = [
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ]

    # Verifica se um identificador foi passado como argumento
    if len(sys.argv) > 1:
        identificador = sys.argv[1]
    else:
        # Caso nenhum identificador seja fornecido, usa um padrão
        identificador = "70441065156"  # CPF de exemplo

    # Tenta diferentes URLs
    for url in urls_para_testar:
        try:
            print(f"\nTestando URL base: {url}")
            cliente = ClienteServidorAPI(base_url=url)

            # Exemplo de busca por CPF ou matrícula
            servidor = cliente.importar_servidor(identificador)
            if servidor:
                print("\nDetalhes do Servidor:")
                print(json.dumps(servidor, indent=2))
                break  # Para se encontrar o servidor
        except Exception as e:
            print(f"Falha ao tentar URL {url}: {e}")