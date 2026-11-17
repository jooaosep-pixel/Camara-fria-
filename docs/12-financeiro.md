# 12 — Financeiro: custos, comparações e pedidos (RODADA 1 — PRELIMINAR)

Autor: subagente agente-financeiro. Data: 17/11/2026.
Contas: `docs/_trabalho/financeiro.py` (rodar com `python3 docs/_trabalho/financeiro.py`). A saída que realmente rodou está colada inteira no Anexo A; as tabelas deste documento foram copiadas dela.

**Versão: PRELIMINAR.** Metade do custo (47 % a 53 % do subtotal) é de itens **sem preço**, para os quais usei uma reserva suposta. Enquanto isso não mudar, o total serve para saber a ordem de grandeza e o que pesa, não para assinar compra.

Eu não projeto equipamento, não escolho local e não decido. Organizo os números e digo para que lado cada conta pende. **Quem decide é o dono.**

## Como ler

- **A** = preço encontrado (anúncio ou tabela pública, com link). Preço de anúncio é indicativo: vale para o dia 17/11/2026 e quase nunca mostra a data de publicação.
- **B** = faixa estimada a partir de preço encontrado de item parecido; a conta está mostrada.
- **C** = **sem preço**. O valor é uma reserva provisória minha, [SUPOSTO], sem fonte. Não é preço. Existe só para o total não sair falsamente baixo. Cada linha C tem um pedido correspondente na seção 2.
- [CALCULADO] = sai de conta do script. [SUPOSTO] = adotado sem fonte. [VALIDAR] = validar com profissional habilitado.
- **[PROVISÓRIO]** = número técnico tirado de documento que está sendo refeito (principalmente o projeto térmico).

### Em que base técnica fiz as contas

O projeto térmico (`docs/01`) foi reprovado pelo revisor e está sendo refeito para "só manga, 12 °C, recepção das 7h às 14h, sem propano montado no local, bateria de apoio". O texto que li ainda era o antigo (duas zonas, 12 kWp, 800 kg de gelo, propano). Usei, como configuração provisória, o que o próprio texto antigo dava para "só manga": **10 kWp, 600 kg de gelo, 2 máquinas de frio**, mais **1 a 2 módulos de bateria de 5,12 kWh**. Tudo isso é [PROVISÓRIO] e está num bloco só, no começo do script, para ser trocado.

### O que consegui e o que não consegui abrir

Testei uma vez, por acesso direto: `www.mercadolivre.com.br` (página inicial abriu; a página de listagem `lista.mercadolivre.com.br` não), `www.elgin.com.br` e `www.embraco.com` (abriram, mas não têm preço), `www.neosolar.com.br`, `www.weg.net` e `www.danfoss.com` (recusaram, erro 403), `www.mfrural.com.br` e `www.casasbahia.com.br` (não resolveram: fora da rede permitida). **Todos os preços deste documento vêm do resumo que a busca devolveu**, não de página que eu tenha lido inteira. Não achei preço em reais para: bateria LiFePO4 em loja brasileira, banco de gelo comercial, estrutura de solo para módulos, unidade condensadora em R513A ou com inversor, drive WEG, evaporadores, frete de contêiner.

---

## 1. Quadro único de custos do protótipo

Configuração provisória: 10 kWp (18 módulos de 550 W), 600 kg de gelo em tanque artesanal, 2 máquinas de frio, 1 a 2 módulos de bateria. [CALCULADO sobre entradas A, B e C]

| Bloco | Item | Mín. (R$) | Máx. (R$) | Grau | Origem da necessidade | Fonte do preço |
|---|---|---|---|---|---|---|
| 1 Invólucro | Reefer de 20 pés usado, só a caixa | 20.000 | 30.000 | A | 01, seções 1.3 e 12 | Anúncios MF Rural, SP, sem frete [F1] |
| 2 Refrigeração | Máquina de frio, 1 a 2 unidades | 5.070 | 39.596 | B | 01, seção 8; 11, seção 4.2 | Piso: 1 condensadora nacional de velocidade fixa (R$ 5.069,90). Teto: 2 importadas com inversor postas no Brasil (2 × R$ 15.941) + custos fixos de um embarque (R$ 7.714) — `docs/11`, seções 4.1 e 4.2 |
| 2 Refrigeração | Evaporador/trocador, serpentina de ar, ventiladores | 8.000 | 25.000 | **C** | 01, itens 6, 7, 14, 15 | sem preço |
| 2 Refrigeração | Válvulas, proteções, gás, tubulação, isolamento | 5.000 | 15.000 | **C** | 01, itens 8 a 10 e 21 | sem preço |
| 2 Refrigeração | Circuito secundário (bombas, glicol, tubos) | 3.000 | 12.000 | **C** | 01, itens 16 a 20 | sem preço |
| 2 Refrigeração | Renovação de ar e sensor de CO₂ | 1.500 | 5.000 | **C** | Parecer do revisor, achado 2 (segurança) | sem preço |
| 3 Armazenamento térmico | Tubo de 16 mm, 802 m (600 kg de gelo) | 5.938 | 15.352 | B | 01, seção 6.2 (1,34 m por kg) | Rolo de 100 m: R$ 739,99 a R$ 1.912,68 [F2]. É tubo multicamada para gás, **não** o PE-RT do projeto |
| 3 Armazenamento térmico | Reservatório (referência: caixa de 2.000 L) | 1.215 | 1.280 | A | 01, seção 6.2 | SINAPI e Telhanorte [F3]. O tanque do projeto é retangular e sob medida: referência fraca |
| 3 Armazenamento térmico | Isolamento do tanque, 8 a 12 m² | 2.344 | 7.332 | B | 01, seção 6.2 | R$ 293 a R$ 611 por m² (`docs/11`, seção 4.7) |
| 3 Armazenamento térmico | Coletores, suportes, estrutura e base do tanque | 3.000 | 10.000 | **C** | 01, itens 11 e 13; revisor, achado 5 | sem preço |
| 3 Armazenamento térmico | Montagem do feixe de tubos | 3.000 | 8.000 | **C** | revisor, achado 5 | sem preço |
| 4 Solar | Módulos de 550 W, 18 unidades (9,9 kWp) | 15.660 | 24.300 | A | 01, seção 5 | R$ 869,99 a R$ 1.350 por módulo (`docs/11`, seção 4.1) |
| 4 Solar | Estrutura dos módulos e fundação | 4.356 | 8.910 | B | 09, seção 5.1 (painéis não cabem no teto) | R$ 2,45/Wp de sistema instalado × 18 % de fatia da estrutura = R$ 0,44/Wp [F4]; teto de R$ 0,90/Wp [SUPOSTO] |
| 4 Solar | Drive solar do compressor, 1 a 2 unidades | 2.814 | 7.138 | B | 01, seção 8.2 | Kits de bombeamento solar, R$ 2.814 e R$ 3.569 (`docs/11`, seção 4.3). WEG: sem preço |
| 4 Solar | Cabos, proteções, aterramento, raio | 3.000 | 8.000 | **C** | 09, seção 5.1 | sem preço (`docs/02` não existe) |
| 5 Bateria | LiFePO4 48 V, 1 a 2 módulos de 5,12 kWh | 8.331 | 26.000 | B | Decisão D4; seção 3(d) | Piso: custo posto de importação, R$ 8.331 (`docs/11`, seção 4.5). Teto de R$ 13.000 por módulo [SUPOSTO]. **Preço de loja no Brasil não encontrado** |
| 5 Bateria | Inversor/carregador 48 V das cargas auxiliares | 3.844 | 8.500 | A | Decisão D4 | Deye híbrido, página de busca da Magazine Luiza [F5] |
| 6 Elétrica | Quadros, cabos, proteções, iluminação | 6.000 | 15.000 | **C** | `docs/02` não existe | sem preço |
| 7 Controle e telemetria | Controlador (referência: CLP) | 1.984 | 1.984 | B | `docs/03` não existe | Exemplo do `docs/11`, seção 4.6 |
| 7 Controle e telemetria | Sensores, quadro, tela, programação | 5.000 | 15.000 | **C** | 01, seção 11.2 | sem preço |
| 7 Controle e telemetria | Kit Starlink | 299 | 2.400 | A | Premissas | Imprensa, novembro de 2026 [F6] |
| 8 Estrutura e obra civil | Bases, recepção coberta, cerca, piso | 15.000 | 50.000 | **C** | 09, seção 5.1 | sem preço |
| 8 Estrutura e obra civil | Balança, caixas, mesa de seleção | 3.000 | 10.000 | **C** | 09, seção 6 | sem preço |
| 9 Mão de obra | Frigorista, 15 a 30 diárias | 5.700 | 13.500 | B | — | Diária de R$ 380 a R$ 450 [F7]; quantidade de diárias [SUPOSTO] |
| 9 Mão de obra | Eletricista, 10 a 20 diárias | 2.690 | 9.000 | B | — | Diária de R$ 269 (PE) a R$ 450 [F7]; quantidade [SUPOSTO] |
| 10 Frete | Reefer até o local, com guindaste | 8.000 | 20.000 | **C** | Anúncios em SP; local em Petrolina | sem preço |
| 10 Frete | Demais equipamentos | 2.000 | 6.000 | **C** | — | sem preço |
| 11 Taxas e responsável técnico | Projeto e ART, laudos, licenças | 5.000 | 20.000 | **C** | 09, seção 5.2; revisor, achado 11 | sem preço |

