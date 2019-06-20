# Colaborador-2.0
Sistema de Colaboradores Atualizado


<b><h2>Requisitos de Implantação</h2></b>
<ul>
  <li>Interpretador Python 3.7;
  <li>VirtualEnvironment</li>  
  <li>Framework Django 2.2 ou Mais recente, sugiro usar a 2.2 mesmo;</li>
  <li>django-widget-tweaks;</li>
  <li>driver conector de banco de dados (eu tô usando o mysql aqui, futuramente pretendo migrar para o PostgreSQL).</li>
</ul>  

<b><h2>Passos Para implantação</h2></b>
<ol>
  <li>Crie uma pasta chamada Colaborador;</li>
  <li>No terminal, dentro da pasta, rode o comando: ` ` ` 
    virtualenv venv --no-site-packages
    ` ` ` ;</li>
  <li>Uma vez que a virtualenv foi criada é necessário ativa-la, leve em consideração que os comandos demonstrados são em linux, se estiver usando windows alguns comando são diferentes ,rode o seguinte comando no terminal:   '''
   venv/bin/activate
    ''';
  </li>
  <li>Tendo ativado a virtualenv é necessário instalar os frmeworks utilizados, rode os comandos:
    <ul>
      <li> ''' pip3 install Django==2.2 ''' </li>
      <li>''' pip3 install django-widget-tweaks'''</li>
      <li>''' pip3 instal mysqlclient <- para o caso de usar o mysql'''</li>
    </ul>
  </li>
  <li>Após as instalações, transfira a pasta baixada no repositório para dentro da pasta Colaborador criada;</li>
</ol>

<b><h2>Configurações de Arquivos</h2></b>
Dentro do diretório Colaborador/Colaborador2/Colaborador2, acesse o arquivo settings.py, faça as alterações de banco no seguinte trecho de código:
<p>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'colaborador',
        'USER': 'root',
        'PASSWORD': 'Hu@n1000',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
</p>

Onde engine é o tipo de banco utilizado, name é o nome do banco, user é o nome do usuário, password é a senha .



<b><h2>Executando as Migrações de banco </h2></b>
No terminal acesse o diretório Colaborador/Colaborador2/Colaborado2 e execute o seguinte comando:

''' python manage.py makemigrations '''

Se tudo tiver ocorrido bem, execute o próximo comando:
''' python manage.py migrate '''

<b><h2>Rodando a Aplicação</h2></b>
Se as migrações tiverem sido executadas corretamente, é hora de rodadar a aplicação.

No mesmo diretório dito anteriormente execute o seguinte comando:
''' python manage.py runserver 8080 ''' 

Após , acesse a url : ''' localhost:8080/Colaborador/login/ '''
