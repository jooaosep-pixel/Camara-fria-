# 10 — Frutas do Nordeste e demanda pelo serviço de câmara fria

Autor: analista-frutas-demanda. Data da pesquisa: 17/11/2026.
Base: `docs/00-premissas.md`. Li também os rascunhos `docs/09-logistica-e-local.md` e `docs/01-projeto-termico.md`.
Este documento não escolhe o local e não projeta equipamento.

## Como ler

- **[Fn]** = número tirado de uma fonte da lista no fim (com link).
- **[CALCULADO]** = conta feita aqui, com os passos à mostra.
- **[SUPOSTO]** = estimativa minha ou conhecimento geral, sem fonte que eu tenha aberto. Precisa ser conferido.
- **[VALIDAR]** = só vale depois de confirmado em campo ou por profissional habilitado.

### O que consegui e o que não consegui abrir

- **Abri e li de verdade:** o banco de dados do IBGE (SIDRA: Produção Agrícola Municipal 2024 e 2025, Censo Agropecuário 2017, Extração Vegetal 2025), dois documentos da Embrapa em PDF (caju, de 2000; perdas pós-colheita, de 1997), o resumo oficial das linhas do Pronaf 2026/2027 (MDA) e um resumo semanal do Prohort/Conab. Estes estão marcados **(aberta)** na lista de fontes.
- **Não abriram** (endereço recusado pela rede da sessão): `www.coldhubs.com`, `www.ecozensolutions.com`, `movimentoeconomico.com.br`. Não tentei outros sites fora da lista liberada.
- **Todo o resto** vem do trecho que a busca na web devolveu, não da leitura da página inteira. Está marcado **(busca)** na lista de fontes.
- **Não achei em lugar nenhum:** preço em R$/kg da manga na CEASA do Recife; preço que a indústria paga pelo pedúnculo do caju; preço do caju de mesa no atacado; tabela de preços atual do ColdHubs e do Ecozen; qualquer câmara fria solar fora da rede funcionando para fruta no Brasil; calendário de safra oficial, mês a mês, para o Nordeste.

---

## Resumo em uma página

1. **O Nordeste produz muita fruta, mas pouca coisa é do pequeno produtor de manga.** A região colhe 84% da manga do país; em Pernambuco, só 17% da manga vem da agricultura familiar (Censo 2017). Goiaba, acerola, maracujá e banana são muito mais "de pequeno" (62% a 81% em PE) [F1][F4].
2. **Manga e caju, juntos, não se sustentam em Pernambuco.** Por dois motivos independentes: (a) pedem temperaturas diferentes (caju 5 °C; manga 10 a 13 °C); (b) não são produzidos no mesmo lugar: 98% da manga está na beira do São Francisco e 88% da castanha de caju está em um único município do Agreste, Buíque [F3]. O estado inteiro colheu 1.894 t de castanha em 2025, o que equivale a cerca de 17 mil t de pedúnculo, quase todo fora do alcance de uma câmara instalada em Petrolina [CALCULADO].
3. **O que complementa a manga no mesmo lugar e na mesma temperatura:** goiaba, acerola, maracujá e mamão. Todas se guardam entre 8 e 10 °C, existem no polo irrigado o ano inteiro e são majoritariamente de agricultura familiar. Uma câmara de **uma zona só, a 10 °C**, atende esse grupo e cabe na premissa (5 a 10 °C).
4. **Guardar manga para "esperar o preço subir" não funciona.** A manga dura 2 a 3 semanas no frio; o preço muda em ciclos de meses (R$ 0,99/kg em fevereiro e R$ 4,94/kg em junho de 2026, no Vale) [F17]. O ganho real do frio é outro: **vender para um comprador melhor** (merenda escolar, PAA, varejo), que exige entrega em dia certo e fruta no ponto, e **perder menos fruta**.
5. **A demanda é fraca como "aluguel de espaço" e pode ser forte como "ferramenta de um grupo que já tem comprador".** Cobrar por caixa por dia, como na Nigéria, pesa demais sobre uma fruta que vale R$ 1,05 a R$ 1,20/kg na roça: cinco dias de câmara a R$ 0,06/kg·dia consomem 25% do valor da fruta [CALCULADO].
6. **Receita só da taxa de armazenagem:** de R$ 4.800 por ano (pessimista) a R$ 29 mil (médio) e R$ 92 mil (otimista), para 4 t úteis [CALCULADO sobre hipóteses SUPOSTAS]. No cenário médio a taxa não paga nem um operador dedicado.
7. **Há evidência contrária séria:** na Índia, em um estudo controlado, só 1% a 2% dos feirantes que tinham de pagar uma pequena taxa usaram a câmara solar em um dia qualquer, e o pequeno agricultor quase não foi beneficiado [F14]. No Brasil não achei nenhum caso em operação para copiar.
8. **Antes de comprar qualquer equipamento:** fazer as entrevistas da seção 9. Regra proposta: seguir só se houver pelo menos um comprador com compromisso por escrito e pelo menos 8 de 15 produtores dispostos a pagar a taxa.

---

## 1. Frutas do Nordeste

### 1.1 Quanto cada estado produz (IBGE, Produção Agrícola Municipal de 2025)

Toneladas, salvo coco e abacaxi, que o IBGE publica em **mil frutos**. Fonte: SIDRA, tabelas 1613 e 1612 [F1][F2] (aberta). "NE/BR" é a fatia do Nordeste no total do Brasil [CALCULADO a partir das duas colunas].

| Fruta | Brasil | Nordeste | NE/BR | MA | PI | CE | RN | PB | PE | AL | SE | BA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manga | 1.905.559 | 1.593.235 | 84% | 433 | 3.301 | 41.352 | 39.735 | 7.083 | **609.940** | 10.066 | 14.155 | **867.170** |
| Castanha de caju | 114.749 | 113.954 | 99% | 2.650 | 14.684 | **69.319** | 19.640 | 419 | 1.894 | 701 | — | 4.647 |
| Uva | 2.197.707 | 970.789 | 44% | — | 67 | 574 | 960 | 1.445 | **851.883** | — | — | 115.860 |
| Melão | 705.848 | 688.578 | 98% | 28 | 35.946 | 120.841 | **362.378** | 158 | 71.248 | 4.166 | — | 93.813 |
| Mamão | 1.158.987 | 611.189 | 53% | 619 | 93 | 119.007 | 102.735 | 35.614 | 16.743 | 14.538 | 2.656 | **319.184** |
| Banana | 7.288.960 | 2.725.849 | 37% | 78.718 | 49.413 | 495.641 | 250.981 | 148.077 | 649.265 | 110.012 | 31.746 | **911.996** |
| Goiaba | 604.455 | 290.909 | 48% | 1 | 673 | 25.906 | 3.261 | 3.187 | **204.287** | 2.828 | 2.666 | 48.100 |
| Acerola | 158.687 | 143.004 | 90% | — | 1.447 | **70.918** | 2.238 | 5.944 | 57.190 | 3.333 | 140 | 1.794 |
| Maracujá | 864.518 | 615.883 | 71% | 171 | 749 | 169.627 | 28.963 | 11.805 | 26.819 | 15.041 | 11.941 | **350.767** |
| Graviola | 172.824 | 170.660 | 99% | — | — | 1.573 | 136 | 924 | 22.463 | 8.734 | 45 | **136.785** |
| Melancia | 2.251.431 | 848.954 | 38% | 25.763 | 76.039 | 66.964 | 179.032 | 7.457 | 123.452 | 28.414 | 3.779 | **338.054** |
| Coco (mil frutos) | 2.018.298 | 1.626.148 | 81% | 5.092 | 6.913 | **587.252** | 79.263 | 94.773 | 263.963 | 79.725 | 145.370 | 363.797 |
| Abacaxi (mil frutos) | 1.596.703 | 618.889 | 39% | 38.428 | 65 | 1.201 | 67.837 | **331.860** | 51.503 | 60.832 | 27.389 | 39.774 |
| Umbu (extrativismo, 2025) | 16.274 | 9.923 | 61% | — | 104 | 27 | 825 | 2.343 | 587 | 321 | — | **5.716** |

Observações:
- **Caju (o pedúnculo, a "fruta") não tem produção publicada pelo IBGE** na pesquisa anual: a linha "Caju" vem vazia; só a castanha é medida [F1]. Regra de conversão: em peso o caju é 10% castanha e 90% pedúnculo [F6], ou seja, 9 kg de pedúnculo para cada 1 kg de castanha. Nordeste 2025: 113.954 × 9 = **cerca de 1,03 milhão de t de pedúnculo** [CALCULADO].
- A safra de castanha de 2025 (114.749 t) foi bem menor que a de 2024 (169.210 t) [F1]. A produção de caju oscila muito de um ano para outro.
- Umbu é coleta na caatinga, não plantio; o número é da pesquisa de extração vegetal [F5].
- Os números de 2024, que o doc 09 usa, estão na seção 11 para comparação.

### 1.2 Principais polos

| Fruta | Polos principais | Fonte |
|---|---|---|
| Manga | Vale do São Francisco: Petrolina 286.250 t, Belém do São Francisco 179.200 t, Lagoa Grande 66.500 t, Santa Maria da Boa Vista 42.500 t (PE, 2025); do lado baiano, Juazeiro e Casa Nova | [F3]; lado baiano: [F27] |
| Caju | Ceará (61% da castanha do país em 2025), Piauí, Rio Grande do Norte. Em PE: Buíque 1.662 t de castanha (88% do estado); o resto é pulverizado | [F1][F3] |
| Uva | Petrolina 621.200 t e Lagoa Grande 191.780 t (PE); Juazeiro e Casa Nova (BA) | [F3] |
| Melão | Rio Grande do Norte (região de Mossoró) e Ceará; em PE, Belém do São Francisco, Ibimirim e Inajá | [F2][F3] |
| Mamão | Bahia (sul do estado), Ceará, Rio Grande do Norte | [F1] |
| Banana | Bahia, Pernambuco (Santa Maria da Boa Vista 210.000 t; Vicência e São Vicente Férrer na Zona da Mata), Ceará | [F1][F3] |
| Goiaba | Pernambuco tem 70% da goiaba do Nordeste: Santa Maria da Boa Vista 80.000 t, Petrolina 48.000 t | [F1][F3] |
| Acerola | Ceará e Pernambuco: Petrolina 30.000 t, Pombos 7.500 t, Orocó 7.000 t, Santa Maria da Boa Vista 6.500 t | [F1][F3] |
| Maracujá | Bahia e Ceará; em PE é pulverizado em 82 municípios (26.819 t) | [F1][F3] |
| Coco | Ceará, Bahia, Pernambuco (Petrolândia e Petrolina) | [F1][F3] |
| Abacaxi | Paraíba; em PE, Gravatá e Pombos | [F2][F3] |
| Graviola | Bahia; em PE, Chã Grande e Gameleira | [F1][F3] |
| Umbu | Bahia e Paraíba | [F5] |

