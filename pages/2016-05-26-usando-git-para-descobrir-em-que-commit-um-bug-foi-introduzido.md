title: Usando git para descobrir em que commit um bug foi introduzido
date: 25/05/2016
description: Git bisect é um comando do git que usa busca binária para encontrar o commit que introduziu um bug.

Esses dias eu atualizei uma biblioteca que uso em um projeto chamada [pydocx](https://github.com/CenterForOpenScience/pydocx). Essa biblioteca converte docx para html, seu uso é bem simples, basta fazer:

    from pydocx import PyDocX
    
    html = PyDocX.to_html('file.docx')

Após atualizar a versão do pydocx de 0.7.0 para 0.9.9 um bug começou a acontecer. Alguns parágrafos do docx começaram a ser interpretados como `<li>` ao invés de `<p>`.

O parágrafo abaixo, por exemplo, começou a ser convertido para `<li>Exercício 08. 80...` ao invés de `<p>Exercício 08. 80...`


    Exercício 08. 80 - O ânion bromato reage com o ânion brometo em meio ácido
    gerando a substância simples bromo segundo a equação:

Para identificar em que commit esse bug foi inserido eu usei um comando do git chamado bisect. Para usarmos o `git bisect` precisamos encontrar um commit em que o bug acontece e um commit em que o bug não acontece, vamos fazer isso criando um teste unitário:

	git clone git@github.com:CenterForOpenScience/pydocx.git && cd pydocx

Vamos para a versão em que o bug não acontecia.

	git checkout v.0.7.0

Vamos criar um caso de teste chamado `docx_test_case.py` que reproduz o comportamento esperado.

    # coding: utf-8

    import unittest
    from pydocx import PyDocX


    class DocxToHtmlTestCase(unittest.TestCase):
    	
      def test_paragraph(self):
        html = PyDocX.to_html('file.docx').encode("utf-8")

        self.assertIn('<p>Exercício 08. 80', html)

    if __name__ == '__main__':
      unitttest.main()

Executando o teste

	python docx_test_case.py

    ----------------------------------------------------------------------
    Ran 1 test in 0.309s

    OK


O caso de teste é bem simples, ele apenas espera que o html gerado contenha um paragráfo `<p>` com o texto `Exercício 08. 80`.

Agora que sabemos que a versão 0.7.0 funciona vamos fazer checkout para o último release do projeto.

	git checkout v0.9.9

Rodando novamente o caso de teste:

	python docx_test_case.py


    ---------------------------------------------------------------------
    Ran 1 test in 0.235s

    FAILED (failures=1)

Opa! O teste começou a falhar. Agora temos as informações necessárias para começar a usar o git bisect.


## Usando git bisect para encontrar o commit que introduziu o bug


Para iniciar o git bisect faça:

	git bisect start

Precisamos informar pro git bisect um commit bom e um commit ruim, no nosso caso v0.7.0 e v0.9.9.

	git bisect good v0.7.0

	git bisect bad v0.9.9

A partir desse ponto o git bisect irá escolher um commit entre o commit bom e o ruim. A saída é semelhante com essa:

    Bisecting: 277 revisions left to test after this (roughly 8 steps)
    [551d8fec898fb773fc6585478918e74c268142f0] Refs #134. More test cases


Rodando novamente o caso de teste percebemos que o teste continua falhando.

	python docx_test_case.py


    ---------------------------------------------------------------------
    Ran 1 test in 0.235s

    FAILED (failures=1)


Iremos informar para o git bisect que o bug continua acontecendo:

    git bisect bad

Se o teste não falhasse, iríamos usar:

    git bisect good

O git bisect irá escolher outro commit e deveremos informar novamente se o bug continua acontecendo ou não. Essse último passo será repetido até que o git bisect encontre o commit em que o bug começou a ocorrer.

No caso desse exemplo o git bisect informou que o seguinte commit introduziu o bug:


    3de61857e0b7efb36a94bd8c26180ee03f7b1030 is the first bad commit
    commit 3de61857e0b7efb36a94bd8c26180ee03f7b1030
    Author: <author> <email>
    Date:   Wed Jul 29 15:17:49 2015 -0400

        Refs #134. Handle tab characters like spaces

Para encerrar o git bisect use:

    git bisect reset


## Modo automatico

O último passo do git bisect pode ser demorado se existirem muitos commits entre o commit bom (good) e o commit ruim (bad).
Para isso o git bisect conta com um modo automático. 

Para usar esse modo você precisa criar um script que reproduza o bug como, por exemplo, o caso de teste que criamos. Esse script precisa retornar código de status 0 se o bug acontecer e código de status diferente de 0 caso contrário.

*Esse script pode ser um caso de teste ou qualquer programa que faça uma asserção.*

Para usar o modo automático basta fazer:

	git bisect run <script> <arguments>

*o git bisect run aceita qualquer executável.*

Vamos então usar o git bisect no modo automático:

1. git bisect start
2. git bisect good v0.7.0
3. git bisect bad v0.9.9
4. git bisect run python docx_test_case.py

*Casos de teste feitos com unittest já retornam status diferente de zero em caso de falha.*

Saída:


    3de61857e0b7efb36a94bd8c26180ee03f7b1030 is the first bad commit
    commit 3de61857e0b7efb36a94bd8c26180ee03f7b1030
    Author: <author> <email>
    Date:   Wed Jul 29 15:17:49 2015 -0400

        Refs #134. Handle tab characters like spaces


Para encerrar o git bisect use:

    git bisect reset

## Resumo:

* Use git bisect start para iniciar.

* Use git bisect good  commit`para informar um commit em que o bug não acontece.

* Use git bisect bad  commit para informar um commit em que o bug acontece.

* Use git bisect run script arguments para usar o modo automático.

* Se você não passar um commit para git bisect good | bad o bisect pegará o commit corrente
 

Você pode encontrar o docx usado nesse post <a target="_blank" href="https://drive.google.com/file/d/0B7-HjtaVhQPSdmROaEs4bDBpWVU/view?usp=sharing">aqui</a>

## Referências:


* [https://git-scm.com/docs/git-bisect](https://git-scm.com/docs/git-bisect)