| Bloco | Mín. (R$) | Máx. (R$) | Fatia do subtotal |
|---|---|---|---|
| 1 Invólucro | 20.000 | 30.000 | 13 % a 7 % |
| **2 Refrigeração** | 22.570 | 96.596 | **15 % a 23 %** |
| 3 Armazenamento térmico | 15.498 | 41.964 | 10 % |
| **4 Solar** | 25.830 | 48.348 | **17 % a 12 %** |
| 5 Bateria | 12.175 | 34.500 | 8 % |
| 6 Elétrica | 6.000 | 15.000 | 4 % |
| 7 Controle e telemetria | 7.283 | 19.384 | 5 % |
| **8 Estrutura e obra civil** | 18.000 | 60.000 | **12 % a 14 %** |
| 9 Mão de obra | 8.390 | 22.500 | 5 % a 6 % |
| 10 Frete | 10.000 | 26.000 | 6 % a 7 % |
| 11 Taxas e responsável técnico | 5.000 | 20.000 | 3 % a 5 % |
| Subtotal | 150.746 | 414.292 | |
| 12 Reserva para imprevistos, 15 % a 25 % [SUPOSTO] | 22.612 | 103.573 | |
| **TOTAL PRELIMINAR** | **173.357** | **517.865** | |

**Leitura:** o protótipo custa entre cerca de **R$ 170 mil e R$ 520 mil**. A faixa é larga porque só 16 % a 27 % do subtotal tem preço encontrado:

| Grau | Mín. (R$) | Máx. (R$) | Fatia |
|---|---|---|---|
| A — preço encontrado | 41.018 | 66.480 | 27 % a 16 % |
| B — faixa estimada | 39.228 | 128.812 | 26 % a 31 % |
| C — sem preço (reserva suposta) | 70.500 | 219.000 | 47 % a 53 % |

O que mais pesa e mais varia: **refrigeração** (a máquina de frio pode custar de R$ 5 mil a R$ 40 mil conforme a decisão c), **obra civil e recepção coberta**, **solar** e **armazenamento térmico**. A bateria mínima pesa 8 %.

Não estão no quadro, por falta de qualquer dado: terreno (suposto cedido pela associação, `docs/09`), água, visita de campo, seguro, e o custo de refazer algo que não funcionar além da reserva.

---

## 2. Pedidos a cada agente

Cada pedido tem um código. A resposta ideal é: **valor, unidade, fonte (link ou cotação) e data**. Onde não houver preço, responder "preço não encontrado" e dizer a quem pedir cotação. As quantidades e potências finais valem mais para mim do que qualquer preço: sem elas não fecho nada.

### 2.1 engenheiro-refrigeracao
- **ER-1.** Configuração final "só manga, 12 °C, recepção 7h–14h": kWp mínimo e recomendado; kg de gelo mínimo e recomendado; número de máquinas de frio; carga diária em kWh de frio com 1 t/dia e sem fruta nova. (Substitui o bloco `CFG` e `T` do script.)
- **ER-2.** Quanto de frio passa pelo gelo por dia (kWh), em dia normal. Usei 40 kWh/dia [SUPOSTO].
- **ER-3.** Rendimento em kWh de frio por kWp por dia, com dado de **catálogo** do compressor: em dia de projeto e em dia nublado de 2,0 e 3,0 kWh/m². Usei 7,2 (autor), 8,5 (revisor) e 1,11 em dia nublado.
- **ER-4.** Decisão (c), opção "unidade selada de fábrica": existe modelo à venda (Brasil ou importado)? Fabricante, modelo, gás, carga de gás, capacidade a −10/+50 °C e a −4/+50 °C, se aceita painel direto, preço, prazo, quem dá assistência. Se não achou nenhum, dizer isso.
- **ER-5.** Decisão (c), opção "R513A montado no local": lista de peças com modelo, quantidade e preço (condensadora ou compressor + condensador, válvula de expansão, proteções, recipiente, gás em kg, preço do R513A por kg), e o COP de catálogo. Diferença de COP entre as duas opções, em %.
- **ER-6.** Decisão (a): para o tanque artesanal corrigido (achado 5 do revisor), a lista de material com metros de tubo, tipo de tubo com temperatura mínima declarada, tanque, isolamento, estrutura e base, e horas de montagem. Para o banco de gelo comercial: especificação fechada (kWh, potência de carga e descarga, com glicol ou expansão direta) para eu e o agente de importação pedirmos cotação.
- **ER-7.** Vida útil esperada (anos) e manutenção anual (o que troca, de quanto em quanto tempo) de: compressor, ventiladores, bombas, glicol, tubos do tanque, vedação da porta do reefer.
- **ER-8.** Serpentina de ar, evaporador ou trocador, bombas, válvulas: modelo, quantidade e preço, ou "preço não encontrado" com a especificação de cotação. Hoje são R$ 16 mil a R$ 52 mil de reserva sem base.
- **ER-9.** Renovação de ar e sensor de CO₂ (achado 2 do revisor): o que entra na lista e quanto custa.
- **ER-10.** Consumo elétrico das cargas da noite, em watts, corrigido (o revisor estima 250 a 400 W contra os 115 W do texto antigo). Dimensiona a bateria.
- **ER-11.** Se a bateria tocasse o compressor num dia nublado: COP nesse regime e potência mínima de partida. Serve para confirmar ou derrubar a conta da seção 3(d).
- **ER-12.** A alternativa mais barata que mantém a segurança: o que pode sair ou diminuir (por exemplo uma máquina em vez de duas, 0,5 t/dia em dia nublado) e o que se perde com isso.

### 2.2 integrador-solar (`docs/02` ainda não existe)
- **IS-1.** Irradiação conferida para Petrolina, mês a mês, no plano dos módulos, e quantos dias por ano ficam abaixo de 2,0 e de 3,0 kWh/m², e a maior sequência de dias assim. **É o dado que mais falta para a decisão (b).**
- **IS-2.** Para 8, 10 e 12 kWp: número de módulos, modelo, preço, e a energia elétrica diária em dia de projeto e em dia nublado.
- **IS-3.** Estrutura: tipo (solo ou cobertura sobre contêiner e recepção), preço por kWp com fundação, e se a estrutura de 10 kWp pode ser comprada já com lugar para 12 kWp (custo de deixar pronto x custo de ampliar depois).
- **IS-4.** Acionamento do compressor: modelo e preço do drive (WEG CFW500 ou outro), confirmado para compressor (torque constante). Quantos.
- **IS-5.** Bateria: modelo à venda no Brasil com registro no Inmetro, preço por módulo, garantia em anos e em ciclos, e a perda de vida útil a 35–40 °C de ambiente. Precisa de abrigo ventilado ou refrigerado? Quanto custa?
- **IS-6.** Arquitetura: em dia nublado, quando o compressor não parte, o arranjo consegue carregar a bateria das cargas auxiliares? (A conta da seção 3(d) depende de um "sim".) Modelo e preço do inversor/carregador.
- **IS-7.** Cabos, proteções, aterramento, proteção contra raio, quadros: lista e preço. Hoje são R$ 9 mil a R$ 23 mil de reserva sem base.
- **IS-8.** Diárias de eletricista necessárias e se precisa de engenheiro eletricista com ART (custo).
- **IS-9.** Vida útil e reposição: módulos, drive, inversor, bateria.

### 2.3 programador-controle (`docs/03` ainda não existe)
- **PC-1.** Controlador escolhido (CLP ou placa), modelo e preço; lista de sensores com preço; quadro, fonte, tela.
- **PC-2.** Horas de programação e de comissionamento, e quem faz.
- **PC-3.** Consumo elétrico do controle e da telemetria em watts, 24 h (entra na bateria).
- **PC-4.** Custo anual: licenças de software, plataforma de telemetria, chip ou assinatura além da Starlink.
- **PC-5.** Starlink: qual kit (Mini, 25 a 40 W, ou Standard, 75 a 100 W) atende. A diferença muda a bateria.

### 2.4 frigorista
- **FR-1.** Diárias (ou preço fechado) para montar cada opção da decisão (c): instalar unidade selada x montar circuito de R513A no local, com teste de estanqueidade, vácuo e carga. Usei 4 a 8 e 10 a 20 diárias [SUPOSTO].
- **FR-2.** Diárias para montar o tanque artesanal de gelo (feixe de tubos, coletores, teste) e para instalar um banco de gelo pronto.
- **FR-3.** Há frigorista em Petrolina com experiência em R513A/R134a e em banco de gelo? Valor da diária local e do deslocamento.
- **FR-4.** Manutenção preventiva por ano: visitas, horas, peças de troca certa (filtro secador, óleo, correias, gás reposto por ano em %).
- **FR-5.** Peças sobressalentes que devem ficar no local desde o primeiro dia, com preço.
- **FR-6.** Ferramentas ou equipamentos especiais a alugar (recolhedora, bomba de vácuo, detector) e custo.

### 2.5 agente-logistica
- **LG-1.** Frete de um reefer de 20 pés vazio até Petrolina, com caminhão munck ou guindaste na descarga: duas cotações, e se há reefer usado à venda mais perto (Suape, Recife, Salvador, Juazeiro).
- **LG-2.** Obra civil: o que é obrigatório para o protótipo funcionar (bases do contêiner e do tanque, cerca) e o que pode esperar (recepção coberta de 40 a 60 m², pátio). Preço por m² de cobertura simples e de piso na região. Hoje são R$ 15 mil a R$ 50 mil sem base.
- **LG-3.** O terreno é cedido sem custo? Há aluguel, taxa da associação, água?
- **LG-4.** Taxas e licenças da seção 5.2 do `docs/09`: quais têm custo e quanto (alvará, vigilância sanitária, Adagro, bombeiros).
- **LG-5.** Operador: valor de mercado em Petrolina para a pessoa que opera (salário e encargos, ou diária), e quantas horas por dia.
- **LG-6.** Balança, caixas plásticas (quantas), mesa de seleção: preço.
- **LG-7.** Seguro: existe seguro para o equipamento e para a fruta de terceiros guardada? Quanto?

