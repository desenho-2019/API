Para realizar login pelo Google no loaclhost, seguir os seguintes passos:</p>
1 - Acessar https://console.developers.google.com/</p>
2 - Ir em "Credenciais"</p>
3 - Crie um projeto</p>
4 - Selecione OAuth client ID no menu de criar Credenciais</p>
5 - Selecione Web Application e preencha os campos,</p>
6 - No campo Authorized redirect URIs adicione os seguintes endereços:</p>
    - http://localhost:8990/social-auth/complete/google-oauth2/</p>
    - https://localhost:8990</p>
    - https://localhost:8990/loginGoogle</p>
7 - Clique em "Criar"</p>
8 - Serão gerados uma chave de acesso e uma senha,</p>
9 - Vá até o settings.py no cafofo_api</p>
10 - Ache SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' e coloque a chave que foi gerada.</p>
11 - Ache SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' e coloque a senha que foi gerada.</p>
12 - Rode a aplicação</p>
13 - acesse localhost:8990/loginGoogle
