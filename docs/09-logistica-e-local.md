# 09 — Logística e escolha do local

Autor: agente-logistica. Versão 5, de 17/11/2026 (com a decisão D6 e a seção 9, "Perguntas de campo: o que a pesquisa já responde") (inclui os números acordados com o analista de frutas e demanda; ver `docs/_trabalho/acordo-logistica-demanda.md`). Histórico: refeita depois do parecer do revisor (`docs/_trabalho/revisao-09-logistica.md`) e ajustada às decisões do dono (tabela "Decisões do dono" em `docs/00-premissas.md`).

**Decisões do dono que valem aqui:** D1 — o protótipo é **só manga**, uma zona a 12 °C, 5 t; o caju fica como estudo futuro. D2 — recepção da fruta **das 7h às 14h**. D5 — **um protótipo só, sem CNPJ** por enquanto. D6 — **outras frutas que convivem com a manga a 12 °C** (banana, mamão, acerola; goiaba e maracujá em giro rápido) podem entrar para completar a ocupação; a manga continua a principal e o caju continua fora.
Base: `docs/00-premissas.md`. Este documento não projeta equipamento.

## Como ler este documento

- **[FONTE n]** = número tirado de uma fonte da lista do fim. **[IBGE]** = tabela que eu mesmo baixei e li nesta versão.
- **[CALCULADO]** = conta feita aqui, com os passos à mostra. **[CALCULADO sobre SUPOSTO]** = a conta está certa, mas parte de um número não confirmado.
- **[SUPOSTO]** = estimativa sem fonte conferida. Precisa ser confirmada.
- **[VALIDAR COM PROFISSIONAL HABILITADO]** = só vale depois de confirmado por quem responde tecnicamente ou pelo órgão competente.

### O que consegui abrir e o que não consegui

| Fonte | Situação nesta versão |
|---|---|
| IBGE/SIDRA, tabela 5457 (PAM 2022–2024) | **Aberta e lida.** Manga e castanha de caju de todos os municípios de Pernambuco, totais de PE, BA e Brasil, e cinco municípios baianos do polo |
| MAPA, plano de trabalho do TED 68/2021 (caju no Pajeú) | **Aberto e lido** |
| Embrapa, página "Pedúnculo" (Agência de Informação Tecnológica) | **Aberta e lida** |
| Embrapa, boletim da manga com a PAM 2024 | **Aberto**, lido em parte |
| Conab/Prohort, centrais de abastecimento 2025 | **Aberto**, lido em parte |
| Codevasf (`www.codevasf.gov.br`) | **Não abriu**: o site recusou o acesso (erro 403) |
| INMET (`portal.inmet.gov.br`) | **Não abriu**: o servidor não respondeu |
| CRESESB (`www.cresesb.cepel.br`) | **Não abriu**: erro de certificado; o endereço que funciona parece ser `cresesb.cepel.br`, sem "www", que não está liberado |
| Todas as demais (notícias, estudos, prefeituras) | Só o **trecho mostrado pela busca**, não a página inteira |

Consequência: produção por município agora é dado conferido. Clima oficial, irradiação e os números do Projeto Nilo Coelho continuam de fonte secundária ou de trecho de busca.

---

## Resumo em uma página

1. **Recomendação para o protótipo (só manga): zona rural de Petrolina-PE, em um núcleo do Projeto Senador Nilo Coelho, em terreno de associação ou cooperativa de colonos.** Nota 86,4 de 100; o segundo colocado tem 69,8. A conferência no IBGE reforçou a escolha.
2. **Petrolina tem pequeno produtor de manga**, e muito: cerca de 1.950 lotes familiares, que vendem na roça pelo preço do comprador. O comprador está ao lado (Mercado do Produtor de Juazeiro, 2º do país).
3. **Escala e uso esperado (acordado com o doc 10):** cenário-base de **até 79 t/ano** (um contrato de merenda escolar, cerca de 0,40 t por dia letivo); com mais de um comprador, **108 t de manga** (agosto a março) mais cerca de 54 t de frutas complementares. O 1 t/dia é teto, garantido por cota. Serve a um **grupo de cerca de 10 famílias** (faixa de 5 a 15), cada uma separando parte da colheita.
4. **Três perguntas eliminam o local, e só a visita responde:** já existe câmara fria com vaga? há quem opere e ceda terreno por escrito? o comprador paga mais por manga resfriada? Nenhuma foi verificada.
5. **Recepção das 7h às 14h (D2) — com um alerta novo.** Um capítulo da Embrapa sobre colheita da manga diz que o horário mais conveniente para colher é **entre 10h e 15h**, quando escorre menos látex, e manda evitar o começo da manhã (seção 9, linha 4). Se o produtor seguir isso, boa parte da manga chega **depois das 14h** e dorme fora da câmara. É o ponto mais importante a medir na visita.
6. **Sem CNPJ (D5),** quem vende, emite nota e assina com a merenda escolar é o produtor ou a associação, não o dono do equipamento. O dono cede o uso. A forma de cobrar pelo serviço sem empresa precisa de contador.
7. **Rede elétrica:** o núcleo recomendado provavelmente tem rede [SUPOSTO, não confirmado]. Isso não muda a pontuação, mas muda o sentido do teste: em Petrolina o protótipo prova a tecnologia, não a necessidade de estar fora da rede. Opções na seção 4.4; a decisão é do dono.
8. **Caju: estudo futuro (seção 10).** A versão 1 apontava o Pajeú como lugar do caju; **estava errado**. Pelo IBGE, 81% da castanha do estado está em Buíque (Agreste) e não há caju onde há manga irrigada. O único município com as duas frutas é São José do Belmonte, em volume pequeno.

---

## 1. Onde se produz manga e caju em Pernambuco

Fonte de toda esta seção, salvo indicação: IBGE, Produção Agrícola Municipal, tabela 5457 [IBGE]. Consulta que usei:
`https://apisidra.ibge.gov.br/values/t/5457/n6/in%20n3%2026/v/214,216/p/2022,2023,2024/c782/40143,40262?formato=json`

### 1.1 Manga por município

Pernambuco, 2024: **560.977 t em 20.246 ha**. Brasil: 1.861.362 t. Participação: 560.977 ÷ 1.861.362 = **30,1%** [CALCULADO].

| Município | 2022 (t) | 2023 (t) | 2024 (t) | Área 2024 (ha) | t/ha | Castanha de caju 2024 (t) |
|---|---|---|---|---|---|---|
| Petrolina | 308.000 | 376.000 | 282.000 | 9.400 | 30 | 0 |
| Belém do São Francisco | 140.000 | 154.000 | 179.200 | 6.400 | 28 | 0 |
| Santa Maria da Boa Vista | 33.250 | 32.500 | 42.500 | 1.700 | 25 | 0 |
| Lagoa Grande | 15.000 | 18.900 | 30.000 | 1.200 | 25 | 0 |
| Orocó | — | — | 8.750 | 350 | 25 | 0 |
| Petrolândia | — | — | 4.375 | 125 | 35 | 0 |
| Cabrobó | — | — | 4.000 | 200 | 20 | 0 |
| São José do Belmonte | 400 | 480 | 400 | 20 | 20 | **151** |
| Salgueiro | 130 | 390 | 390 | 30 | 13 | 0 |
| Serra Talhada | — | — | 200 | 10 | 20 | 0 |
| Verdejante | 140 | 140 | 168 | 6 | 28 | 0 |
| Mirandiba | 45 | 45 | 90 | 10 | 9 | 0 |
| Carnaíba | 32 | 36 | 41 | 12 | 3,4 | 50 |

("—" = não extraí o ano. Serra Talhada, Orocó, Petrolândia e Cabrobó de 2024: conferidos pelo revisor na mesma tabela.)

- Sete municípios da beira do São Francisco: 282.000 + 179.200 + 42.500 + 30.000 + 8.750 + 4.375 + 4.000 = **550.825 t = 98,2% do estado** [CALCULADO]. Todo o resto de Pernambuco: 560.977 − 550.825 = **10.152 t**.
- Correções em relação à versão 1: Lagoa Grande tinha 10.000 t (o certo é 30.000 t); o total do estado tinha 540.977 t (o certo é 560.977 t).
- A produção de Petrolina oscila muito de um ano para o outro (376 mil t em 2023, 282 mil t em 2024).
- **Dados de 2025** [IBGE, mesma tabela, conferidos; são os que o doc 10 usa]: Pernambuco 609.940 t em 23.276 ha; Petrolina 286.250 t (11.450 ha); Belém do São Francisco 179.200 t; **Lagoa Grande 66.500 t** (1.900 ha — mais que dobrou em um ano); Santa Maria da Boa Vista 42.500 t; Orocó 10.500 t; Cabrobó 7.400 t; Petrolândia 4.375 t; São José do Belmonte 400 t. A ordem dos municípios muda (Lagoa Grande passa Santa Maria da Boa Vista); a conclusão não.

**O lado baiano do mesmo polo** (a ponte liga Petrolina a Juazeiro) [IBGE, 2024]:

| Município (BA) | Manga (t) | Área (ha) |
|---|---|---|
| Juazeiro | 417.566 | 13.737 |
| Casa Nova | 196.161 | 6.480 |
| Sento Sé | 36.500 | 1.180 |
| Curaçá | 32.120 | 1.114 |
| Sobradinho | 8.731 | 513 |

Soma: **691.078 t** [CALCULADO], mais que os sete municípios pernambucanos. Nenhum deles tem castanha de caju registrada. Segundo o boletim da Embrapa, o Vale do São Francisco passou de 1,24 milhão de t e responde por 67,5% da manga do país [FONTE 1]. O que isso muda para o candidato de Petrolina: (a) o comprador do Mercado do Produtor de Juazeiro tem o dobro de oferta para escolher; (b) as câmaras, cooperativas e packing houses do lado baiano também são concorrência e também são possíveis parceiros (por exemplo a cooperativa Manga Brasil, de Juazeiro [FONTE 9]); (c) vender em Juazeiro é **trânsito interestadual** de fruta (seção 5.2). Não levantei as estruturas de frio do lado baiano.

### 1.2 Manga — quem é pequeno e quem é grande em Petrolina

| Dado | Valor | Fonte |
|---|---|---|
| Lotes irrigados no Distrito Nilo Coelho | 2.326 lotes em 23.448 ha; 84,5% de pequenos produtores (trecho de busca) | [FONTE 6] |
| Usuários do distrito (2012) | 2.309: 1.954 lotes familiares e 355 empresas | [FONTE 8] |
| Área ocupada por colonos | 12.520 ha de 18.667 ha irrigáveis | [FONTE 7] (trecho; o site da Codevasf não abriu) |
| Lote familiar | famílias com 6 a 12 ha; estudo antigo da Embrapa: 6,11 ha irrigáveis em média | [FONTE 9]; [FONTE 59] |
| Estabelecimentos com manga no Submédio São Francisco | 75% têm até 5 ha (IBGE 2009, citado pela Embrapa) | [FONTE 5] |
| Manga no distrito | cerca de 40% do cultivo permanente | [FONTE 6] |
| Rendimento do pequeno | média de 25 t/ha em estudo com 75 produtores do distrito (2014–2018) | [FONTE 60] |

- 12.520 ha ÷ 1.954 lotes = **6,4 ha por lote** [CALCULADO sobre SUPOSTO: fontes de anos diferentes]. Conferência por outro caminho: 2.326 × 0,845 = 1.965 lotes; 12.520 ÷ 1.965 = 6,4 ha.

**Lotes não são toneladas.** Pelo Censo Agropecuário de 2017, só **17% do volume** de manga de Pernambuco saiu da agricultura familiar (doc 10, seção 1.3, tabela 6955 do IBGE). Há muitos lotes familiares, mas a maior parte da fruta é de médios e grandes. Para o protótipo isso não é problema — sobram famílias para formar um grupo de 10 —, mas pesa na hora de pensar em escala.

**Como o pequeno vende hoje** [FONTE 10, estudo da Embrapa de 2023, trecho de busca]: é "tomador de preço"; o comprador vai ao pomar e classifica em primeira, segunda e "arrastão" ou refugo; o pequeno diz não ter estrutura para vender sozinho.

**Quem já tem estrutura:** exportadores e a Aprovale, com packing house e frio [FONTE 11]; as cooperativas do N-6 (Petrolina) e Manga Brasil (Juazeiro), com packing house e câmara fria obtidos por programas federais [FONTE 9] — **não verifiquei se funcionam hoje**. Boa parte dos pequenos não está em cooperativa nem associação [FONTE 12].

### 1.3 Caju

Fora do protótipo por decisão do dono (D1). O que apurei, já corrigido com o IBGE, está na seção 10, "Estudo futuro — caju". Em uma linha: os municípios da manga irrigada têm zero castanha de caju registrada; o caju de Pernambuco está em Buíque, no Agreste.

### 1.4 A conta de escala da manga (refeita)

Quantos lotes familiares a câmara atende, em um ano:

- Lote: 6,4 ha (seção 1.2). Parte do lote com manga: 40% [SUPOSTO — é a participação da manga no cultivo permanente do distrito inteiro (FONTE 6), não uma medida por lote]. 6,4 × 0,40 = **2,56 ha de manga**.
- Rendimento do pequeno: 25 t/ha [FONTE 60]. 2,56 × 25 = **64 t de manga por lote por ano**.
- Câmara: 1 t/dia × 250 dias = 250 t/ano [SUPOSTO para os 250 dias].
- 250 ÷ 64 = **3,9 lotes** [CALCULADO sobre SUPOSTO].

