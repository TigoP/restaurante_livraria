class Livro:
    """Representa uma livraria e suas características apresentando uma lista de livros"""
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        """
        Inicializa uma instância de Livro.
        Parâmetros:
        - titulo (str): O nome do livro.
        - Autor (str): O autor e assim por diante.
        """
        self._titulo = titulo.title()
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        """Retorna uma representação em string do livro."""
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}'
    
    @classmethod
    def listar_livros(cls):
        """Exibe uma lista formatada de todos os livros e seus cabeçalhos."""

        print(f'{'Nome do Livro'.ljust(36)} | {'Autor'.ljust(25)} | {'Ano'.ljust(9)} | {'Status'}')
        print('---------------------------------------------------'*(2))
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(36)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(9)} | {livro.disponivel}')
        print('---------------------------------------------------'*(2))
    
    @property
    def disponivel(self):
        """Retorna um símbolo indicando o estado de atividade."""
        return '✅' if self._disponivel else '❌'
    
    def emprestar(self):
        """Alterna o estado de atividade."""
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis