Para realizar login pelo Google no loaclhost, seguir os seguintes passos:</p>
1 - Acessar https://console.developers.google.com/
2 - Ir em "Credenciais"
3 - Crie um projeto
4 - Selecione OAuth client ID no menu de criar Credenciais
5 - Selecione Web Application e preencha os campos,
6 - No campo Authorized redirect URIs adicione os seguintes endereços:
    - http://localhost:8990/social-auth/complete/google-oauth2/
    - https://localhost:8990
    - https://localhost:8990/loginGoogle
7 - Clique em "Criar"
8 - Serão gerados uma chave de acesso e uma senha,
9 - Vá até o settings.py no cafofo_api
10 - Ache SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' e coloque a chave que foi gerada.
11 - Ache SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' e coloque a senha que foi gerada.
12 - Rode a aplicação
13 - acesse localhost:8990/loginGoogle