| Hipótese | Lotes atendidos |
|---|---|
| Lote inteiro com manga, 25 t/ha, 250 dias (versão 1) | 1,6 |
| 40% com manga, 30 t/ha, 250 dias | 3,5 |
| **40% com manga, 25 t/ha, 250 dias (caso central)** | **3,9** |
| 40% com manga, 25 t/ha, 365 dias | 5,7 |

**Faixa honesta: de 2 a 6 lotes, valor central perto de 4.** A versão 1 dizia "cerca de dois lotes"; era o extremo da faixa.

**O que limita de verdade é o pico, não o ano.** A manga irrigada é colhida por talhão, em poucas semanas. Se um lote colhe suas 64 t em 3 semanas [SUPOSTO — não achei fonte para a duração da colheita do pequeno]: 64 ÷ 21 = **3 t/dia, três vezes o que a câmara aceita**. Por isso a operação precisa de **cota diária por produtor** (seção 6) e a pergunta 3 da seção 8 ("em quantos dias o senhor colhe um talhão?") é a mais importante da visita.

**Outra medida da família (Censo 2017):** em Petrolina, 734 estabelecimentos familiares colheram 15.646 t de manga, cerca de **21 t cada** (conta do revisor do doc 10, tabela 6955 do IBGE). É bem menos que as 64 t acima, porque inclui pomar pequeno e de sequeiro e é de 2017. Fico com 64 t para o colono irrigado e registro 21 t como limite inferior (divergência 6 do acordo).

**Giro esperado (número do doc 10, adotado aqui):** os 250 t acima são o **teto**. O que se espera de fato, no cenário médio do analista de frutas e demanda, é **108 t por ano** (estoque médio de 2,25 t, permanência de 5 dias, 240 dias de operação) [SUPOSTO; doc 10, seção 6.2]; a faixa vai de 25 t (pessimista) a 289 t (otimista, só com outras frutas). Com 10 famílias: 108 ÷ 10 = cerca de **11 t por família por ano, um sexto das 64 t de um lote** [CALCULADO sobre SUPOSTO].

Conclusão que continua de pé: no polo irrigado a câmara serve a um grupo pequeno que separa **parte** da fruta para vender melhor. Para comparar: Petrolina colhe 282.000 t/ano; 250 t são 0,09%.

### 1.5 Calendário de uso (número do doc 10, adotado aqui)

O calendário de ocupação é do analista de frutas e demanda (`docs/10-frutas-e-demanda.md`, seção 2.4). A versão anterior deste documento dizia "manga o ano todo"; **corrijo**: há manga irrigada o ano todo, mas de abril a julho ela é pouca, cara (R$ 4,94/kg em junho de 2026 contra R$ 0,99/kg em fevereiro, segundo o Cepea citado no doc 10) e vendida na hora. Não há o que guardar.

| Mês | Jan | Fev | Mar | Abr | Mai | Jun | Jul | Ago | Set | Out | Nov | Dez |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Uso (só manga) | alto | médio | médio | parado | parado | parado | parado | médio | médio | alto | alto | alto |
| Estoque médio (t) | 3,0 | 1,5 | 1,5 | 0 | 0 | 0 | 0 | 1,5 | 1,5 | 3,0 | 3,0 | 3,0 |
| Entrada média (t/dia) | 0,6 | 0,3 | 0,3 | 0 | 0 | 0 | 0 | 0,3 | 0,3 | 0,6 | 0,6 | 0,6 |

Os níveis (alto, médio, muito baixo) são do doc 10. Os números por mês são a minha tradução deles, feita para fechar com o cenário médio dele: ocupação média de (4 × 60% + 4 × 30%) ÷ 8 = 45% e 0,6 × 120 + 0,3 × 120 = **108 t no ano** [CALCULADO sobre SUPOSTO]. Tudo [SUPOSTO]: nenhum de nós achou calendário de colheita do pequeno produtor de Petrolina (pergunta 3 da seção 8).

**Com as frutas complementares (decisão D6)** — níveis do doc 10 (seção 2.4: "média" de abril a julho, "média a alta" em fevereiro e março, "média" em agosto e setembro); números meus, a confirmar pelo analista de frutas [SUPOSTO]:

| Mês | Jan | Fev | Mar | Abr | Mai | Jun | Jul | Ago | Set | Out | Nov | Dez |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manga, entrada (t/dia) | 0,6 | 0,3 | 0,3 | 0 | 0 | 0 | 0 | 0,3 | 0,3 | 0,6 | 0,6 | 0,6 |
| Complementares, entrada (t/dia) | 0 | 0,15 | 0,15 | 0,3 | 0,3 | 0,3 | 0,3 | 0,15 | 0,15 | 0 | 0 | 0 |
| Total (t/dia) | 0,6 | 0,45 | 0,45 | 0,3 | 0,3 | 0,3 | 0,3 | 0,45 | 0,45 | 0,6 | 0,6 | 0,6 |
| Estoque médio (t), 5 dias | 3,0 | 2,25 | 2,25 | 1,5 | 1,5 | 1,5 | 1,5 | 2,25 | 2,25 | 3,0 | 3,0 | 3,0 |
| Quais complementares | — | acerola, goiaba | acerola, goiaba | acerola, goiaba, maracujá | idem | idem | idem | acerola, goiaba | acerola, goiaba | — | — | — |

Soma: manga 108 t + complementares (0,3 × 120 + 0,15 × 120 = 54 t) = **162 t por ano**, ocupação média de 45% nos 12 meses [CALCULADO sobre SUPOSTO]. **É teto de uso com mais de um comprador, não previsão.** Acerola, goiaba e maracujá só em giro rápido, porque a 12 °C ficam fora do ideal delas, e todas são "candidatas a testar": nenhuma tem vida útil a 12 °C com fonte, e fruta madura solta etileno que adianta a manga verde-madura (revisor do doc 10). **Banana fora** até ensaio: dano por frio abaixo de cerca de 13 °C.

**Cenário-base (acordado):** um contrato de merenda escolar com teto de **79 t por ano** (10 famílias × R$ 40.000 ÷ R$ 5,06/kg), cerca de **0,40 t por dia letivo** em cerca de 200 dias, sem janeiro. Quanto a prefeitura compra de fato é a pergunta 1 da visita (seção 9).

**De onde viriam, no raio de coleta do local recomendado** [IBGE, tabela 1613, Petrolina, 2025, conferida]: banana 41.600 t; goiaba 48.000 t; acerola 30.000 t; maracujá 1.980 t. **Mamão: não há produção registrada em Petrolina**; o mais próximo é Lagoa Grande (3.680 t, segundo o doc 10), a cerca de 55 km [SUPOSTO], fora do raio de 10 a 15 km. São culturas dos mesmos lotes irrigados do Nilo Coelho (o distrito cita goiaba entre as principais [FONTE 7]); **se o núcleo escolhido as tem, e em que meses, é pergunta de campo** (pergunta 20b).

**Muda o horário de chegada?** Pouco, e para melhor: acerola e goiaba costumam ser colhidas cedo [SUPOSTO], então chegam dentro da janela de 7h às 14h. **Muda o grupo?** O tamanho não (cerca de 10 famílias); a composição pode mudar de abril a julho, se quem tem banana ou acerola não for quem tem manga. Ressalvas de logística que mantenho: banana viaja verde e sem frio, e boa parte da acerola vai para a indústria no mesmo dia — não há prova de que alguém pague para guardá-las.

Consequência prática: **o protótipo precisa estar instalado antes de outubro** para ser testado no pico da manga.

---

## 2. Para onde a fruta vai

Preço do serviço, receita e viabilidade são do analista de frutas e demanda. **Não levantei preços: preço não encontrado** (manga na roça, no Mercado do Produtor, na CEASA-PE, no PNAE). Sem diferença de preço não se sabe se tirar a fruta do circuito "vende na roça" compensa.

### 2.1 Centrais de abastecimento

| Destino | Dado | Fonte |
|---|---|---|
| Mercado do Produtor de Juazeiro (BA) | 1.620.627 t em 2025, R$ 6,11 bilhões; 2º do país em volume | [FONTE 63] — Conab/Prohort, documento aberto |
| CEASA-PE, Recife | 826.427 t em 2025; 7º do país | [FONTE 63] |
| CEASA-PE, Caruaru | Citada no relatório da Conab; não extraí o volume. A central municipal (Ceaca) fica na BR-104, km 71; horário divergente entre fontes | [FONTE 63][FONTE 35] |
| Central em Petrolina | **Lacuna: não pesquisei.** O atacado regional se faz em Juazeiro | — |
| Central em Serra Talhada, Arcoverde ou Salgueiro | Não encontrei | — |
| Feiras da agricultura familiar | **Lacuna: não levantei** | — |

Caixa: uso a caixa de **20 kg do projeto térmico** (`docs/01-projeto-termico.md`): 1 t = 50 caixas; 5 t = 250 caixas. No comércio do Recife a manga é cotada em caixa de 23 a 27 kg [FONTE 26]. 

### 2.2 Distâncias por rodovia

| Trecho | Distância | Marcação |
|---|---|---|
| Petrolina – Recife | 715 km, 9h56 de carro | [FONTE 36] |
| Petrolina – Caruaru | 583 km | [FONTE 36] |
| Núcleos do Nilo Coelho – Mercado do Produtor de Juazeiro | 10 a 40 km | [SUPOSTO] |
| Santa Maria da Boa Vista – Petrolina | cerca de 110 km | [SUPOSTO] |
| Lagoa Grande – Petrolina | cerca de 55 km | [SUPOSTO] |
| São José do Belmonte – Recife | 474 km | [FONTE 65, trecho de busca] |
| São José do Belmonte – Serra Talhada / Salgueiro | cerca de 60 a 80 km cada | [SUPOSTO] |
| Serra Talhada – Recife | cerca de 415 km | [SUPOSTO] |

Todas as distâncias [SUPOSTO] são de memória: **conferir no mapa antes de usar.**

### 2.3 Polpa e suco

Sem mudança em relação à versão 1, tudo de trecho de busca e sem dado atual: indústria de polpa em Petrolina com cerca de quinze frutas [FONTE 37]; cooperativa baiana que processa cerca de 70 t de manga por ano com 285 cooperados [FONTE 40]; polpa em assentamentos de Serra Talhada [FONTE 41]. Fruta para polpa paga menos e não precisa de câmara.

### 2.4 Compras públicas

- **PNAE:** teto de R$ 40.000 por agricultor (CAF), por ano, por entidade executora — Resolução FNDE nº 04/2026 [FONTE 43]. Segundo a imprensa, a resolução foi alterada pela Resolução CD/FNDE nº 17, de 22/10/2026, mantendo o teto [FONTE 66, trecho de busca]. **Conferir o texto vigente.**
- 10 famílias × R$ 40.000 = R$ 400.000 por ano [CALCULADO] é **teto legal, não demanda**: nada indica que uma prefeitura compre esse valor em manga. Quanto ela compra é a pergunta 25 da seção 8.
- **PAA:** R$ 15.000 por família por ano e R$ 1,5 milhão por organização, segundo notícia e decreto [FONTE 45]. [VALIDAR na Conab]
- A prefeitura de São José do Belmonte declara comprar da agricultura familiar para a merenda [FONTE 44].
- **Efeito da decisão D5 (sem CNPJ):** PNAE e PAA compram do agricultor com CAF ou da organização dele. O dono do equipamento não entra como vendedor. Isso combina com o modelo proposto (a associação opera e vende), mas a cobrança pelo uso da câmara, sem empresa, precisa de orientação de contador. [VALIDAR COM PROFISSIONAL HABILITADO]

---

## 3. Critérios de escolha

A versão 1 somava tudo numa tabela só. O revisor apontou, e eu concordo, que três fatores não são "pontos a mais": se falharem, o local cai. Separei.

### 3.1 Critérios eliminatórios (sim ou não, respondidos em campo)

| # | Pergunta | Se a resposta for esta, o local cai |
|---|---|---|
| E1 | Já existe câmara fria com vaga e preço que o pequeno consegue pagar? | **Sim** — o problema local não é falta de frio |
| E2 | Há associação ou cooperativa que aceita operar e ceder o terreno por escrito? | **Não** |
| E3 | Há comprador que paga mais por fruta resfriada e entregue em dia certo? | **Não** |

**Nenhum dos três foi verificado para nenhum candidato.** Não levantei as câmaras existentes em nenhum local.

### 3.2 Critérios com peso (somam 100)

Pesos são decisão minha [SUPOSTO]; o dono pode mudar. Como o protótipo é só manga (D1), **saiu o critério "ter as duas frutas"**; seus 10 pontos foram para o raio de coleta e para o encaixe de escala.