**Ponto que interessa ao projeto:** os mesmos municípios da beira do São Francisco que têm a manga também têm goiaba, acerola, banana, uva e coco em grande volume. O caju não está lá.

### 1.3 Quanto é da agricultura familiar (Censo Agropecuário 2017)

Fatia da quantidade produzida que saiu de estabelecimentos classificados como agricultura familiar. Fonte: SIDRA, tabela 6955 [F4] (aberta). O Censo conta só pomares com 50 pés ou mais; os volumes de 2017 são menores que os de hoje. Percentuais [CALCULADO].

| Fruta | Nordeste | Pernambuco | Leitura |
|---|---|---|---|
| Maracujá | 70% | 81% | Fruta de pequeno |
| Caju (castanha) | 62% | 77% | Fruta de pequeno |
| Caju (fruto) | 67% | 22% (base pequena: 3.901 t) | Em PE, pouco volume e pouco familiar |
| Graviola | 60% | 54% | |
| Acerola | 54% | 62% | Fruta de pequeno |
| Goiaba | 51% | 62% | Fruta de pequeno |
| Banana | 51% | 71% | Fruta de pequeno |
| Coco | 34% | 39% | |
| **Manga** | **25%** | **17%** | **Dominada por médio e grande** |
| Mamão | 12% | 61% | No NE é de empresa; em PE o volume é pequeno |
| Uva de mesa | 10% | 11% | Fruta de empresa |
| Melão, abacaxi, melancia | sem dado | sem dado | A tabela que consultei (6957) veio sem o recorte familiar para esses produtos |

**Leitura direta:** das duas frutas escolhidas pelo dono, a manga é a menos "de pequeno produtor" de toda a lista, e o caju é de pequeno mas quase não existe em Pernambuco. Se o público do projeto é o pequeno, goiaba, acerola, maracujá e banana têm mais gente dentro.

### 1.4 Calendário de safra

Não achei calendário oficial mês a mês para o Nordeste. A tabela junta o que tem fonte com o que é conhecimento geral. **Toda a tabela precisa ser conferida em campo [VALIDAR].**

Legenda: **P** = pico; **x** = tem oferta; **–** = pouca ou nenhuma.

| Fruta e região | J | F | M | A | M | J | J | A | S | O | N | D | Base |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Manga irrigada (Vale do São Francisco) | P | x | x | x | x | x | x | x | x | P | P | P | doc 09, seção 1.5 |
| Manga de sequeiro | x | – | – | – | – | – | – | – | – | x | P | P | doc 09 [SUPOSTO lá] |
| Caju (Nordeste) | x | – | – | – | – | – | – | x | P | P | x | x | doc 09, seção 1.5 |
| Goiaba irrigada | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO]: com poda e irrigação colhe-se o ano todo |
| Acerola irrigada | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO]: várias colheitas por ano sob irrigação |
| Maracujá irrigado | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO] |
| Mamão | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO] |
| Banana | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO] |
| Uva (Vale) | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO]: duas safras por ano |
| Melão (RN/CE) | x | – | – | – | – | – | – | x | P | P | P | x | Parcial: a temporada de exportação de frutas pelo Pecém abre em setembro [F32]; meses [SUPOSTO] |
| Umbu | x | x | x | – | – | – | – | – | – | – | – | x | [SUPOSTO] |
| Coco | x | x | x | x | x | x | x | x | x | x | x | x | [SUPOSTO] |

Preço da manga no ano (ajuda a ler o calendário): no Vale, a tommy valeu R$ 1,33/kg em dezembro de 2024, R$ 2,23 a R$ 2,55 em agosto e setembro de 2025, R$ 0,99 em fevereiro de 2026, **R$ 4,94 em junho de 2026** e R$ 1,20 em novembro de 2026 [F17]. Preço baixo de outubro a fevereiro (muita fruta), preço alto no meio do ano (pouca fruta).

### 1.5 Fichas pós-colheita

"Dano por frio" é o estrago que a fruta tropical sofre quando fica abaixo de uma certa temperatura: escurece por dentro, mancha e não amadurece direito. "Etileno" é um gás que a fruta madura solta e que faz as vizinhas amadurecerem mais depressa.

| Fruta | Temperatura | Umidade | Vida útil no frio | Vida útil sem frio | Dano por frio | Etileno | Fonte |
|---|---|---|---|---|---|---|---|
| **Manga** | 13 °C (verde-madura); 10 °C (madura) | 85–90% | 2 a 3 semanas | cerca de 1 semana [SUPOSTO] | **Sim**, abaixo de 10 a 13 °C; a Embrapa viu escurecimento da polpa entre 8 e 10 °C | Produz e é sensível [SUPOSTO] | [F7] tabela 5; doc 01, seção 2.1 |
| **Caju (pedúnculo)** | 5 °C | 85–90% | cerca de 15 dias embalado em bandeja com filme; 10 a 25 dias conforme o clone | **menos de 2 dias** [SUPOSTO; a Embrapa fala em "reduzido período de pós-colheita" sem dar número no trecho lido] | Clones de pedúnculo vermelho sofrem a 5 °C | Não amadurece depois de colhido; produz pouco [SUPOSTO] | [F6]; doc 01, seção 2.1 |
| Goiaba | 8 a 10 °C | 85–90% | até 16 dias (ensaio com Paluma a 10 °C) | 3 a 5 dias [SUPOSTO] | Sim, abaixo de 8 °C [SUPOSTO] | Produz e é sensível [SUPOSTO] | [F20] |
| Acerola | 8 °C (um estudo); 10 a 12 °C (outro, feito em Petrolina) | 90% | até 11 dias a 8 °C no melhor genótipo | 2 a 3 dias [SUPOSTO] | Indícios abaixo de 10 °C (por isso o segundo estudo recomenda 10 a 12 °C) | Não respondeu ao etileno | [F20] |
| Maracujá | 7 a 10 °C | 85–90% | 3 a 5 semanas | 3 a 7 dias | Sim, abaixo de 7 °C [SUPOSTO] | Produz [SUPOSTO] | [F7] tabela 5; [F20] |
| Mamão | 7 °C (maduro) a 13 °C | 85–90% | 1 a 3 semanas | 4 a 7 dias [SUPOSTO] | Sim | Sensível | [F7] tabela 5; [F21] |
| Abacaxi | 7 a 13 °C | 85–90% | 2 a 8 semanas | 1 a 2 semanas [SUPOSTO] | Sim, abaixo de 7 °C | Pouco sensível [SUPOSTO] | [F7] tabela 5 |
| Melão | 2 a 5 °C (cantaloupe); 7 a 10 °C para o amarelo [SUPOSTO] | 85–95% [SUPOSTO] | Amarelo: semanas; ensaios da Embrapa foram até 54 e 59 dias | Amarelo: 2 a 4 semanas [SUPOSTO] | Imaturos sofrem | Cantaloupe produz e é sensível | [F21]; [F20] |
| Uva | –1 a –0,5 °C | 90–95% | 1 a 6 meses | poucos dias [SUPOSTO] | Não | Pouco sensível [SUPOSTO] | [F7] tabela 5 |
| Banana | 13 a 14 °C | 85–90% [SUPOSTO] | 1 a 3 semanas [SUPOSTO] | 1 semana [SUPOSTO] | **Sim**: já aparece a 10,5 °C; nanicão e maçã sofrem mais que a prata | Produz e é muito sensível | [F20]; [F21] |
| Umbu | cerca de 14 °C | — | até 19 dias | 2 a 3 dias | Provável abaixo de 14 °C [SUPOSTO] | — | [F20] |
| Limão | 12 a 14 °C | 85–90% | 2 a 3 meses | — | Sim | — | [F7] tabela 5 |
| Laranja | 3 a 9 °C | 85–90% | 3 a 8 semanas | — | — | — | [F7] tabela 5 |
| Coco verde, graviola, melancia | **não encontrei dado** | | | | | | Pesquisar se entrarem no projeto |

**Quem pode dividir a câmara com quem** (pela temperatura; o etileno pede atenção quando há fruta madura junto com fruta verde) [CALCULADO a partir da tabela acima]:

| Grupo | Temperatura do ar | Frutas |
|---|---|---|
| A — frio | 5 °C | Caju; laranja. (Uva e melão cantaloupe aguentam, mas pedem ainda menos.) |
| B — meio | 8 a 10 °C | Goiaba, maracujá, mamão maduro, acerola, abacaxi, melão amarelo, **manga já madura ou "de vez", por poucos dias** |
| C — fresco | 12 a 14 °C | Manga verde-madura (para guardar 2 a 3 semanas), banana, umbu, limão |

- Caju **não** divide câmara com nenhuma fruta do grupo B ou C: a 5 °C elas sofrem dano por frio.
- Dentro do grupo B, separar em pilhas distintas a fruta madura (que solta etileno) da fruta que se quer segurar verde, e ventilar [SUPOSTO; regra geral de pós-colheita citada em [F21]].

---

## 2. Compatibilidade com a câmara do projeto (5 a 10 °C, 5 t)

### 2.1 Quais servem

| Fruta | Serve? | Em que temperatura | Comentário |
|---|---|---|---|
| Caju | **Sim** | 5 °C | A fruta que mais ganha com o frio (de menos de 2 dias para cerca de 15). Exige bandeja e filme. Não aceita companhia |
| Goiaba | **Sim** | 10 °C | Fruta de pequeno, o ano todo, muito volume em PE |
| Maracujá | **Sim** | 10 °C | Fruta de pequeno; aguenta semanas |
| Acerola | **Sim** | 10 °C | Fruta de pequeno; mas boa parte vai direto para a indústria, que congela (seção 8) |
| Mamão | **Sim** | 10 °C | Pouco volume em PE |
| Abacaxi | **Sim** | 10 °C | Em PE fica no Agreste (Gravatá, Pombos), longe do sertão |
| Melão amarelo | Sim, mas precisa pouco | 10 °C | Dura semanas fora do frio; baixo ganho |
| **Manga** | **No limite** | 10 °C, só para fruta madura e por poucos dias | Para guardar manga verde-madura por 2 a 3 semanas o certo é 12 a 13 °C, **fora da faixa da premissa**. Ver conflito na seção 12 |
| Uva | Não | pede –1 a 0 °C | E é fruta de empresa, com estrutura própria |
| Banana | **Não** | pede 13 a 14 °C | A 10 °C escurece |
| Umbu | Não | pede cerca de 14 °C | |
| Limão | Não | pede 12 a 14 °C | |
| Coco verde, melancia | Não compensa | — | Volumosos, baratos por quilo, duram sem frio [SUPOSTO] |

