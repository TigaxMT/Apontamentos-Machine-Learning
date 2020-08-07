#!/usr/bin/env python
# coding: utf-8

# # Numpy
# 
# Esta biblioteca é utilizada para manipulação de listas(arrays/vetores) e matrizes(vetores multidimensionais/array de arrays).<br>Com ela podem aplicar cálculos entre múltiplas listas/matrizes e ainda chamar funções para modificar essas listas/matrizes.<br><br>
# Agora vocês perguntam-se:<br>
# -*Python já tem listas e nós podemos manipulá-las e aplicar cálculos, porquê usar uma biblioteca!?*<br><br>
# Apesar de tudo isso ser verdade, vocês devem ter lido na [Introdução](https://github.com/TigaxMT/Apontamentos-Machine-Learning/blob/master/00.%20Introdu%C3%A7%C3%A3o/Introdu%C3%A7%C3%A3o.pdf) que cada feature é uma dimensão, imaginem que temos 100 features, sendo assim temos 100 dimensões (100D). São muitas dimensões para o Python processar, e sendo ela uma linguagem de programação interpretada tornará o processo muito lento!<br><br>
# -*Ok ... mas se Numpy é uma biblioteca de Python, não será "lenta" da mesma forma?*<br><br>
# Não, e o porquê é simples, ela foi escrita em <u>Linguagem C</u> que é uma linguagem compilada (faz com que tudo seja mais rápido!).<br><br>
# E por fim, outro motivo para aprender Numpy é o facto de ele ser a base de outra biblioteca MUITO importante na análise de dados: o ***Pandas***.<br><br>
# Bora aprender um pouquinho!

# ## Instalação
# Antes de tudo precisamos instalar o Numpy! E para isso vocês pode usar o `pip` ou o `conda`, eu pessoalmente utilizo o `pip`, mas irei deixar abaixo o comando de instalação para ambos:<br>
# * Pip: `pip install numpy`
# * Conda: `conda install numpy`
# 
# É só correr um desses comandos no terminal e o numpy ficará instalado!<br>
# #### Nota
# * **Primeiro**: Para quem usa alguma distribuição Linux, tenha atenção ao pip! Pois pode haver ainda algumas distribuições a usar Python 2 como padrão e aí o vosso `pip` será do Python 2 (pip2). O melhor é usar `pip3 install numpy`, dessa forma reforçam que querem usar o `pip` do Python 3 (pip3).<br>Iremos usar Python 3 pelo simples motivo que o Python 2 foi descontinuado no início de 2020.
# * **Segundo**: Se der erro de permissão ao usar o `pip` usem o seguinte comando: `pip install numpy --user`.

# ## Básico
# Agora vamos importar o numpy

# In[2]:


import numpy as np


# Para não termos de escrever a palavra `numpy` usammos o `as` para atribuir um alias, no caso chamamos ele de `np`.<br>
# Dessa forma só temos de escrever 2 letras (np) em vez de 5 (numpy).

# ### Arrays e Matrizes
# 
# Comecemos pelo básico, por exemplo vamos criar um array(ou seja, uma lista ou também chamado de vetor) e depois criaremos uma matriz (que não é nada mais que uma lista com outras listas dentro dela).<br>

# In[3]:


# Criar uma lista/array/vetor
lista = np.array([1,2,3,4,5])

print(lista)


# Como podem ver é uma lista igual ao Python. Vamos ver o tipo

# In[4]:


print( type(lista) )


# Podemos ver que já não é uma *list* do Python e sim um numpy array!<br><br>
# Agora vamos criar uma matriz, que como já disse é uma lista de listas

# In[5]:


# Criar uma matriz
matriz = np.array([ [1,2,3],
                    [4,5,6] ])

print(matriz)


# E temos aqui uma matriz! Podemos ver que tem 2 linhas e 3 colunas. E como sabemos isso?!<br>
# Bem primeiro vejam visualmente, nós temos uma lista representada por *[ ]* e dentro dela temos mais 2 listas:<br>
# *[1 2 3]* e *[4,5,6]*<br><br>
# O número de listas dentro da lista são as **linhas**.<br><br>
# As colunas é fácil, é o **número de elementos que está dentro das listas**. Cada lista tem 3 números, logo temos 3 colunas!<br><br>
# #### Nota
# Vocês podem ter o número de linhas que quiserem, **mas** têm de ter o mesmo número de elementos em todas as listas!!<br>
# Vejam este exemplo:

# In[6]:


# Aqui eu criei uma matriz, contudo a primeira linha tem 3 colunas e a segunda 2 colunas

matriz_errada = np.array([
    [1,2,3],
    [4,5]
])


# In[7]:


print( matriz_errada )


