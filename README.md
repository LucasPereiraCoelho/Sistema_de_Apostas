# Sistema de Apostas
Sistema de apostas realizado durante a aula de Padrões com Inteface Gráfica, com os seguintes requisitos:


Desenvolva um sistema de cadastro de apostas em jogos de futebol. O sistema deve permitir que os usuários insiram suas apostas e, posteriormente, verificar quem foi o apostador que acertou a aposta com base no resultado gerado aleatoriamente.

O sistema deve conter os seguintes campos para o cadastro de apostas:

      •     Nome do apostador: [Campo de texto]
      •     Time da casa: [Campo de texto]
      •     Time visitante: [Campo de texto]
      •     Valor da aposta: [Campo numérico]
      •         Placar com dois campos para quantidade de gols, um para cada time [campo numerico]


Após o cadastro das apostas, o sistema deve gerar um resultado aleatório para o jogo, demonstrando o placar.

Em seguida, o sistema deverá verificar as apostas cadastradas e aplicar as seguintes condições para determinar os ganhadores:

      •     Se um apostador acertar apenas o vencedor do jogo (time da casa ou time visitante), ele receberá 50% do valor da aposta como prêmio, somado ao valor apostado.
      •     Se um apostador acertar tanto o vencedor do jogo quanto o placar correto, ele receberá o valor apostado como prêmio, somado a 100% desse valor.

O sistema deve exibir na tela o nome do apostador vencedor, o valor da aposta acertada e o prêmio recebido.

As apostas devem ser registradas em banco de dados.
