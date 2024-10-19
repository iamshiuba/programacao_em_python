# Inclusão de turmas

1. Minha turma não é incluída

- Pode ser o idioma do projeto, se estiver em `en-us` no settings.py, a ordem da data é *ano-mes-dia*, se for em ``pt-br``, *dia-mes-ano*.

2. Tenha certeza de ter criado a definição corretamente em views.py, que tenha incluido o modelo Turma em models.py, inclua Turma em admin.py, crie TurmaForm em forms.py

3. Tenha certeza que ao criar o modelo, tenha feito o comando ``python manage.py makemigrations`` + ``python manage.py migrate`` para que o modelo seja reconhecido no banco de dados.