# O que acontece aqui é que não é criado um numpy array e sim um numpy array com duas listas de Python dentro!<br>
# **Tenham atenção a isso!**<br><br>
# Agora vamos aprender como ver quantas linhas e colunas tem um numpy array/matriz

# In[8]:


print(lista.shape)
print(matriz.shape)


# O `shape` é um atributo do nosso numpy array, ele retorna uma tupla onde:<br><br>
# No caso de um array/lista/vetor:
# * O primeiro e único elemento da tupla, representa o número de elementos
# 
# No caso de uma matriz/array de arrays/vetor multidimensional:
# * O primeiro elemento é o número de linhas
# * O segundo elemento é o número de colunas
# 
# Como podem observar o shape da lista é: `(5,)` - o que significa que só está a contar as colunas e não as linhas já que ele tem apenas 1 linha e 5 colunas(números/elementos).<br>Sempre que virem um shape neste formato `(x,)` é porque o numpy array é realmente uma lista/array e não uma matriz.<br><br>
# Já a nossa matriz retornou: `(2,3)` - o que bate certo 2 linhas e 3 colunas.<br><br>

# Há outro método para criar matrizes: `matrix()`, mas a própria documentação não recomenda o uso dele, logo não vou mostrar aqui.

# ### Métodos
# Numpy tem vários métodos que manipulam os nossos arrays e/ou matrizes, vou mostrar alguns aqui

# In[9]:


"""

    O método arange serve para criar arrays de x a y números. 
    Por exemplo um array com números de 0 a 9
    
"""

# Vamos criar um array de 0-9
lista = np.arange(0,10)
print("Lista de 0 a 9: ", lista)


# In[10]:


""" 

    Podemos definir os steps,ou seja, pensem num range() do Python, se eu fizer: range(0, 10, 2) - ele vai contar de 0 a 9
    de 2 em 2: 0 2 4 6 8 - é igual no método arange
    
"""

# Criar um array de 0-9, só que contando de 2 em 2
lista = np.arange(0,10,2)
print("Lista de 0 a 9, contado de 2 em 2: ", lista)


# In[11]:


"""

    No caso de quererem criar arrays ou matrizes preenchidas com zeros ou com uns, há métodos para isso
    
"""

# Criar uma array com 5 colunas preenchidas com zeros
lista = np.zeros(5)

print("Lista com 0s: ", lista)

# Criar um array com 5 colunas preenchidas com uns

lista = np.ones(5)
print("Lista com 1s: ", lista)

# Criar matriz com 3 linhas e 5 colunas preenchidas com zeros

matriz = np.zeros((3,5))
print("Matriz com 0s:\n", matriz)

# Criar matriz com 3 linhas e 5 colunas preenchidas com uns

matriz = np.ones((3,5))
print("\nMatriz com 1s:\n", matriz)


# Isto pode ser útil no caso de quererem inicializar um array/matriz e ainda não terem valores para colocar lá.

# In[12]:


"""
    Este método cria uma matriz identidade

"""
# Criar matriz identidade de 4 por 4
matriz_identidade = np.eye(4)

print("Com método eye:\n", matriz_identidade)

# Criar a mesma matriz identidade com outro método
matriz_identidade = np.identity(4)
print("\nCom método identity:\n", matriz_identidade)


# A diferença entre um método e outro é que o método `eye` permite que explicitemos o índice da diagonal, já o `identity` apenas usa a diagonal principal.

# In[13]:


"""
    
    Vamos usar o eye novamente mas agora iniciamos a diagonal do índice 1 (coluna 2)

"""
print("Diagonal começada do índice 1:\n", np.eye(4, k=1))


# Deu para ver que a diagonal começou no índice 1 (coluna 2) da primeira linha.<br>
# O porquê da criação da matriz identidade, eu explicarei mais à frente.

# In[14]:


"""

    Vamos novamente criar um array, mas agora vamos fazer que nem o arange só que vamos decidir quantos valores queremos
    passando um dado intervalo.
    
    É meio confuso vejam o exemplo:
    Eu digo que quero um intervalo de 0 a 10, contudo digo que só quero 2 números ... O que ele retorna?
    
    Retorna: [0, 10]
    Se eu pedisse 3 números ficaria: [0, 5, 10]
    Se pedisse 4 número ficaria: [0, 3.3333333, 6.6666667, 10]
    
    Ele cria um array num dado intervalo com espaços iguais entre os números. 
    Ele conta até X (X é o número máximo do nosso intervalo) com base em quantos números nós queremos.

"""

# Criar array de 0 a 10 em que retorna somente 2 números igualmente espaçados

lista = np.linspace(0, 10, 2)
print("Intervalo de 0 a 10, com 2 número igualmente espaçados: ", lista)