### 2.2 Manga + caju se sustenta?

**Não, em Pernambuco, como par único de frutas num mesmo ponto.** As razões:

1. **Temperatura.** Caju a 5 °C, manga a 10 a 13 °C. Não há temperatura de compromisso boa (doc 01, seção 2.2). A saída do engenheiro são duas zonas, e isso baixa a capacidade para cerca de 4 t (doc 01, seção 13.3, item 8).
2. **Geografia.** Dados municipais do IBGE para 2025 [F3]:
   - Manga: sete municípios da beira do São Francisco somam 596.725 t de 609.940 t = **98%** [CALCULADO].
   - Castanha de caju: Buíque 1.662 t de 1.894 t = **88%** [CALCULADO]. Nos municípios próximos do polo da manga o IBGE registra quase nada: Floresta 5 t, Jatobá 5 t, Tacaratu 15 t de castanha.
   - Buíque fica no Agreste, a centenas de quilômetros de Petrolina [SUPOSTO; a distância é assunto do doc 09].
3. **Volume.** Pernambuco inteiro: 1.894 t de castanha × 9 = **17.046 t de pedúnculo** em 2025 [CALCULADO]. Só Buíque: 1.662 × 9 = 14.958 t. Todo o Sertão do Pajeú (São José do Belmonte 77 + Flores 28 + Carnaíba 10 = 115 t de castanha): 115 × 9 = **1.035 t de pedúnculo no ano** [CALCULADO].
4. **Calendário.** No sequeiro as duas amadurecem nos mesmos meses (doc 09, seção 1.5): não dá para alternar por safra.
5. **Destino do caju.** O pedúnculo quase não é vendido fresco: a Embrapa estimava o aproveitamento em cerca de 12%, quase todo como suco [F6]; reportagem de 2024 fala em 90% de desperdício no Ceará [F11]. O mercado de caju de mesa existe (embalagem padrão na Ceagesp é caixa de papelão de 1,2 kg [F29]), mas é um produto delicado, de bandeja, com clone próprio.

**Onde a combinação se sustentaria:** em outro estado (Ceará, Piauí, Rio Grande do Norte), onde há caju em volume e manga de sequeiro na mesma região; ou em Pernambuco com **duas câmaras em dois lugares**. Isso é decisão do dono (seção 13).

### 2.3 O que complementa a manga

No polo irrigado, as frutas que estão no mesmo lugar, na mesma faixa de temperatura e nas mãos de pequenos:

| Complemento | Volume no entorno (2025) [F3] | Fatia familiar em PE [F4] | Temperatura |
|---|---|---|---|
| Goiaba | Santa Maria da Boa Vista 80.000 t; Petrolina 48.000 t | 62% | 8–10 °C |
| Acerola | Petrolina 30.000 t; Orocó 7.000 t; Santa Maria da Boa Vista 6.500 t | 62% | 8–12 °C |
| Maracujá | Santa Maria da Boa Vista 2.800 t; Petrolina 1.980 t | 81% | 7–10 °C |
| Mamão | Cabrobó 4.950 t; Lagoa Grande 3.680 t; Orocó 3.360 t | 61% | 7–13 °C |

**Proposta deste documento:** tratar a câmara como **uma zona a 10 °C para manga madura, goiaba, maracujá, mamão e acerola**, e deixar o caju como segunda etapa ou segundo local.

### 2.4 Calendário anual de ocupação

Para um ponto no polo irrigado do São Francisco (o local é do doc 09). Ocupação esperada é [SUPOSTO] e depende inteiramente de haver comprador.

| Meses | Fruta principal | Complemento | Ocupação esperada | Por quê |
|---|---|---|---|---|
| Out–Jan | **Manga** (pico de oferta, preço baixo) | Goiaba, acerola | Alta | Sobra fruta; quem tem comprador fixo precisa segurar e regular a entrega |
| Fev–Mar | Manga (fim do pico) | Goiaba, maracujá, mamão, acerola | Média | |
| Abr–Jul | Goiaba, maracujá, acerola | Pouca manga (falta fruta, preço alto, vende-se na hora) | **Baixa** | É a entressafra da câmara. Coincide com o ano letivo, o que ajuda a merenda escolar |
| Ago–Set | Manga (oferta voltando) | Goiaba, acerola; **caju, só se o campo confirmar oferta** | Média | |

Para um ponto no Agreste do caju (Buíque): caju de setembro a janeiro e **câmara quase parada de fevereiro a agosto**, a menos que haja goiaba ou maracujá por perto [SUPOSTO; não verifiquei].

---

## 3. Perdas pós-colheita

### 3.1 O que há de número

| Fruta | Perda estimada | De quando e de quem | Fonte |
|---|---|---|---|
| Manga | 27,5% | Estimativa do Ministério da Agricultura de 1992, reproduzida pela Embrapa em 1997 | [F7] (aberta) |
| Mamão | 30,4% | idem | [F7] |
| Banana | 40,1% | idem | [F7] |
| Abacaxi | 23,7% | idem | [F7] |
| Frutas em geral | 30,0% | idem, 1990–1992 | [F7] |
| Frutas e hortaliças | 30% a 35% da produção ao consumidor | Levantamento com 132 vendedores na CEASA de Salvador, 2024 | [F22] |
| Mamão | 25% "como normalmente ocorre"; 2% com embalagem melhor | Reportagem sobre pesquisa da Embrapa | [F22] |
| Caju (pedúnculo) | cerca de 88% não aproveitado (aproveitamento de 12%) | Embrapa, 2000 | [F6] (aberta) |
| Caju (pedúnculo) | cerca de 90% desperdiçado no Ceará | Reportagem, 2024 | [F11] |

**Cuidado com esses números:**
- Os percentuais por fruta têm **mais de 30 anos**. A própria Embrapa escreveu, no mesmo documento, que as informações sobre perdas no Brasil "são insuficientes" [F7]. Uma revisão acadêmica diz que a faixa de 30% a 45%, muito repetida, é difícil de comprovar [F22].
- **Não achei número específico para o Nordeste nem para Pernambuco**, nem para goiaba, acerola e maracujá.
- O "desperdício" do caju não é fruta que estragou esperando comprador: é pedúnculo que **nunca foi colhido para venda**, porque quem compra a castanha não quer o pedúnculo. Frio não resolve isso sozinho; precisa existir quem compre a fruta.

### 3.2 Quanto o frio reduz

- **Vida útil** (o efeito mais bem documentado): caju de menos de 2 dias para cerca de 15 [F6]; maracujá de 3 a 7 dias para 3 a 5 semanas [F7][F20]; umbu de 2 a 3 dias para até 19 [F20]; manga para 2 a 3 semanas [F7].
- **Perda em quilos:** o ColdHubs (Nigéria) afirma reduzir o estrago em até 80% e aumentar a renda dos usuários em 50% [F12]. São números **divulgados pela própria empresa**, sem avaliação independente que eu tenha achado.
- Um estudo de viabilidade em Uganda **projetou** (não mediu) redução de 30% nas perdas e aumento de 39% na receita, com o serviço custando 13,6% da receita [F16].
- **Não achei medição brasileira** de quanto uma câmara fria reduz a perda de manga, goiaba ou caju na mão do pequeno produtor. Para as contas, usar 30% a 50% de redução da perda como hipótese [SUPOSTO] e medir no piloto.

---

## 4. Demanda pelo serviço

### 4.1 Quem pagaria

| Quem | Pagaria? | Por quê | Base |
|---|---|---|---|
| Produtor sozinho, que vende na roça | **Provavelmente não** | O comprador vai ao pomar, classifica e leva no dia; o produtor é "tomador de preço" (doc 09, seção 1.2). Não há o que guardar | doc 09 |
| **Grupo de 5 a 15 famílias com comprador fixo** (merenda, PAA, mercado, restaurante) | **Sim: é o cliente natural** | Precisa entregar em dia certo, fruta no ponto, em quantidade combinada. Sem frio, não consegue | doc 09, seções 1.4 e 2.4 |
| Cooperativa ou associação | Sim, como dona ou gestora | Já tem operador, CNPJ, acesso a crédito e a compras públicas | [F8] |
| Atravessador ou feirante | Talvez, por dia | É o usuário típico do ColdHubs, que fica dentro de mercados e feiras [F12]. No estudo da Índia, quem mais usou foram os comerciantes maiores [F14] | [F12][F14] |
| Agroindústria de polpa | Pouco provável | Trabalha com fruta congelada e tem frio próprio; compra o refugo barato [SUPOSTO] | — |
| Comprador público (PAA/PNAE) | Não paga a câmara, mas **é quem cria a demanda** | Paga preço bem acima da roça e exige regularidade | [F18][F19] |
| Exportador | Não | Tem packing house (galpão de embalagem) e câmara próprios (doc 09, seção 1.2) | doc 09 |

### 4.2 Quanto ganha a mais quem guarda

Três ganhos diferentes. É importante não misturar.

**(a) Esperar o preço subir entre safra e entressafra: não dá.**
- Manga tommy no Vale: R$ 0,99/kg (fev/2026) e R$ 4,94/kg (jun/2026) [F17]. Diferença de 5 vezes.
- Mas entre fevereiro e junho passam 4 meses, e a manga dura 2 a 3 semanas [F7]. **A câmara não atravessa a entressafra.** Quem faz isso é a indústria, congelando polpa.

**(b) Esperar alguns dias: ganho possível, mas incerto.**
- As notas semanais do Cepea mostram o preço da tommy variando +24%, –19%, +26% e +34% **de uma semana para a outra** [F17].
- Para quem pode segurar a fruta uma ou duas semanas isso é oportunidade, mas a variação vai nos dois sentidos. Não é renda garantida [CALCULADO a partir das variações citadas].