### 2.6 analista-frutas-demanda
- **FD-1.** **Quanto vale a fruta perdida num evento sem frio:** se 5 t de manga a 12 °C ficarem 1, 2 ou 3 dias subindo 4 a 5 °C por dia, que fração se perde ou é vendida mais barato? Usei 30 % [SUPOSTO, sem fonte]. É o número que decide quanto vale cobrir dia nublado.
- **FD-2.** Estoque médio provável dentro da câmara em cada cenário, em toneladas e em reais (preço de roça e preço do canal melhor), para eu pôr valor em "fruta em risco".
- **FD-3.** Quem responde pela fruta perdida se o equipamento falhar (dono ou associação)? Isso muda quem deve pagar a reserva de frio.
- **FD-4.** Confirmar se os R$ 12.000 por ano de operação sem operador incluem internet, limpeza, caixas e manutenção. Minha soma do que tem número dá R$ 6 mil a R$ 18 mil sem limpeza nem seguro.
- **FD-5.** Algum modelo de cobrança em que o dono recebe parte do ganho de preço das famílias (R$ 108 mil por ano no cenário médio, segundo o `docs/10`) e não só a taxa? Em reais por quilo.
- **FD-6.** Financiamento: sem CNPJ e sem ser agricultor familiar, o dono acessa alguma das linhas da seção 7? Se a compradora for a associação, qual linha e qual limite valem?

### 2.7 agente-importacao
- **IM-1.** Unidade selada de fábrica (especificação do ER-4): cotação FOB real de dois fornecedores, custo posto via importadora por conta e ordem, margem da importadora, prazo. **Sem CNPJ (D5), essa via existe para o protótipo?** Se não, dizer com clareza: isso praticamente decide a opção (c).
- **IM-2.** Banco de gelo ou módulo de armazenamento térmico pronto (especificação do ER-6): existe? Preço FOB e posto.
- **IM-3.** Para cada item do quadro com grau B que usa número do `docs/11`: confirmar ou corrigir (condensadora R$ 15.941 posta; bateria R$ 8.331 posta; custos fixos de R$ 7.714 por embarque).
- **IM-4.** Preço de revenda no Brasil, com nota fiscal, de bateria LiFePO4 de 48 V e 100 Ah (procurei e não achei).
- **IM-5.** Sobressalentes que precisam vir no mesmo embarque e quanto somam; custo e prazo de uma peça de reposição depois, por remessa.
- **IM-6.** Sensibilidade ao câmbio dos itens importados: câmbio usado e data.

### 2.8 Perguntas que só o dono responde (levadas pelo orquestrador)
- **DN-1.** O protótipo é para medir (aceita não dar retorno) ou precisa se pagar? A conta da seção 4 muda de sentido conforme a resposta.
- **DN-2.** Quem opera: alguém da associação sem custo para o dono, ou operador pago?
- **DN-3.** Quantos dias nublados seguidos quer atravessar sem perder fruta: 1, 2 ou 3? (seção 3b)

---

## 3. Comparações das decisões em aberto — MÉTODO e exemplo provisório

Em todas: o método é o que vale; os números do exemplo são [PROVISÓRIO] e mudam na segunda rodada. Custos unitários usados [CALCULADO a partir do quadro]:

| Grandeza | Faixa |
|---|---|
| 1 kWp a mais (módulos + estrutura) | R$ 2.022 a R$ 3.355 |
| 1 kg de gelo a mais (tubo × 1,3) | R$ 12,90 a R$ 33,30, isto é, R$ 139 a R$ 359 por kWh de frio guardado |
| 1 kWh de bateria (nominal) | R$ 1.627 a R$ 2.539 |
| 1 kWh de frio guardado em bateria (bateria tocando o compressor, COP 2,2, 81 % de aproveitamento) | R$ 913 a R$ 1.425 |
| Bateria ÷ gelo, por kWh de frio guardado | 2,5 a 10 vezes mais cara |

### 3(a) Tanque de gelo artesanal x banco de gelo comercial

**Números que entram:** investimento de cada um; manutenção por ano; chance de ter de refazer parte (o artesanal é a peça que o revisor considerou não construível como descrita); vida útil; frio que passa pelo gelo em 10 anos; e, se o comercial for de expansão direta (só possível com R513A), o ganho de COP, que vira painel a menos.

**Fórmula:** custo em 10 anos = investimento × (1 + 10 × manutenção anual + chance de retrabalho × fração refeita). Custo por kWh = custo em 10 anos ÷ kWh de frio entregues pelo gelo em 10 anos.

**Exemplo [PROVISÓRIO]:** 600 kg = 55,7 kWh. Frio pelo gelo: 40 kWh/dia × 240 dias × 10 anos = 96.000 kWh [SUPOSTO].

| | Artesanal | Comercial |
|---|---|---|
| Investimento | R$ 15.498 a R$ 41.964 (R$ 278 a R$ 754 por kWh de capacidade) | **sem preço** |
| Manutenção por ano [SUPOSTO] | 2 % | 1 % |
| Retrabalho [SUPOSTO] | 30 % de chance de refazer metade | 5 % de chance de refazer 20 % |
| Fator | 1,35 | 1,11 |
| Custo em 10 anos | R$ 20.922 a R$ 56.651 | — |
| Por kWh de frio entregue | R$ 0,22 a R$ 0,59 | — |

Como não há preço do comercial, o script calcula o **preço de empate**: o banco de gelo comercial custa o mesmo que o artesanal em 10 anos se sair por **R$ 18.848 a R$ 51.037**, instalado. Se for de expansão direta e render 10 % a mais de COP, o empate sobe para R$ 20.870 a R$ 54.392.

**Risco:** artesanal — não funcionar ou vazar, sem garantia de ninguém, e parar o protótipo inteiro. Comercial — não existir no tamanho certo (o menor que o engenheiro achou é dez vezes maior), prazo, dependência de fornecedor.

**O que muda a escolha:** a cotação do comercial (IM-2, ER-6); a lista de material do artesanal corrigido (ER-6); as diárias de montagem (FR-2); e a decisão (c), porque banco de expansão direta só existe com R513A.

**Leitura PRELIMINAR:** sem preço do comercial **não há como decidir**. O que posso dizer: até cerca de **R$ 50 mil** instalado o comercial empata ou ganha; acima disso o artesanal é mais barato no papel, mas ver o conflito 1 da seção 7.

### 3(b) Tamanho do arranjo solar, combinado com gelo e bateria

**Números que entram:** carga diária com e sem fruta nova; rendimento em kWh de frio por kWp em dia de projeto e em dia nublado; gelo disponível no início da sequência nublada; preço por kWp, por kg de gelo e por kWh de bateria; valor da fruta guardada; fração perdida num evento; quantos eventos por ano.

**Fórmulas:**
- Sobra ou falta em dia de projeto = kWp × rendimento − carga diária.
- Déficit em dia nublado, sem fruta nova = carga sem fruta − kWp × rendimento nublado.
- Dias nublados cobertos = (kg de gelo × 0,0928 kWh/kg × 70 %) ÷ déficit.
- Depois de acabar o gelo, a fruta aquece (déficit ÷ 5,2 kWh por grau) por dia.
- Custo por dia coberto = custo a mais ÷ dias a mais. Número de perdas evitadas que paga o custo a mais = custo a mais ÷ (valor da fruta × fração perdida).

**Exemplo [PROVISÓRIO]** — carga de 68,0 kWh/dia com fruta, 35,6 sem fruta; dia nublado rende 1,11 kWh de frio por kWp:

| kWp | Gelo (kg) | Dia de projeto: sobra (+) ou falta (−), kWh — conta do autor / do revisor | Déficit em dia nublado (kWh) | Dias nublados cobertos | Depois disso a fruta aquece (°C por dia) | Solar + gelo, ponto médio (R$) |
|---|---|---|---|---|---|---|
| 8 | 400 | −10,4 / 0,0 | 26,7 | 1,0 | 5,1 | 45.623 |
| 8 | 600 | −10,4 / 0,0 | 26,7 | 1,5 | 5,1 | 50.236 |
| 8 | 800 | −10,4 / 0,0 | 26,7 | 1,9 | 5,1 | 54.849 |
| 10 | 400 | +4,0 / +17,0 | 24,5 | 1,1 | 4,7 | 51.000 |
| 10 | 600 | +4,0 / +17,0 | 24,5 | 1,6 | 4,7 | 55.612 |
| 10 | 800 | +4,0 / +17,0 | 24,5 | 2,1 | 4,7 | 60.225 |
| 12 | 400 | +18,4 / +34,0 | 22,3 | 1,2 | 4,3 | 56.376 |
| 12 | 600 | +18,4 / +34,0 | 22,3 | 1,7 | 4,3 | 60.989 |
| 12 | 800 | +18,4 / +34,0 | 22,3 | 2,3 | 4,3 | 65.602 |

O que a tabela mostra:
- **8 kWp só fecha o dia normal se valer a conta do revisor**; pela do autor faltam 10 kWh por dia. É exatamente a dúvida registrada no `docs/07`: depende do COP de catálogo e da irradiação conferida.
- De 10 para 12 kWp a diferença é de **R$ 4 mil a R$ 6,7 mil** (2 kWp), cerca de 1 % a 2 % do total do protótipo.
- **Mais painel quase não ajuda em dia nublado** (0,1 a 0,2 dia a mais por 2 kWp). Quem cobre dia nublado é o gelo: cada 200 kg dão cerca de meio dia.
- Cada dia nublado coberto a mais custa cerca de **R$ 9.500** se for comprado em gelo, e R$ 55 mil a R$ 61 mil se for comprado em painel.

Onde pôr o dinheiro para atravessar N dias nublados seguidos (R$ por kWh de frio disponível na sequência, ponto médio):

| N dias seguidos | Mais gelo | Mais painel | Bateria tocando o compressor |
|---|---|---|---|
| 1 | 249 | 2.425 | 1.169 |
| 2 | 249 | 1.213 | 1.169 |
| 3 | 249 | 808 | 1.169 |
| 5 | 249 | 485 | 1.169 |
| 10 | 249 | 243 | 1.169 |

O painel só empata com o gelo em sequências de cerca de 10 dias nublados; mas o painel também trabalha nos dias normais, e o gelo não.

**Quanto vale a fruta que se perderia:** 5 t valem R$ 6.000 a preço de roça e R$ 25.300 no canal de compra pública (`docs/10`, seção 4.2). Com perda de 30 % por evento [SUPOSTO, sem fonte — pedido FD-1], passar de 8 kWp + 400 kg para 10 kWp + 800 kg (+R$ 14.602, +1,1 dia) se paga se evitar cerca de **3 perdas em 10 anos**. Não sei quantos eventos há por ano em Petrolina (pedido IS-1).