# Criar array de 0 a 10 em que retorna somente 3 números igualmente espaçados

lista = np.linspace(0, 10, 3)
print("Intervalo de 0 a 10, com 3 número igualmente espaçados: ", lista)

# Criar array de 0 a 10 em que retorna somente 4 números igualmente espaçados

lista = np.linspace(0, 10, 4)
print("Intervalo de 0 a 10, com 4 número igualmente espaçados: ", lista)

# Criar array de 0 a 10 em que retorna somente 5 números igualmente espaçados

lista = np.linspace(0, 10, 5)
print("Intervalo de 0 a 10, com 5 número igualmente espaçados: ", lista)


# Espero que tenha dado para entender o que este método faz. Alguma dúvida é só dizer!

# In[15]:


"""

    Vamos criar alguns arrays/matrizes com números aleatórios 


"""

# Criar um array com 10 números ENTRE 0 e 1 aleatórios

lista = np.random.rand(10)
print("Array com 10 números aleatórios[entre 0-1]:\n", lista)


# Se multiplicarmos por 100 por exemplo obterão resultado entre 0 e 100. 

# In[16]:


# Criar um array com 10 números ENTRE 0 e 100 aleatórios

lista = np.random.rand(10) * 100
print("Array com 10 números aleatórios[entre 0-100]:\n", lista)


# In[17]:


"""

    Também podemos criar matrizes de números aleatórios

"""

# Criar matriz de 10 linhas por 2 colunas (10x2) com número aleatórios de 0 a 1
matriz = np.random.rand(10,2)

print("Matriz 10x2 com número aleatórios:\n", matriz)


# In[18]:


"""

    Podemos criar arrays/matrizes com números inteiros aleatórios
    
    Aqui é um pouco diferente, porque temos que passar um intervalo de números, onde o primeiro argumento é o número mínimo, 
    ou seja, de onde parte o intervalo, e o segundo argumento é o número máximo (o fim do intervalo).
    
    Ainda temos o argumento "size", se especificarem apenas um número, obteremos um array (array de 1 dimensão). 
    No caso de especificarem uma tupla, definem o número de linhas e colunas (no caso de ser uma matriz 2D, como nos exemplos
    que tenho mostrado).
    
    Imaginem que passamos: size=(3,2) - Então teremos uma matriz com 3 linhas e 2 colunas
    Agora se passarmos: size=(3,2,4) - Temos uma matriz, que neste caso é melhor pensarmos que tem um X=3, um Y=2, e um Z=4, 
    ou seja, aqui temos uma matriz de 3 dimensões (3D).
    
    E assim vai, eu vou ficar pelas 2 Dimensões(Linhas e Colunas) fica muito mais fácil de visualizarem!

"""

# Criar um array com 5 inteiros com inteiros de 0 a 20

lista = np.random.randint(0, 20, size=5)
print("Array de 5 inteiros com inteiros de 0 a 20: ", lista)

# Criar uma matriz com 3 linhas e 2 colunas de 0 a 20

matriz = np.random.randint(0, 20, (3,2))
print("Matriz 3x2 com inteiros de 0 a 20:\n", matriz)


# Se repararem eu omiti o `size=` no caso da matriz. Isto para vos mostrar que é indiferente, neste caso, especificar explicitamente o `size=`<br><br>
# #### Nota
# Se omitirem o valor máximo, por exemplo: `np.random.randint(5, size=(3,2))` - neste caso os inteiros vão de 0 a 5, e somos obrigados a passar o `size=` explicitamente, **NÃO podemos omitir**. 

# In[19]:


"""

    Outro método extremamente importante é o reshape. Ele permite alterar a estrutura de um array/matriz

"""

# Vamos criar um array de 0 a 15
lista = np.arange(15)

# Agora vamos transformar este array de 1 dimensão em uma matriz de 5 linhas por 3 colunas
# Já que 5 x 3 = 15
print("Array original: ", lista)
print("\nArray transformado em uma matriz 5x3:\n", lista.reshape((5,3)))


# Atenção que têm de passar valores válidos para o número de linhas e colunas!!<br>Para saberem se é um valor válido simplesmente multipliquem ambos, o resultado tem que dar o tamanho do vosso array inicial!<br><br>
# 
# Agora imaginem que uma função está a reclamar porque vocês passaram um array de 1 dimensão e não uma matriz. O que vocês podem fazer??<br>
# Bem se fizerem isto abaixo, vocês convertem um array para uma matriz:

# In[20]:


print( lista.reshape(1, -1) )


# Como podemos confirmar ???<br>Bem, podem comparar o `shape` da lista original com o shape da lista transformada

# In[21]:


print("Shape original: ", lista.shape)
print("Shape após a lista ser transformada em matriz: ", lista.reshape(1, -1).shape)


# Aqui dá para ver que a lista tinha simplesmente 15 elementos dentro dela. Logo depois que foi feito o `reshape` ela passou a ser uma matriz de 1 linha com 15 colunas.<br><br>
# Agora vocês perguntam:<br>
# -*Certo, então e se eu fizer reshape(-1, 1)? Muda alguma coisa??*<br><br>
# Vamos testar!

# In[22]:


print("reshape(1, -1) = ", lista.reshape(1, -1))
print("reshape(-1, 1) = \n", lista.reshape(-1, 1))


# Dá para ver que a primeira matriz tem simplesmente 1 linha e 15 colunas. Já a segunda tem o contrário, 15 linhas e 1 coluna.<br>
# Acho que deu para entender que inverter os valores faz com que o número de linhas troque com o número de colunas.<br><br>
# 
# Este último exemplo fez me lembrar de um atributo dos `numpy.ndarray` (classe de arrays que estamos a usar).<br>Este atributo é chamado de `T`, que no caso siginfica "Transpose", ou seja, **Transposição**.<br><br>
# *Para que serve a transposição? E o que é transposição?*<br><br>
# Para que serve é algo que vocês entenderão mais à frente (nas aritméticas). Vamos ver então o que ele faz:

# In[23]:


""" 

    Vou criar 2 matrizes

"""

# Matriz de 1 linha e 5 colunas
matriz1 = np.array([[1,2,3,4,5]])

# Matriz de 5 linhas e 1 coluna
matriz2 = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])


# In[24]:


# Agora vamos transpor a primeira matriz

print("matriz1 original: ", matriz1)
print("matriz1 transposta:\n", matriz1.T)


# Deu para ver?! Passamos de uma matriz de 1 linha e 5 colunas, para uma matriz de 5 linhas e 1 coluna!!!!<br>
# Literalmente fizemos o mesmo que `reshape(1, -1)`

# In[25]:


# Agora vamos transpor a segunda matriz

print("matriz2 original: \n", matriz2)
print("matriz2 transposta: ", matriz2.T)


# Aconteceu o mesmo novamente, só que na situação oposta! Neste caso fizemos o mesmo que um `reshape(-1, 1)`<br><br>
# 
# #### Nota
# Quando temos uma matriz com 1 linha e N colunas, chamamos essa matriz de, **matriz Linha**(em inglês, row matrix).<br>
# Uma matriz com N linhas e 1 coluna, chama-se de **matriz Coluna**(em inglês, column matrix)<br><br>
# É bom saber isto porque é útil quando se faz cálculos entre matrizes.

# E agora vamos para os últimos métodos "básicos", estes permitem-nos obter os mínimos e os máximos.

# In[26]:


"""

    Vamos obter os máximos e os mínimos de uma dada matriz também se aplica a arrays)

"""

matriz = np.array([
    [24, 35],
    [12, 56]
])

print("Máximo da matriz: ", matriz.max())
print("Mínimos da matriz: ", matriz.min())


# In[27]:


"""

    Vamos obter os índices dos máximos e mínimos da matriz

"""
print("Índice do máximo da matriz: ", matriz.argmax())
print("Índice do mínimo da matriz: ", matriz.argmin())


# <br>
# Já mostrei alguns métodos úteis que o numpy disponibiliza e ainda irei mostrar mais.<br>
# No entanto, os próximo são mais usados em aritméticas, portanto mostrarei quando estiver nas aritméticas.<br>
# 

# ## Fatiamento e índices de arrays e matrizes
# 
# Já sabemos criar arrays/matrizes e aplicar alguns métodos para retirar algumas informações deles. Está a faltar uma coisa:<br>-*Então e se quisermos apenas os valores de uma parte do array/matriz?*<br><br>
# É isso que vamos aprender aqui, como retirar uma "fatia" do nosso array/matriz

# In[28]:


# Vamos criar uma matriz com 5 linhas e 4 colunas

matriz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print(matriz)


# Ok, agora que temos a nossa matriz, vamos começar a "fatiá-la".<br><br>
# Vamos começar pelas linhas, eu quero apenas mostrar a linha 2 e 3.
# 
# #### Nota
# Lembrem-se que a linha 2 tem índice 1, e a linha 3 tem índice 2, normalmente em programação começamos a contar a partir do 0 e não do 1.

# In[29]:


# Mostrar apenas as linhas 2 e 3
print(matriz[1:3])