| # | Critério | Peso | Observação |
|---|---|---|---|
| 1 | Distância e estrada até os produtores | 20 | |
| 2 | Distância até os compradores | 15 | |
| 3 | Meses por ano com pelo menos 1 t/dia de manga ao alcance | 15 | Volume acima de 1 t/dia não vale ponto a mais |
| 4 | Encaixe de escala: há pequenos produtores do tamanho da câmara | 20 | |
| 7 | Sol e clima | 5 | **Sem dado de irradiação** |
| 8 | Água | 7 | |
| 9 | Segurança | 3 | **Sem dado** |
| 10 | Céu aberto para Starlink | 2 | **Sem dado** |
| 11 | Acesso de caminhão | 13 | |

"Cooperativa para operar" e "concorrência de câmaras", pedidos na definição da tarefa, viraram os eliminatórios E2 e E1.

---

## 4. Candidatos, pontuação e recomendação

### 4.1 Os quatro candidatos (manga)

| | Local | Manga 2024 [IBGE] | A favor | Contra |
|---|---|---|---|---|
| A | **Petrolina — núcleo do Projeto Senador Nilo Coelho** | 282.000 t em 9.400 ha | Cerca de 1.950 lotes familiares; Mercado do Produtor ao lado; uso de agosto a março [SUPOSTO]; asfalto; água de canal; técnico de refrigeração na cidade [SUPOSTO] | Frio já existe na região (E1 em dúvida); câmara pequena para o colono; concorrência do lado baiano |
| B | **Belém do São Francisco** | 179.200 t em 6.400 ha | Segundo do estado; associações de agricultores familiares, uma em ilha [FONTE 46] | **Não sei se a manga é de empresa ou de pequeno**; longe dos compradores; fruta de ilha depende de barco |
| C | **Santa Maria da Boa Vista / Lagoa Grande** | 42.500 t e 30.000 t (72.500 t) | Mesmo polo, a cerca de 55 a 110 km de Petrolina [SUPOSTO]; área de manga em crescimento (Lagoa Grande dobrou de 2022 a 2024) | **Não levantei quem produz** (colonos, assentados ou empresas); menos estrutura e menos técnicos que Petrolina [SUPOSTO] |
| D | **São José do Belmonte** | 400 t em 20 ha | Produção pequena, do tamanho da câmara: 400 t em cerca de 120 dias de safra [SUPOSTO] = 3 t/dia no município; merenda compra da agricultura familiar [FONTE 44]; é o único com caju também (estudo futuro) | Poucos meses de uso; longe dos mercados; não sei de quem é a manga; água [SUPOSTO] escassa |

Saíram da lista, por não terem manga: Buíque–Tupanatinga e Carnaíba–Flores (ver seção 10).

### 4.2 Tabela de pontuação

Notas de 1 a 5. **Todas são julgamento meu.** Com asterisco (*): nota dada **sem dado nenhum**. Pontos = nota × peso ÷ 5.

| Critério | Peso | A Petrolina | B Belém S.F. | C S.M. Boa Vista / Lagoa Grande | D S.J. Belmonte |
|---|---|---|---|---|---|
| 1 Raio de coleta | 20 | 5 | 3* | 3* | 3* |
| 2 Compradores | 15 | 5 | 2 | 4* | 2 |
| 3 Meses com 1 t/dia | 15 | 5 | 4 | 4 | 2 |
| 4 Encaixe de escala | 20 | 2 | 2* | 2* | 4 |
| 7 Sol e clima | 5 | 5* | 5* | 5* | 4* |
| 8 Água | 7 | 5 | 5 | 5 | 2* |
| 9 Segurança | 3 | 3* | 3* | 3* | 3* |
| 10 Starlink | 2 | 4* | 4* | 4* | 4* |
| 11 Caminhão | 13 | 5 | 3* | 4* | 3* |
| **Total (0 a 100)** | 100 | **86,4** | 61,2 | 69,8 | 58,0 |

Conferência da coluna A: (5×20 + 5×15 + 5×15 + 2×20 + 5×5 + 5×7 + 3×3 + 4×2 + 5×13) ÷ 5 = 432 ÷ 5 = 86,4 [CALCULADO].

**Como ler, com franqueza:**
- Petrolina vence com folga e venceria com quase qualquer peso (o revisor testou e chegou à mesma conclusão).
- Boa parte da vantagem vem de critérios que medem "estar num polo desenvolvido" (1, 2, 8 e 11: 55 pontos). Nos candidatos B, C e D quase todas as notas têm asterisco: **a distância entre eles e Petrolina é em boa parte falta de informação minha, não defeito comprovado do local.**
- O ponto fraco de Petrolina é o critério 4 (nota 2): o colono é grande para a câmara. É o que a cota diária tenta resolver.
- A soma não cobre os três eliminatórios. Um "sim" em E1 derruba Petrolina mesmo com 86 pontos.

### 4.3 Recomendação

**Zona rural de Petrolina-PE, dentro ou na borda de um núcleo do Projeto Senador Nilo Coelho, em terreno de associação ou cooperativa de colonos, a menos de 40 km do Mercado do Produtor de Juazeiro.** O núcleo exato só se escolhe em visita. Pontos de partida para conversa: Cooperativa do N-6 [FONTE 9] e associação de agricultores familiares do N-3 [FONTE 48]; não verifiquei a situação de nenhuma.

**Por quê:**
1. É onde há, com dado, muitos pequenos produtores de manga juntos e vendendo em posição fraca.
2. O comprador está ao lado.
3. Há manga para guardar em cerca de oito meses do ano, de agosto a março [SUPOSTO; doc 10]. Os outros candidatos do mesmo polo têm o mesmo calendário; São José do Belmonte teria menos.
4. Para um **protótipo único** (D5), pesa ter asfalto, água, técnico de refrigeração e loja de peças na cidade [SUPOSTO]: o primeiro equipamento vai precisar de ajuste.
5. É o clima mais quente e ensolarado entre os candidatos: se funciona lá, funciona nos outros.

**Para que ele serve nesse local:** para um **grupo de cerca de 10 famílias (5 a 15), com cota diária**, tirar 1 t por dia do circuito "vende na roça" e entregar manga resfriada, em dia marcado, a quem paga mais: merenda escolar, PAA, varejo local, boxes do Mercado do Produtor.

**O que derruba a recomendação:**
- Qualquer dos três eliminatórios (E1, E2, E3) dar errado na visita.
- O DINC ou a Codevasf não autorizarem a instalação no perímetro.
- A visita mostrar que o colono colhe tudo em poucos dias e não aceita cota.
- Os compradores do mercado interno não valorizarem manga resfriada (muita manga de mercado interno viaja sem frio [SUPOSTO]).

**Condições combinadas com o doc 10 para seguir:** um comprador com compromisso por escrito (pelo menos 50 t por ano), uma associação que opere e ceda o terreno, pelo menos 8 de 15 produtores dispostos a pagar, e nenhuma câmara fria com vaga por perto.

**Alternativas, em ordem:** C (Santa Maria da Boa Vista / Lagoa Grande), se em Petrolina o frio já sobrar; D (São José do Belmonte), se o dono preferir um lugar onde a câmara seja do tamanho da produção local e onde o caju possa ser estudado depois; B (Belém do São Francisco), só depois de uma visita para descobrir quem são os pequenos.

---

### 4.4 O local recomendado tem rede elétrica? O que isso muda

O analista de frutas e demanda perguntou, com razão, se um protótipo "fora da rede" faz sentido num polo irrigado que tem energia.

**O que sei:** não confirmei. Os onze núcleos habitacionais do projeto têm escolas, postos de saúde e comércio [FONTE 69, trecho de busca], então **é razoável supor que o núcleo tem rede** [SUPOSTO]. A energia do bombeamento é do distrito e é rateada na tarifa de água [FONTE 70, trecho de busca]; isso não diz se cada lote tem ligação própria, se é trifásica ou se é estável. A página da Codevasf não abriu. Quem responde é o DINC ou a visita (pergunta 20a).

**O que isso significa:** nenhum critério da minha pontuação mede "falta de rede". Petrolina ganhou por fruta, comprador e acesso. Se houver rede no terreno, ali o protótipo **prova a tecnologia** (funcionar só com sol e gelo), mas **não prova a necessidade**: uma câmara comum na tomada seria mais barata, como aponta o doc 10. As opções, sem escolher:

| Opção | A favor | Contra |
|---|---|---|
| A. Petrolina, fora da rede mesmo com rede perto | Fruta, comprador, asfalto e técnico à mão; a rede próxima serve de plano B se o protótipo falhar com fruta dentro; clima mais severo | Não prova o mercado do "fora da rede"; o usuário pode perguntar por que não ligar na tomada |
| B. Mesmo polo, em ponto de rede fraca ou ausente (ilhas de Belém do São Francisco, ponta de linha, assentamentos) | Testa tecnologia e necessidade juntas, sem sair da manga | **Não sei se esses pontos existem com manga de pequeno produtor**; exige visita; mais longe de comprador e de técnico |
| C. Município de sertão com rede pior (por exemplo São José do Belmonte) | Necessidade mais crível; produtor do tamanho da câmara | Pouca manga, poucos meses, longe do comprador; a rede de lá também não foi verificada |
| D. Petrolina, solar com a rede como apoio | Mais barato e mais seguro para a fruta | Deixa de ser "fora da rede": muda a razão de ser do projeto; a decisão D4 do dono (bateria, sem gerador) aponta no sentido contrário |

Se o dono quiser que a falta de rede pese na escolha, é preciso criar esse critério e levantar a qualidade da rede em cada candidato. **Esse dado hoje não existe para nenhum deles.**

---

## 5. Requisitos do terreno e da instalação

Orientação de logística. As dimensões de equipamento são do projeto térmico e do integrador solar.

### 5.1 Terreno

O projeto térmico cresceu para cerca de **11 a 12 kWp de painéis** e um tanque de gelo de várias centenas de quilos (`docs/01-projeto-termico.md`, que está sendo refeito para só manga e recepção até as 14h). A área da versão 1 (300 a 500 m²) foi suposta para 5 kWp e **está superada**. Se o número de painéis mudar, a área muda junto.

| Parcela | Área | Marcação |
|---|---|---|
| Painéis: 11 a 12 kWp | 55 a 65 m² de módulos (estimativa do revisor). No chão, com corredores e afastamento: cerca de 100 a 120 m² | [SUPOSTO] — o integrador define |
| Contêiner de 20 pés | cerca de 15 m² (6,1 m × 2,4 m), mais 1,5 m livre em volta: cerca de 50 m² | [SUPOSTO] |
| Máquinas e tanque de gelo, do lado de fora | 15 a 25 m², com o afastamento que o projeto térmico pedir | [SUPOSTO] |
| Recepção coberta (balança, mesa de seleção, caixas vazias) | 40 a 60 m² | [SUPOSTO] |
| Pátio de manobra de caminhão de dois eixos | 200 a 300 m² | [SUPOSTO] |
| **Total** | **cerca de 600 a 800 m²**, por exemplo 20 m × 35 m | [SUPOSTO] |

**Os painéis não cabem em cima do contêiner** (60 m² contra 15 m² de teto). Ou vão para estrutura própria no chão, ou cobrem a recepção e o contêiner numa estrutura maior. Usar painel como telhado é decisão de estrutura, vento, ventilação das máquinas e afastamento do gás: **[VALIDAR COM PROFISSIONAL HABILITADO]**. Não tratar como dado.

| Item | Requisito | Marcação |
|---|---|---|
| Piso e base | Terreno firme, plano, que não alague. Contêiner sobre sapatas ou laje niveladas, acima do chão. Recepção com piso lavável, caimento e ralo — **o ralo longe das máquinas a gás** | [VALIDAR COM PROFISSIONAL HABILITADO] |
| Sombra | Nenhuma sombra sobre os painéis das 8h às 16h, o ano todo. Contêiner e recepção, ao contrário, na sombra | [VALIDAR] com o integrador |
| Posição em relação ao sol | Painéis voltados para o norte, pouco inclinados. Porta da câmara para o sul ou para a área coberta, nunca para o oeste | [VALIDAR] com o integrador |
| Acesso | Caminhão de dois eixos o ano todo; portão de 4 m ou mais; encostar de ré na porta | [SUPOSTO] |
| Entrega do contêiner | Caminhão com guindaste ou prancha: vão livre, sem fio baixo | [SUPOSTO] |
| Cerca e vigilância | Cerca, portão com cadeado, iluminação, casa habitada à vista | [SUPOSTO] |
| Água | Limpa, para lavar caixas, piso e mãos. Água de canal não é potável | [VALIDAR] com a vigilância sanitária |
| Resíduos | Destino para água de lavagem e fruta descartada (fruta apodrecendo atrai mosca-das-frutas) | [VALIDAR] |
| Starlink | Céu aberto; testar obstrução com o aplicativo antes de fechar o terreno | [SUPOSTO] |

### ⚠ SEGURANÇA — o que o terreno precisa permitir