**(c) Vender para um comprador melhor: é o ganho que sustenta o projeto.**

| Canal | Preço da manga | Fonte |
|---|---|---|
| Na roça, Petrolina (10/11/2026) | R$ 1,05/kg (palmer) e R$ 1,20/kg (tommy) | [F17] |
| Pesquisa de preços para compras da agricultura familiar, Emater-RN (maio/2026) | R$ 5,06/kg | [F18] |
| CEASA do Recife | **não encontrei valor em R$/kg** | — |

- Diferença entre a roça e a referência de compra pública: 5,06 – 1,20 = **R$ 3,86/kg** [CALCULADO]. Atenção: o preço público é do Rio Grande do Norte, não de Pernambuco, e inclui classificação, embalagem e entrega na escola. Serve como ordem de grandeza. [VALIDAR com a chamada pública do município escolhido]
- Teto da merenda escolar: R$ 40.000 por agricultor, por ano, por entidade compradora; e desde 2026 pelo menos 45% do dinheiro federal da merenda tem de ir para a agricultura familiar [F19].
- Conta: 10 famílias × R$ 40.000 = R$ 400.000 por ano por prefeitura (igual ao doc 09, seção 2.4). A R$ 5,06/kg isso é 400.000 ÷ 5,06 = **79 t de fruta por ano** [CALCULADO]: cerca de 0,3 t por dia em 270 dias. **É um terço da entrada diária que a câmara aceita.** Um contrato de merenda com uma prefeitura ocupa a câmara só em parte.

**(d) Perder menos.** Se a perda cai de 27,5% para a metade [SUPOSTO, seção 3.2], o grupo vende 13,75% a mais da mesma colheita. Em 100 t a R$ 1,20/kg são 13,75 t × 1.200 = **R$ 16.500 por ano** [CALCULADO]. A preço de roça é pouco; só pesa quando a fruta salva é vendida no canal melhor.

### 4.3 Tamanho do mercado em número de câmaras

Método: (produção da agricultura familiar nas frutas que servem) × (fatia que passaria por câmara comunitária) ÷ (toneladas que uma câmara gira por ano).

**Passo 1 — produção familiar das frutas do grupo B**, aplicando a fatia familiar de 2017 [F4] ao volume de 2025 [F1]. Supõe que a fatia não mudou [SUPOSTO].

| Fruta | Nordeste (t) | Pernambuco (t) |
|---|---|---|
| Manga | 1.593.235 × 25,4% = 404.682 | 609.940 × 17,3% = 105.520 |
| Goiaba | 290.909 × 51,2% = 148.945 | 204.287 × 62,3% = 127.271 |
| Acerola | 143.004 × 53,8% = 76.936 | 57.190 × 62,0% = 35.458 |
| Maracujá | 615.883 × 70,2% = 432.350 | 26.819 × 81,2% = 21.777 |
| Mamão | 611.189 × 11,9% = 72.731 | 16.743 × 60,6% = 10.146 |
| **Soma** | **1.135.645** | **300.172** |

[CALCULADO]

**Passo 2 — giro de uma câmara:** 97 a 231 t por ano nos cenários médio e otimista (seção 6). Adoto 150 t/ano [SUPOSTO].

**Passo 3 — fatia que passaria por câmara comunitária.** **Este é o número que ninguém tem.** Três hipóteses [SUPOSTO]:

| Fatia | Nordeste | Pernambuco |
|---|---|---|
| 1% | 1.135.645 × 1% ÷ 150 = **76 câmaras** | 300.172 × 1% ÷ 150 = **20 câmaras** |
| 3% | **227** | **60** |
| 10% | **757** | **200** |

[CALCULADO]

- Caju, se entrar: pedúnculo familiar no Nordeste ≈ 1.025.586 × 62,5% = 641.000 t [CALCULADO]. É um volume enorme no papel, mas hoje quase todo sem comprador de fruta fresca (seção 3.1). Não somei.
- **Como ler:** a conta mostra que, se o modelo funcionar, há espaço para dezenas de unidades em Pernambuco e centenas no Nordeste. Ela **não prova** que alguém vai pagar. Quem decide entre 1% e 10% são as entrevistas da seção 9.

---

## 5. Modelos de cobrança e referências

### 5.1 Como cobram os de fora

| Empresa | Como cobra | Quanto | Observação | Fonte |
|---|---|---|---|---|
| **ColdHubs** (Nigéria) | Por caixa plástica de 20 kg, por dia ("paga enquanto guarda") | 100 nairas em fontes de 2018–2020; 200 nairas em fontes mais novas. As fontes equiparam a US$ 0,25 a US$ 0,50 da época | Câmaras dentro de feiras e pontos de concentração. A empresa declara mais de 50 unidades e mais de 11 mil usuários; outra fonte fala em 24 câmaras e 3.517 usuários. Números não batem entre fontes | [F12] (busca; o site não abriu) |
| **Ecozen Ecofrost** (Índia) | Três modelos: **venda** a produtores médios e grandes; **aluguel mensal** do equipamento; **pagamento por uso**, por caixa, direto ou via cooperativa | Venda: 5 a 15 lakh de rupias conforme o tamanho; uso: 1 a 2 rupias por quilo | Fontes de 2018 a 2022. Não achei tabela atual nem preço por caixa por dia | [F13] (busca; o site não abriu) |
| **Oorja** (Índia, Bihar) | Por caixa por dia, sem o produtor comprar nada | não encontrado | | [F13] |

Conversão para reais: não fiz. O câmbio da naira mudou muito desde essas reportagens e eu não tenho cotação com fonte. Em ordem de grandeza, as referências ficam entre **alguns centavos e cerca de 15 centavos de real por quilo por dia** [SUPOSTO]. Use como faixa, não como preço.

### 5.2 Opções de cobrança para este projeto

| Modelo | Como funciona | Bom para | Risco |
|---|---|---|---|
| Por caixa por dia | Caixa de 20 a 25 kg, paga na retirada | Feirante, atravessador, uso avulso | Receita imprevisível; alguém tem de controlar caixa por caixa |
| Por quilo movimentado (taxa única) | Taxa fixa por kg que passa pela câmara, até um número de dias | Grupo com comprador fixo | Precisa de balança e de regra para quem passa do prazo |
| Mensalidade por cota | Cada família paga um valor fixo por mês e tem direito a tantas caixas | Associação | Na entressafra a família para de pagar |
| Embutido na venda | A associação vende, desconta um percentual e paga a câmara | Cooperativa que comercializa | Só funciona se a cooperativa vender bem |
| Venda ou aluguel do equipamento | O dono do projeto fabrica; cooperativa compra com crédito | Escalar | Tira o risco de operação do dono e passa para a cooperativa |

### 5.3 Iniciativas parecidas no Brasil

- **Câmara fria solar fora da rede, para fruta, em operação: não encontrei nenhuma.**
- Paraíba: cooperativa de mulheres agricultoras em que a rede elétrica não aguentava a câmara fria e os freezers juntos; painéis solares resolveram. A reportagem não diz se é fora da rede [F24].
- Paraná (Maringá): cooperativa recebeu usina solar e duas câmaras frias, R$ 696 mil, dos quais R$ 600 mil do governo do estado; ligada à rede [F24].
- Amazonas (Instituto Mamirauá e USP): máquinas de gelo solares **sem bateria** para comunidades ribeirinhas, cerca de R$ 25 mil cada, 30 kg de gelo por dia; apresentado como experimental [F23]. É o parente mais próximo em tecnologia, mas para pescado.
- Vale do São Francisco: cooperativas de pequenos com packing house e câmara fria obtidos por programas federais (doc 09, seção 1.2). Procurei notícia de estrutura parada e não achei; **não achar não quer dizer que funcionem** [VALIDAR em campo].

### 5.4 Concorrentes e substitutos

| Substituto | Situação | Comentário |
|---|---|---|
| **Vender na roça no mesmo dia** | É o padrão hoje (doc 09) | O concorrente mais forte: custo zero, risco zero, dinheiro na hora |
| **Vender para polpa** | Indústria compra refugo e fruta de segunda | Preço baixo, mas absorve volume; não achei o preço pago |
| **Câmara ligada à rede** | Onde há rede trifásica é mais barata de comprar | O polo irrigado tem rede. O solar fora da rede só se justifica onde a rede é fraca, cara ou não chega |
| **Contêiner frigorífico usado** | Anúncios de 20 pés usado por R$ 20.000 a R$ 30.000 em São Paulo, sem frete | Precisa de energia elétrica. Preço de aluguel mensal: não encontrado [F26] |
| Caminhão refrigerado | Usado pelo exportador | Não é alternativa para o pequeno [SUPOSTO] |
| Packing house de exportador ou de cooperativa | Existe no Vale | Atende quem vende para eles |

---

## 6. Conta simples de viabilidade

Só o lado da receita. O custo do protótipo (aqui chamado **X**) ainda não está fechado.

### 6.1 Hipóteses (todas [SUPOSTO]; trocar pelas do campo)

| Hipótese | Pessimista | Médio | Otimista |
|---|---|---|---|
| Capacidade útil | 4 t (doc 01: duas zonas) | 4 t | 4 t |
| Ocupação média nos dias de operação | 20% | 45% | 70% |
| Dias de operação por ano | 200 | 270 | 330 |
| Taxa por quilo por dia | R$ 0,03 | R$ 0,06 | R$ 0,10 |
| Equivale a, por caixa de 20 kg por dia | R$ 0,60 | R$ 1,20 | R$ 2,00 |
| Permanência média da fruta | 6 dias | 5 dias | 4 dias |

### 6.2 Receita [CALCULADO]

Receita anual = capacidade (kg) × ocupação × dias × taxa.

| | Pessimista | Médio | Otimista |
|---|---|---|---|
| Conta | 4.000 × 0,20 × 200 × 0,03 | 4.000 × 0,45 × 270 × 0,06 | 4.000 × 0,70 × 330 × 0,10 |
| **Receita por ano** | **R$ 4.800** | **R$ 29.160** | **R$ 92.400** |
| Receita por mês (média dos 12 meses) | R$ 400 | R$ 2.430 | R$ 7.700 |
| Receita por mês em operação | R$ 720 | R$ 3.240 | R$ 8.400 |
| Fruta que passa por dia (estoque ÷ permanência) | 0,13 t | 0,36 t | 0,70 t |
| Fruta que passa por ano | 27 t | 97 t | 231 t |
| Taxa total por quilo (taxa × permanência) | R$ 0,18 | R$ 0,30 | R$ 0,40 |
| Mesma conta com 5 t úteis (× 1,25) | R$ 6.000 | R$ 36.450 | R$ 115.500 |