# Funcionou!!! Mas secalhar vocês perguntam-se:<br>
# *Porquê [1:3]?? Não deveria ser [1:2]??*<br><br>
# Realmente eu disse acima que o índice da linha 3 era 2, contudo eu coloquei 3 ... Porquê?<br>
# Assim como no `range()` o número máximo nunca é contado, ou seja, se o nosso número máximo é 10, ele contará somente até ao 9!<br>
# Por essa razão eu passei o índice limite como 3 (que refere-se à linha 4), porque ele vai só contar até ao índice 2 (que refere-se à linha 3).<br><br>
# 
# **Recapitulando**<br>
# Nós queremos ver a linha 2 e 3, então nós passamos o índice 1 que é a linha de partida, e passamos o índice 3 para ver a linha 3 (não esquecendo que a linha 3 tem índice 2 e **NÃO** 3!<br>
# Fica assim: `matriz[1:3]`<br><br><br>
# Agora vamos às colunas. Eu quero ver todas as linhas, mas só quero ver os valores das colunas 1 e 2 (ou seja, índices 0 e 1).<br>

# In[30]:


# Mostrar todas as linhas, mas apenas as colunas 1 e 2

print( matriz[:, 0:2] )


# Vamos observar isto bem de perto:<br><br>
# Comecemos pelos primeiros dois pontos -> matriz[ ***:*** , 0:2] - Passar os dois pontos sem qualquer valor é o mesmo que: `matriz[0:-1, 0:2]`, ou seja, o ponto de partida é no primeiro valor da matriz (índice 0) e o ponto de chegada é no último valor da matriz (índice -1). Logo ele percorre todas as linhas desde da 0 até à última(-1).<br><br>
# Agora vem uma vírgula, essa vírgula separa o fatiamento das linhas e das colunas. Portanto à esquerda da vírgula estamos a definir que linhas queremos ver (no caso queremos ver todas, do índice 0 ao -1), à direita da vírgula vamos definir que colunas queremos ver.<br><br>
# Por fim o nosso: matriz[:, ***0:2***] - este tem a mesma lógica que as linhas. Estou a definir que quero ver a partir da linha 1 (índice 0) até à linha 2 (índice 1, mas passamos 2 porque o python não conta com ele). Uma pergunta pertinente seria:<br>
# *Então e neste caso, podemos omitir o 0?*<br><br>
# E a reposta é ... **CLARO!**, 0 e -1 podem sempre ser omitidos, portanto ficaria assim: `matriz[:, :2]`.

# <br>
# Eu sei, isto por escrito é muito confuso, a melhor forma de entender isto de fatiamento e índices, é colocar na prática e ver os resultados. Vão ver que depois de uns testes vão entender a lógica.

# ## Aritméticas
# 
# Por fim chegamos às aritméticas. E é para isso que o numpy serve, para fazer aritméticas em matrizes gigantes! Por essa razão é muito importante saber como aplicá-las e também saber como funcionam.

# ### Soma de arrays/matrizes por números
# 
# Caso tenhamos um array/matriz e um número, podemos somá-los facilmente.

# In[31]:


# Criar um array com 3 elementos

lista = np.array([1,2,3])

# Criar uma matriz de 2 linhas e 3 colunas

matriz = np.array([
    [1,2,3],
    [4,5,6]
])

print( "lista + 5 = ", lista + 5 )
print( "matriz + 5 =\n", matriz + 5 )


# Funcionou certinho! Basicamente o que acontece é que o 5 é somado a cada elemento do array/matriz

# ### Soma de arrays/matrizes por outros arrays/matrizes
# 
# Também é possível somar 2 arrays/matrizes ou mesmo 1 array e 1 matriz.

# In[32]:


# Vou usar a lista e matriz já criada no último exemplo

print( "lista + lista = ", lista + lista )
print( "\nlista + matriz =\n", lista + matriz )
print( "\nmatriz + matriz =\n", matriz + matriz )


# Então *lista + lista* é nada mais nada menos que pegar no valor de índice 0 da 1ª lista e somar ao valor de índice 0 da 2ª lista. E assim sucessivamente<br><br>
# A *matriz + matriz* é a mesma coisa, só que aqui temos múltiplas linhas, pegamos na 1ª linha e 1º valor (índice 0) e somamos à 1ª linha e 1º valor da outra matriz, assim sucessivamente.<br><br>
# A *lista + matriz*, é pegar no array/lista e somar o valor de índice 0 ao valor de índice 0 de cada linha da matriz. Depois o valor de índice 1 ao valor de índice 1 de cada lista ... E assim vai. **Mas espera!**, há uma senão ... O tamanho da lista tem que ser **igual** ao número de colunas, caso contrário vai dar um erro, porque vai sobrar ou faltar valores para somar!<br>
# Poderá haver vezes que fazer um `reshape` ao array (para assim tornar-se uma matriz) pode ajudar caso ambas as matrizes fiquem com o mesmo número de colunas.