- **Gás inflamável.** Pela decisão D3 do dono não haverá circuito de propano montado no local; pode haver **unidade selada de fábrica com gás inflamável**. Nesse caso as máquinas ficam do lado de fora, afastadas da porta e de ralos, **ao ar livre**, longe de fogão, queima de lixo e fumantes, e **nunca sob cobertura fechada**. Não encostar em casa, cozinha comunitária ou depósito de defensivos. [VALIDAR COM PROFISSIONAL HABILITADO]
- **Tensão contínua.** Os painéis ficam energizados sempre que há sol, mesmo com tudo desligado. Área de painéis e cabos cercada, sinalizada, fora do alcance de crianças.
- **Vento.** 60 m² de painéis são uma vela. A estrutura e a fundação precisam de cálculo. [VALIDAR COM PROFISSIONAL HABILITADO]
- **Raio.** Estrutura metálica em campo aberto pede aterramento e proteção contra descargas. [VALIDAR COM PROFISSIONAL HABILITADO]
- **Espaço fechado e falta de oxigênio.** Fruta respira e solta gás carbônico; numa câmara fechada o ar fica pobre em oxigênio. Porta que abre por dentro, ventilar antes de entrar, ninguém entra sozinho. Seguir o procedimento do projeto térmico.
- **Caminhão de ré.** Pátio de manobra separado de onde as pessoas descarregam à mão.

### 5.2 Licenças, cadastros e papéis

Não abri as normas. A lista é do que **perguntar**. Tudo [VALIDAR COM PROFISSIONAL HABILITADO] ou no próprio órgão.

| Onde | O que perguntar |
|---|---|
| Associação ou cooperativa | Ata de assembleia; contrato escrito de cessão de uso com prazo, quem paga o quê, de quem é o equipamento, o que acontece se a parceria acabar, **quem responde pela fruta perdida se o equipamento falhar** |
| DINC e Codevasf | É permitido instalar dentro do perímetro? Em que tipo de área? |
| Prefeitura | Alvará; licença de obra para contêiner; uso do solo rural |
| Vigilância sanitária municipal | Exigências para armazenar fruta in natura de terceiros |
| Adagro | Há controle obrigatório de mosca-das-frutas no Vale [FONTE 49]. Um ponto que junta fruta de vários produtores precisa de cadastro como unidade de consolidação? Para vender em Juazeiro-BA (outro estado) é preciso Permissão de Trânsito de Vegetais e Certificado Fitossanitário de Origem? |
| CPRH | Dispensa de licenciamento ambiental para esse porte |
| Corpo de Bombeiros | Exigências com gás inflamável |
| Contador | **Sem CNPJ (D5):** como o dono pode ceder o equipamento e ser remunerado; quem emite a nota da fruta; acesso a PNAE e PAA exige CAF [FONTE 43] |
| Inmetro | Balança aferida, se houver compra e venda por peso |

---

## 6. Modelo de operação em uma página

**Resfriar rápido, guardar pouco, sair em carga fechada. Manga como fruta principal (D1), a 12 °C; frutas complementares autorizadas (D6).**

| Pergunta | Resposta | Marcação |
|---|---|---|
| Quem entrega | Cerca de 10 famílias com CAF (faixa de 5 a 15), raio de 10 a 15 km, em carro, moto com carreta ou trator, em caixas de 20 kg da associação | [SUPOSTO] |
| Quanto cada um entrega | **Cota diária** combinada na véspera, somando no máximo 1 t (50 caixas de 20 kg). Sem cota, um só lote em colheita entrega 3 t/dia (seção 1.4) | [CALCULADO sobre SUPOSTO] |
| Quanto entra de fato | **Média de 0,45 t/dia** nos 240 dias de operação (0,6 t/dia de outubro a janeiro; 0,3 t/dia em fevereiro, março, agosto e setembro); **1 t/dia é teto, não rotina** | [SUPOSTO; doc 10] |
| A que horas colhem | Há duas orientações em conflito: meio do dia, por causa do látex [FONTE 80]; horas mais frescas, por causa do calor [FONTE 50] | fontes divergentes |
| **A que horas a manga chega** | **Entre 9h e 16h.** A Embrapa (capítulo de 2002) indica colher **entre 10h e 15h**, quando há menos látex, e evitar o começo da manhã [FONTE 80]; uma exportadora, ao contrário, passou a priorizar as horas mais frescas [FONTE 50]. Não sei qual prática o pequeno segue | **[SUPOSTO]** — só a visita responde |
| **Horário de recepção** | **Das 7h às 14h** | **Decisão D2 do dono** |
| Manga que chega depois das 14h | Espera à sombra, em caixa aberta, e entra na manhã seguinte a partir das 7h. Regra combinada com o grupo: **colher cedo e sair da roça até as 13h** | regra proposta |
| Temperatura da fruta na chegada | **30 °C** como valor de projeto (o da premissa); pode chegar a 35 °C em manga colhida perto do meio-dia | [SUPOSTO] — medir na visita |
| Quanto tempo fica | **5 dias em média** (faixa de 2 a 5). A manga aguenta 2 a 3 semanas a 12 °C, mas guardar 14 dias derruba o giro para 5 t ÷ 14 = 0,36 t/dia | [SUPOSTO; doc 10] |
| Quem busca | Comprador com caminhão em dias fixos (por exemplo segunda, quarta e sexta), ou frete do grupo até o Mercado do Produtor e as escolas | [SUPOSTO] |
| Quem opera | Uma pessoa da associação que já trabalha no local, **sem salário dedicado**, com ajuda de custo saída da taxa, e substituto treinado: abre, pesa, anota, confere temperatura, limpa. (Acordado com o doc 10; minha ressalva: abrir das 7h às 14h todo dia sem pagamento certo é risco de porta fechada — divergência 3 do acordo) | [SUPOSTO] |
| Quem vende e emite nota | O produtor ou a associação. O dono do equipamento não tem CNPJ (D5) e não compra nem vende fruta | D5 + [VALIDAR com contador] |
| Quem paga a operação | O grupo, pela associação: taxa por quilo movimentado ou desconto na venda. Referência do doc 10: **R$ 0,06 por kg por dia** (R$ 1,20 por caixa de 20 kg por dia; R$ 0,30 por kg em 5 dias). Produtor isolado que vende na roça não é cliente | [SUPOSTO; doc 10] |

**Como isso encaixa em 1 t/dia e 5 t:**
- Estoque = entrada diária × dias de permanência. No teto: 1 t/dia × 5 dias = 5 t, câmara cheia. No esperado: 0,45 t/dia × 5 dias = 2,25 t; no pico, 0,6 × 5 = 3 t [CALCULADO].
- Retirada três vezes por semana: cerca de 1 t por viagem no esperado (0,45 t/dia × 7 ÷ 3), 2 a 3 t no teto. **É carga de caminhonete ou caminhão pequeno, não de caminhão toco** [CALCULADO]. Retirada uma vez por semana: 5 t de uma vez, câmara no limite e nenhuma folga para atraso [CALCULADO].
- **Regra: marcar a retirada antes de aceitar a fruta.** Fruta sem comprador marcado não entra.

**Efeito da janela de 7h às 14h para o projeto térmico:** a carga de fruta quente entra junto com o sol alto, o que é bom para um sistema movido direto pelos painéis; mas a fruta que entra às 13h ou 14h ainda está esfriando quando o sol acaba. O gelo tem de ser dimensionado para isso (é o que D2 determina). Se a visita mostrar que quase tudo chega antes das 11h, há folga; se mostrar que quase tudo chega depois das 13h, a regra "sair da roça até as 13h" passa a ser essencial.

**O que a câmara não faz:** não amadurece, não lava, não classifica, não vende. Precisa, ao lado, de recepção coberta com mesa de seleção e balança.

### ⚠ SEGURANÇA — operação

- Ninguém entra na câmara sozinho; porta abre por dentro; ventilar antes de entrar (fruta respira e o ar fica pobre em oxigênio).
- Pilha de caixas só até a altura do projeto.
- Operador não mexe em painel, quadro elétrico ou tubulação de gás. Defeito: desligar pelo procedimento e chamar o técnico.

---

## 7. Dados de interface para as outras disciplinas

| Dado | Valor | Marcação |
|---|---|---|
| Local | **Petrolina-PE**, zona rural, núcleo do Projeto Senador Nilo Coelho, a definir em visita | Recomendação provisória |
| Fruta | Só manga, uma zona a 12 °C, 5 t | Decisão D1 |
| Coordenadas | Cerca de 9,4° S, 40,5° O; altitude cerca de 370 a 380 m | [SUPOSTO] |
| Temperatura média anual | Acima de 26 °C; 26,6 °C | [FONTE 52][FONTE 53] |
| Máxima média de outubro e novembro | Cerca de 34 °C | [FONTE 54][FONTE 55] — fontes secundárias |
| **Maior temperatura encontrada** | **41,0 °C em 22/09/2021** (Apac), a maior de Pernambuco naquele ano; reportagem de 2019 dava 41 °C como recorde do estado | [FONTE 67, trecho de busca] |
| Premissa de 40 °C | **Não está acima do recorde: é ultrapassada em dias extremos.** Fica cerca de 6 °C acima da máxima média do mês mais quente. Manter ou não é decisão do engenheiro térmico e do dono, não da logística | dado + ressalva |
| Chuva; horas de sol | Cerca de 443 mm/ano; cerca de 2.845 h/ano | [FONTE 53] — fonte secundária |
| Normais oficiais do INMET | **Não obtidas** (site não respondeu) | pendência |
| Irradiação (kWh/m²·dia) | **Não obtida** (CRESESB não abriu) | pendência do integrador |
| Horário de recepção | 7h às 14h | Decisão D2 |
| Horário provável de chegada | **Entre 9h e 16h.** Se o produtor colher entre 10h e 15h, como recomenda um capítulo da Embrapa [FONTE 80], a maior parte chega entre 11h e 16h, isto é, **parte depois do fechamento das 14h**. Caso a verificar pelo térmico: 1 t inteira entrando entre 13h e 14h | **[SUPOSTO]**, com apoio parcial de fonte |
| Temperatura da fruta na chegada | **30 °C** (valor único de projeto). Sensibilidade a 35 °C: 1.000 kg × 3,77 kJ/kg·K × 5 K = 18.850 kJ = **5,2 kWh de frio a mais por dia** | [SUPOSTO] + [CALCULADO pelo revisor] |
| Meses de uso | Manga: **agosto a março** (alto de outubro a janeiro). Abril a julho: só frutas complementares (D6), uso médio a baixo | [SUPOSTO; doc 10] |
| Fruta por ano | **Base: até 79 t** (um contrato de merenda). Com mais de um comprador: 108 t de manga + cerca de 54 t de complementares = cerca de 162 t | [CALCULADO sobre SUPOSTO] |
| Frutas complementares | Acerola, goiaba, maracujá (giro rápido), todas a testar. **Mamão não há em Petrolina. Banana fora até ensaio** (dano por frio abaixo de cerca de 13 °C) | [IBGE 2025]; revisor do doc 10 |
| Entrada diária | Média de **0,45 t/dia**; pico de safra 0,6 t/dia; **teto de 1 t/dia** por cota. A logística recomenda manter 1 t/dia como entrada de projeto, porque a fruta chega em dias de colheita, não espalhada por igual | [SUPOSTO] |
| Estoque médio | 2,25 t (3 t no pico) | [SUPOSTO; doc 10] |
| Rede elétrica no local | Provável no núcleo; **não confirmada** no terreno | [SUPOSTO] |
| Caixa | 20 kg; 50 por tonelada; 250 para 5 t (a do projeto térmico) | alinhado ao 01 |
| Permanência média | 5 dias (faixa de 2 a 5) | [SUPOSTO; doc 10] |
| Aberturas de porta | Concentradas das 7h às 14h e na retirada, em dias fixos | D2 + [SUPOSTO] |
| Área do terreno | 600 a 800 m² | [SUPOSTO] |
| Água | Provável água de canal, não potável | [SUPOSTO] |
| Assistência técnica | Na cidade de Petrolina | [SUPOSTO] |

**Sensibilidade para outro ponto do sertão:** Santa Maria da Boa Vista, Lagoa Grande e Belém do São Francisco ficam na mesma beira de rio, com clima que deve ser muito parecido com o de Petrolina [SUPOSTO; sem dado]. São José do Belmonte é sertão mais alto, provavelmente um pouco menos quente [SUPOSTO; sem dado].

---

## 8. O que só a visita resolve — perguntas prontas

Leve: este documento, termômetro de espeto, celular com o aplicativo da Starlink, trena, caderno.

### 8.1 Para os produtores (pelo menos 10, de lugares diferentes)

1. Quantos hectares o senhor tem? Quantos são de manga? De que variedade?
2. (Estudo futuro) Tem caju? Quantos pés, de que tipo (anão ou comum)? O que faz com a fruta, fora a castanha?
3. **Em quantos dias o senhor colhe um talhão? Quantas caixas por dia nesses dias?** Em que meses?
4. **A que horas começa e termina a colheita? A que horas a fruta sai da roça?** Quem colhe: a família ou a turma do comprador?
5. Para quem vendeu a última safra? Quanto pagou pela primeira, pela segunda e pelo arrastão?
6. Quanto se perdeu ou saiu barato porque amadureceu antes de achar comprador?
7. Já usou câmara fria de alguém? De quem, quanto custou, por que parou?
8. Com uma câmara a menos de 10 km, levaria fruta? Quantas caixas por dia? **Aceitaria uma cota diária?** Pagaria quanto por caixa?
9. Como levaria? A estrada passa na chuva?
10. Participa de associação ou cooperativa? Confia nela para cuidar da sua fruta?
11. Tem CAF? Já vendeu para merenda ou PAA?
12. **Posso medir a temperatura de uma fruta recém-colhida?** (anotar hora e temperatura)
13. (Estudo futuro) Do caju que o senhor colhe, quanto é apanhado no pé e quanto é do chão?