**Leitura PRELIMINAR:** pende para **10 kWp**, com a estrutura comprada já com lugar para 12 kWp, e para gastar em **gelo**, não em painel nem em bateria, o que for destinado a dia nublado. A compra de 12 em vez de 10 kWp custa pouco e pode esperar o COP de catálogo e a irradiação conferida. **8 kWp é aposta:** só fecha numa das duas contas.

### 3(c) Unidade selada de fábrica x R513A montado no local

**Números que entram:** preço do equipamento de cada opção; margem da importadora e custos fixos do embarque; sobressalentes; diárias de frigorista; gás inicial e gás reposto por ano; manutenção anual; diferença de COP (vira kWp); prazo; frio entregue em 10 anos.

**Fórmula:** custo em 10 anos = equipamento × (1 + 10 × manutenção anual) + mão de obra de montagem + gás reposto em 10 anos. Custo por kWh = custo em 10 anos ÷ (carga diária × dias × 10).

**Exemplo [PROVISÓRIO]**, 2 máquinas em cada opção:

| | Selada, importada via importadora | R513A montado no local |
|---|---|---|
| Equipamento | 2 × R$ 15.941 (posto, `docs/11`) + margem de 0 a 25 % [SUPOSTO] + 10 % de sobressalentes + R$ 7.714 de custos fixos | 2 × (condensadora nacional R$ 5.070 a R$ 9.883 + drive R$ 2.814 a R$ 3.569) + extras R$ 3 mil a R$ 8 mil [C] + gás R$ 1 mil a R$ 3 mil [C] |
| Montagem | 4 a 8 diárias [SUPOSTO] | 10 a 20 diárias [SUPOSTO] |
| **Investimento** | **R$ 44.304 a R$ 55.152** | **R$ 23.568 a R$ 46.904** |
| Manutenção por ano [SUPOSTO] | 2 % | 3 %, mais 5 a 10 % do gás por ano |
| **Custo em 10 anos** | **R$ 52.861 a R$ 65.462** | **R$ 29.998 a R$ 61.275** |
| Por kWh de frio (163.200 kWh em 10 anos: 68 kWh × 240 dias × 10) | R$ 0,32 a R$ 0,40 | R$ 0,18 a R$ 0,38 |
| Efeito no solar | — | Se permitir gelo por expansão direta (+10 % de COP [SUPOSTO]): 1 kWp a menos, R$ 2.022 a R$ 3.355 |
| Prazo | 75 a 120 dias (`docs/11`) [SUPOSTO] | peças de pronta entrega [SUPOSTO] |

Diferença em 10 anos (selada menos local): de −R$ 8 mil a +R$ 35 mil. As faixas **se sobrepõem**: no papel o R513A local tende a ser mais barato, mas não em todos os casos.

**Não está na conta, por falta de dado:** (1) se a unidade selada certa existe — o `docs/11` não achou anúncio que reúna gás, inversor, potência e preço, e as condensadoras nacionais com preço são de velocidade fixa e em R22/R404A, não em R513A; (2) preço do R513A; (3) custo de ficar parado esperando peça importada; (4) restrição futura a gases HFC (o R513A tem potencial de aquecimento da ordem de 630, segundo o revisor); (5) se a importação via importadora é possível sem CNPJ (D5).

**Risco:** selada — assistência distante, peça que demora, e a unidade pode vir com gás inflamável (fica do lado de fora; `docs/09`, bloco de segurança). Local — qualidade depende do frigorista; vazamento de gás caro; sem ensaio de fábrica.

**Leitura PRELIMINAR:** pelo custo e pelo prazo, pende para **R513A montado no local**; mas a ordem de preferência técnica do revisor é a inversa (ver conflito 2, seção 7). O que decide: ER-4 (a unidade selada existe e quanto custa?) e IM-1 (dá para trazer sem CNPJ?).

### 3(d) Bateria de apoio: o tamanho que compensa

**Método:** separar duas funções. (1) **Manter as cargas pequenas ligadas à noite** (bomba, ventiladores, controle, Starlink): sem isso o gelo não entrega frio. (2) **Guardar frio para dia nublado**, fazendo a bateria tocar o compressor: aqui a bateria concorre com o gelo.

Função 1 — bateria nominal = watts da noite × 14 h ÷ (80 % de uso × 90 % de rendimento):

| Cargas da noite | Energia por noite | Bateria nominal | Módulos de 5,12 kWh | Custo |
|---|---|---|---|---|
| 140 W (texto antigo + Starlink Mini) | 2,0 kWh | 2,7 kWh | 1 | R$ 8.331 a R$ 13.000 |
| 500 W (estimativa do revisor + Starlink padrão) | 7,0 kWh | 9,7 kWh | 2 | R$ 16.662 a R$ 26.000 |

Em dia nublado de 2,0 kWh/m², 10 kWp ainda geram cerca de 15 kWh elétricos, e as cargas auxiliares de 24 h pedem 3,4 a 12,0 kWh. Ou seja: **a bateria das cargas auxiliares só precisa durar uma noite, mesmo numa sequência nublada**, desde que o arranjo elétrico deixe os painéis carregá-la quando o compressor não parte (pergunta IS-6).

Função 2 — cobrir dia sem sol nenhum, sem fruta nova (35,6 kWh de frio por dia):

| Dias | Só com bateria | Só com gelo (tubo; fora o tanque maior) |
|---|---|---|
| 1 | 20 kWh: R$ 32.506 a R$ 50.724 | 384 kg: R$ 4.937 a R$ 12.763 |
| 2 | 40 kWh: R$ 65.013 a R$ 101.449 | 767 kg: R$ 9.874 a R$ 25.526 |
| 3 | 60 kWh: R$ 97.519 a R$ 152.173 | 1.151 kg: R$ 14.811 a R$ 38.289 |

Fora isso, para a bateria tocar o compressor seria preciso um inversor maior e um compressor que aceite essa alimentação (não cotado), e a bateria se repõe: R$ 833 a R$ 1.300 por módulo por ano, com vida de 10 anos [SUPOSTO; as garantias achadas são de 5 a 10 anos, e calor encurta a vida].

**Leitura PRELIMINAR:** a resposta que as premissas admitem — "só a mínima" — é a que a conta indica: **1 a 2 módulos (5 a 10 kWh)** para as cargas auxiliares, e o frio para dia nublado guardado em gelo. Guardar frio em bateria custa de 2,5 a 10 vezes mais do que em gelo. **O que faria mudar:** tanque de gelo que não possa crescer (espaço, peso, decisão a), preço de bateria bem abaixo do que estimei (IS-5, IM-4), ou consumo noturno maior que 500 W (ER-10).

---

## 4. Receita e retorno

Duas leituras da receita, **lado a lado, sem refazer nenhuma**:
- **Autor** (`docs/10`, seção 6.2, só manga, 5 t): R$ 4.500 / R$ 32.400 / R$ 115.500 por ano, só da taxa de armazenagem; taxa média de R$ 0,30 por quilo; 108 t por ano no cenário médio.
- **Revisor** (`docs/_trabalho/revisao-10-demanda.md`): a aritmética do autor confere, mas a estimativa independente dele é **R$ 3 mil / R$ 15 mil / R$ 50 mil** por ano (taxa de R$ 0,10 a R$ 0,20 por quilo que passa, contra R$ 0,30 a R$ 0,40 do autor). Ancorada no único comprador quantificado (merenda escolar, no teto legal) dá **R$ 14.200 a R$ 23.700** por ano. Para o revisor, o cenário otimista do autor **não tem sustentação**.

**Decisão D6 do dono:** outras frutas que convivem com a manga a 12 °C podem entrar para completar a ocupação de abril a julho. Por isso o cenário **otimista do autor (R$ 115.500) passa a ser permitido**, mas **depende das frutas complementares** (banana, mamão, acerola; goiaba e maracujá em giro rápido), cujo calendário e preço o revisor diz que ainda não têm fonte (achado 4 dele). Os cenários pessimista e médio do autor são só manga.

**Confronto com o quadro de custos** — maior custo que cada receita paga em 10 anos = (receita − operação) ÷ fator; operação de R$ 12 mil por ano (sem operador pago) [CALCULADO; nas linhas do autor bate com o `docs/10`, seção 6.3]:

| Receita anual | Origem | Só manga? | Sem juros | 2 % ao ano | 7,5 % ao ano | Retorno simples (custo mín. / máx.) |
|---|---|---|---|---|---|---|
| R$ 3.000 | Revisor, pessimista | sim | não paga a operação | — | — | nunca |
| R$ 4.500 | Autor, pessimista | sim | não paga a operação | — | — | nunca |
| R$ 14.200 a R$ 23.700 | Revisor, ancorado na merenda | sim | R$ 22 mil a R$ 117 mil | R$ 20 mil a R$ 105 mil | R$ 15 mil a R$ 80 mil | 15 a 235 anos |
| R$ 15.000 | Revisor, médio | — | R$ 30 mil | R$ 27 mil | R$ 21 mil | 58 / 173 anos |
| R$ 32.400 | Autor, médio | sim | R$ 204 mil | **R$ 183 mil** | R$ 140 mil | 8 / 25 anos |
| R$ 50.000 | Revisor, otimista | — | R$ 380 mil | R$ 341 mil | R$ 261 mil | 5 / 14 anos |
| R$ 115.500 | Autor, otimista | **não: depende das frutas complementares (D6)** | R$ 1.035 mil | R$ 930 mil | R$ 710 mil | 2 / 5 anos |
| **Custo do protótipo nesta rodada** | | | **R$ 173 mil a R$ 518 mil** | | | |

Com operador pago (R$ 36 mil por ano), só o otimista do autor paga alguma coisa (R$ 714 mil a 2 % ao ano).

