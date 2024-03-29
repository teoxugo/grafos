#vertices = [[7 for x in range(2)] for y in range(10)]
vertices = [1, 2, 3, 4, 5, 6]
arestas = [[1, 5],[1, 3],[3, 2], [3, 4],[4, 2],[4, 5],[4, 6],[5, 3],[5, 6]]
pesos = []
contadorDoNumero = 0
C = [0, 0, 0, 0, 0, 0]

def haCicloEuleriano(arestas):
  for x in vertices:
    for i in arestas:
      for j in i :
        if j == x:
          global contadorDoNumero
          contadorDoNumero += 1
    if contadorDoNumero < 2:
      return 0
    if contadorDoNumero % 2 == 0:
      contadorDoNumero = 0
    else:
      return 0
  return 1


def buscarSubCicloEuleriano(vertice1, vertices, arestas):
  ciclo = []
  ciclo.append(vertice1)
  arestasRestantes = arestas
  while len(arestasRestantes) != 0:
    checador = 0
    for i in arestasRestantes:
      #print(i)
      for j in range(2) :
        if i[j] == vertice1:
          #print(arestasRestantes)
          #print(vertice1)
          tamanho_ciclo = len(ciclo)
          if len(ciclo) > 2:
            for indexDoVertice in range(tamanho_ciclo -1, 0, -1):
              if ciclo[indexDoVertice] == vertice1:
                #print("vo iseri",i[(j+1)%2])
                ciclo.insert(indexDoVertice+1, i[(j+1)%2])
                vertice1 = i[(j+1)%2]
                checador = 1
                break
          else:
            ciclo.append(i[(j+1)%2])
            vertice1 = i[(j+1)%2]
          arestasRestantes.pop(arestasRestantes.index(i))
          #print('ciclo', ciclo)
          break
    if checador == 0 and len(ciclo) > 2:
      vertice1 = ciclo[(ciclo.index(vertice1) + 1)%len(ciclo)]
      #ciclo2 = buscarSubCicloEuleriano(vertice1, vertices, arestasRestantes)
      #print(ciclo2)
      if vertice1 == ciclo[0] and len(arestasRestantes) == 110:
        print("nao ha ciclo")
        return
  ciclo.append(ciclo[0])
  return ciclo



def hierholzer(vertices, arestas):
  vertice1 = vertices[0]
  print(buscarSubCicloEuleriano(vertice1, vertices, arestas))
  return

if haCicloEuleriano(arestas) == 1:
  print("1, Há ciclo")
  hierholzer(vertices, arestas)
else:
  print("0, não há ciclo")
"""
Input :um grafo G = (V,E)
1 C i c l o ← (v)
2 t ← v
3 repeat
// Só prossegue se existir uma aresta não-visitada conectada a C i c l o.
4 if @u ∈ N(v) :C{u,v} =false then
5 return (false,null)
6 else
7 {v,u} ← selecionar uma aresta e ∈ E tal que Ce =false
8 C{v,u} ← true
9 v ← u
// Adiciona o vértice v ao final do ciclo.
10 C i c l o ← C i c l o ·(v)
11 until v = t
/* Para todo vértice x no C i c l o que tenha uma aresta adjacente não
visitada. */
12 foreach x ∈
©
u ∈C i c l o : ∃{u,w} ∈ {e ∈ E :Ce =false}
ª
do
13 (r,C i c l o0
) ← buscar Subci c l oEuler i ano(G,x,C)
14 if r =false then
15 return (false,null)
16 Assumindo que C i c l o = 〈v1, v2,...,x,..., v1〉 e C i c l o0 = 〈x,u1,u2,...,uk ,x〉, alterar
C i c l o para C i c l o = 〈v1, v2,...,x,u1,u2,...,uk ,x,..., v1〉, ou seja, inserir o C i c l o0
no lugar da posição de x em C i c l o.
17 return (true,C i c l o)
"""
