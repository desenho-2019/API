Se estiver no localhost, esses são os passos para conseguir o login por Facebook:
1 - Acessar https://developers.facebook.com/
2 - Clicar em Adicionar novo aplicativo,
3 - Preencher os campos e criar, será redirecionado ao dashboard.
4 - Ir em configurações, clicar em básico,
5 - No campo "Domínios do aplicativo", colocar "localhost",
6 - Lá no fim da página, clique no botão "Adicionar plataforma" e selecionar "website" ou "site" no pop-up uqe abrir,
7 - colocar o endereço do seu localhost, no caso do cafofo "https://localhost:8990/",
8 - salvar alterações,
9 - copiar o appID e o app Secret,
10 - vá até o settings.py no cafofo_api
11 - ache SOCIAL_AUTH_FACEBOOK_KEY = '' e coloque o appID que você copiou,
12 - ache SOCIAL_AUTH_FACEBOOK_SECRET = '' e coloque o app Secret que você copiou,
13 - rode a aplicação
14 - acesse localhost:8990/loginFb