**Leitura:** pela conta do autor, o cenário médio paga um protótipo de até R$ 183 mil — o piso da minha faixa cabe por pouco; o ponto médio (R$ 346 mil) não. **Pela conta do revisor, nenhum cenário só de manga paga o protótipo**: o médio dele paga R$ 27 mil, e a merenda no teto, no máximo R$ 105 mil. Só os otimistas (o do revisor, R$ 50 mil, e o do autor, que exige outras frutas) pagam parte ou o todo da faixa.

Indicadores com a receita do autor (os do revisor ficam todos abaixo destes):

| Indicador [CALCULADO] | Pessimista | Médio | Otimista (com frutas complementares) |
|---|---|---|---|
| Sobra anual sem operador pago | −R$ 7.500 | R$ 20.400 | R$ 103.500 |
| Sobra anual com operador pago | −R$ 31.500 | −R$ 3.600 | R$ 79.500 |
| Retorno simples com operador | nunca | nunca | 2 / 7 anos |
| Taxa de empate por kg por dia (2 % a.a., sem operador; custo mín. / máx.) | R$ 0,21 / R$ 0,46 | R$ 0,058 / R$ 0,129 | R$ 0,027 / R$ 0,060 |
| A mesma, por caixa de 20 kg por dia | R$ 4,17 / R$ 9,29 | R$ 1,16 / R$ 2,58 | R$ 0,54 / R$ 1,21 |
| Taxa do cenário, por kg por dia (`docs/10`) | R$ 0,03 | R$ 0,06 | R$ 0,10 |

O revisor também alerta (achado 8) que a taxa de R$ 0,06 a R$ 0,10 por kg por dia não tem referência brasileira. Isso pesa: a taxa de empate do cenário médio, com o custo médio, fica acima de R$ 0,06.

**Ponto de equilíbrio em ocupação** (taxa de R$ 0,06/kg·dia, 240 dias, 2 % ao ano, sem operador): 43 % com o custo mínimo, 70 % com o custo médio, 97 % com o custo máximo. O cenário médio supõe 45 %.

**Sensibilidade** do resultado anual no cenário médio, custo no ponto médio (R$ 346 mil), 2 % ao ano, sem operador — base: **−R$ 18.076 por ano**:

| Mudança | Resultado anual |
|---|---|
| Ocupação de 45 % para 70 % | −R$ 76 |
| Ocupação de 45 % para 20 % | −R$ 36.076 |
| Taxa de R$ 0,06 para R$ 0,10 | +R$ 3.524 |
| Taxa de R$ 0,06 para R$ 0,03 | −R$ 34.276 |
| Custo do protótipo no mínimo | +R$ 1.101 |
| Custo do protótipo no máximo | −R$ 37.252 |
| Dólar 20 % mais caro | custo total +6 % (os itens ligados ao dólar são cerca de 30 % do subtotal) |

As três alavancas pesam parecido: ocupação, taxa e custo. Câmbio pesa pouco.

**O que a taxa não mostra:** o `docs/10` estima (e o revisor questiona, achados 7 e 12) que, no cenário médio, as famílias ganham R$ 108 mil por ano se venderem R$ 1,00/kg mais caro. Esse dinheiro não é receita do dono (pedido FD-5). E, por D5, o protótipo é um só e sem CNPJ: o `docs/10` propõe tratá-lo como instrumento para **medir** ocupação e ganho por quilo numa safra (pergunta DN-1).

---

## 5. Custos de operação por ano

| Item | Valor por ano | Grau | Fonte |
|---|---|---|---|
| Starlink | R$ 2.268 a R$ 2.988 | A | R$ 189 a R$ 249 por mês [F6] |
| Manutenção e peças | R$ 3.015 a R$ 12.429 | [SUPOSTO] | 2 % a 3 % do subtotal; pedidos ER-7 e FR-4 |
| Reposição de bateria (um décimo por ano) | R$ 833 a R$ 2.600 | B | seção 3(d) |
| Operador | R$ 0 (pessoa da associação) ou R$ 24.000 | [SUPOSTO] | `docs/10`, seção 6.3 (diferença entre R$ 36 mil e R$ 12 mil) |
| Limpeza | sem dado | — | pedido LG-5 |
| Seguro | sem dado | — | pedido LG-7 |
| Licenças e taxas anuais | sem dado | — | pedido LG-4 |
| **Soma do que tem número, sem operador** | **R$ 6.116 a R$ 18.017** | | o `docs/10` supôs R$ 12.000: compatível |

---

## 6. Financiamento

Linhas encontradas pelo analista de demanda (`docs/10`, seção 7; condições [VALIDAR] no banco). Parcela anual pela tabela Price, 10 anos, sem contar a carência [CALCULADO]:

| Valor financiado | Sem juros | 2 % ao ano (Pronaf Mais Alimentos, armazenagem) | 7,5 % ao ano (Pronaf Agroindústria; faixa do FNE) |
|---|---|---|---|
| R$ 150.000 | R$ 15.000 | R$ 16.699 | R$ 21.853 |
| R$ 173.357 (piso do quadro) | R$ 17.336 | R$ 19.299 | R$ 25.256 |
| R$ 250.000 (limite por família) | R$ 25.000 | R$ 27.832 | R$ 36.421 |
| R$ 450.000 (limite para fruticultura) | R$ 45.000 | R$ 50.097 | R$ 65.559 |
| R$ 517.865 (teto do quadro) | R$ 51.786 | R$ 57.652 | R$ 75.446 |

- O piso da faixa cabe no limite de R$ 250 mil por família; o teto passa do limite de R$ 450 mil.
- **Encaixe do protótipo: provavelmente nenhum, hoje.** O Pronaf é para agricultor familiar com cadastro (CAF) e suas organizações; o dono não tem CNPJ (D5) e o `docs/10` já registra que ele provavelmente não acessa essas linhas em nome próprio. Os juros acima servem para comparar e para o dia em que uma associação for a compradora (pedido FD-6).
- Recurso não reembolsável (BNDES Fundo Socioambiental) e taxa do FNE Sol para o agro: o `docs/10` não confirmou edital nem taxa. Sem dado.

---

## 7. Conflitos (o dono é o mediador; não resolvidos aqui)

**Conflito 1 — tanque de gelo: o mais barato no papel x o que alguém garante.**
- Pelo custo: o artesanal sai por R$ 15 mil a R$ 42 mil; o comercial não tem preço. Se a cotação do comercial vier acima de cerca de R$ 50 mil, o artesanal é mais barato mesmo contando 30 % de chance de retrabalho.
- Pelo revisor (achado 5, bloqueante): o artesanal, como descrito, **não é construível** e ninguém dá garantia; ele prefere banco de gelo comercial.
- O que cada escolha arrisca: artesanal — a peça central falhar e parar o protótipo; comercial — pagar mais, ou não achar no tamanho.

**Conflito 2 — máquina de frio: custo e prazo x ordem de preferência do revisor.**
- Pelo custo e prazo (seção 3c): R513A montado no local, R$ 24 mil a R$ 47 mil, contra R$ 44 mil a R$ 55 mil da selada importada; em 10 anos as faixas se sobrepõem.
- Pelo revisor (conflito C1 do parecer): primeiro a unidade **monobloco de fábrica**, ensaiada; o R513A montado no local vem em segundo, por depender do frigorista e por usar gás com restrição futura.
- As duas respeitam a decisão D3. **Nenhuma das duas economias reduz segurança frente à outra de forma que eu consiga medir**; a diferença é de garantia de fábrica x montagem local.

**Conflito 3 — bateria no lugar de gerador (D4) x custo de cobrir dia nublado.**
- A decisão do dono é bateria, "pelo que compensa". A conta diz que compensa só a mínima (5 a 10 kWh, R$ 8 mil a R$ 26 mil).
- Consequência que precisa ficar clara: com bateria mínima e 600 kg de gelo, a câmara atravessa cerca de **1,6 dia nublado** sem fruta nova; depois a fruta aquece 4 a 5 °C por dia [PROVISÓRIO]. Cobrir 3 dias só com bateria custaria R$ 98 mil a R$ 152 mil; com gelo, R$ 15 mil a R$ 38 mil de tubo mais um tanque maior.
- Não é questão de segurança de pessoas; é risco de perder fruta de terceiros (pedido FD-3: quem responde).

**Conflito 4 — custo do protótipo x o que a receita paga.**
- `docs/10` (autor): no cenário médio a taxa paga até R$ 183 mil, e só sem operador pago.
- Revisor do `docs/10`: médio de R$ 15 mil por ano, que paga cerca de R$ 27 mil; otimista do autor sem sustentação.
- Este documento: R$ 173 mil a R$ 518 mil.
- Não é erro de nenhum dos dois: é o resultado. Leva à pergunta DN-1.


**⚠ SEGURANÇA — economias que eu NÃO recomendo, mesmo reduzindo custo.** Estão no quadro e somam de R$ 9,5 mil a R$ 33 mil; nenhuma comparação deste documento as corta:
- renovação de ar e sensor de CO₂ na câmara (espaço fechado; achado 2 do revisor);
- projeto e ART de profissional habilitado, teste de estanqueidade e de pressão (alta pressão; gás);
- aterramento, proteção contra raio e proteções do lado de corrente contínua dos painéis (tensão contínua);
- estrutura dos painéis calculada para vento.
Se algum agente propuser cortar um desses itens para baixar o total, registro como conflito e levo ao dono com este aviso.

---

## 8. Recomendação por decisão — PRELIMINAR

| Decisão | Para que lado pende hoje | Depende de |
|---|---|---|
| (a) Tanque artesanal x banco comercial | **Indefinido.** Comercial vence se custar até cerca de R$ 50 mil instalado | Cotação do comercial (IM-2, ER-6); material e diárias do artesanal corrigido (ER-6, FR-2) |
| (b) Arranjo solar | **10 kWp, com estrutura pronta para 12.** Dinheiro para dia nublado vai para gelo | COP de catálogo (ER-3); irradiação e dias nublados (IS-1); valor da fruta perdida (FD-1) |
| (c) Selada de fábrica x R513A no local | **R513A no local pelo custo e prazo; o revisor prefere a selada** | A selada existe e dá para trazer sem CNPJ? (ER-4, IM-1); lista e preço do R513A (ER-5) |
| (d) Bateria | **Só a mínima: 1 a 2 módulos (5 a 10 kWh)** | Consumo noturno real (ER-10, PC-3, PC-5); preço no Brasil (IS-5, IM-4); arquitetura (IS-6) |

