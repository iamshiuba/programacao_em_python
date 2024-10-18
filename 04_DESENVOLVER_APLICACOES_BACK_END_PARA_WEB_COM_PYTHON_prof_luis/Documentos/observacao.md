# Inclusão de turmas

1. Minha turma não é incluída

- Pode ser o idioma do projeto, se estiver em `en-us` no settings.py, a ordem da data é *ano-mes-dia*, se for em ``pt-br``, *dia-mes-ano*.

2. Tenha certeza de ter criado a definição corretamente em views.py, que tenha incluido o modelo Turma em models.py, inclua Turma em admin.py, crie TurmaForm em form.py

3. Tenha certeza que ao criar o modelo, tenha feito o comando ``python manage.py makemigrations`` + ``python manage.py migrate`` para que o modelo seja reconhecido no banco de dados.

# Atrelar alunos e professores a Cursos e Turmas

Infelizmente nosso professor não teve tempo de ensinar a como fazer isso, então eu, iSHIUBA, irei fazê-lo após o término do curso.
- Será criado um diretório 05_COMPLEMENTOS_OPCIONAIS_DE_FEATURES onde eu irei complementar tudo o que eu considerar necessário e que me for possível de fazê-lo.
- Esse diretório também estará no repo secundário, onde eu irei criar um diretório chamado Django.
  > https://github.com/iamshiuba/guide_html_css_js_py