**Teste de realidade da taxa:** no cenário médio o produtor paga R$ 0,30 por quilo. Manga na roça vale R$ 1,20/kg [F17]: a taxa come 0,30 ÷ 1,20 = **25% do valor da fruta**. Só se paga se a venda depois do frio render bem mais que R$ 1,50/kg. Com o canal de merenda (referência de R$ 5,06/kg [F18]) rende; vendendo ao mesmo comprador da roça, não [CALCULADO].

**Limite físico:** com 4 t e permanência de 5 dias, a câmara gira no máximo 4 ÷ 5 = 0,8 t por dia. A entrada de 1 t/dia da premissa só cabe se a fruta ficar 4 dias ou menos [CALCULADO].

### 6.3 Ponto de equilíbrio em função do custo X

Custo anual = parcela do investimento + custo de operação.

- Parcela anual = X × fator. Em 10 anos: a 2% ao ano (Pronaf, armazenagem [F8]) o fator é 0,02 ÷ (1 – 1,02⁻¹⁰) = **0,1113**; a 7,5% ao ano (Pronaf "demais investimentos" e faixa do FNE [F8][F25]) é 0,075 ÷ (1 – 1,075⁻¹⁰) = **0,1457** [CALCULADO]. Sem juros, X ÷ 10.
- Custo de operação por ano, duas hipóteses [SUPOSTO]: **R$ 12.000** (sem operador dedicado: manutenção, limpeza, internet, caixas; quem opera é alguém da associação que já está lá) ou **R$ 36.000** (com uma pessoa paga só para isso).

**Receita anual necessária para empatar** [CALCULADO]:

| Custo X | 2% a.a., operação R$ 12 mil | 2% a.a., operação R$ 36 mil | 7,5% a.a., operação R$ 12 mil | 7,5% a.a., operação R$ 36 mil |
|---|---|---|---|---|
| R$ 150.000 | R$ 28.699 | R$ 52.699 | R$ 33.853 | R$ 57.853 |
| R$ 300.000 | R$ 45.398 | R$ 69.398 | R$ 55.706 | R$ 79.706 |
| R$ 500.000 | R$ 67.663 | R$ 91.663 | R$ 84.843 | R$ 108.843 |
| R$ 800.000 | R$ 101.061 | R$ 125.061 | R$ 128.549 | R$ 152.549 |

**Maior custo X que cada cenário de receita paga** = (receita – operação) ÷ fator [CALCULADO]:

| Cenário (4 t) | 2% a.a., operação R$ 12 mil | 2% a.a., operação R$ 36 mil | 7,5% a.a., operação R$ 12 mil | 7,5% a.a., operação R$ 36 mil |
|---|---|---|---|---|
| Pessimista (R$ 4.800) | não paga nem a operação | não paga | não paga | não paga |
| Médio (R$ 29.160) | **R$ 154 mil** | não paga a operação | R$ 118 mil | não paga |
| Otimista (R$ 92.400) | **R$ 722 mil** | R$ 507 mil | R$ 552 mil | R$ 387 mil |

### 6.4 O que a conta diz

1. **Só com taxa de armazenagem, o negócio fecha apenas no cenário otimista** ou, no médio, se o equipamento custar menos de cerca de R$ 150 mil **e** não houver operador pago.
2. O projeto térmico cresceu para 12 kWp, 800 kg de gelo e dois compressores (doc 01). Não tenho o custo, mas é razoável esperar X bem acima de R$ 150 mil [SUPOSTO]. Se for assim, **a taxa de armazenagem sozinha não paga o equipamento** no cenário médio.
3. O valor que a câmara gera está em outro lugar: no ganho de quem vende melhor. No cenário médio passam 97 t/ano. Se o grupo ganha R$ 1,00/kg a mais por vender no canal melhor, são R$ 97.000 por ano de ganho para as famílias, contra R$ 29.160 de taxa [CALCULADO]. Então o modelo que faz sentido é **a câmara como patrimônio da associação ou cooperativa, paga com crédito subsidiado ou recurso a fundo perdido, e sustentada pela margem da venda**, não um serviço avulso de aluguel de espaço.
4. As três alavancas, em ordem de peso: **ocupação** (ter fruta e comprador o ano todo), **quem opera** (não ter folha de pagamento própria) e **custo X**.

---

## 7. Fontes de financiamento e apoio

Só o que achei com fonte. Condições mudam todo ano: confirmar no banco antes de contar com elas [VALIDAR].

| Fonte | O que financia | Condições encontradas | Fonte |
|---|---|---|---|
| **Pronaf Mais Alimentos** (safra 2026/2027, vigente de 01/07/2026 a 30/06/2027) | "Armazenagem" está na lista de itens com juro reduzido | **2% ao ano, até 10 anos, 3 de carência**; limite de R$ 250 mil por família (R$ 450 mil para fruticultura, entre outras atividades). Máquinas e equipamentos para família com renda abaixo de R$ 150 mil: 1,5% ao ano, até R$ 120 mil | [F8] (aberta) |
| **Pronaf Bioeconomia** | "Tecnologias de energia renovável" | 2% ao ano, 10 anos, até 5 de carência, até R$ 250 mil | [F8] |
| **Pronaf Agroindústria** | Implantação de agroindústria, **armazenagem**, energia renovável; pessoa física, empreendimento familiar e cooperativa | 7,5% ao ano, até 10 anos, 3 de carência; R$ 210 mil (pessoa física), R$ 450 mil (empreendimento familiar), até R$ 50 milhões (cooperativa singular) | [F8] |
| **Pronaf A (cooperativas da reforma agrária)** | Investimento para atender cooperados | 3% ao ano, 8 anos, até R$ 1 milhão | [F8] |
| **Pronaf Semiárido** (Adaptação Climática e Convivência com o Semiárido) | Infraestrutura produtiva | 2% ao ano, 10 anos, 3 a 5 de carência; R$ 45 mil a R$ 60 mil | [F8] |
| **BNB / FNE Sol** | Energia solar para agroindústria, produtor rural, cooperativa | Reportagem cita prazo de até 12 anos com 1 de carência (data da notícia incerta). Taxa atual para o agro: não encontrada | [F25] (busca) |
| **FNE (crédito rural, julho/2026 a junho/2027)** | Investimento rural | Linhas de sustentabilidade: 7,52% ao ano prefixado com bônus de adimplência; demais: 7,65% a 12,45% | [F25] (busca) |
| **BNDES Fundo Socioambiental** | Apoio não reembolsável a empreendimentos coletivos da agricultura familiar no Semiárido (edital em parceria); notícia de edital BNDES–ONU de R$ 1 bilhão para o sertão | Não confirmei edital aberto em 2026 nem se câmara fria é item apoiável | [F25] (busca) |
| **Sebrae (Sebraetec)** | Consultoria tecnológica subsidiada | Subsídio varia por estado (70% citado para 2023; 100% em um edital de Goiás para produtor rural). Financia serviço, não equipamento. Regra de PE em 2026: não encontrada | [F25] (busca) |
| **Sudene** | — | **Não achei** linha ou edital da Sudene para este tipo de equipamento | — |
| Compras públicas (PNAE, PAA) | Não financiam a câmara; garantem a venda | PNAE: R$ 40 mil por agricultor por ano por entidade; 45% mínimo para agricultura familiar [F19]. PAA: limite por família citado como R$ 15 mil, não confirmado (doc 09, seção 2.4) | [F19] |

**Leitura:** a linha que melhor casa é o Pronaf Mais Alimentos (armazenagem, 2% ao ano), mas o limite por família (R$ 250 mil a R$ 450 mil) pode ficar abaixo do custo do equipamento. Para valores maiores o caminho é a cooperativa (Pronaf Agroindústria, 7,5%) ou recurso não reembolsável.

---

## 8. Sinais de que a demanda NÃO existe ou é fraca

Procurei de propósito. O que achei:

1. **Estudo controlado na Índia (Rourkela, Odisha, 2025).** 300 feirantes em cinco mercados; metade recebeu acesso grátis à câmara solar, metade pagava uma pequena taxa diária. **Só 1% a 2% dos que pagavam usaram a câmara em um dia qualquer.** O benefício ficou com comerciantes grandes; o efeito sobre pequenos agricultores foi "pouco ou nenhum". Os próprios autores dizem não saber explicar bem a baixa adesão [F14]. É a evidência mais forte contra o modelo de pagar por dia.
2. **Vontade declarada não é uso pago.** Em Gana, mais de dois terços de 1.001 pequenos produtores disseram que adotariam câmara solar. Na Tanzânia, os obstáculos apontados foram custo alto, baixa capacidade de pagamento, pouco conhecimento e preferência do consumidor por produto não refrigerado [F15]. Não achei dado de taxa de ocupação real de nenhuma câmara de serviço.
3. **Os números de sucesso do ColdHubs são da própria empresa** e divergem entre fontes [F12].
4. **O pequeno produtor de manga vende na roça, no dia, pelo preço do comprador** (doc 09, seção 1.2). O problema dele é poder de venda, não falta de frio. Câmara sem comprador novo só adia a mesma venda.
5. **A manga não é fruta de pequeno em PE:** 17% do volume [F4]. E a escala não casa: um lote familiar produz 150 a 180 t por ano, o que a câmara gira no ano inteiro (doc 09, seção 1.4).
6. **A manga não atravessa a entressafra no frio** (seção 4.2). O argumento "guardar para vender caro" não vale.
7. **Caju de mesa é nicho.** Cerca de 88% a 90% do pedúnculo não é aproveitado [F6][F11]; a renda do produtor vem da castanha. Em PE o volume é mínimo e concentrado em um município. A safra de castanha caiu 32% de 2024 para 2025 (169.210 para 114.749 t [F1]): fornecimento instável.
8. **Onde há fruta em volume, já há frio.** O polo irrigado tem rede elétrica, packing houses e cooperativas com câmara (doc 09). O diferencial "fora da rede" vale pouco ali.
9. **Acerola e goiaba têm destino industrial forte.** Um documento da Embrapa (antigo) dá 46% da acerola para a indústria [F34]. Quem entrega para a indústria no mesmo dia não precisa de câmara.
10. **Não existe caso brasileiro funcionando para copiar** (seção 5.3). Quem for primeiro paga o aprendizado.
11. **Equipamento comunitário parado:** procurei notícias de câmara fria ou packing house de associação abandonados no Nordeste e não achei caso documentado. Achei uma menção, de fonte fraca, a três agroindústrias de castanha em PE que "nunca funcionaram por falta de castanha" (doc 09, seção 1.3). O risco de o equipamento virar depósito é real e a ausência de notícia não o afasta [VALIDAR em campo: perguntar às cooperativas que receberam câmara se ela está ligada].

