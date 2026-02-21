# Must View em Python usando Flask

O Must View é uma aplicação web desenvolvida em Flask para organizar conteúdos que você deseja assistir, jogar ou ler. Com uma interface simples e estilizada, o sistema permite cadastrar itens como filmes, séries, jogos e livros, além de acompanhar datas de conclusão e editar ou remover registros facilmente.

O objetivo do projeto é ajudar na organização pessoal de entretenimento, funcionando como uma lista de prioridades para momentos de lazer.

Para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork deste repositório, clicando no botão `Fork`

2. Clone seu repositório localmente:

    ~~~bash
    git clone <url_seu_repositorio>
    ~~~

3. Abra o projeto utilizando seu IDE preferido.

4. Crie, preferencialmente, um ambiente virtual utilizando uma versão do Python >3.12.10:

    ~~~bash
    python -m venv .venv
    ~~~

5. Ative seu ambiente virtual.

    No bash:

        ~~~bash
        source .venv/Scripts/activate
        ~~~

    No PowerShell:
    
        ~~~powershell
        .\.venv\Scripts\Activate.ps1
        ~~~

6. Instale todas as dependências constantes no arquivo `requirements.txt`:

    ~~~python
    pip install -r requirements.txt
    ~~~

7. Copie o arquivo `.env.example`, cole na raiz do projeto e renomeie a cópia para `.env`.

8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Exemplo:

    ~~~env
    DATABASE='./data/meubanco.db'
    ~~~

9. Rode a aplicação no Python utilizando o comando:

    ~~~bash
    flask run
    ~~~

10. Acesse a aplicação no endereço e porta indicados no terminal. Exemplo: `http://127.0.0.1:5000`