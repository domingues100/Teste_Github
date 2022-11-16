dados = []
arquivo =open("test.txt", 'r')
for lines in arquivo:
    lst=lines.split()
    dados.append(lst)
dados = list(filter(None, dados)) 

def fatorial(n):
    if n >= 2:
        return n * fatorial(n-1)
    else:
        return 1

def fibonacci(n):
    if ( n == 1 or n == 2):
        return(1)

    fibo = (fibonacci(n-1) + fibonacci(n-2))

    return(fibo)

def test_compare():
  erro = False
  lista = [] 

  for row in range(1,len(dados)):
    n = int(dados[row][0])

    if fibonacci(n) == int(dados[row][2]): pass
    else:
        lista.append(n)
        erro = True

    if fatorial(n) == int(dados[row][1]): pass
    else: 
        lista.append(n)
        erro = True

  assert erro ==  False, f"erros quando n(#) = {lista}"
