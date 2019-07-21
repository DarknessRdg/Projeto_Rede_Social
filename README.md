# Projeto_Rede_Social
Projeto de uma Rede Social para a disciplina de Programação para Internet II do curso de Análise e Desenvolvimento de Sistemas.

Alunos         |
---------------|
Carlos Henrique|
Geovane Narciso|
Luan Rodrigues |


## Funcionalidades da rede social
- [x] 1) Rejeitar solicitação: 
O usuário rejeita a solicitação de amizade e uma nova pode ser enviada.

- [x] 2) Desfazer amizade: 
O usuário desfaz a amizade, removendo um perfil da sua lista de contatos.

- [X] 3) Alterar senha:
O usuário fornece a senha antiga e uma atual com confirmação e o sistema atualiza.

- [ ] 4) Recuperar senha:
O usuário fornece os dados de email e um e-mail com link para alteração de senha com
validade é enviado para o e-mail. Ao clicar no link, o usuário será direcionado a uma página
de redefinição.

- [X] 5) Cadastrar super usuário:
Crie um super usuário no banco e estando logado com ele você poderá atribuir a um outro
usuário/perfil o status de super usuário. Nota: isso deve ser feito setando o atributo
is_superuser da classe User.

- [X] 6) Bloquear usuário:
O usuário seleciona exibe um perfil e o bloqueia. Use confirmação JavaScript. O bloqueio
deve refletir na interface e nas outras funcionaliaddes para outros usuário.

- [X] 7) Incluir postagem:
Incluir postagem com texto. A data de postagem deve ser pega do sistema e salva
automaticamente. A postagem deve pertencer um perfil.

- [X] 8) Exibir timeline:
Ao logar, o usuário comum deve ser exibida sua timeline com suas postagens e de seus
contatos em ordem decrescente de data de postagem. A sugestão é criar uma aplicação para
gerenciar postagens.

- [X] 9) Pesquisar usuário:
O usuário digita um “username” e o sistema exibe os usuários com opções de adicionar
aos contatos ao lado de cada usuário que não for contato.

- [X] 10) Excluir postagem:
Ao lado de cada uma deve ser exibido uma opção de excluir. A exclusão deve ser feita
após uma uma confirmação via javascript. Restrição: só deve ser possível excluir suas próprias
postagens.

- [X] 11) Novo leiaute

- [x] 12) Página do super usuário

- [X] 13) Desativar perfil/ativar perfil:
O usuário logado pode desativar seu perfil mediante uma justificativa que deve ser salva.
Após isso, ao tentar se logar deverá aparecer uma informação de conta desativada com a
opção de reativar. As referências desse usuário em páginas de amigos deve sinalizar essa
situação

- [X] 14) Excluir postagem via Super usuário:
O super usuário pode excluir qualquer postagem.

- [X] 15) Usuário e postagens com foto:
O usuário a qualquer momento pode fazer o upload de uma foto pessoal como foto do
perfil. Deve ser possível também postar texto e foto ao mesmo tempo.

- [X] 16) Feedback ao usuário:
Estude um mecanismo de mensagens e forneça para cada operação um feedback
apropriado.

- [X] 17) Paginação:
As listagens de postagens e de usuários devem ter no máximo 10 ou 15 registros. Fora
isso, deve ser usado o mecanismo de paginação do Django.

- [X] 18) Uso de transações:
Operações que envolvam mais de uma operação de banco devem ser gerenciadas por
transações. Em caso de falha, todas as operações da transação devem ser canceladas.

- [X] 19) Internacionalização:
Deve ser possível mudar toda a linguagem do sistema usando o esquema de
internacionalização do Django.

- [X] 20) Proponha 5 funcionalidades além das que foram propostas. Discuta previamente com o
professor tais funcionalidades.

11. Novo layout
  * Os convites recebidos devem ser exibidos à direita, numa tag aside;
  * Ainda na aside, exibir os convites enviados;
  * A timeline deve ser exibida ao meio;
  * Exibir contatos à esquerda, numa tag nav;
  * Não deve ser possível convidar a si mesmo.
 
12. Página do superusuário
  * Ao entrar, devem ser possível ver todos os perfis conforme feito em sala;
  * Seus contatos e convites conforme já fizemos em sala;
  * Deve haver um link para a timeline do próprio super usuário.
 
 20. 5 novas funcionalidades
    * Editar postagem
    * Alterar visibilidade da postagem: privado ou abertado para amigos
    * Curtir / Descurtir postagem: reagir com Gostei ou Nao Gostei
    * Exibir gráfico de ativades: quantidade de curtir, postagen e comentarios no mês durante o ano
    * Marcar amigo na postagem
    
   
 
    >> print('Hello world!')
    Já chega!
    >>