### Onde a demanda é fraca e onde é forte

| Condição | Demanda |
|---|---|
| Produtor isolado, vende na roça, sem comprador novo | **Fraca** |
| Aluguel avulso por caixa por dia, operador próprio pago | **Fraca** |
| Manga verde para "esperar preço" | **Fraca** |
| Caju em Pernambuco, no polo da manga | **Inexistente** pelos dados |
| Local com rede elétrica boa e packing house por perto | Fraca para o solar; uma câmara comum resolve |
| **Grupo organizado, com contrato de merenda, PAA ou varejo, entregando 2 a 3 vezes por semana** | **Forte** |
| **Mistura de frutas de pequeno (goiaba, maracujá, acerola, manga madura) o ano todo** | **Forte** |
| **Local com rede fraca ou sem rede, longe de packing house** | **Forte** para o solar |
| **Polo de caju de mesa (CE, PI, RN) com comprador de fruta fresca** | Forte em tese; fora de PE |

---

## 9. Roteiro de validação em campo

Fazer **antes** de comprar equipamento. O doc 09 (seção 8) tem perguntas sobre local e logística; estas são sobre **dinheiro e uso**. Dá para aplicar as duas listas na mesma visita.

### 9.1 Para produtores (meta: 15 entrevistas, em pelo menos 3 núcleos)

1. Que frutas o senhor colhe, e quantas caixas por semana em cada mês do ano?
2. Para quem vendeu a última colheita? Por quanto? Quem pôs o preço?
3. Quantos dias passam entre colher e entregar?
4. De cada 10 caixas colhidas, quantas o senhor não consegue vender ou vende como refugo? Por quê?
5. Já deixou de colher por falta de comprador? Em que mês?
6. Se pudesse segurar a fruta 5 dias sem estragar, venderia para quem? Esse comprador já existe? Como se chama?
7. Já usou câmara fria de alguém? De quem, quanto pagou, por que parou?
8. Mostrar o preço: "R$ 1,20 por caixa de 20 kg por dia. O senhor usaria? Quantas caixas por semana? Em que meses?"
9. E se fosse o dobro? E a metade? (Achar o preço em que ele desiste.)
10. Prefere pagar por caixa, mensalidade fixa ou desconto na venda feita pela associação?
11. Levaria a fruta até a câmara antes das 10 h? Com que transporte? Até quantos quilômetros?
12. Participa de associação ou cooperativa? Tem CAF? Vende ou já vendeu para merenda ou PAA?
13. Tem caju? Quantos pés? O que faz com o pedúnculo hoje?
14. Daria R$ 100 de sinal agora para garantir vaga na primeira safra? (Pergunta de compromisso real, não de opinião.)

### 9.2 Para cooperativas e associações (meta: 3)

1. Quantos sócios ativos? Quantos têm CAF?
2. Quanto venderam para PNAE e PAA no último ano? Quanto deixaram de vender por não conseguir entregar regularmente?
3. Têm câmara fria ou já tiveram? Está funcionando? Se não, por quê?
4. Quem operaria a câmara? Essa pessoa já é paga hoje?
5. Assumiriam um financiamento do Pronaf para comprar? Até que valor de parcela anual?
6. Cederiam terreno e assinariam um termo de uso por um ano de teste?
7. Que frutas os sócios entregam em cada mês?
8. Qual a conta de luz e a qualidade da rede no galpão? (Para saber se o solar fora da rede é mesmo necessário.)

### 9.3 Para compradores (meta: 5 — nutricionista ou setor de merenda de 2 prefeituras, 1 supermercado ou sacolão, 1 atacadista de CEASA ou Mercado do Produtor, 1 indústria de polpa)

1. Que frutas compra, quantos quilos por semana, em que meses?
2. Quanto pagou por quilo na última compra de manga, goiaba, maracujá e acerola?
3. Compraria de um grupo de agricultores familiares com entrega refrigerada em dia fixo? Quanto por semana?
4. Paga mais por fruta resfriada e no ponto? Quanto?
5. Assinaria carta de intenção ou incluiria o grupo na próxima chamada pública? Quando sai a chamada?
6. Compra caju de mesa? De onde vem hoje? A que preço?
7. (Polpa) Quanto paga pelo quilo de manga, goiaba, acerola e caju para processar?

### 9.4 Número mínimo para seguir

Regra proposta [SUPOSTO; o dono pode mudar]:

| Grupo | Mínimo para seguir |
|---|---|
| Compradores | **Pelo menos 1 de 5 com compromisso por escrito** (carta de intenção ou chamada pública com data) que cubra no mínimo 50 t por ano |
| Cooperativas e associações | **Pelo menos 1 de 3** disposta a ceder terreno, indicar operador e assinar termo de uso |
| Produtores | **Pelo menos 8 de 15** dizendo que usariam ao preço mostrado **e pelo menos 5 dando o sinal** (pergunta 14) |
| Volume | A soma do que os interessados declaram tem de chegar a **1,5 t de estoque médio** (cerca de 40% da câmara) por pelo menos 8 meses do ano |

- Se os compradores falharem: **parar**. Sem comprador novo a câmara não tem função.
- Se só os produtores falharem: rever preço e modelo de cobrança (seção 5.2) e repetir.
- Se tudo passar: fazer o piloto de uma safra medindo ocupação diária, quilos que entram e saem, preço de venda e perda, para trocar cada [SUPOSTO] da seção 6 por número medido.

---

## 10. Dados de interface para o projeto térmico

### 10.1 Lista de frutas a considerar

| Fruta | Temperatura do ar | Umidade | Meses de uso | Embalagem | Prioridade |
|---|---|---|---|---|---|
| Manga madura ou "de vez", giro de até 5 dias | 10 °C | 85–90% | Ago a Mar (pico Out a Jan) | Caixa plástica de 20–25 kg | **1** |
| Goiaba | 8 a 10 °C | 85–90% | Ano todo | Caixa plástica | **1** |
| Maracujá | 7 a 10 °C | 85–90% | Ano todo | Caixa ou saco | 2 |
| Acerola | 8 a 10 °C | 90% | Ano todo | Caixa baixa (fruta amassa) | 2 |
| Mamão | 10 °C | 85–90% | Ano todo | Caixa | 3 |
| Manga verde-madura para guardar 2 a 3 semanas | **12 a 13 °C** | 85–90% | Out a Jan | Caixa | Só se o dono aceitar sair da faixa de 5 a 10 °C |
| Caju (pedúnculo) | **5 °C** | 85–90% | Set a Dez | Bandeja com filme, uma camada | **Condicional**: só se o campo confirmar oferta, ou em segundo local |

### 10.2 Recados para o engenheiro

- Umidade é a mesma para todas: 85% a 90%.
- **Caso mais frequente de uso, na visão deste documento: uma zona, 10 °C, frutas misturadas, entrada de 0,3 a 0,7 t/dia** (seção 6.2), e não 1 t/dia de caju a 5 °C.
- A entrada de 1 t/dia é o teto da premissa; o cenário otimista de demanda chega a 0,7 t/dia.
- Não achei dado de respiração para goiaba, acerola e maracujá. Goiaba e maracujá amadurecem depois de colhidos e respiram forte [SUPOSTO]; o engenheiro deve buscar os valores antes de fechar a carga.
- Fruta madura e fruta verde na mesma zona: prever renovação de ar por causa do etileno [SUPOSTO].
- Entressafra da câmara: abril a julho. O equipamento vai trabalhar com pouca carga nesses meses.

---

## 11. Acordo com a logística

Divisão combinada: o doc 09 é dono de local, municípios, distâncias, compradores por local, modelo de operação e horário. Este documento é dono de frutas, pós-colheita, compatibilidade, calendário de ocupação, perdas, quem paga, cobrança, receita e financiamento. Nos pontos de contato eu usei o doc 09, salvo onde tenho fonte melhor (li as tabelas do IBGE direto, o que o doc 09 não conseguiu).

### (a) Pontos em que concordo e adoto o doc 09

1. Manga e caju não coexistem num mesmo raio de coleta em Pernambuco (doc 09, resumo, item 1). **Confirmado** com dados municipais do IBGE de 2024 e 2025.
2. Quase toda a manga de PE está em sete municípios da beira do São Francisco (doc 09: 98%). Minha conta com 2025: 98%.
3. Escala: a câmara equivale a 1,4 a 1,7 lote familiar; o cliente é um grupo de 5 a 15 famílias que separa parte da fruta para vender melhor (doc 09, seção 1.4).
4. Calendário de safra de manga e caju (doc 09, seção 1.5). Adotei sem refazer.
5. O pequeno é "tomador de preço" e vende na roça (doc 09, seção 1.2).
6. Tetos de PNAE e a conta de R$ 400 mil por ano para 10 famílias (doc 09, seção 2.4).
7. Regra "fruta sem comprador marcado não entra" e permanência de 2 a 5 dias (doc 09, seção 6).
8. Começar só com manga no local recomendado; caju depois, se confirmado (doc 09, seção 6). Eu acrescento os complementos da seção 2.3.

### (b) Pontos em que tenho número ou conclusão diferente