### 8.2 Para a associação ou cooperativa

14. Quantos sócios ativos? Quantos com manga? Quantos com caju?
15. **Existe câmara fria por aqui com vaga? De quem? Quanto cobra?** (eliminatório E1)
16. **A assembleia cederia um terreno de 600 a 800 m², por escrito, por 10 anos?** (eliminatório E2)
17. Quem seria o operador? A taxa por caixa paga um salário?
18. Já houve furto de cabo, bomba ou painel solar?
19. De onde vem a água? É tratada?
20. Há eletricista e frigorista de confiança por perto?
20a. **Há rede elétrica no terreno? Monofásica ou trifásica? Cai muito? Quanto é a conta de luz do galpão da associação?** (Define o sentido do teste: ver seção 4.4.)
20b. Que outras frutas os sócios colhem de abril a julho (banana, acerola, goiaba)? Para quem vendem?

### 8.3 Para os compradores

21. **O senhor paga mais por fruta resfriada e entregue em dia certo? Quanto a mais por caixa?** (eliminatório E3)
22. Que variedade e que ponto de maturação? Quantas caixas por semana?
23. (Estudo futuro) Compra caju de mesa? De onde vem hoje? A que preço? Em que embalagem?
24. Busca no local? Em que dias?
25. (Secretarias de Educação e de Agricultura) Quanto a merenda compra de manga e de caju por ano? Quando sai a próxima chamada pública? Em quantos pontos e em que dias entrega?
26. (Indústria de polpa) Compra de pequeno produtor? Paga quanto? Exige fruta resfriada?

### 8.4 Para os órgãos

27. **DINC e Codevasf:** posso instalar dentro do perímetro? Qual a área de manga dos lotes familiares e quantos colonos plantam manga? Algum planta caju?
28. **Adagro:** um ponto que recebe fruta de vários produtores precisa de cadastro? O que é preciso para levar manga a Juazeiro-BA?
29. **Vigilância sanitária:** o que exige para armazenar fruta de terceiros?

### 8.5 No terreno escolhido

32. Fotos do horizonte ao norte, leste e oeste às 8h e às 16h.
33. Medir terreno, portão e estrada; procurar fio baixo.
34. Perguntar a um vizinho se alaga.
35. Distância até o asfalto, o poste mais próximo e a casa habitada mais próxima.

### 8.6 Para o estudo futuro do caju — Buíque (não é do protótipo)

36. Na Secretaria de Agricultura, no sindicato rural e no IPA local: onde ficam os 1.385 ha de cajueiro? Quantos produtores? Anão ou comum?
37. Quem compra a castanha? O que se faz com o pedúnculo? Alguém vende caju de mesa?
38. Em que meses há caju?
39. Há associação com sede e terreno? Há fornecedores em terra indígena Kapinawá?
40. As estradas das áreas de caju (solo de areia) passam caminhão o ano todo?
41. Quem compraria caju de mesa resfriado: Arcoverde, Caruaru, Recife?

### 8.7 Para o estudo futuro das duas frutas — São José do Belmonte (não é do protótipo)

42. Onde ficam os 251 ha de cajueiro e os 20 ha de manga? São dos mesmos produtores? A manga é irrigada?
43. Os 151 t de castanha de 2024 se repetem? O que mudou em relação a 2022 e 2023?
44. Caju e manga amadurecem nos mesmos meses?
45. A merenda do município compraria caju e manga resfriados? Quanto?

---

## 9. Perguntas de campo: o que a pesquisa já responde

O dono pediu que eu procurasse resposta para o que tinha ficado para a visita. Pesquisa de 17/11/2026. **Quase tudo abaixo vem de trecho de busca, não de página aberta**; os sites da Codevasf, do DINC, do IFSertãoPE, da prefeitura e da Adagro não abriram nesta sessão. Só usei contato que a própria entidade ou um cadastro público divulga como institucional. **Confirmar todo telefone, e-mail e endereço antes de usar.**

Confiança: **alta** = dado oficial que eu abri; **média** = trecho de busca de fonte oficial ou acadêmica; **baixa** = trecho de busca de blog, diretório ou fonte antiga; **nenhuma** = não encontrado.

