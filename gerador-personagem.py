import clipboard # type: ignore

def codigo_pericia(pericia):
  codigo = ("""
                  <div class="poster-info">
                    <div class="poster-fill-in">Perícias:</div>
                    <div class="poster-filler">{per}</H1></div>
                  </div>           
    """).format(per = pericia)
  return codigo

def gera_pericia(n):
  codigo_pericias = ''
  while n > 0:
    pericia = input('Perícia de número ' + str(n)+ '\n')
    code = codigo_pericia(pericia)
    codigo_pericias = codigo_pericias + code
    n = n-1
  return codigo_pericias

#perguntas
print('Por favor forneça todas as respostas em português, exceto em alinhamento. \n Para perguntas de número, responda apenas o número. \n')
id = int(input('Quantos personagens há no site? \n')) + 1
nome = input('Qual o nome do personagem?\n')
descricao = input('Qual a breve descrição dele? \n')
nivel = input('Qual o nível dele? \n')
classe = input('Qual a classe dele? \n')
raca = input('Qual a raça dele? \n')
alinhamento = input('Qual o alinhamento dele? Responda no formato N.G = Neutral Good, C.E. = Chaotic Evil, etc...\n')
numero_pericias = int(input('Quantas perícias ele tem? \n'))
percode = gera_pericia(numero_pericias)


codigo = ("""
            <!-- Cartaz {id}-->
             <div class="poster">
              <div class="poster-inner">
        
                <!-- Frente do Cartaz -->
                <div class="poster-front">
                  <button class="flip-btn" onclick="flipCard(this)">⟳</button>
                  <img src="src/personagens/{nome}.jpg" alt="Cartaz {id}">
                  <div class="poster-title">{nome}</div>

                  <div class="poster-subtitle" id="poster-subtitle">
                  {descricao}
                  </div>

                </div>
        
                <!-- Verso do Cartaz -->
                <div class="poster-back">
                  <h2>Detalhes</h2>
                  <div class="poster-info">
                    <div class="poster-fill-in">Nível:</div>
                    <div class="poster-filler">{nivel}</div>
                  </div>
                  <div class="poster-info">
                    <div class="poster-fill-in">Classe:</div>
                    <div class="poster-filler">{classe}</div>
                  </div>
                  <div class="poster-info">
                    <div class="poster-fill-in">Raça:</div>
                    <div class="poster-filler">{raca}</H1></div>
                  </div>
                  <div class="poster-info">
                    <div class="poster-fill-in">Alinhamento:</div>
                    <div class="poster-filler">{alinhamento}</H1></div>
                  </div>
            """).format(id = id,nome = nome,descricao = descricao,nivel = nivel,classe = classe,raca = raca,alinhamento = alinhamento)

codigo_final = codigo + percode +  ("""
            <!-- Fim do cartaz {id} -->
            </div>""").format(id = id)
clipboard.copy(codigo_final)
print(codigo_final)
input('O código foi copiado \n pressione qualquer coisa para sair ')