| Assunto | Doc 09 | Este documento | Fonte de cada um | Tipo |
|---|---|---|---|---|
| Manga, total de PE em 2024 | 540.977 t | **560.977 t** | Doc 09: reportagem (FONTE 3). Aqui: SIDRA, tabela 1613 [F1], aberta | Correção de fonte |
| Manga, Lagoa Grande em 2024 | 10.000 t (400 ha) | **30.000 t**; em 2025, 66.500 t | Doc 09: boletim Embrapa (FONTE 1). Aqui: SIDRA [F3] | Correção de fonte |
| Manga, PE em 2025 | não tem | 609.940 t; Petrolina 286.250 t | SIDRA [F1][F3] | Atualização |
| Castanha de caju em PE | 3.126 t; Buíque o maior; tabela ilegível (FONTE 14, blog) | **3.099 t em 2024, 1.894 t em 2025; Buíque 2.521 t (81%) e 1.662 t (88%)**; Tupanatinga 165 e 56 t | SIDRA [F3] | Correção de fonte; a "maior lacuna" do doc 09 fica resolvida |
| Peso do Pajeú no caju | cerca de 9% do estado; 281 t de castanha; cerca de 2.800 t de pedúnculo | 2024: São José do Belmonte 151 + Carnaíba 50 + Flores 42 + Santa Terezinha 7 = 250 t (8%), 2.250 t de pedúnculo. **2025: 115 t (6%), 1.035 t de pedúnculo** | SIDRA [F3]; conversão 9:1 [F6] | Confirma a ordem de grandeza; 2025 é metade |
| Conversão castanha → pedúnculo | 10 kg por kg (pomar irrigado, FONTE 29) | 9 kg por kg (10% castanha, 90% pedúnculo) | [F6] | Diferença pequena |
| **Alternativa de local para o caju** | Sertão do Pajeú "empata se o caju for prioridade" | Pelos dados, **o caju de PE está em Buíque e Tupanatinga (Agreste), não no Pajeú**. Com 1.035 t de pedúnculo por ano em todo o Pajeú, espalhadas por vários municípios, uma câmara dificilmente junta 1 t/dia num raio de coleta | SIDRA [F3] | **Divergência de conclusão.** O local é do doc 09; registro a minha leitura e peço que o agente de logística reavalie o candidato de caju |
| Giro da câmara | 250 t por ano (1 t/dia × 250 dias) | 97 t (médio) a 231 t (otimista); teto físico de 0,8 t/dia com 4 t e 5 dias de permanência | Seção 6.2 | Divergência de hipótese: o doc 09 usa o teto de entrada; eu uso ocupação esperada |
| Fatia do pequeno na manga | "Petrolina não é só exportador grande"; 84,5% dos lotes são de pequenos | Em **volume**, a agricultura familiar fez 17% da manga de PE (Censo 2017) | [F4] | Não é contradição (um conta lotes, outro conta toneladas), mas muda o tom: o pequeno existe e é minoria na fruta |
| Horário de chegada | Manga das 10 h às 15 h; recepção das 7 h às 14 h | Não tenho dado próprio. Observo que o doc 01 pede fruta nova **até as 10 h** | doc 01, seção 13.1, item 10 | **Conflito entre doc 09 e doc 01**; vai para o dono (seção 12) |

### (c) Texto comum que proponho

- **Fruta principal:** "Manga para o mercado interno (madura ou 'de vez', giro de até 5 dias), acompanhada de goiaba, maracujá, acerola e mamão, todas na mesma câmara a 10 °C. Caju fica fora da primeira unidade, a menos que a visita de campo confirme pelo menos 0,3 t por dia de pedúnculo num raio de 15 km durante 3 meses."
- **Local:** "O indicado pelo doc 09 (núcleo de colonos no polo irrigado do São Francisco, em terreno de associação ou cooperativa), **condicionado** a existir um comprador com compromisso por escrito e a a associação indicar o operador. Se o dono priorizar o caju, o candidato a reavaliar é Buíque e Tupanatinga, não o Pajeú."
- **Calendário de uso:** "Ano todo. Uso alto de outubro a janeiro (manga), médio de fevereiro a março e de agosto a setembro, baixo de abril a julho (goiaba, maracujá e acerola para a merenda escolar)."
- **Horário de chegada:** "Fruta colhida de manhã cedo e entregue até as 10 h, se o campo confirmar que os colonos conseguem; se não conseguirem, o dono decide entre a regra do doc 01 e a janela do doc 09."
- **Tamanho do grupo atendido:** "5 a 15 famílias com CAF, em um raio de 10 a 15 km, girando 100 a 230 t por ano, com meta inicial de um contrato de merenda (cerca de 80 t por ano para 10 famílias em uma prefeitura)."

---

## 12. Conflitos registrados (o dono é o mediador; não resolvidos aqui)

| # | Assunto | Posição A | Posição B | O que cada escolha custa ou arrisca |
|---|---|---|---|---|
| 1 | **Duas zonas (caju a 5 °C e manga a 12 °C) ou uma zona a 10 °C** | **Doc 01:** duas zonas com divisória; equipamento dimensionado para a câmara inteira a 5 °C com 1 t/dia de caju: 79,5 kWh de frio por dia, 12 kWp, 800 kg de gelo, cerca de 4 t úteis | **Este documento:** no local recomendado não há caju em volume [F3]. Uma zona a 10 °C atende manga madura, goiaba, maracujá, mamão e acerola. Pelos números do próprio doc 01, só manga pede 66,6 a 69,8 kWh por dia, 12% a 16% menos que o caso do caju [CALCULADO: (79,5 – 69,8) ÷ 79,5 e (79,5 – 66,6) ÷ 79,5] | A: equipamento maior e mais caro, 1 t a menos de capacidade, mas pronto para o caju se ele aparecer ou se a unidade mudar de lugar. B: mais barato e mais simples, mas fecha a porta para o caju nesta unidade. Quanto se economiza é conta do engenheiro |
| 2 | **Temperatura da manga** | **Premissa:** câmara de 5 a 10 °C. **Doc 01:** 12 °C para manga verde-madura | **Este documento:** 10 °C serve para manga madura de giro rápido, que é o uso do mercado interno; 12 a 13 °C só é preciso para guardar manga verde por semanas [F7] | Se o grupo quiser estocar manga verde por 2 a 3 semanas, tem de aceitar 12 a 13 °C, e aí goiaba, maracujá e acerola ficam fora da faixa ideal |
| 3 | **Fruta escolhida pelo dono (manga e caju) x frutas que os dados indicam** | **Premissa:** manga e caju | **Este documento:** manga com goiaba, maracujá, acerola e mamão; caju em segunda etapa ou segundo local | Manter o caju obriga a mudar de local (Agreste, ou outro estado) ou a fazer duas unidades |
| 4 | **Capacidade e entrada** | **Premissa:** 5 t e 1 t/dia | **Doc 01:** cerca de 4 t com duas zonas. **Este documento:** a demanda esperada é de 0,13 a 0,70 t/dia; 1 t/dia é teto, não rotina | Dimensionar para 1 t/dia de caju encarece um equipamento que, pela demanda estimada, trabalhará quase sempre abaixo disso |
| 5 | **Horário de chegada** | **Doc 01:** fruta nova até as 10 h | **Doc 09:** manga chega das 10 h às 15 h; recepção até as 14 h | Regra do doc 01 reduz o gelo necessário (400 kg em vez de 700 a 800, segundo o próprio doc 01) mas pode não caber na rotina do colono |
| 6 | **Modelo de negócio** | **Premissa:** câmara "como serviço" para pequenos produtores | **Este documento:** aluguel avulso por caixa não se paga no cenário médio; o modelo viável é a câmara como bem de uma associação ou cooperativa, com crédito subsidiado, sustentada pela margem da venda | Serviço avulso: o dono fica com o risco de ocupação. Venda para cooperativa: o dono vira fabricante e precisa de cliente com crédito |

---

## 13. Fechamento

### Decisões tomadas neste documento

1. Usar os dados do IBGE (SIDRA) de 2025 como base de produção, com 2024 para comparar com o doc 09.
2. Classificar as frutas em três grupos de temperatura (5 °C; 8 a 10 °C; 12 a 14 °C).
3. Tratar manga + caju no mesmo ponto como **não sustentável em Pernambuco** e propor goiaba, maracujá, acerola e mamão como complemento da manga.
4. Tratar "guardar para esperar preço" como argumento inválido para a manga.
5. Fazer a viabilidade só pela receita, com ponto de equilíbrio em função do custo X.
6. Propor regra de seguir ou parar baseada em compromisso de comprador.

### Pendências para humanos (decisões do dono)

1. **Manter o caju?** Se sim: mudar o local para o Agreste (Buíque), para outro estado, ou fazer duas unidades. Se não: uma zona a 10 °C (conflitos 1 e 3).
2. **Aceitar goiaba, maracujá, acerola e mamão** como frutas do projeto, além da manga?
3. **Quem é o cliente:** serviço avulso operado pelo dono, ou equipamento da associação ou cooperativa (conflito 6)?
4. **Fazer as entrevistas da seção 9 antes de comprar equipamento?** Recomendo que sim.
5. **Aceita a regra de parada** (sem comprador com compromisso por escrito, não segue)?
6. Horário de chegada (conflito 5) e temperatura da manga (conflito 2).
7. O projeto precisa mesmo ser fora da rede no local escolhido? No polo irrigado há rede; perguntar à associação.

### O que não consegui verificar

- Preços: manga na CEASA do Recife em R$/kg; caju de mesa no atacado; pedúnculo pago pela indústria; preço de polpa pago ao produtor; aluguel mensal de contêiner frigorífico; preço de compra pública de fruta em Pernambuco (usei o do Rio Grande do Norte).
- Tabela de preços atual do ColdHubs e do Ecozen (os sites não abriram); avaliação independente dos resultados deles.
- Ocupação real de qualquer câmara de serviço, em qualquer país.
- Perdas pós-colheita recentes, por fruta, no Nordeste.
- Calendário de safra oficial por mês; todos os "ano todo" da seção 1.4 são [SUPOSTO].
- Temperatura de armazenagem de coco verde, graviola e melancia; respiração de goiaba, acerola e maracujá.
- Fatia da agricultura familiar em melão, abacaxi e melancia.
- Se as câmaras frias de cooperativas do Vale estão funcionando.
- Linha da Sudene; edital não reembolsável aberto em 2026; regra do Sebraetec em PE; taxa do FNE Sol para o agro.
- Distância Buíque–Petrolina e existência de goiaba ou maracujá perto de Buíque.
- A fatia familiar é de 2017; apliquei a volumes de 2025.

### Dados de interface

- Para o engenheiro de refrigeração: seção 10.
- Para a logística: seção 11.
- Para o revisor: todas as hipóteses [SUPOSTO] que mais pesam estão nas seções 6.1 (ocupação, taxa, dias), 4.3 (fatia de mercado) e 1.4 (calendário).
- Para a importação e o custo: a receita que o equipamento precisa pagar está na seção 6.3.

---