# ### Subtração de arrays/matrizes por números
# 
# É exatamente o mesmo que na soma, portanto é só ler as explicações acima e substituir "soma" por "subtração".

# In[33]:


print( "lista - 5 = ", lista - 5 )
print( "matriz - 5 =\n", matriz - 5 )


# ### Subtração de arrays/matrizes por outros arrays/matrizes
# 
# Digo o mesmo, é tudo igual à soma.

# In[34]:


print( "lista - lista = ", lista - lista )
print( "\nlista - matriz =\n", lista - matriz )
print( "\nmatriz - matriz =\n", matriz - matriz )


# ### Multiplicação de arrays/matrizes por números
# 
# Exatamente o mesmo que soma e subtração, só que agora vamos multiplicar.<br><br>
# #### Nota
# Eu tenho falado: "Soma/Subtração/Multiplicação de arrays/matrizes por números" - mas uma forma de o dizer mais "corretamente", é substituir *números* por *escalares*.

# In[35]:


print( "lista * 5 = ", lista * 5 )
print( "matriz * 5 =\n", matriz * 5 )


# ### Multiplicação de arrays/matrizes por arrays/matrizes
# 
# Este é outro caso que é igual a todos os outros. **Não se habituem que a seguir vem um tipo de multplicação diferente!**

# In[36]:


print( "lista * lista = ", lista * lista )
print( "\nlista * matriz =\n", lista * matriz )
print( "\nmatriz * matriz =\n", matriz * matriz )


# ### Produto Escalar entre matrizes
# 
# Aqui é um pouco diferente, mas vamos primeiro ao exemplo.

# In[37]:


# Criar uma matriz de 3 linhas e 4 colunas
a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

# Criar outra matriz de 3 linhas e 4 colunas
b = np.array([
    [13,14,15,16],
    [17,18,19,20],
    [21,22,23,24]
])

print( "Matriz a =\n", a)
print( "\nMatriz b =\n", b)


# In[38]:


print( "Produto escalar entre a e b =\n", a.dot(b.T))


# **HORA DA MATEMÁTICA!**<br><br>
# Não se assustem, com calma vamos todos entender isto.<br><br>
# Primeiramente, um array é um vetor. E uma matriz é um vetor multidimensional.<br><br>
# Aqui o que se aplica é a regra **RC - Row by Column**, que em português ficaria **LC - Linha por Coluna**. Nós pegamos a primeira linha da matriz *a* = [1,2,3,4] e pegamos a primeira coluna da matriz *b* =<br><br>
# &nbsp;[13,<br>
# &nbsp;14,<br>
# &nbsp;15,<br>
# &nbsp;16]

# -*Espera lá! A primeira coluna do vetor b não tem os valores: 13, 17 e 21 ?!?!*<br><br>
# É verdade, mas se repararem nós aplicamos um `.T` (uma transposição). Observem abaixo:

# In[39]:


print( "\nMatriz b transposta =\n", b.T)


# Temos de fazer isto porque a regra **LC ou RC** obriga-nos a que **a matriz** ***a*** **tenha tantas linhas quanto a matriz** ***b*** **tenha de colunas**. Isto é, se *a* tem 3 linhas, a matriz *b* tem de ter 3 colunas.<br><br>
# Vamos confirmar abaixo:

# In[40]:


print("Shape da matriz a = ", a.shape)
print("Shape da matriz b transposta = ", b.T.shape)


# Confirma-se, *a* tem 3 linhas e *b transposto* tem 3 colunas.

# Continuando a explicação do produto escalar ... Após termos 2 matrizes: uma com N linhas e outra com N colunas - pegamos na 1ª linha e 1º valor da matriz *a* e multplicamos pelo 1º valor da 1ª coluna da matriz *b*.<br><br>Depois pegamos na 1ª linha e 2º valor da matriz *a* e multiplicamos pelo 2º valor da 1ª coluna da matriz *b*... e assim vamos.<br><br>No fim, somamos todos os produtos gerados entre a 1ª linha de uma matriz e 1ª coluna da outra matriz. Esse valor é o produto escalar da linha 1, da matriz *a*, pela coluna 1 da matriz *b*.<br><br>
# De seguida pegamos novamente na 1ª linha e no 1º valor da matriz *a* e multplicamos pela 2ª coluna e 1ª valor da matriz *b*. E vamos multplicar valor por valor, para no fim fazermos novamente a soma de produtos.<br><br>
# Após a 1ª linha da matriz *a* multplicar por todas as colunas da matriz *b*, partimos para a 2ª linha da matriz *a* e repetimos todo o processo...<br><br>
# No fim obtemos uma **matriz quadrada**, isto é, uma matriz com o mesmo número de linhas e colunas. Isto devido à tal regra de **Linha por Coluna**, pois o número de linhas de *a* tem de ser o mesmo que o número das colunas de *b*.<br><br><br>
# 
# Por ser algo difícil de explicar por palavras, vou mostrar uma imagem que poderá ajudar

