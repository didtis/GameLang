# Interpretador da GameLang - Sprint 4

class Interpretador:
    def __init__(self):
        self.personagens = {}

    def executar(self, ast):
        print("=== EXECUÇÃO DO COMBATE ===")

        for comando in ast.comandos:
            self.executar_comando(comando)

        print("\n=== FIM DO COMBATE ===")

    def executar_comando(self, comando):
        print(f"Comando recebido: {type(comando).__name__}")