## Fontes

**(aberta)** = abri e li o dado. **(busca)** = vi só o trecho devolvido pela busca.

- **[F1]** IBGE, SIDRA, tabela 1613 — Produção Agrícola Municipal, lavouras permanentes, por estado, 2024 e 2025 (aberta): https://apisidra.ibge.gov.br/values/t/1613/n1/all/n2/2/n3/all/v/214/p/2025/c82/all (trocar `2025` por `2024` para o ano anterior)
- **[F2]** IBGE, SIDRA, tabela 1612 — lavouras temporárias (melão, abacaxi, melancia), 2024 e 2025 (aberta): https://apisidra.ibge.gov.br/values/t/1612/n1/all/n2/2/n3/all/v/214/p/2025/c81/all
- **[F3]** IBGE, SIDRA, tabelas 1613 e 1612 por município de Pernambuco, 2024 e 2025 (aberta): https://apisidra.ibge.gov.br/values/t/1613/n6/in%20n3%2026/v/214/p/2025/c82/all e https://apisidra.ibge.gov.br/values/t/1612/n6/in%20n3%2026/v/214/p/2024/c81/all
- **[F4]** IBGE, SIDRA, tabela 6955 — Censo Agropecuário 2017, lavoura permanente por tipologia (agricultura familiar), Nordeste e Pernambuco (aberta): https://apisidra.ibge.gov.br/values/t/6955/n2/2/n3/26/v/9504,9506/p/2017/c227/all/c829/all
- **[F5]** IBGE, SIDRA, tabela 289 — Produção da Extração Vegetal, 2025 (umbu) (aberta): https://apisidra.ibge.gov.br/values/t/289/n1/all/n2/2/n3/in%20n2%202/v/144/p/last%201/c193/all
- **[F6]** Embrapa Agroindústria Tropical / Sebrae-CE, Documentos 38, junho de 2000, sobre processamento do caju (aberta): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/422033/1/Dc038.pdf
- **[F7]** Embrapa, Documentos 27, 1997, perdas pós-colheita em frutos e hortaliças; tabelas 3, 4 e 5 (aberta): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/415584/1/1997DOC0027.pdf
- **[F8]** MDA, "Resumo das linhas de crédito rural do Pronaf — Safra 2026/2027" (aberta): https://www.gov.br/mda/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/plano-safra-da-agricultura-familiar/documentos/Pronaf20262027ResumoLinhas.pdf
- **[F9]** Conab/Prohort, Resumo Executivo Semanal nº 40, 19/10/2026 (aberta; o trecho da manga veio ilegível na extração e não foi usado): https://www.gov.br/conab/pt-br/atuacao/informacoes-agropecuarias/hortigranjeiros-prohort/resumo-executivo-semanal/resumo-executivo-2026-1/resumo-executivo-prohort-40-26.pdf
- **[F11]** Diário do Nordeste, desperdício de pedúnculo no Ceará (busca): https://diariodonordeste.verdesmares.com.br/negocios/ceara-desperdica-mais-de-800-toneladas-de-caju-e-deixa-de-faturar-milhoes-todos-os-anos-1.3742190
- **[F12]** ColdHubs (busca): https://www.ifpri.org/blog/coldhubs-addressing-crucial-problem-food-loss-nigeria-solar-powered-refrigeration ; https://www.howwemadeitinafrica.com/pay-as-you-go-cold-rooms-businessman-wants-to-expand-beyond-nigeria/145059/ ; https://coldhubs.com/coldhub ; https://techxlab.org/solutions/cold-rooms-by-coldhubs/ ; https://p4gpartnerships.org/partnership/coldhubs ; https://energy-base.org/l/news/coldhubs-revolutionising-nigerias-agriculture-with-cooling-solutions/
- **[F13]** Ecozen e Oorja (busca): https://thebetterindia.com/258160/iit-kharagpur-startup-portable-solar-powered-ai-cold-storage-farm-produce-fresh ; https://ashden.org/awards/winners/ecozen-solutions/ ; https://www.pv-magazine-india.com/2021/06/07/solar-powered-cold-storage-as-a-service
- **[F14]** Universidade de Wisconsin, estudo com feirantes em Rourkela, Índia, 21/11/2025 (busca): https://aae.wisc.edu/2025/11/21/is-cold-storage-a-viable-climate-adaptation-strategy-for-produce-vendors-in-india/ ; registro do experimento: https://www.socialscienceregistry.org/trials/12900
- **[F15]** Estudos sobre adoção de câmara solar em Gana e na Tanzânia (busca; não confirmei qual link corresponde a qual país): https://www.frontiersin.org/articles/10.3389/fsufs.2025.1525148/full ; https://www.frontiersin.org/articles/10.3389/fsufs.2022.990528
- **[F16]** Ayuda en Acción, avaliação pós-colheita em Uganda (busca): https://ayudaenaccion.org/uploads/2024/05/AeA-Uganda-Post-Harvest-Assessment-Report-small.pdf
- **[F17]** Preços da manga (busca): Cepea — https://cepea.org.br/br/manga-cepea/manga-cepea-com-oferta-limitada-tommy-atinge-maior-cotacao-do-ano.aspx ; https://cepea.org.br/br/manga-cepea/manga-cepea-preco-da-tommy-cai-no-vale-palmer-sobe.aspx ; https://cepea.org.br/br/manga-cepea/manga-cepea-baixa-oferta-impulsiona-preco-no-vale.aspx ; Agrolink — https://www.agrolink.com.br/noticias/com-maior-oferta--precos-da-manga-recuam-no-vale-no-comeco-deste-mes_510749.html ; https://www.agrolink.com.br/cotacoes/pe ; Boca — https://boca.com.br/agronegocio/manga-palmer-e-tommy-tem-precos-em-alta-no-nordeste
- **[F18]** Pesquisa de preços da Emater-RN para compras da agricultura familiar, publicada no DOE-RN em 08/05/2026 (busca): https://www.legisweb.com.br/legislacao/?id=495541
- **[F19]** PNAE, Resolução CD/FNDE nº 04/2026 e Lei nº 15.226/2025 (busca): https://www.canalrural.com.br/politica/resolucao-do-pnae-redefine-compras-da-agricultura-familiar/ ; https://ifrs.edu.br/wp-content/uploads/2026/03/Quadro-comparativo-alteracoes-Resolucao-FNDE-no-04-2026.pdf
- **[F20]** Pós-colheita, estudos brasileiros (busca): maracujá — https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1140518/1/Madalena-Shelf-life-of-BRS-perola-do-cerrado.pdf ; goiaba — https://apct.sede.embrapa.br/pab/article/download/5140/2332/19268 ; acerola — https://ppgcta.ufc.br/wp-content/uploads/2018/08/sandralopes.pdf e https://www.redalyc.org/pdf/1190/119017431011.pdf e https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1102405/1/Vagner.pdf ; umbu — https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/574197/1/OPB2523.pdf e https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1080419/1/Padrao-respiratorio-refrigeracao-e-atmosfera-modificada.pdf ; melão — https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/427484/1/SP-4473.pdf ; banana — https://locus.ufv.br/bitstreams/4d4fb1bf-9807-4d11-be78-419328ef576b/download . Não confirmei qual link corresponde a cada dado dentro de cada fruta.
- **[F21]** Guia de armazenagem CPMA 2022, com dados da UC Davis (busca): https://cpma.ca/docs/default-source/education/2022/cpma_2022_storage-guide.pdf
- **[F22]** Perdas (busca): CEASA de Salvador — https://ojs.uel.br/revistas/uel/index.php/semagrarias/article/download/50314/50858/278734 ; revisão — https://www.scielo.br/j/hb/a/KRW5wC3LmKzPZZnXt8fPbRL/?lang=en ; mamão e embalagem — https://www.revistacultivar.com.br/noticias/tecnologia-reduz-perdas-na-pos-colheita-de-frutas
- **[F23]** Máquinas de gelo solares, Instituto Mamirauá (busca): https://canalsolar.com.br/maquina-de-gelo-movida-a-solar-beneficia-comunidades-da-amazonia/ ; https://revistapesquisa.fapesp.br/maquina-produz-gelo-na-amazonia/
- **[F24]** Cooperativas com câmara fria e energia solar (busca): https://jornaldaparaiba.com.br/_/162019 ; https://mundocoop.com.br/economia-negocios/cooperativa-de-maringa-adere-a-geracao-solar-e-reduz-em-70-a-conta-de-energia
- **[F25]** Crédito e apoio (busca): FNE — https://www.correiodamanha.com.br/economia/2026/07/302403-projetos-rurais-sustentaveis-terao-juros-mais-baixos.html ; FNE Sol — https://canalsolar.com.br/bnb-financiamento-energia-solar/ e https://www.pv-tech.org/northeast-brazilian-bank-creates-credit-line-for-micro-and-mini-renewable-p ; BNDES — https://www.bndes.gov.br/fundosocioambiental e https://monitormercantil.com.br/bndes-e-onu-lancam-edital-de-r-1-bi-para-sertao-nordestino/ ; Sebraetec — https://monitormercantil.com.br/sebraetec-quase-23-mil-negocios-foram-beneficiados-em-2023/ e https://sistemafaeg.com.br/storage/arquivos/EDITAL-DE-SELE%C3%87%C3%83O.pdf-manifesto.pdf
- **[F26]** Anúncios de contêiner frigorífico usado (busca): https://www.mfrural.com.br/busca/container-frigorifico-20-pes
- **[F27]** Polos baianos de manga (busca): https://movimentoeconomico.com.br/agronegocio/2024/09/30/frutas-bahia/
- **[F29]** Ceagesp, ficha de medidas de frutas (caixa de caju de 1,2 kg) (busca): https://ceagesp.gov.br/wp-content/uploads/2015/06/medidaFrutas.pdf
- **[F32]** Temporada de exportação de frutas pelo Pecém (busca): https://movimentoeconomico.com.br/agronegocio/2025/09/22/ce-enviara-200-conteineres-semanais-de-frutas-para-europa-ate-2026/
- **[F34]** Embrapa, destino da acerola (busca; documento antigo, não confirmei qual dos dois traz o dado): https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/132160/1/1995-A-cultura-da-acerola.pdf ; https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/114145/1/Aculturadaacerola.pdf
- Documentos internos: `docs/09-logistica-e-local.md` e `docs/01-projeto-termico.md` (rascunhos lidos em 17/11/2026).