# <img src="img/produto_escalar_matrizes.jpg" width=1280 height=720>

# Peço desculpa pelas minhas habilidades de esboço serem quase nulas, mas espero que assim dê para esclarecer alguma confusão.<br><br>
# Podemos confirmar os resultados que o numpy obteve e os resultados que calculei manualmente ... e deu exatamente o mesmo!
# 
# #### Nota
# O vetor *b* tem expoente *T*, porque é a forma de assinalar transposição em matemática. No numpy limitamo-nos a: `b.T`

# ### Multiplicação de arrays/matrizes por matriz identidade
# 
# Eu disse que explicaria o que é matriz identidade mais para a frente, e aqui está.

# In[62]:


# Criar uma matriz de 3 linhas e 2 colunas
matriz = np.arange(1,7).reshape((3,2))

# Criar uma matriz identidade com 2 linhas e 2 colunas
matriz_identidade = np.identity(2)

print("Matriz 3x2 =\n", matriz)
print("\nMatriz Identidade 2x2 =\n", matriz_identidade)


# In[156]:


print("Produto escalar entre matriz e matriz identidade =\n", matriz.dot(matriz_identidade))


# Parece que multiplicar a nossa *matriz* pela *matriz identidade*, resulta na própria *matriz*!<br>
# O que podemos concluir é que a matriz identidade é como o 1 na multiplicação!<br><br>
# **MAS ATENÇÃO**: A matriz identidade é uma matriz quadrada (número de linhas = número de colunas), e esse número de linhas e colunas tem que ser **igual** ao número de colunas da matriz em que estão a calcular o produto escalar! Caso contrário obterão erros.

# Eu não dei nenhum exemplo com arrays nas últimas explicações, mas é exatamente o mesmo, a diferença que em vez de linhas e colunas, temos apenas elementos (1 linha com N elementos/colunas). O produto escalar no caso não irá ser uma matriz quadrada e sim um número/escalar.

# ### Divisão de arrays/matrizes por escalares
# 
# Novamente, é tudo igual às restantes operações. O escalar divide cada elemento do array/matriz.

# In[70]:


# Crirar uma matriz 3x2
matriz = np.arange(1,7).reshape((3,2))

print("matriz / 2 =\n", matriz/2)


# ### Divisão de arrays/matrizes por arrays/matrizes
# 
# Bem aqui o caso já muda. Não existe divisão de arrays/matrizes, mas é possível dividí-los.<br>
# -*O quê!?*<br><br>
# Já vamos entender isso, primeiro vamos dividir 2 matrizes e ver o resultado.

# In[81]:


# Criar uma matriz 3x3
matriz1 = np.arange(1,10).reshape((3,3))

# Criar outra matriz 3x3
matriz2 = np.arange(10, 19).reshape((3,3))


# In[85]:


print("matriz1 / matriz2 =\n", matriz1 / matriz2)


# Parece que dividiu (mesmo não "existindo" divisão)!!<br> Na verdade o que se passou aqui foi uma divisão elemento por elemento (como na multiplicação sem ser com produto escalar). Nós queremos realmente dividir a matriz por outra matriz e não elemento por elemento. E é isso que vou explicar daqui para a frente.
# #### Nota
# Os arrays/matrizes têm de ter o mesmo shape (número de linhas, colunas etc).<br><br>
# 
# **HORA DA MATEMÁTICA**<br>
# Agora eu vou explicar isso de "Não haver divisão".<br><br>
# Primeiro quero que pensem em um número, vou usar o 14. E quero que se lembrem que o 14 parece que está sozinho, mas na realidade não está.<br>
# <img src="img/14.png" />

# Podemos ver que o número 14 tem expoente 1 e está a ser dividido por 1. Nós omitimos isso, porque 14 elevado a expoente 1 = 14 e 14 dividido por 1 = 14.<br><br>
# Muito bem, agora imaginem que estão num mundo onde não há divisão direta, ou seja, não podem fazer isto: *14 / 7*<br><br>
# No entanto, vocês querem dividir 14 tarefas por 7 pessoas, por exemplo. Como podem fazer isto ?!<br><br>
# A resposta é ... **Multiplicação de um número pelo inverso de outro número**!<br>
# Se 7 é o mesmo que 7 dividido por 1, o inverso seria 1 / 7 !<br>
# <img src="img/1_7.png"/>