| # | Pergunta (nº na seção 8) | Resposta encontrada | Fonte e data | Confiança | O que ainda só se resolve no local |
|---|---|---|---|---|---|
| 1 | Quantos hectares e quanto de manga por lote (1) | Lote familiar de cerca de 6 ha (6,11 ha irrigáveis em estudo antigo); manga é cerca de 40% do cultivo permanente do distrito; 75% dos estabelecimentos com manga do Submédio têm até 5 ha de manga | [FONTE 59], [FONTE 6], [FONTE 5]; estudos de 2001 a 2022 | Média | Área de manga e variedade de cada família do grupo |
| 2 | Em quantos dias colhe um talhão, quantas caixas por dia, em que meses (3) | **Não encontrado** para o pequeno produtor. Só o geral: oferta alta de outubro a janeiro, baixa de abril a julho (preço de R$ 0,99/kg em fevereiro e R$ 4,94/kg em junho de 2026, Cepea citado no doc 10) | doc 10, seção 1.4 | Baixa | **Tudo.** É o que define a cota diária |
| 3 | Rendimento | 25 t/ha em média, em 75 produtores do distrito (2014–2018); Petrolina no IBGE: 30 t/ha em 2024, 25 t/ha em 2025 (286.250 t ÷ 11.450 ha) | [FONTE 60]; [IBGE] 2024 e 2025 | Alta (IBGE), média (estudo) | — |
| 4 | **A que horas se colhe e a fruta sai da roça (4)** | **Fontes em conflito.** (a) Capítulo "Colheita e pós-colheita" da Embrapa (livro A Cultura da Mangueira, 2002): o horário mais conveniente é **entre 10h e 15h**, quando o fluxo de látex é mínimo; evitar as primeiras horas da manhã. (b) Manual de manga para exportação da Embrapa: **transportar** pela manhã ou no fim da tarde. (c) Notícia da Embrapa Semiárido (2026): uma exportadora passou a colher nas horas mais frescas para reduzir o escurecimento da polpa | [FONTE 80] (2002 e manual sem data no trecho); [FONTE 50] (21/09/2026) | Média para as recomendações; **nenhuma para o costume do pequeno** | Hora real de colheita e de chegada. **Se a colheita for das 10h às 15h, parte da fruta chega depois das 14h** (limite da decisão D2) |
| 5 | Temperatura da fruta recém-colhida (12) | **Não encontrado** | — | Nenhuma | Medir com termômetro de espeto |
| 6 | Para quem vende e por quanto (5) | Vende na roça, ao comprador que vai ao pomar e classifica em primeira, segunda e "arrastão"; é tomador de preço. Preço na roça em Petrolina em 10/11/2026: R$ 1,05/kg (palmer) e R$ 1,20/kg (tommy), segundo o doc 10 (Cepea/Agrolink) | [FONTE 10] (2023); doc 10, seção 4.2 | Média | Preço de cada classe; nome dos compradores |
| 7 | Quanto se perde (6) | **Não encontrado** para o Vale. Estimativa nacional antiga: 27,5% para manga (1992, citada pela Embrapa em 1997) | doc 10, seção 3.1 | Baixa | Perda real do grupo |
| 8 | **Existe câmara fria por perto? Em uso ou parada? (7, 15)** | Há frio no polo, mas não achei situação atual de nenhuma unidade: (a) Cooperativa do N-6 (Petrolina) e Manga Brasil (Juazeiro) têm packing house com câmara fria, de programas federais — estudo antigo, sem dizer se funcionam; (b) Aprovale e exportadores têm frio próprio; (c) em 2026 um senador disse ter indicado, pela Codevasf, uma câmara fria para a cooperativa CoopGrapes, do Projeto Maria Tereza — anúncio, não confirmação de instalação; (d) um vereador denunciou equipamentos da Codevasf parados em pátio no Núcleo 3 (caminhões, tratores, caixas-d'água; não cita câmara fria). **Procurei notícia de câmara parada ou abandonada e não achei** | [FONTE 9]; [FONTE 11]; [FONTE 78] (blog, 2026); RedeGN, sem data: https://redegn.com.br/?cod_noticia=198252&sessao=noticia | Baixa | **Tudo: é o eliminatório E1.** Quais câmaras existem no núcleo, se estão ligadas, se têm vaga, quanto cobram, e por que as paradas pararam |
| 9 | **Quais associações e cooperativas existem nos núcleos (10, 14)** | Lista parcial, sem confirmação de atividade: **Coopexvale** — Cooperativa de Produtores Exportadores do Vale do São Francisco, fundada em 2004, sede no **Núcleo 8**; contato divulgado em diretório de exportadores: coopexvale@uol.com.br, (87) 3031-8702, site coopexvale.com.br. **COANA** — Cooperativa Agrícola Nova Aliança, fundada em 2005, **Núcleo 2, lote 551**; sac@coanabr.com.br, (87) 3986-1542. **COOAPINC-04** — Cooperativa Agrícola dos Produtores Irrigantes do Núcleo 4 (citada em estudo do Banco Mundial e em cadastro de certificadora de orgânicos); contato não encontrado. **Cooperativa do N-6** (packing house com câmara fria); nome completo e contato não encontrados. **AAFPMN3** — Associação dos Agricultores Familiares do N-3, site aafpmn3.org. **CoopGrapes** (Projeto Maria Tereza). Associação de Pequenos Produtores do **Núcleo 2** (Asa Branca): cadastro "inapto". Associação do **Núcleo 5**: CNPJ baixado em 2008. Um artigo da Univasf contou 4 associações só de produtores com 766 sócios no perímetro, mais associações mistas; a tabela com os nomes não apareceu | [FONTE 74]; [FONTE 76]; [FONTE 9]; [FONTE 48]; [FONTE 78]; [FONTE 77]; [FONTE 75] | Média (existência), baixa (contatos e situação atual) | Quais estão ativas, quantos sócios com manga, se aceitam operar. **Não sei se Coopexvale e COANA trabalham manga de pequeno produtor** (são exportadoras). Pedir a lista atual ao DINC |
| 10 | Assembleia cederia terreno; quem operaria (16, 17) | **Não encontrado** (não é coisa que se ache em pesquisa) | — | Nenhuma | **Tudo: eliminatório E2** |
| 11 | Furto de cabo, bomba, painel (18) | **Não encontrado** nada específico dos núcleos | — | Nenhuma | Perguntar aos vizinhos |
| 12 | De onde vem a água (19) | O projeto tem 39 estações de bombeamento e distribui água do São Francisco por canais; é água de irrigação. Água tratada nos núcleos: não encontrado | [FONTE 7] (trecho) | Média | Se há água tratada no terreno |
| 13 | **Há rede elétrica nos lotes? (20a)** | **Não confirmado.** O que achei: onze núcleos com escolas, postos de saúde e comércio (logo, rede no núcleo, por dedução); a energia das estações de bombeamento é paga pelos usuários na conta mensal de água do distrito; em maio de 2026 houve corte de energia da Neoenergia em **outros** projetos (Brígida, em Orocó, e Caraíbas, em Santa Maria da Boa Vista), e o mesmo texto diz que os produtores do Nilo Coelho pagam em dia | [FONTE 69]; [FONTE 84] (DINC e blog de maio/2026) | Baixa | Se o terreno tem poste, se é trifásico, se cai. Define o sentido do teste (seção 4.4) |
| 14 | **Há frigoristas e empresas de refrigeração? Quanto cobram? (20)** | Empresas que anunciam câmaras frigoríficas em Petrolina: **China Refrigeração** (câmaras e baús frigoríficos; diz ser autorizada Carrier e Thermo King; BR-428, km 183, Jardim Amazonas; site chinarefrigeracaope.com.br); **Grupo Hermonex** (anuncia projeto, instalação e manutenção de câmaras em Petrolina; não sei se tem base na cidade); **Climafrio** (listada em diretório com serviços de refrigeração e câmaras frias). Há também oficinas pequenas de refrigeração em listas telefônicas, sem indicação de que atendam câmara fria. **Preço de visita, hora técnica ou manutenção: preço não encontrado** | [FONTE 79] (sites e diretórios, sem data) | Baixa | Quem atende os packing houses, quanto cobra, se trabalha com o gás escolhido |
| 15 | **Quem compra manga de pequeno produtor (21 a 24)** | **Mercado do Produtor de Juazeiro** (AMA): 1.620.627 t em 2025, 2º do país; horário divulgado: segunda a sexta das 2h às 22h, sábado das 2h às 17h, domingo a partir das 21h (a mesma página traz outro horário, de 8h às 14h — confirmar); telefone 74 98846-0016; cotação diária no Instagram @mercadodoprodutorjuazeirooficial. Nomes de boxes ou atacadistas: **não encontrado** | [FONTE 63] (2025, aberta); [FONTE 83] (prefeitura de Juazeiro, sem data) | Alta (volume), média (horário e contato) | **Se pagam mais por manga resfriada: eliminatório E3.** Quais boxes compram de pequeno |
| 16 | Indústria de polpa, com nome (26) | **Nome não encontrado.** Só um estudo da Embrapa sobre "uma indústria de polpas de Petrolina" com 14 funcionários, sem nome, que vende polpa de acerola, goiaba, manga, cajá e maracujá. Preço pago pela manga: **não encontrado** | [FONTE 37] (estudo antigo) | Baixa | Nomes, preço e exigências |
| 17 | **Chamadas públicas do PNAE e do PAA, com preço e data (25)** | (a) **IFSertãoPE, campus Petrolina Zona Rural, Chamada Pública PNAE nº 01/2026**: publicada em 29/10/2026; propostas até **18/11/2026, 16h**; abertura em 19/11/2026, 10h; retificação em 09/11/2026; exige DAP ou CAF. (b) **IFSertãoPE, campus Petrolina**: 27 itens (frutas, verduras, polpas, entre outros), 4 meses de fornecimento, valor estimado de **R$ 155.854,69**, propostas até **01/12/2026** pela plataforma Contrata+Brasil. (c) **Prefeitura de Petrolina, Chamada nº 001/2026**: pesquisa de preços com agricultores familiares, para futura compra da merenda; data divergente entre fontes (abril ou agosto de 2026). **Preço por kg da manga em qualquer delas: não encontrado** (os anexos não apareceram). Referência de fora: R$ 5,06/kg na pesquisa da Emater-RN de maio de 2026 (doc 10). **PAA:** o governo federal abriu em 20/05/2026 a seleção de municípios para executar o PAA em 2026; **não achei se Petrolina foi selecionada**, nem preço | [FONTE 71]; [FONTE 72]; [FONTE 73]; [FONTE 85]; doc 10, seção 4.2 | Média (existência e datas), nenhuma (preço) | Abrir os anexos dos editais e ver se há manga e a que preço; quanto a prefeitura compra por ano |
| 18 | **Licenças: prefeitura e vigilância sanitária (29)** | Alvará sanitário: pela **Agência Municipal de Vigilância Sanitária (AMVS)**, por sistema online; envio de documentos, visita técnica, alvará provisório e depois definitivo; WhatsApp divulgado (87) 99190-7667. Alvará de licença: na sede da prefeitura, Av. Guararapes, 2114, Centro; carta de serviços informa taxa de R$ 5,00. **Lista de documentos e exigências técnicas para armazenar fruta: não encontrado.** Licença ambiental municipal: não encontrado | [FONTE 81] (prefeitura; notícias de 2019 a 2021 e carta de serviços sem data) | Média | Se um protótipo sem CNPJ, em terreno de associação, precisa de alvará próprio ou entra no da associação [VALIDAR] |
| 19 | **Licenças: Adagro (28)** | A Adagro inscreve e fiscaliza **Unidades de Produção e Unidades de Consolidação** e emite a Permissão de Trânsito de Vegetais (PTV) pelo sistema Siapec3; o pedido online exige cadastro atualizado do produtor e da propriedade. Emitiu 45.291 PTVs em 2024, com 161 mil t de manga. Mantém escritório e plantão em Petrolina. **Requisitos para cadastrar um ponto que consolida fruta de vários produtores, e exigência para entrar na Bahia: não encontrado** | [FONTE 82] (relatório de gestão e notícias da Adagro, 2023 a 2025) | Média | Se o protótipo é "unidade de consolidação"; o que a Bahia (ADAB) exige para manga vinda de Petrolina |
| 20 | Autorização do DINC e da Codevasf (27) | **Não encontrado** nada sobre instalar equipamento de terceiros no perímetro | — | Nenhuma | Perguntar ao DINC |
| 21 | Frutas complementares de abril a julho (20b) | Em Petrolina, 2025: banana 41.600 t, goiaba 48.000 t, acerola 30.000 t, maracujá 1.980 t; mamão não aparece | [IBGE], tabela 1613, 2025 | Alta | Se o núcleo escolhido tem essas frutas, em que meses, e se alguém pagaria para guardá-las |
| 22 | Distâncias, obstrução da Starlink, sombras, alagamento, fio baixo (31 a 35) | **Não encontrado** (dependem do terreno) | — | Nenhuma | Tudo, no terreno |
| 23 | De quem é a manga de Belém do São Francisco e de São José do Belmonte (30, 42) | **Não encontrado** | — | Nenhuma | Só importa se Petrolina cair |
| 24 | Caju: Buíque e São José do Belmonte (36 a 45) | Só os volumes do IBGE (seção 10). Em Buíque, parte do caju é do povo Kapinawá [FONTE 61]. Associações, compradores, estradas: **não encontrado** | [IBGE] 2024 e 2025 | Alta (volume), nenhuma (o resto) | Estudo futuro |

### O que a pesquisa mudou

1. **Horário de colheita:** há recomendação técnica de colher manga **entre 10h e 15h**. Isso enfraquece a minha suposição de chegada "entre 9h e 15h" e ameaça a janela de recepção até as 14h. Não reabro a decisão D2; aviso que ela precisa de confirmação em campo antes de fechar o tamanho do gelo.
2. **Há venda pública aberta agora:** duas chamadas do IFSertãoPE em Petrolina com prazo em novembro e dezembro de 2026. Não servem para o protótipo (não há tempo), mas mostram que o canal existe e dão o tamanho: R$ 155.854,69 em quatro meses para 27 itens, em um campus.
3. **Há cooperativas com endereço nos núcleos 2, 4, 6 e 8** e uma associação no núcleo 3. A visita já pode começar com uma lista, em vez de sair procurando.
4. **Continuo sem nenhum dado sobre os três eliminatórios.** Pesquisa de mesa não os resolve.

### O que realmente sobra para o dono perguntar pessoalmente, em ordem de importância

1. **Ao comprador (merenda de Petrolina, IFSertãoPE, dois ou três boxes do Mercado do Produtor):** o senhor compraria manga resfriada, em dia certo, de um grupo de dez famílias? Quanto por semana, a que preço, e põe isso por escrito?
2. **Às cooperativas dos núcleos 4, 6 e 8 e à associação do núcleo 3:** existe câmara fria aqui? Está ligada? Tem vaga? Se está parada, por quê?
3. **À mesma associação:** cederia 600 a 800 m² por escrito e indicaria quem abre a porta das 7h às 14h?
4. **A dez produtores:** a que horas o senhor colhe e a que horas a fruta sai da roça? (E medir a temperatura de uma manga recém-colhida.)
5. **Aos mesmos:** em quantos dias colhe um talhão, e aceitaria uma cota diária? Pagaria R$ 1,20 por caixa por dia?
6. **No terreno:** tem poste de energia? É trifásico? Cai muito?
7. **Ao DINC:** posso instalar no perímetro? Tem a lista atual de associações e cooperativas?
8. **À Adagro de Petrolina:** juntar fruta de vários produtores exige cadastro de unidade de consolidação? O que é preciso para vender em Juazeiro?
9. **À vigilância sanitária (AMVS):** um protótipo em terreno de associação precisa de alvará próprio?
10. **A uma empresa de refrigeração da cidade:** atende câmara fria em zona rural? Quanto cobra a visita? Trabalha com o gás do projeto?
11. **Aos sócios:** que outras frutas colhem de abril a julho, e para quem vendem?
12. **No terreno:** teste de obstrução da Starlink, fotos de sombra, alagamento, fio baixo, vizinho mais próximo.

---

## 10. Estudo futuro — caju (fora do protótipo)

Por decisão do dono (D1) o caju não entra no protótipo nem na pontuação. Fica registrado o que apurei, **corrigido com o IBGE**, para quando o assunto voltar. Tabela 5457 do IBGE, mesma consulta da seção 1.

**Correção da versão 1:** ela apontava o Pajeú (Carnaíba–Flores–Serra Talhada) como o lugar do caju. Estava errado.

Pernambuco, castanha de caju: 2.806 t (2022), 2.821 t (2023), **3.099 t em 2.220 ha (2024)**. Brasil 2024: 169.210 t em 463.177 ha. O IBGE não publica o pedúnculo ("caju" fruta).

Todos os municípios com mais de 10 t em 2024, e os do Pajeú citados antes:

| Município | Região | 2022 (t) | 2023 (t) | 2024 (t) | Área 2024 (ha) | t/ha | Manga 2024 (t) |
|---|---|---|---|---|---|---|---|
| **Buíque** | Agreste | 2.426 | 2.399 | **2.521** | 1.385 | 1,82 | 0 |
| Tupanatinga | Agreste, vizinho de Buíque | 89 | 97 | 165 | 110 | 1,50 | 0 |
| **São José do Belmonte** | Sertão Central | 40 | 51 | **151** | 251 | 0,60 | 400 |
| Taquaritinga do Norte | Agreste | — | — | 120 | 200 | 0,60 | 10 |
| Carnaíba | Sertão do Pajeú | 45 | 45 | 50 | 100 | 0,50 | 41 |
| Flores | Sertão do Pajeú | 30 | 21 | 42 | 70 | 0,60 | 0 |
| Tacaratu | Sertão de Itaparica | — | — | 12 | 25 | 0,48 | 150 |
| Mirandiba | Sertão Central | 9 | 0 | 0 | 0 | — | 90 |
| Serra Talhada | Sertão do Pajeú | — | — | 0 | 0 | — | 200 |

Leituras [CALCULADO]:
- Buíque: 2.521 ÷ 3.099 = **81%** do estado. Buíque + Tupanatinga: 2.686 t = **87%**.
- Pajeú (nove municípios, soma do revisor): 118 t = **3,8%**. Carnaíba + Flores: 92 t.
- São José do Belmonte é o único município com mais de 100 t das duas culturas.

**Em 2025** [IBGE, conferido; doc 10]: a castanha de Pernambuco caiu para 1.894 t; Buíque 1.662 t (88%), São José do Belmonte 77 t, Tupanatinga 56 t, Flores 28 t, Carnaíba 10 t. No país a safra caiu de 169.210 t para 114.749 t. O caju oscila muito de um ano para o outro, e a posição de Buíque se manteve.

**Três cuidados com esses números:**
1. **O rendimento de Buíque é estranho.** 1,82 t de castanha por hectare é cinco vezes a média do Brasil (169.210 ÷ 463.177 = 0,37 t/ha) e três vezes a dos vizinhos de sequeiro (0,5 a 0,6). Pode ser pomar de cajueiro-anão bem cuidado ou pode ser estimativa alta do levantamento. Com a média brasileira, Buíque teria 1.385 ha × 0,37 = **506 t** — ainda de longe o maior do estado, mas cinco vezes menos. Uso os dois valores nas contas abaixo.
2. **O salto de São José do Belmonte** (40 → 51 → 151 t com a mesma área) pode ser pomar novo entrando em produção ou ajuste do levantamento. Um ano bom não é uma série.
3. O IBGE mede **castanha**. Que parte do pedúnculo serve para mesa é outra conta (abaixo).

**O que as outras fontes dizem:**
- O plano de trabalho do MAPA/Embrapa para o Pajeú (2021), que li inteiro, conta a história: o Pajeú tinha 65% da área e 55% da castanha do estado em 1990; caiu para 20% da área e 9% da produção em 2020; a área de cajueiro na região caiu de 3.000 ha para 452 ha. Os municípios históricos são São José do Belmonte, Flores, Carnaíba, Mirandiba e Santa Terezinha. A Embrapa encontrou ali "forte capital social da agricultura familiar" [FONTE 15]. O IBGE de 2024 mostra que a queda continuou (3,8%).
- Em Buíque, a página de história da prefeitura diz que o povo indígena Kapinawá planta mandioca, milho, feijão e caju, "do qual extraem a castanha, sua maior fonte de renda" [FONTE 61, trecho de busca, texto antigo]. **Não achei associação, cooperativa, fábrica de castanha ou de polpa em Buíque.** É a principal lacuna do candidato.
- Carnaíba: prefeitura distribuiu 20 mil mudas (25 por agricultor) e depois 10 mil de cajueiro-anão; uma associação local tem 80 sócios [FONTE 17][FONTE 18].
- O caju cotado na CEASA do Recife tem origem Piauí [FONTE 26, sem data no trecho].
- Agricultura familiar: 77,36% da castanha de PE no Censo 2017 [FONTE 24].

**Quanto caju de mesa isso pode dar** — conta em quatro passos, cada um com sua marcação:

1. Pedúnculo por castanha: o pedúnculo é cerca de 90% do peso do caju [FONTE 62, trecho de busca], isto é, **9 kg de pedúnculo por 1 kg de castanha** [CALCULADO]. (A versão 1 usava 10.)
2. Parte que serve para mesa: **10% a 30%** [SUPOSTO — é o fator proposto pelo revisor; ver "Discordâncias", item 2]. Referência que achei: no Nordeste a indústria aproveita só 10% a 20% do pedúnculo e 80% a 90% se perdem [FONTE 51, página lida]. Caju de mesa é colhido à mão, no pé; o que cai no chão não serve para câmara.
3. Duração da safra: **150 dias** [SUPOSTO]. O plano do MAPA/Embrapa diz que a safra no sertão se concentra de junho a dezembro [FONTE 15].
4. Raio de coleta: a câmara só alcança uma parte do município. Não apliquei esse corte; os valores abaixo são do **município inteiro**.

| Local | Castanha (t) | Pedúnculo bruto (×9) | De mesa (10% a 30%) | Por dia (÷150) |
|---|---|---|---|---|
| Buíque + Tupanatinga, dado do IBGE | 2.686 | 24.174 t | 2.417 a 7.252 t | **16 a 48 t/dia** |
| Buíque, se o rendimento for o da média do Brasil | 506 | 4.554 t | 455 a 1.366 t | **3 a 9 t/dia** |
| São José do Belmonte, 2024 | 151 | 1.359 t | 136 a 408 t | **0,9 a 2,7 t/dia** |
| São José do Belmonte, 2022–2023 | 40 a 51 | 360 a 459 t | 36 a 138 t | **0,2 a 0,9 t/dia** |
| Carnaíba + Flores | 92 | 828 t | 83 a 248 t | **0,6 a 1,7 t/dia** |

Tudo [CALCULADO sobre SUPOSTO]. Leitura: **em Buíque sobra caju para uma câmara de 1 t/dia mesmo na hipótese pessimista. Em São José do Belmonte e no Pajeú a oferta do município inteiro fica perto ou abaixo de 1 t/dia**, antes de descontar a distância.

A frase da versão 1 — "uma associação de 80 famílias com 25 cajueiros cada é um fornecedor do tamanho da câmara" — **estava errada e foi retirada**. Pela conta do revisor, que aceito: 2.000 plantas ≈ 10 ha ≈ 10 t de castanha ≈ 90 a 100 t de pedúnculo por safra, ou menos de 0,3 t/dia de caju de mesa.

**Se um dia houver uma unidade de caju, as duas saídas são:**

| | Buíque – Tupanatinga | São José do Belmonte |
|---|---|---|
| Está no sertão? | Não (Agreste) | Sim |
| Caju de mesa possível | 3 a 48 t/dia no município [CALCULADO sobre SUPOSTO] | 0,2 a 2,7 t/dia no município [CALCULADO sobre SUPOSTO] |
| Manga | Nenhuma | 400 t/ano |
| Clima | Serra de cerca de 800 m (798 a 814 m conforme a fonte [FONTE 64]); provavelmente abaixo dos 40 °C da premissa e talvez com menos sol [SUPOSTO]. Há tabela de 30 anos no Climatempo, mas a busca não mostrou os valores [FONTE 68] | Sertão, próximo da premissa [SUPOSTO] |
| Acesso | BR-232 até Arcoverde e PE-270 até Buíque [FONTE 64]; cerca de 280 km do Recife [SUPOSTO] | 474 km do Recife [FONTE 65] |
| O que não sei | Quase tudo além do volume: quem produz, como vende, estradas, compradores, água, quem operaria. Parte do caju é do povo indígena Kapinawá [FONTE 61], o que pode trazer regras próprias | Se a oferta chega a 1 t/dia; se há associação; de quem é a manga |

**Calendário do caju:** a safra no sertão se concentra de junho a dezembro [FONTE 15]. Para Buíque não achei calendário [SUPOSTO que seja parecido]. Caju de mesa pede temperatura mais baixa que a manga, outra embalagem (bandeja) e entrada no mesmo dia da colheita: é outro projeto de operação.

**Resposta à pergunta original do dono** ("um lugar que seja a ponte para as duas frutas"): com volume comprovado, esse lugar não existe em Pernambuco. O mais próximo é São José do Belmonte, em escala pequena. As perguntas de campo para esse estudo estão nas seções 8.6 e 8.7.

---

## 11. Discordâncias com a revisão

Aceitei e corrigi a maior parte do parecer, inclusive o item bloqueante. Onde não concordo, ou não fiz, registro as duas posições. **O dono é o mediador.**

| # | Achado do revisor | Posição do revisor | Minha posição |
|---|---|---|---|
| 1 | 1 (caju, hoje estudo futuro) | Buíque–Tupanatinga "passa a ser o candidato principal de caju"; é "de longe o maior polo" | **Concordo com o lugar, discordo da firmeza.** O rendimento de 1,82 t/ha é cinco vezes a média do Brasil (o próprio revisor pede confirmação). Com rendimento normal seriam cerca de 500 t, não 2.500 t. Buíque continua o maior, mas trato o volume como **não confirmado** e mostro as duas contas. Além disso, de Buíque só tenho o número do IBGE: nenhuma associação, comprador ou estrada |
| 2 | 4 | Aplicar fator de aproveitamento de mesa de 10% a 30% | **Apliquei, mas o fator não tem fonte** — é suposição do revisor. A Embrapa dá 10% a 20% para o que a **indústria** aproveita, que é outra coisa. Em pomar de cajueiro-anão colhido à mão a parte de mesa pode ser bem maior; em cajueiro comum alto, perto de zero. A faixa pode estar errada para os dois lados; só a pergunta 13 resolve |
| 3 | 27 | "Pajeú com 9%" estava "acima do dado atual" | **As duas coisas são verdade.** Li o documento do MAPA: os 9% são de 2020. Os 3,8% são do IBGE de 2024. A versão 1 errou ao usar o número de 2020 como atual; a tendência de queda é o dado relevante |
| 4 | 16 e 19 | Buscar cotações de preço e o modelo de cobrança do ColdHubs | **Não fiz.** Pela nova divisão de trabalho, preço do serviço, quem paga e viabilidade são do analista de frutas e demanda. Escrevi "preço não encontrado" e deixei como pendência dele. Se o dono preferir que a logística levante os preços por local, eu levanto |
| 5 | 7 | Com as notas dadas, Petrolina vence com quase qualquer peso | **Concordo com a aritmética, discordo de parar nela.** A soma mistura fatores de polo desenvolvido, e nos outros candidatos quase todas as notas são sem dado. A vantagem de Petrolina é em parte falta de informação sobre os demais. A meu ver a tabela não deve ser lida como "Petrolina ganhou, assunto encerrado": os três eliminatórios decidem |
| 6 | 9 | Retirar a decisão sobre os 40 °C | **Concordo** e retirei. Registro só que o recorde de 41,0 °C é de um dia; a máxima média do mês mais quente é de cerca de 34 °C. As duas informações vão para o engenheiro térmico |
| 7 | 8 e 18 | Levantar câmaras existentes, irradiação, central de Petrolina e feiras | **Não consegui.** Codevasf, INMET e CRESESB não abriram mesmo depois da liberação. Marquei com asterisco as notas sem dado e declarei as lacunas |

Os conflitos A (horário), B (uma ou duas zonas) e C (Agreste ou sertão) **foram resolvidos pelo dono**: recepção das 7h às 14h (D2), só manga em uma zona (D1), caju como estudo futuro. Este documento segue essas decisões.

**Um aviso que mantenho depois da decisão D2:** a janela até as 14h foi decidida sem dado de campo sobre o horário real de chegada. Se a visita mostrar que a manga chega mais tarde, a regra de "sair da roça até as 13h" terá de ser cobrada do grupo, ou a fruta dormirá fora da câmara.

---

## 12. Acordo com frutas e demanda

O texto completo está em `docs/_trabalho/acordo-logistica-demanda.md` (acordado, divergências que restam e perguntas ao dono). Resumo do que este documento passou a usar do doc 10:

| Item | Número adotado | Dono do número |
|---|---|---|
| Fruta | Manga a 12 °C, uma zona, 5 t; complementares (D6) a testar: acerola, goiaba, maracujá. Mamão não há em Petrolina; banana fora até ensaio | Frutas e demanda (D1 e D6), revisor do doc 10 |
| Calendário de uso | Manga de agosto a março; complementares de fevereiro a setembro (seção 1.5) | Frutas e demanda |
| Toneladas por ano | Base: até 79 t (merenda). Com mais de um comprador: 108 t de manga + cerca de 54 t de complementares | Frutas e demanda; base proposta pelo revisor |
| Entrada diária | Média de 0,45 t/dia; teto de 1 t/dia | Frutas e demanda (média); logística (teto e cota) |
| Permanência | 5 dias | Frutas e demanda |
| Grupo | 10 famílias (5 a 15), com comprador fixo, via associação | Os dois |
| Operador | Pessoa da associação, com ajuda de custo | Frutas e demanda, com ressalva minha |
| Taxa de referência | R$ 0,06 por kg por dia | Frutas e demanda |
| Dados de 2025 do IBGE | Incorporados (seções 1.1 e 10) | Frutas e demanda; conferidos por mim |
| Local, municípios, horário, modelo de operação | Os deste documento | Logística |

**Divergências que restam** (detalhe no arquivo do acordo): (1) dimensionar a entrada pelo teto de 1 t/dia ou pela média; (2) quais frutas complementares fazem sentido em Petrolina — há banana e acerola, **não há mamão** [IBGE 2025], e não há prova de que alguém pagaria para guardá-las; (3) operador com ou sem pagamento certo; (4) o calendário é suposição dos dois lados; (5) lotes familiares são muitos, mas só 17% do volume; (6) manga por família: 64 t por lote (conta deste documento) contra 21 t por estabelecimento familiar (Censo 2017, conta do revisor do doc 10).

**Ponto do doc 10 que ficou desatualizado:** ele ainda cita "150 a 180 t por lote" e "1,4 a 1,7 lote", que eram da versão 1 deste documento. O número corrigido é cerca de 64 t de manga por lote (seção 1.4).

---

## 13. Fechamento

### Decisões do dono aplicadas
- D1: protótipo só de manga, uma zona a 12 °C, 5 t. Caju como estudo futuro (seção 10).
- D2: recepção das 7h às 14h.
- D5: um protótipo, sem CNPJ.

### Decisões tomadas neste documento
1. Local recomendado para o protótipo: **Petrolina-PE, zona rural, Projeto Senador Nilo Coelho** (provisório até a visita).
2. Público: grupo de 5 a 15 famílias, com cota diária.
3. Três critérios passam a ser eliminatórios (frio existente, operador, comprador).
4. Manga que chega depois das 14h entra na manhã seguinte; regra de sair da roça até as 13h.
5. Área de terreno: 600 a 800 m².
6. Retirado o Pajeú como lugar do caju; registrados Buíque e São José do Belmonte para estudo futuro.

### Pendências para o dono
0. **O protótipo serve para provar a tecnologia ou a necessidade de estar fora da rede?** (seção 4.4). (As frutas complementares já foram autorizadas: D6.) As perguntas completas estão em `docs/_trabalho/acordo-logistica-demanda.md`.
1. Fazer a visita com as perguntas da seção 8, **começando pelos três eliminatórios** (perguntas 15, 16 e 21).
2. Escolher a associação ou cooperativa operadora e o núcleo.
3. Definir por escrito: cessão do terreno, **valor da taxa por caixa** e **quem responde por fruta perdida se o equipamento falhar**.
4. Consultar um contador sobre como ceder o equipamento e ser remunerado sem CNPJ.
5. Obter do DINC/Codevasf a autorização para instalar no perímetro.
6. Mediar as discordâncias da seção 11.

### O que não consegui verificar
- Câmaras frias existentes e preço do frio em qualquer dos locais (eliminatório E1).
- Preços de manga e caju em qualquer ponto da cadeia.
- Normais do INMET, irradiação do CRESESB e a página da Codevasf (não abriram).
- De quem é a manga de Belém do São Francisco, de Santa Maria da Boa Vista, de Lagoa Grande e de São José do Belmonte.
- Em que meses o pequeno produtor de Petrolina colhe.
- **Se há rede elétrica no terreno do núcleo recomendado**, e de que qualidade.
- Para o estudo futuro do caju: tudo sobre Buíque além do IBGE, e se o rendimento de lá é real.
- Central de abastecimento de Petrolina e feiras da agricultura familiar.
- Estruturas de frio e cooperativas do lado baiano.
- Situação atual da cooperativa do N-6, da Manga Brasil e da associação do N-3.
- Distâncias marcadas [SUPOSTO]; normas da Adagro, vigilância e DINC.
- Horário real de colheita e de chegada, e temperatura real da fruta.

### Dados de interface
Tabela da seção 7.

---

## Fontes

**[IBGE]** IBGE/SIDRA, Produção Agrícola Municipal, tabela 5457 — baixada e lida em 17/11/2026:
- Municípios de PE: https://apisidra.ibge.gov.br/values/t/5457/n6/in%20n3%2026/v/214,216/p/2022,2023,2024/c782/40143,40262?formato=json
- PE, BA e Brasil: https://apisidra.ibge.gov.br/values/t/5457/n3/26,29/n1/all/v/214,216/p/2024/c782/40143,40262?formato=json
- Municípios baianos: https://apisidra.ibge.gov.br/values/t/5457/n6/2918407,2907202,2909901,2930774,2930204/v/214,216/p/2024/c782/40143,40262?formato=json

Abertas nesta versão: 1, 15, 51 (página "Pedúnculo") e 63. As demais: **só o trecho mostrado pela busca**. Na fonte 62 a busca não deixou claro de qual link do resultado saiu o número; tratar como [SUPOSTO].

1. Embrapa — Atualização dos dados sobre a cultura da manga com dados da PAM/IBGE até 2024: https://www.embrapa.br/documents/1355026/60636822/Boletim+Manga+-+PAM+2024/ae831b0a-98e1-c106-26c3-1372d5d2a933
5. Embrapa — Produção Integrada de Manga: https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/160990/1/OPB1949.pdf
6. USP/ESALQ — tese (Caliane Borges Ferreira): https://teses.usp.br/teses/disponiveis/11/11132/tde-10062022-151607/publico/Caliane_Borges_Ferreira.pdf
7. Codevasf — Projeto Público de Irrigação Nilo Coelho (não abriu; trecho de busca): https://www.codevasf.gov.br/assuntos/agricultura-irrigada/projetos-de-irrigacao/em-producao/nilo-coelho
8. Editora Poisson — capítulo com dados do DINC: https://editorapoisson.com.br/livros-api/api/capitulos/7306/view ; DINC: https://www.dinc.org.br/o-perimetro-2/
9. Caminhos de Geografia (UFU) — o caso do polo frutícola Petrolina: https://seer.ufu.br/index.php/caminhosdegeografia/article/download/18291/12824
10. Embrapa — Análise do processo de comercialização de manga (2023): https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1162389/1/Analise-do-processo-de-comercializacao-de-manga-produzida-2023.pdf
11. IPEA — Texto para Discussão nº 1036: https://repositorio.ipea.gov.br/server/api/core/bitstreams/a900376c-f008-446a-9d48-a378940be230/content
12. IPEA — Desenvolvimento territorial e perímetros irrigados: https://www.ipea.gov.br/ppp/index.php/PPP/article/download/198/192/576
15. MAPA — Plano de Trabalho do TED nº 68/2021 (lido): https://www.gov.br/agricultura/pt-br/acesso-a-informacao/convenios-e-ted/termos-de-execucao-descentralizada/2021/termo-de-execucao-descentralizada-ted-no-68-2021/plano-de-trabalho-ted-68-2021
17. Diario de Pernambuco — Agricultores retomam o plantio do caju em Carnaíba: https://www.diariodepernambuco.com.br/noticia/vidaurbana/2019/07/agricultores-retomam-o-plantio-do-caju-em-carnaiba-sertao-do-pajeu.html
18. Prefeitura de Carnaíba — Cajucultura é discutida em associação de Serra Branca: https://carnaiba.pe.gov.br/cajucultura-e-discutida-em-associacao-de-serra-branca/
24. BNB — Agricultura familiar em Pernambuco, Censo Agropecuário de 2017: https://app.bnb.gov.br/documents/80223/8054629/E_1263.pdf/84ffff26-e71b-6df3-b6d6-bfc9dc4983ad
26. CEASA-PE — Cotação de frutas: https://www.ceasape.org.br/cotacao/frutas
35. Prefeitura de Caruaru — Central de Abastecimento: https://caruaru.pe.gov.br/central-de-abastecimento-de-caruaru-oferta-alimentos-com-precos-mais-acessiveis/
36. Em Sampa — Rotas rodoviárias: https://www.emsampa.com.br/rotas_rodoviarias_VII/recife_petrolina.htm ; https://www.emsampa.com.br/rotas_rodoviarias_VIII/petrolina_caruaru.htm
37. Embrapa — Coordenação da qualidade de frutas para produção de polpas: https://ainfo.cnptia.embrapa.br/digital/bitstream/item/44761/1/1-177-2.pdf
40. Governo da Bahia (SDR) — cooperativa e beneficiamento de manga: https://www.ba.gov.br/sdr/noticias/2023-05-31/cooperativa-da-agricultura-familiar-e-destaque-em-beneficiamento-de-manga-e
41. UFPB — Transformações no espaço agrário do Sertão do Pajeú: https://repositorio.ufpb.br/jspui/bitstream/tede/9812/2/Arquivototal.pdf
43. FNDE — Material ilustrativo da Resolução CD/FNDE nº 04/2026: https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae/media-pnae/MaterialIlustrativodaResoluoCD.FNDE04.2026atualizaes.pdf
44. Prefeitura de São José do Belmonte — agricultura familiar e merenda: https://saojosedobelmonte.pe.gov.br/prefeitura-incentiva-agricultura-familiar-e-garante-merenda-de-qualidade/
45. Agência Gov — PAA/Conab: https://agenciagov.ebc.com.br/noticias/202604/paa-conab-abre-chamada-para-aquisicao-de-sementes-e-materiais-propagativos-da-agricultura-familiar ; Decreto 11.802/2023: https://www.legjur.com/legislacao/art/DEC_00118022023-6
46. Jusbrasil — Associação Santa Luzia, Ilha Grande, Belém do São Francisco: https://www.jusbrasil.com.br/nome/associacao-dos-agricultores-e-agricultoras-familiar-santa-luzia-da-comunidade-ilha-grande-municipio-de-belem-do-sao-francisco-pe/cnpj-QgX44nT4Lju
48. AAFPMN3 — Associação dos Agricultores Familiares do N3: https://aafpmn3.org/
49. Adagro — Sanidade vegetal: https://www.adagro.pe.gov.br/sanidade-animal-roda-2 ; mosca-das-frutas: https://www.adagro.pe.gov.br/blog/11-blog/blog/1905-adagro-realiza-operacao-para-controle-da-mosca-das-frutas-no-vale-do-sao-francisco
50. Movimento Econômico — Pesquisa evita corte negro: https://movimentoeconomico.com.br/agronegocio/2026/09/21/pesquisa-evita-corte-negro-e-rejeicao-de-manga-exportada-do-vale-do-sao-francisco/
51. Embrapa, Agência de Informação Tecnológica — Pedúnculo (lida): https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/caju/pos-producao/tecnologia-de-processamento-agroindustrial/pedunculo ; Cultivo do Cajueiro-Anão Precoce (trecho): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/421404/1/Sp012aed.pdf
52. UFJF — Variabilidade climática em Petrolina: https://periodicos.ufjf.br/index.php/geografia/article/download/39026/25442/169324
53. Climate-Data — Petrolina: https://en.climate-data.org/south-america/brazil/pernambuco/petrolina-31938/
54. Climatempo — Climatologia de Petrolina: https://www.climatempo.com.br/climatologia/258/petrolina-pe
55. Onde e Quando — Petrolina em novembro: https://www.onde-e-quando.net/when/america-do-sul/brasil/petrolina/novembro/
59. Embrapa — Desempenho do distrito (citada pelo revisor): https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/489198/1/Desempenhodistrito.pdf
60. UFV, Revista Engenharia na Agricultura — estudo com 75 produtores (citada pelo revisor): https://periodicos.ufv.br/rea/article/download/7678/3161/32743
61. Prefeitura de Buíque — História: https://buique.pe.gov.br/historia/
62. (link incerto) Embrapa — pedúnculo como 90% do peso do caju: https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/422033/1/Dc038.pdf ; ou https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/410033/1/Com.Tec.214.pdf
63. Conab/Prohort — Centrais de abastecimento, comercialização de frutas e hortaliças 2025 (aberto): https://www.gov.br/conab/pt-br/atuacao/informacoes-agropecuarias/hortigranjeiros-prohort/centrais-de-abastecimento-comercializacao-de-frutas-e-hortalicas-2025.pdf
64. Buíque, altitude e acesso (espelho da Wikipédia e Geógrafos): https://en.wikipedia.com/wiki/Buique ; https://www.geografos.com.br/cidades-pernambuco/buique.php
65. Revista Algomais — São José do Belmonte e a Serra do Catolé: https://algomais.com/sao-jose-do-belmonte-o-sebastianismo-e-a-serra-do-catole/
66. Canal Rural — Resolução do PNAE (citada pelo revisor): https://www.canalrural.com.br/politica/resolucao-do-pnae-redefine-compras-da-agricultura-familiar/
67. Folha de Pernambuco — Com 41 °C, Petrolina bate recorde: https://www.folhape.com.br/noticias/com-41oc-petrolina-bate-recorde-de-temperatura-registrada-em/198898/ ; Diario de Pernambuco (2019): https://www.diariodepernambuco.com.br/noticia/vidaurbana/2019/12/registrando-40-7-c-pernambuco-chega-proximo-do-recorde-historico-de-a.html
68. Climatempo — Climatologia de Buíque: https://www.climatempo.com.br/climatologia/5674/buique-pe

69. DINC — Projeto Irrigado Senador Nilo Coelho celebra 36 anos: https://www.dinc.org.br/noticias/projeto-irrigado-nilo-coelho-celebra-36-anos-de-desenvolvimento-no-vale-do-sao-francisco/
70. Embrapa — Desempenho do Distrito de Irrigação Senador Nilo Coelho (Revista Brasileira de Engenharia Agrícola e Ambiental): https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/134430/1/RevistaBrasileiradeEngenhariaAgricolaeAmbientalv.5n.2p.2042092001.pdf

71. IFSertãoPE, campus Petrolina Zona Rural — Chamada Pública PNAE nº 01/2026 (29/10/2026): https://ifsertaope.edu.br/zonarural/2026/10/29/ifsertaope-abre-chamada-publica-para-aquisicao-de-alimentos-da-agricultura-familiar-2/ ; edital: https://ifsertaope.edu.br/zonarural/editais/edital-de-chamada-publica-pnae-n-o-01-2026/
72. IFSertãoPE, campus Petrolina — chamada pública pela plataforma Contrata+Brasil: https://ifsertaope.edu.br/petrolina/campus-petrolina-do-ifsertaope-abre-chamada-publica-para-aquisicao-de-alimentos-da-agricultura-familiar/
73. Prefeitura de Petrolina, Chamada nº 001/2026, pesquisa de preços (notícia): https://didigalvao.com.br/prefeitura-de-petrolina-abre-chamada-publica-para-pesquisa-de-precos-da-agricultura-familiar-destinada-a-alimentacao-escolar/
74. Frutas do Brasil, diretório de exportadores — Coopexvale: https://frutasdobrasil.org/exportadores/coop-de-prod-exportadores-do-vale-do-sao-francisco-coopexvale/ ; COANA: https://frutasdobrasil.org/exportadores/cooperativa-agricola-nova-alianca-coana/
75. Univasf, revista Extramuros — formas associativas no perímetro: https://www.periodicos.univasf.edu.br/index.php/extramuros/article/download/794/555/2731
76. Banco Mundial — Desafios da gestão social dos perímetros públicos de irrigação: https://documents1.worldbank.org/curated/en/841601467995400382/pdf/106301-PORTUGUESE-PUB-P146301-ADD-SERIES-ISBN-PUBLIC-Agua-Brasil-series-no-9.pdf ; Ecocert, COOAPINC 04: https://certificat.ecocert.com/company/30813848-2C82-4606-8248-0A98AFC2E4F0
77. IPEA, Mapa das OSC — associação do Núcleo 2: https://mapaosc.ipea.gov.br/detalhar/1197786 ; Casa dos Dados — associação do Núcleo 5: https://casadosdados.com.br/solucao/cnpj/assoc-dos-peq-prod-rur-do-nucleo-5-proj-sen-nilo-coelho-00796012000174
78. Blog do Mário Martins — câmara fria indicada para a CoopGrapes: https://mariomartins.blog.br/em-petrolina-humberto-reforca-defesa-da-fruticultura-irrigada-do-sertao-do-sao-francisco/
79. Refrigeração em Petrolina — China Refrigeração: https://www.chinarefrigeracaope.com.br/ ; Grupo Hermonex: https://grupohermonex.com.br/cidades/petrolina/camaras-frigorificas ; Climafrio (diretório): https://brasilhvac.com/refrigeration-cool-rooms/climafrio-refrigera-o-ar-condicionado-automotivo-petrolina-p ; TeleListas: https://www.telelistas.net/pe/petrolina/produtos+equipamentos+e+conserto+para+refrigeracao
80. Embrapa — A Cultura da Mangueira, capítulo 17, Colheita e pós-colheita (2002): https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/150626/1/AculturadaMangueira2002c.17p.381405.pdf ; Manga para exportação, procedimentos: https://ainfo.cnptia.embrapa.br/digital/bitstream/item/185568/1/Manga-para-exportacao-procedimentos.pdf
81. Prefeitura de Petrolina — alvará sanitário online: https://petrolina.pe.gov.br/sistema-online-permite-emissao-de-alvara-sanitario-sem-burocracia-em-petrolina/ ; alvará de licença: https://petrolina.pe.gov.br/cartadeservico/alvara-de-licenca/
82. Adagro — relatório de gestão: https://www.lai.pe.gov.br/adagro/wp-content/uploads/sites/10/2024/03/2023-RELATORIO-DE-GESTAO-EXERCICIO-2022.pdf ; plantão em Petrolina: https://www.adagro.pe.gov.br/blog/11-blog/blog/1974-plantao-de-carnaval-da-adagro-garante-exportacao-de-mais-de-5-mil-toneladas-de-frutas
83. Prefeitura de Juazeiro — Mercado do Produtor, horário e contato: https://www.juazeiro.ba.gov.br/mercado-do-produtor-de-juazeiro-nao-tera-alteracao-no-horario-de-funcionamento-durante-o-feriado-de-natal/
84. DINC — O Projeto Público Irrigado: https://www.dinc.org.br/empresa/ ; Blog Carlos Britto — cortes de energia no Brígida e no Caraíbas (maio/2026): https://www.carlosbritto.com/a-exemplo-do-brigida-produtores-do-caraibas-sofrem-sem-energia/
85. Agência Brasil — municípios podem manifestar interesse em executar o PAA em 2026: https://agenciabrasil.ebc.com.br/politica/noticia/2026-05/municipios-ja-podem-manifestar-interesse-em-executar-paa-em-2026

(A numeração tem saltos porque fontes da versão 1 que deixaram de ser usadas foram retiradas.)
