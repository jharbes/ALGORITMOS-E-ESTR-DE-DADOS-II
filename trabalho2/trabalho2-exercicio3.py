"""
a) Mostre que a ordenação por inserção pode ordenar as n/k sublistas, cada uma de comprimento k, em Θ(nk) tempo do pior caso.

Para cada vetor de tamanho k o insertion-sort vai demorar Θ(k²), então para cada n/k sublistas teremos:

theta(n/(k*k^2)) = theta(nk)




b) Mostre como intercalar as sublistas em tempo do pior caso Θ(nlg(n/k)).

Se já temos as n/k sublistas (i.e o processo de divisão já foi realizado), então só precisamos continuar dividindo-as até terem tamanho 1. O merge-sort demora lgn para dividir uma lista de comprimento n. Sendo assim, para dividir n/k listas, vai demorar lg(n/k). Por fim, basta intercalar as n/k listas e o tempo final será de Θ(nlg(n/k)).

Prova:

número de níveis:
n/(k*2^i) = 1

n/k = 2^i

i = lg(n/k)


no último nível:
2^(lg(n/k)) = (n/k)^(lg(2)) = theta(n/k)


custo:
sum(i=0,lg(n/k))*2^i(cn/2^i) + theta(n/k)
sum(i=0,lg(n/k))*cn((2^i)/(2^i)) + theta(n/k)
cn*sum(i=0,(lg(n/k))*1 + theta(n/k)
cn*lg(n/k) + theta(n/k)
theta(nlg(n/k))


O que fiz foi uma árvore de recursão, já que na minha opinião é o método mais fácil de visualizar isso, dá para provar via indução, entretanto fiquei meio confuso durante a prova e optei por fazer desse modo, que é ensinado no capítulo 4.



c) Dado que o algoritmo modificado é executado em tempo do pior caso Θ(nk + nlg(n/k)), qual é o menor valor de k em função de n para qual o algoritmo modificado tem o mesmo tempo de execução que a ordenação por intercalação-padrão, em termos da notação Θ.


É pedido um valor de k tal que o tempo do pior caso vá de Θ(nk + nlg(n/k)) para Θ(nlg(n)). É facilmente visto um valor de k tal que a fórmula se adapte, então vamos algebrar para isolar o k.

nk + nlg(n/k) = nlg(n)
nk = nlg(n) - nlg(n/k)
k = lg(n) - lg(n/k)
k = lg(n/n/k)
k = lg(nk/n)
k = lg(k)


Substituindo na fórmula original vamos encontrar:

2nlg(n) - nlg(lg(n)) = theta(nlg(n))

d) Como k deve ser escolhido na prática?

Depende dos valores da entrada, não tem como saber diretamente. Entretanto, poderiamos gastar Θ(n) para analisar a entrada e escolher um k a partir da análise feita.
"""