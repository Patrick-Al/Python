class Livro :
    def __init__ (self, titulo, autor, isbn) :
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
class Biblioteca :
    def __init__ (self, nome) :
        self.nome = nome
        self.livros = []
    def adicionar_livro(self, livro) :
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')
    def remover_livro(self, isbn) :
        for livro in self.livro:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro com ISBN "{livro.titulo}" removido da biblioteca"{self.nome}".')
                return
        print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')        
    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não tem livros.')
        else: 
            print(f'Livros na biblioteca "{self.nome}":')
            for livro in self.livros:
                print(f'- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn}')

# Testando as classes

# CRIANDO ALGUNS LIVROS

livro1 = Livro(titulo= 'O Senhor dos Anéis', autor='J.R.R Tolkien', isbn='1234567890')
livro2 = Livro(titulo= '1984', autor= 'George Owell', isbn= '0987654321')
livro3 = Livro(titulo= 'Apanhador No Campo de Centeio', autor='J.D Salinger', isbn='1122334455')

# Criando uma biblioteca
biblioteca = Biblioteca('Biblioteca central')


# Adicionando livros á biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros da biblioteca :
biblioteca.listar_livros()

# Removendo um livro da biblioteca
biblioteca.remover_livro('0987654321')

# Listando todos os livros da biblioteca após a remoção 
biblioteca.listar_livros()


