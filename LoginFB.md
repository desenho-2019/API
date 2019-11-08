Se estiver no localhost, esses são os passos para conseguir o login por Facebook:</p>
1 - Acessar https://developers.facebook.com/apps</p>
2 - Clicar em Adicionar novo aplicativo.</p>
3 - Preencher os campos e criar, será redirecionado ao dashboard.</p>
4 - Ir em configurações, clicar em básico,</p>
5 - No campo "Domínios do aplicativo", colocar "localhost",</p>
6 - Lá no fim da página, clique no botão "Adicionar plataforma" e selecionar "website" ou "site" no pop-up uqe abrir,</p>
7 - colocar o endereço do seu localhost, no caso do cafofo "https://localhost:8990/",</p>
8 - salvar alterações,</p>
9 - copiar o appID e o app Secret,</p>
10 - vá até o settings.py no cafofo_api</p>
11 - ache SOCIAL_AUTH_FACEBOOK_KEY = '' e coloque o appID que você copiou,</p>
12 - ache SOCIAL_AUTH_FACEBOOK_SECRET = '' e coloque o app Secret que você copiou,</p>
13 - rode a aplicação</p>
14 - acesse localhost:8990/loginFb