# Vamos testar então!<br>
# <img src="img/inv_numero.jpg"/>

# Bateu certo ! 14 / 7 = 7<br><br>
# Tudo isto para explicar que a divisão de 2 matrizes: *a / b* = *a . b*<sup>-1</sup><br>
# <img src="img/mult_inv.jpg"/>

# In[132]:


# Criar matriz 2x2
a = np.array([
    [1,2],
    [3,4]
])

# Criar outra matriz
b = np.array([
    [5,6],
    [7,8]
])

# Vamos inverter a matriz b usando o método linalg.inv()
b_inv = np.linalg.inv(b)

print("Matriz a =\n", a)
print("\nMatriz b =\n", b)
print("\nMatriz b inversa =\n", b_inv)


# Para comprovarmos se a matriz inversa foi corretamente calculada, basta fazer o produto escalar da matriz original pela sua inversa, e o resultado é a matriz identidade!<br>
# <img src="img/verify_inv.jpg"/>

# In[134]:


print("Produto escalar entre b e b inversa =\n", np.round( b.dot(b_inv) ))


# Parece que deu certo!! Eu apliquei um arredondamento, porque nem sempre os valores dão 1 ou 0!<br>Devido aos arrendondamentos e aos formatos dos números (inteiros, decimais etc), há certas imprecisões (0.00000000000000000000000000234 ou 1,000000000000000004), ao aplicar arredondamento a 0 casas decimais eu escondi essas imprecisões.

# In[148]:


print("Produto escalar entre a e b inversa =\n", a.dot(b_inv) )


# Bem aplicá-mos a fórmula para calcular a divisão entre 2 matrizes. Têm de ter atenção que há matrizes que não são **inversíveis**, portanto não a podemos dividir por outra matriz. Chamamos a essas matrizes, **matrizes singulares**

# -*Como podemos calcular a matriz inversa??*<br><br>
# Há uma fórmula para isso, mas eu só vou mostrar utilizando uma matriz 2x2, porque à medida que a matriz cresce mais difícil fica aplicar a fórmula (é necessário fazer muitos mais cálculos).<br><br>
# Tendo uma matriz como a seguinte:<br>
# <img src="img/eq.jpg"/>

# A inversa é calculada através da seguinte fórmula:<br>
# <img src="img/formula_inv.jpg"/>    

# Se aplicarmos a fórmula à nossa matriz, resulta em:<br>
# <img src="img/applied_formula.jpg"/>

# E assim obtemos a matriz inversa da nossa matriz original.

# ### Outras operações em arrays/matrizes
# 
# Podemos também calcular raízes quadradas e aplicar expoentes nos elementos do array/matriz.

# In[150]:


print("Matriz a =\n", a)


# In[153]:


print("Raíz quadrada da Matriz a =\n", np.sqrt(a))
print("\nMatriz a expoente 2 =\n", a ** 2)


# # Conclusão
# 
# Aqui pudemos ver um pouco do potencial do numpy. Lembro que não há mal algum não quererem já focar na matemática por detrás dos métodos. Primeiro de tudo brinquem com tudo isto, façam os vossos próprios testes, releiam etc.<br><br>
# Isto não é um curso, mas sim um conjunto de apontamentos, portanto levem isto como um dicionário com alguns métodos e explicações de Numpy.<br><br>
# Talvez ainda adicione e explique outros métodos que me recorde e que ache importante vocês terem em mente.<br>Finalizo pedindo que caso haja dúvidas ou queiram inserir algo, é só contactar-me (todos os meus contactos estão aqui abaixo).<br><br>
# Deixo aqui alguns links para vídeo aulas da khan academy para ajudar-vos com  a matemática:<br><br>
# [Soma e subtração de matrizes](https://pt.khanacademy.org/math/algebra-home/alg-matrices/alg-adding-and-subtracting-matrices/v/matrix-addition-and-subtraction-1)<br>
# [Multiplicação de matrizes por escalares](https://pt.khanacademy.org/math/algebra-home/alg-matrices/alg-multiplying-matrices-by-scalars/v/scalar-multiplication)<br>
# [Multiplicação de matrizes por matrizes](https://pt.khanacademy.org/math/algebra-home/alg-matrices/alg-multiplying-matrices-by-matrices/v/matrix-multiplication-intro)<br>
# [Introdução às matrizes inversas](https://pt.khanacademy.org/math/algebra-home/alg-matrices/alg-intro-to-matrix-inverses/v/inverse-matrix-part-1)<br>
# 
# # Contactos
# [Twitter](https://twitter.com/iN127pkt)<br>
# [Instagram](https://www.instagram.com/t_1g4_x/)<br>
# [Email](tiagodeha@protonmail.com)<br>