O que o dono precisa decidir (quando chegarem os números): DN-1 (medir ou se pagar), DN-2 (quem opera), DN-3 (quantos dias nublados cobrir), e os conflitos 1 e 2.

---

## 9. Base para a lista de compras e para o RESUMO

**Para `docs/05-lista-de-compras.csv`** — só o que tem alguma referência hoje. Nenhuma linha tem modelo fechado; **não comprar por esta tabela**.

| Item | Modelo | Fabricante | Qtde | Preço (R$) | Link | Prazo |
|---|---|---|---|---|---|---|
| Reefer 20 pés usado, só a caixa | a definir, com teste de perda de calor | — | 1 | 20.000 a 30.000 | [F1] | sem dado |
| Módulo fotovoltaico 550 W | a definir (IS-2) | OSDA, Jinko ou outro com Inmetro | 18 [PROVISÓRIO] | 870 a 1.350 cada | `docs/11`, seção 4.1 | pronta entrega [SUPOSTO] |
| Bateria LiFePO4 48 V 100 Ah | a definir (IS-5) | Elgin, Intelbras, Unipower, Deye | 1 a 2 | preço não encontrado no Brasil | fichas técnicas [F8] | sem dado |
| Inversor/carregador 48 V | a definir (IS-6) | — | 1 | 3.844 a 8.500 | [F5] | sem dado |
| Drive solar | a definir (IS-4) | WEG CFW500 ou outro | 1 a 2 | 2.814 a 3.569 (kits de outra marca) | `docs/11`, seção 4.3 | sem dado |
| Máquina de frio | a definir (decisão c) | — | 1 a 2 | 5.070 a 15.941 cada | `docs/11`, seção 4.2 | 0 a 120 dias |
| Tubo 16 mm para o tanque | a definir (ER-6) | — | cerca de 800 m [PROVISÓRIO] | 7,40 a 19,13 por metro | [F2] | sem dado |
| Kit Starlink | Mini ou Standard (PC-5) | Starlink | 1 | 299 a 2.400 | [F6] | sem dado |
| Demais itens | — | — | — | sem preço | — | — |

**Para o `RESUMO.md`:**
- Custo total do protótipo: **R$ 170 mil a R$ 520 mil (preliminar; metade sem preço)**.
- Custo de operação: R$ 6 mil a R$ 18 mil por ano sem operador pago; mais R$ 24 mil com operador.
- Prazo: **sem dado.** O único prazo com referência é o de importação, 75 a 120 dias [SUPOSTO no `docs/11`].
- Retorno: pela conta do autor do `docs/10`, só com manga o protótipo se paga apenas perto do piso da faixa e sem operador pago; pela do revisor, não se paga só com manga. O cenário otimista (permitido por D6) exige frutas complementares.

---

## 10. Fechamento

### Decisões tomadas neste documento
Nenhuma decisão de projeto. Decisões de método: três graus de confiança (A, B, C); total sempre em faixa; reserva de imprevistos de 15 % a 25 %; comparação em 10 anos; onde falta preço de uma das opções, calcular o preço de empate em vez de supor um.

### O que muda na segunda rodada
Trocar no início de `financeiro.py`: `CFG` e `T` (respostas ER-1 a ER-3, ER-10, IS-1), os preços `P` (cotações), tirar linhas de `C` à medida que virarem preço, `A_PAR["preco_comercial"]` (cotação do banco de gelo), `C_PAR` (ER-4, ER-5, FR-1, IM-1) e `FRACAO_PERDIDA` (FD-1). O resto recalcula sozinho.

### O que não consegui verificar
- Nenhuma página de preço lida por inteiro: tudo veio de resumo de busca (lista de sites na abertura).
- Preço no Brasil de: bateria LiFePO4, banco de gelo comercial, estrutura de solo, condensadora em R513A ou com inversor, drive WEG, evaporadores, trocadores, bombas, válvulas, frete de contêiner, obra civil, ART.
- Os anúncios de reefer são de São Paulo e sem data; os preços de tubo são de tubo multicamada para gás, não do tubo do projeto.
- A fatia de 18 % da estrutura vem de artigo assinado por fabricante, sobre usinas grandes; pode não valer para 10 kWp.
- Quantidade de diárias, manutenção anual, chance de retrabalho, vida da bateria e fração de fruta perdida: todas [SUPOSTO].
- Quantos dias nublados há por ano em Petrolina.
- Se o dono acessa alguma linha de crédito sem CNPJ.
- O projeto térmico novo: li a versão antiga.
- A saída do script usa ponto como separador decimal em alguns valores pequenos (por exemplo "R$ 0.22"); nas tabelas do texto está com vírgula.

### Dados de interface
- Para todos: os pedidos da seção 2.
- Para o orquestrador e o `RESUMO.md`: seção 9.
- Para o revisor: os [SUPOSTO] que mais pesam são as reservas de grau C (R$ 70 mil a R$ 219 mil), o teto do preço da bateria, o rendimento em dia nublado (1,11 kWh de frio por kWp) e os parâmetros de retrabalho da seção 3(a).

## Fontes

Preços vistos em 17/11/2026, pelo resumo da busca; anúncios sem data de publicação.

- [F1] MF Rural, busca "reefer 20 pés": https://www.mfrural.com.br/busca/reefer-20-pes — R$ 20.000 (Arealva-SP) e R$ 30.000 (Santos-SP), frete por conta do comprador. A página não abriu por acesso direto.
- [F2] Tubo multicamada PEX 16 mm, rolo de 100 m: R$ 739,99 em anúncio do Mercado Livre (lojas https://www.mercadolivre.com.br/loja/multicamadas e https://www.mercadolivre.com.br/loja/emilpec apareceram no resultado; não sei em qual das duas está o anúncio) e R$ 1.912,68 em página de busca da Magazine Luiza (https://www.magazineluiza.com.br/busca/16mm+pe).
- [F3] Caixa d'água de polietileno de 2.000 L: SINAPI de maio de 2026, R$ 1.272,45 (https://orcamentor.com/insumo/34640/); Telhanorte, R$ 1.279,99 ou R$ 1.215,90 no Pix (https://www.telhanorte.com.br/caixa-de-agua-green-2000-litros-acqualimp-2365014/p).
- [F4] Preço médio de R$ 2,45 por Wp de sistema residencial instalado, 1º trimestre de 2026: https://monitordomercado.com.br/economia-2/399791-quanto-custa-instalar-energia-solar-em-uma-casa-pequena-em-2026-e-quando-a-conta-de-luz-ainda-nao-compensa-o-investimento/ . Estruturas como cerca de 18 % do investimento em usina de solo: artigo do Canal Solar assinado por fabricante (https://canalsolar.com.br/diferenciais-boa-estrutura-para-usinas-solo/ ou outro da mesma série; a busca não deixou claro qual). Manual de estrutura de solo 1×4 da Elgin, sem preço: https://content.elgin.com.br/assets/arquivos/manual_estrutura_solo_mesa_1x4_10-25graus_45ms_elgin.pdf
- [F5] Inversor híbrido Deye 5 kW 48 V, R$ 7.800 a R$ 8.500; Deye 6 kW a partir de R$ 3.844,31: página de busca da Magazine Luiza, https://m.magazineluiza.com.br/busca/inversor+solar/
- [F6] Starlink: Residencial R$ 189/mês e Residencial Max R$ 249/mês em 08/11/2026; kit Mini R$ 299 em promoção (R$ 499 normal) e Standard R$ 2.400: https://comprerural.com/precos-da-starlink-planos-partem-de-r-189-por-mes-veja-o-que-muda-com-o-vivo-satelite/
- [F7] Diária de técnico de refrigeração autônomo, R$ 380 a R$ 450, data-base outubro de 2026 (referência de instalação de ar-condicionado, não de câmara fria): https://larpontual.com.br/portal/ferramentas/base-larpontual/profissionais/tecnico-de-refrigeracao . Diária de eletricista, R$ 269,27 em Pernambuco, até R$ 450: https://larpontual.com.br/portal/ferramentas/base-larpontual/profissionais/eletricista
- [F8] Baterias à venda no Brasil, sem preço: Intelbras EBL 4800 (https://www.intelbras.com/pt-br/bateria-recarregavel-li-ion-48-v-100-ah-ebl-4800); Unipower UPLFP48-100 (https://download.aldo.com.br/pdfprodutos/Produto339501IdArquivo28080.pdf); Deye SE-F5, garantia de 5 a 10 anos (https://deye.com/pt/product/se-f5-plus-a/).
- Demais números: `docs/01-projeto-termico.md`, `docs/_trabalho/revisao-01-termico.md`, `docs/09-logistica-e-local.md`, `docs/10-frutas-e-demanda.md` e `docs/11-importacao.md`, nas seções indicadas em cada linha.

## Anexo A — saída de `docs/_trabalho/financeiro.py` (rodada em 17/11/2026)

```text
financeiro.py — RODADA 1, PRELIMINAR — entradas de 17/11/2026
Configuracao provisoria: {'kwp': 10.0, 'gelo_kg': 600.0, 'n_maquinas': 2, 'bat_modulos': 2, 'capacidade_t': 5.0}

====================================================================================================
1. QUADRO DE CUSTOS (R$) — A = preco encontrado; B = faixa estimada; C = sem preco (reserva suposta)
====================================================================================================
Bloco                     Item                                                                           Min       Max  Grau
1 Involucro               Reefer 20 pes usado (so a caixa)                                            20.000    30.000  A
2 Refrigeracao            Maquina de frio, 1 a 2 un. (nacional fixa ... importada inverter posta       5.070    39.596  B
2 Refrigeracao            Evaporador/trocador, serpentina de ar, ventiladores                          8.000    25.000  C
2 Refrigeracao            Valvulas, protecoes, gas, tubulacao, isolamento                              5.000    15.000  C
2 Refrigeracao            Circuito secundario (bombas, glicol, tubos)                                  3.000    12.000  C
2 Refrigeracao            Renovacao de ar e sensor de CO2                                              1.500     5.000  C
3 Armaz. termico          Tubo 16 mm, 802 m (600 kg de gelo)                                           5.938    15.352  B
3 Armaz. termico          Reservatorio (ref.: caixa de 2.000 L)                                        1.215     1.280  A
3 Armaz. termico          Isolamento do tanque, 8 a 12 m2                                              2.344     7.332  B
3 Armaz. termico          Coletores, suportes, estrutura e base do tanque                              3.000    10.000  C
3 Armaz. termico          Montagem do feixe                                                            3.000     8.000  C
4 Solar                   Modulos 550 W, 18 un. (9.9 kWp)                                             15.660    24.300  A
4 Solar                   Estrutura dos modulos e fundacao                                             4.356     8.910  B
4 Solar                   Drive solar do compressor, 1 a 2 un.                                         2.814     7.138  B
4 Solar                   Cabos CC, protecoes, aterramento, raio                                       3.000     8.000  C
5 Bateria                 LiFePO4 48 V, 1 a 2 modulos de 5,12 kWh                                      8.331    26.000  B
5 Bateria                 Inversor/carregador 48 V das cargas auxiliares                               3.844     8.500  A
6 Eletrica                Quadros, cabos, protecoes CA, iluminacao                                     6.000    15.000  C
7 Controle e telemetria   Controlador (ref. CLP)                                                       1.984     1.984  B
7 Controle e telemetria   Sensores, quadro, IHM, programacao                                           5.000    15.000  C
7 Controle e telemetria   Kit Starlink                                                                   299     2.400  A
8 Estrutura e obra civil  Bases, recepcao coberta, cerca, piso                                        15.000    50.000  C
8 Estrutura e obra civil  Balanca, caixas, mesa de selecao                                             3.000    10.000  C
9 Mao de obra             Frigorista, 15 a 30 diarias                                                  5.700    13.500  B
9 Mao de obra             Eletricista, 10 a 20 diarias                                                 2.690     9.000  B
10 Frete                  Reefer ate o local, com guindaste                                            8.000    20.000  C
10 Frete                  Demais equipamentos                                                          2.000     6.000  C
11 Taxas e resp. tecnico  Projeto/ART, laudos, licencas                                                5.000    20.000  C

Subtotal por bloco:
  1 Involucro                      R$ 20.000 a    R$ 30.000   (13.3 % a  7.2 % do subtotal)
  2 Refrigeracao                   R$ 22.570 a    R$ 96.596   (15.0 % a 23.3 % do subtotal)
  3 Armaz. termico                 R$ 15.498 a    R$ 41.964   (10.3 % a 10.1 % do subtotal)
  4 Solar                          R$ 25.830 a    R$ 48.348   (17.1 % a 11.7 % do subtotal)
  5 Bateria                        R$ 12.175 a    R$ 34.500   ( 8.1 % a  8.3 % do subtotal)
  6 Eletrica                        R$ 6.000 a    R$ 15.000   ( 4.0 % a  3.6 % do subtotal)
  7 Controle e telemetria           R$ 7.283 a    R$ 19.384   ( 4.8 % a  4.7 % do subtotal)
  8 Estrutura e obra civil         R$ 18.000 a    R$ 60.000   (11.9 % a 14.5 % do subtotal)
  9 Mao de obra                     R$ 8.390 a    R$ 22.500   ( 5.6 % a  5.4 % do subtotal)
  10 Frete                         R$ 10.000 a    R$ 26.000   ( 6.6 % a  6.3 % do subtotal)
  11 Taxas e resp. tecnico          R$ 5.000 a    R$ 20.000   ( 3.3 % a  4.8 % do subtotal)
  SUBTOTAL                        R$ 150.746 a   R$ 414.292
  12 Reserva imprevistos 15 a 25 %: R$ 22.612 a R$ 103.573
  TOTAL PRELIMINAR: R$ 173.357 a R$ 517.865

Quanto do subtotal tem cada grau de confianca:
  A preco encontrado                 R$ 41.018 a    R$ 66.480   (27.2 % a 16.0 %)
  B faixa estimada                   R$ 39.228 a   R$ 128.812   (26.0 % a 31.1 %)
  C sem preco (reserva suposta)      R$ 70.500 a   R$ 219.000   (46.8 % a 52.9 %)

====================================================================================================
2. CUSTOS UNITARIOS USADOS NAS COMPARACOES
====================================================================================================
kWp adicional (modulo + estrutura):       R$ 2.022 a R$ 3.355 por kWp
Gelo adicional (tubo x 1,3):              R$ 12.9 a R$ 33.3 por kg  =  R$ 139 a R$ 359 por kWh de frio guardado
Bateria:                                  R$ 1.627 a R$ 2.539 por kWh eletrico nominal
Bateria tocando compressor (COP 2.2, uso 81 %): R$ 913 a R$ 1.425 por kWh de frio guardado
Razao bateria / gelo, por kWh de frio guardado: 2.5 a 10.3 vezes

====================================================================================================
3(a). TANQUE DE GELO ARTESANAL x BANCO DE GELO COMERCIAL
====================================================================================================
Capacidade: 600 kg = 55.7 kWh de frio. Frio que passa pelo gelo em 10 anos: 40 x 240 x 10 = 96.000 kWh [SUPOSTO]
Formula: custo em 10 anos = investimento x (1 + 10 x manutencao/ano + chance de retrabalho x fracao refeita)
Artesanal: investimento R$ 15.498 a R$ 41.964  (R$ 278 a R$ 754 por kWh de capacidade)
           fator 1.35  ->  10 anos: R$ 20.922 a R$ 56.651  =  R$ 0.22 a R$ 0.59 por kWh de frio entregue
Comercial: SEM PRECO. Fator 1.11. Preco de EMPATE (o comercial custa o mesmo em 10 anos): R$ 18.848 a R$ 51.037
           Se o comercial for de expansao direta (so com R513A) e render 10 % a mais de COP, vale ainda R$ 2.022 a R$ 3.355 de painel a menos -> empate sobe para R$ 20.870 a R$ 54.392

====================================================================================================
3(b). ARRANJO SOLAR x GELO: dia de projeto e sequencia de dias nublados (sem fruta nova)
====================================================================================================
Carga com 1 t/dia: 68.0 kWh/dia; sem fruta nova: 35.6 kWh/dia; dia nublado rende 1.11 kWh de frio por kWp [TODOS PROVISORIOS]
Fruta em risco (5 t): R$ 6.000 (preco de roca) a R$ 25.300 (canal de compra publica)
 kWp gelo kg   sobra/falta dia proj.   deficit nubl. dias nubl. aquec. dia seg.   custo solar+gelo (meio)
               (autor / revisor) kWh         kWh/dia   cobertos       graus/dia                        R$
   8     400       -10.4 /   +0.0               26.7        1.0             5.1                    45.623
   8     600       -10.4 /   +0.0               26.7        1.5             5.1                    50.236
   8     800       -10.4 /   +0.0               26.7        1.9             5.1                    54.849
  10     400        +4.0 /  +17.0               24.5        1.1             4.7                    51.000
  10     600        +4.0 /  +17.0               24.5        1.6             4.7                    55.612
  10     800        +4.0 /  +17.0               24.5        2.1             4.7                    60.225
  12     400       +18.4 /  +34.0               22.3        1.2             4.3                    56.376
  12     600       +18.4 /  +34.0               22.3        1.7             4.3                    60.989
  12     800       +18.4 /  +34.0               22.3        2.3             4.3                    65.602

Custo de cada dia nublado coberto a mais, contra a combinacao mais barata (8 kWp, 400 kg):
   8 kWp + 600 kg: +R$ 4.613 para +0.5 dia(s)  ->  R$ 9.494 por dia coberto; paga-se se evitar 1.0 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
   8 kWp + 800 kg: +R$ 9.226 para +1.0 dia(s)  ->  R$ 9.494 por dia coberto; paga-se se evitar 2.0 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
  10 kWp + 400 kg: +R$ 5.376 para +0.1 dia(s)  ->  R$ 61.193 por dia coberto; paga-se se evitar 1.1 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
  10 kWp + 600 kg: +R$ 9.989 para +0.6 dia(s)  ->  R$ 16.173 por dia coberto; paga-se se evitar 2.1 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
  10 kWp + 800 kg: +R$ 14.602 para +1.1 dia(s)  ->  R$ 12.726 por dia coberto; paga-se se evitar 3.1 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
  12 kWp + 400 kg: +R$ 10.753 para +0.2 dia(s)  ->  R$ 55.660 por dia coberto; paga-se se evitar 2.3 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
  12 kWp + 600 kg: +R$ 15.366 para +0.8 dia(s)  ->  R$ 19.810 por dia coberto; paga-se se evitar 3.3 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])
  12 kWp + 800 kg: +R$ 19.979 para +1.4 dia(s)  ->  R$ 14.711 por dia coberto; paga-se se evitar 4.3 perda(s) em 10 anos (perda = 30 % da fruta [SUPOSTO])

Onde por R$ 1 para atravessar N dias nublados seguidos (R$ por kWh de frio disponivel na sequencia, ponto medio):
 N dias   mais gelo   mais painel   bateria no compressor
      1         249         2.425                   1.169
      2         249         1.213                   1.169
      3         249           808                   1.169
      5         249           485                   1.169
     10         249           243                   1.169
  (o painel adicional so empata com o gelo acima de 9.8 dias nublados seguidos; mas o painel tambem serve nos dias normais e o gelo nao)

====================================================================================================
3(c). UNIDADE SELADA DE FABRICA x R513A MONTADO NO LOCAL
====================================================================================================
2 maquinas em cada opcao [PROVISORIO].
Selada importada (via importadora): investimento R$ 44.304 a R$ 55.152; em 10 anos R$ 52.861 a R$ 65.462
R513A montado no local:             investimento R$ 23.568 a R$ 46.904; em 10 anos R$ 29.998 a R$ 61.275
Credito possivel do R513A com expansao direta no gelo (+10 % de COP [SUPOSTO] = 1.0 kWp a menos): R$ 2.022 a R$ 3.355
Diferenca em 10 anos (selada - local), sem o credito: R$ -8.414 a R$ 35.464
Por kWh de frio em 10 anos (163.200 kWh): selada R$ 0.324 a 0.401; local R$ 0.184 a 0.375
NAO esta na conta (sem dado): preco e existencia da unidade selada certa; preco do R513A; custo de parada por falta de assistencia; restricao futura a HFC.

====================================================================================================
3(d). BATERIA DE APOIO: o tamanho que compensa
====================================================================================================
Cargas da noite 140 W x 14 h = 2.0 kWh  ->  bateria nominal (80 % de uso, 90 % de rendimento) = 2.7 kWh = 0.5 modulo(s) de 5,12 kWh  ->  R$ 8.331 a R$ 13.000
Cargas da noite 500 W x 14 h = 7.0 kWh  ->  bateria nominal (80 % de uso, 90 % de rendimento) = 9.7 kWh = 1.9 modulo(s) de 5,12 kWh  ->  R$ 16.662 a R$ 26.000
Dia nublado (2,0 kWh/m2, desempenho 0,75): 10 kWp geram cerca de 15 kWh eletricos; as cargas auxiliares de 24 h pedem 3.4 a 12.0 kWh.
  -> mesmo em dia nublado os paineis recarregam a bateria das cargas auxiliares, SE o arranjo eletrico permitir (pergunta ao integrador).
Cobrir 1 dia(s) sem sol nenhum e sem fruta nova (36 kWh de frio): so bateria = 20 kWh (R$ 32.506 a R$ 50.724); so gelo = 384 kg (R$ 4.937 a R$ 12.763 de tubo, fora tanque maior)
Cobrir 2 dia(s) sem sol nenhum e sem fruta nova (71 kWh de frio): so bateria = 40 kWh (R$ 65.013 a R$ 101.449); so gelo = 767 kg (R$ 9.874 a R$ 25.526 de tubo, fora tanque maior)
Cobrir 3 dia(s) sem sol nenhum e sem fruta nova (107 kWh de frio): so bateria = 60 kWh (R$ 97.519 a R$ 152.173); so gelo = 1151 kg (R$ 14.811 a R$ 38.289 de tubo, fora tanque maior)
Reposicao: bateria com vida de 10 anos [SUPOSTO; garantias de 5 a 10 anos] -> R$ 833 a R$ 1.300 por modulo por ano.

====================================================================================================
4. RECEITA E RETORNO (receita do doc 10 s.6.2, so manga, 5 t)
====================================================================================================
Cenario       Receita/ano  Sobra s/ operador  Sobra c/ operador   Retorno simples (anos), custo min / max
pessimista       R$ 4.500          R$ -7.500         R$ -31.500       sem oper.: nunca | com oper.: nunca
medio           R$ 32.400          R$ 20.400          R$ -3.600      sem oper.: 8 / 25 | com oper.: nunca
otimista       R$ 115.500         R$ 103.500          R$ 79.500       sem oper.: 2 / 5 | com oper.: 2 / 7

Maior custo que cada cenario paga em 10 anos = (receita - operacao) / fator   [mesma conta do doc 10 s.6.3]
  pessimista sem operador sem juros: nao paga; Pronaf 2% a.a.: nao paga; 7,5% a.a.: nao paga
  pessimista com operador sem juros: nao paga; Pronaf 2% a.a.: nao paga; 7,5% a.a.: nao paga
  medio      sem operador sem juros: R$ 204.000; Pronaf 2% a.a.: R$ 183.245; 7,5% a.a.: R$ 140.027
  medio      com operador sem juros: nao paga; Pronaf 2% a.a.: nao paga; 7,5% a.a.: nao paga
  otimista   sem operador sem juros: R$ 1.035.000; Pronaf 2% a.a.: R$ 929.698; 7,5% a.a.: R$ 710.432
  otimista   com operador sem juros: R$ 795.000; Pronaf 2% a.a.: R$ 714.116; 7,5% a.a.: R$ 545.694
  -- leitura do revisor (revisao-10-demanda.md) --
  rev. pessimista   R$ 3.000 sem operador: sem juros: nao paga; Pronaf 2% a.a.: nao paga; 7,5% a.a.: nao paga | retorno simples (custo min/max): nunca
  rev. medio       R$ 15.000 sem operador: sem juros: R$ 30.000; Pronaf 2% a.a.: R$ 26.948; 7,5% a.a.: R$ 20.592 | retorno simples (custo min/max): 58 / 173 anos
  rev. otimista    R$ 50.000 sem operador: sem juros: R$ 380.000; Pronaf 2% a.a.: R$ 341.338; 7,5% a.a.: R$ 260.835 | retorno simples (custo min/max): 5 / 14 anos
  merenda (min)    R$ 14.200 sem operador: sem juros: R$ 22.000; Pronaf 2% a.a.: R$ 19.762; 7,5% a.a.: R$ 15.101 | retorno simples (custo min/max): 79 / 235 anos
  merenda (max)    R$ 23.700 sem operador: sem juros: R$ 117.000; Pronaf 2% a.a.: R$ 105.096; 7,5% a.a.: R$ 80.310 | retorno simples (custo min/max): 15 / 44 anos
  Quadro de custos desta rodada: R$ 173.357 a R$ 517.865

Receita anual necessaria para empatar (parcela de 10 anos + operacao):
       Custo       sem juros, op 12k       sem juros, op 36k  Pronaf 2% a.a., op 12k  Pronaf 2% a.a., op 36k       7,5% a.a., op 12k       7,5% a.a., op 36k
  R$ 173.357               R$ 29.336               R$ 53.336               R$ 31.299               R$ 55.299               R$ 37.256               R$ 61.256
  R$ 345.611               R$ 46.561               R$ 70.561               R$ 50.476               R$ 74.476               R$ 62.351               R$ 86.351
  R$ 517.865               R$ 63.786               R$ 87.786               R$ 69.652               R$ 93.652               R$ 87.446              R$ 111.446

Taxa de empate, R$ por kg por dia e por caixa de 20 kg por dia (Pronaf 2 %, sem operador pago):
  pessimista custo min  R$ 0.209/kg.dia = R$ 4.17/caixa.dia  (taxa do cenario: R$ 0.03/kg.dia)
  pessimista custo max  R$ 0.464/kg.dia = R$ 9.29/caixa.dia  (taxa do cenario: R$ 0.03/kg.dia)
  medio      custo min  R$ 0.058/kg.dia = R$ 1.16/caixa.dia  (taxa do cenario: R$ 0.06/kg.dia)
  medio      custo max  R$ 0.129/kg.dia = R$ 2.58/caixa.dia  (taxa do cenario: R$ 0.06/kg.dia)
  otimista   custo min  R$ 0.027/kg.dia = R$ 0.54/caixa.dia  (taxa do cenario: R$ 0.10/kg.dia)
  otimista   custo max  R$ 0.060/kg.dia = R$ 1.21/caixa.dia  (taxa do cenario: R$ 0.10/kg.dia)

Ocupacao de empate com a taxa media (R$ 0,06/kg.dia, 240 dias, Pronaf 2 %, sem operador):
  custo min     R$ 173.357: 43 %
  custo medio   R$ 345.611: 70 %
  custo max     R$ 517.865: 97 %

Sensibilidade do resultado anual no cenario medio (Pronaf 2 %, sem operador), custo no ponto medio:
  base: R$ -18.076
  ocupacao 45 % -> 70 %   : R$ -76
  ocupacao 45 % -> 20 %   : R$ -36.076
  taxa 0,06 -> 0,10       : R$ 3.524
  taxa 0,06 -> 0,03       : R$ -34.276
  custo no minimo         : R$ 1.101
  custo no maximo         : R$ -37.252
  cambio: itens ligados ao dolar (modulos, bateria, inversores, maquina) = 29 % a 30 % do subtotal; dolar +20 % -> custo total +6 % a +6 %

Ganho das familias (nao e receita do dono): fruta que passa por ano x R$ 1,00/kg a mais de preco [doc 10 s.6.4]
  pessimista : 25 t/ano -> R$ 25.000 por ano
  medio      : 108 t/ano -> R$ 108.000 por ano
  otimista   : 289 t/ano -> R$ 288.750 por ano

====================================================================================================
5. CUSTO DE OPERACAO POR ANO
====================================================================================================
Starlink (A): R$ 2.268 a R$ 2.988
Manutencao e pecas, 2 a 3 % do subtotal [SUPOSTO]: R$ 3.015 a R$ 12.429
Reposicao de bateria (1/10 por ano) [B]: R$ 833 a R$ 2.600
Operador: R$ 0 (pessoa da associacao) ou R$ 24.000 (dedicado) [doc 10, SUPOSTO]
Limpeza, seguro, licencas: SEM DADO
Soma do que tem numero, sem operador: R$ 6.116 a R$ 18.017  (doc 10 supos R$ 12.000)

====================================================================================================
6. FINANCIAMENTO: parcela anual estimada (tabela Price, 10 anos, sem contar carencia)
====================================================================================================
  Valor financiado         sem juros    Pronaf 2% a.a.         7,5% a.a.
        R$ 150.000         R$ 15.000         R$ 16.699         R$ 21.853
        R$ 250.000         R$ 25.000         R$ 27.832         R$ 36.421
        R$ 450.000         R$ 45.000         R$ 50.097         R$ 65.559
        R$ 173.357         R$ 17.336         R$ 19.299         R$ 25.256
        R$ 517.865         R$ 51.786         R$ 57.652         R$ 75.446
Limites do Pronaf Mais Alimentos (doc 10 s.7): R$ 250 mil por familia; R$ 450 mil para fruticultura.
```
