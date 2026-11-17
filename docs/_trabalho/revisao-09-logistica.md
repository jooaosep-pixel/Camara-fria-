# Parecer de revisão — `docs/09-logistica-e-local.md`

Revisor técnico independente. Data: 17/11/2026.
Lidos: `docs/00-premissas.md`, `.claude/agents/agente-logistica.md`, `docs/09-logistica-e-local.md` (inteiro, 553 linhas) e, para cruzamento, `docs/01-projeto-termico.md` (por busca de termos, não na íntegra).

## Limite desta revisão

Durante quase todo o trabalho eu, como o autor, **não consegui abrir páginas**: só a busca funcionou (SIDRA, `www.embrapa.br`, `www.cnpmf.embrapa.br` e `www.chicosabetudo.com.br` foram recusados). No fim, o dono liberou alguns sites e **o SIDRA/IBGE abriu**. Com isso:

- **Baixei a PAM 2024 (tabela 5457) para todos os municípios de Pernambuco, manga e castanha de caju.** Os números estão na seção "Dados do IBGE obtidos pelo revisor", com o endereço da consulta. Eles mudam vários achados e passam a ser a base deste parecer.
- As demais fontes do documento continuam **não conferidas na íntegra**: o que confirmei fora do IBGE foi por trecho de busca. Não tentei abrir os outros sites liberados (Embrapa, Codevasf, INMET, CRESESB); fica para o autor.
- Onde uso número meu sem fonte, está escrito "estimativa do revisor".

## Dados do IBGE obtidos pelo revisor (PAM 2024, tabela 5457)

Consulta (abre em navegador ou com `curl`):
`https://apisidra.ibge.gov.br/values/t/5457/n6/in%20n3%2026/v/214,216/p/2024/c782/40143,40262?formato=json`
(variável 214 = quantidade produzida; 216 = área colhida; produto 40143 = castanha de caju; 40262 = manga). Totais do estado e do Brasil: mesma tabela com `n3/26/n1/all`.

**Totais.** Manga, Pernambuco: 511.148 t (2022), 601.475 t (2023), **560.977 t em 20.246 ha (2024)**; Brasil 2024: 1.861.362 t; 560.977 ÷ 1.861.362 = 30,1%. Castanha de caju, Pernambuco: 2.806 t (2022), 2.821 t (2023), **3.099 t em 2.220 ha (2024)**; Brasil 2024: 169.210 t. O produto "caju" (pedúnculo) não tem dado na tabela.

**Manga 2024 — os maiores (56 municípios têm manga):**

| Município | Produção (t) | Área colhida (ha) | Castanha de caju (t) |
|---|---|---|---|
| Petrolina | 282.000 | 9.400 | 0 |
| Belém do São Francisco | 179.200 | 6.400 | 0 |
| Santa Maria da Boa Vista | 42.500 | 1.700 | 0 |
| Lagoa Grande | **30.000** | **1.200** | 0 |
| Orocó | 8.750 | 350 | 0 |
| Petrolândia | 4.375 | 125 | 0 |
| Cabrobó | 4.000 | 200 | 0 |
| Lagoa dos Gatos | 2.250 | 150 | 0 |
| Belo Jardim | 1.250 | 50 | 0 |
| Bonito | 1.250 | 250 | 0 |
| Chã Grande | 1.000 | 50 | 0 |
| São José do Belmonte | 400 | 20 | 151 |
| Salgueiro | 390 | 30 | 0 |
| Ipubi | 360 | 30 | 0 |
| Serra Talhada | 200 | 10 | 0 |
| Mirandiba | 90 | 10 | 0 |

Sete municípios do São Francisco: 550.825 t = 98,2% do estado. Resto do estado: 10.152 t.

**Castanha de caju 2024 — todos os municípios com produção (19):**

| Município | Região | Castanha (t) | Área (ha) | Manga (t) |
|---|---|---|---|---|
| Buíque | Agreste | **2.521** | 1.385 | 0 |
| Tupanatinga | Agreste (vizinho de Buíque) | 165 | 110 | 0 |
| São José do Belmonte | Sertão Central | 151 | 251 | 400 |
| Taquaritinga do Norte | Agreste | 120 | 200 | 10 |
| Carnaíba | Pajeú | 50 | 100 | 41 |
| Flores | Pajeú | 42 | 70 | 0 |
| Tacaratu | Sertão de Itaparica | 12 | 25 | 150 |
| Santa Terezinha | Pajeú | 7 | 16 | 28 |
| Floresta | Sertão de Itaparica | 5 | 8 | 0 |
| Afogados da Ingazeira, Solidão, Brejinho, Iguaracy, Tabira, Itapetim | Pajeú | 4, 4, 3, 3, 3, 2 | 5 a 8 cada | 20 a 56 cada |
| Jatobá | Sertão de Itaparica | 4 | 8 | 32 |
| Brejo da Madre de Deus, Caruaru, Riacho das Almas | Agreste | 1 cada | 1 a 5 | 0 a 25 |

Leituras diretas [CALCULADO pelo revisor sobre o IBGE]:
- Buíque sozinho: 2.521 ÷ 3.099 = **81%** da castanha do estado; com Tupanatinga, 87%. O rendimento de Buíque (2.521 t ÷ 1.385 ha = 1,8 t/ha) é alto para sequeiro e merece confirmação com o IBGE local ou o IPA.
- Pajeú inteiro (nove municípios): 118 t = **3,8%** do estado, não 9%.
- Nenhum município da beira do São Francisco com manga em volume tem castanha de caju registrada. Mirandiba: zero.
- Único município com as duas culturas acima de 100 t: **São José do Belmonte** (151 t de castanha e 400 t de manga).

## O que conferi e bateu

| Item | Resultado |
|---|---|
| Somas da tabela de pontuação (5 colunas, pesos originais) | Refeitas: A 83,6; B 65,4; C 66,0; D 58,4; E 62,4. Todas corretas. Pesos somam 100 |
| Somas do teste "caju é prioridade" | Refeitas: 71,6; 56,4; 71,0; 65,4; 63,4. Corretas. Pesos somam 100 |
| Soma dos sete municípios e percentual do estado | A aritmética fecha, mas sobre dois números errados (achado 26) |
| Petrolina, 282.000 t em 9.400 ha (2024) | **Confirmado no IBGE** |
| Belém do São Francisco, 179.200 t (2024) | **Confirmado no IBGE**, com 6.400 ha (28 t/ha) |
| Santa Maria da Boa Vista, Orocó, Petrolândia, Cabrobó | **Confirmados no IBGE** |
| Buíque como maior produtor de castanha do estado | **Confirmado no IBGE** (2.521 t) |
| Rendimento de 25 t/ha para pequenos do Nilo Coelho | Um estudo com 75 produtores do distrito (2014–2018) dá média de 25 t/ha (https://periodicos.ufv.br/rea/article/download/7678/3161/32743, trecho de busca) |
| Lote de colono com cerca de 6 ha irrigáveis | Estudo antigo da Embrapa dá 6,11 ha irrigáveis em média (https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/489198/1/Desempenhodistrito.pdf, trecho de busca) |
| Mercado do Produtor de Juazeiro, 1.620.627 t, 2º do país | Confirmado em tabela da Conab/Prohort 2025 (https://www.gov.br/conab/pt-br/atuacao/informacoes-agropecuarias/hortigranjeiros-prohort/centrais-de-abastecimento-comercializacao-de-frutas-e-hortalicas-2025.pdf) |
| PNAE, R$ 40.000 por CAF, por ano, por entidade | Confirmado. Há alteração posterior (achado 21) |
| Distâncias rodoviárias marcadas [SUPOSTO] | Ordem de grandeza plausível; não conferi em mapa |

## Tabela de achados

| Nº | Seção | Gravidade | O que está errado | Minha conta ou fonte | O que o autor deve fazer |
|---|---|---|---|---|---|
| 1 | 1.3; 4.1; 4.2; 4.3; Resumo itens 1 e 5; 9 | **BLOQUEANTE** | Toda a parte do caju foi escrita sem a tabela do IBGE, e o IBGE **contradiz a alternativa recomendada**. O documento aponta o Pajeú (Carnaíba–Flores–Serra Talhada) como o lugar do caju e trata Buíque como "fonte fraca". Pelo IBGE, o caju de Pernambuco está em Buíque e arredores; o Pajeú é marginal e Serra Talhada e Mirandiba não têm castanha registrada. As notas dos candidatos C, D e E, a "alternativa 1" da seção 4.3, a pendência 1 ("com caju, Pajeú") e a sensibilidade de clima da seção 7 (Serra Talhada) estão apoiadas no lugar errado | PAM 2024: Buíque 2.521 t (81% do estado); Tupanatinga 165 t; São José do Belmonte 151 t; Carnaíba 50 t; Flores 42 t; Pajeú inteiro 118 t (3,8%). Ver seção de dados acima | Refazer 1.3 com a tabela do IBGE; refazer os candidatos de caju (Buíque/Tupanatinga passa a ser o candidato principal de caju; São José do Belmonte o único com as duas frutas); refazer notas, alternativas e pendências. Levantar clima, estrada, associações e compradores de Buíque, que hoje o documento não tem |
| 1b | Resumo item 1; 4.3 | **IMPORTANTE** | "As duas frutas não se encontram no mesmo raio de coleta" foi escrita como conclusão sem dado. Com o IBGE ela passa a estar **sustentada para volume comercial**, com uma exceção que o documento não viu | Zero castanha nos sete municípios da manga irrigada; zero manga em Buíque e Tupanatinga. Exceção: São José do Belmonte, 151 t de castanha e 400 t de manga (20 ha). Estimativa do revisor para Belmonte: 151 t × 10 = cerca de 1.500 t de pedúnculo bruto por safra, mais 400 t de manga | Reescrever a frase com os números e citar Belmonte. Ressalva que deve constar: a PAM não capta bem fruta de quintal e de sequeiro miúdo, então a coexistência em pequena escala (Araripe, Pajeú) continua sendo pergunta de campo |
| 26 | 1.1 | **IMPORTANTE** | Dois números da tabela de manga estão errados e a soma herdou o erro. (a) Lagoa Grande: o documento traz 400 ha e 10.000 t. (b) Total de Pernambuco: o documento traz 540.977 t e 29,42% do Brasil. (c) Total de castanha do estado: 3.126 t | IBGE, PAM 2024: Lagoa Grande **1.200 ha e 30.000 t**; Pernambuco **560.977 t**, 30,1% do Brasil; castanha 3.099 t. Soma correta dos sete: 550.825 t = 98,2%; resto do estado 10.152 t (o documento dizia "da ordem de 10 mil t", o que continua certo por coincidência) | Corrigir a tabela, a soma e o percentual, citando o SIDRA em vez dos blogs |
| 27 | 1.3 (Pajeú) | **IMPORTANTE** | "Pajeú com cerca de 9% da produção estadual" e a conta "281 t de castanha → 2.800 t de pedúnculo → 23 t/dia" estão acima do dado atual | IBGE 2024: 118 t no Pajeú inteiro (3,8%). 118 × 10 = 1.180 t de pedúnculo ÷ 120 dias = **9,8 t/dia bruto** em nove municípios; Carnaíba + Flores: 92 t → 920 t → 7,7 t/dia bruto. Com aproveitamento de mesa de 10% a 30% [SUPOSTO do revisor]: 0,8 a 2,3 t/dia no eixo Carnaíba–Flores inteiro, antes de aplicar raio de coleta | Refazer a conta com o IBGE; ver também achado 4 |
| 2 | 1.4 e Resumo item 3 | **IMPORTANTE** | A "conta de escala" marcada [CALCULADO] tem três suposições embutidas: (a) lote inteiro plantado com manga; (b) rendimento do município (dominado por empresas) aplicado ao colono; (c) 250 dias de operação. O resultado "a câmara equivale a cerca de dois lotes" está exagerado e contradiz dados do próprio documento (manga é cerca de 40% do cultivo permanente, FONTE 6; 75% dos estabelecimentos com manga têm até 5 ha de manga, FONTE 5) | Com 40% do lote em manga: 6,4 ha × 0,40 = 2,56 ha; × 25 t/ha = 64 t/ano por lote. 250 t ÷ 64 t = **3,9 lotes**; faixa de 3,5 a 4,2 lotes com 6 ha e 25–30 t/ha. Com 365 dias: 5,7 lotes. O rendimento de 25 t/ha para pequenos tem apoio (estudo com 75 produtores); a área de manga por lote não tem | Remarcar como [CALCULADO sobre SUPOSTO], mostrar a faixa (2 a 6 lotes) e corrigir o resumo. A conclusão qualitativa (a câmara atende um grupo pequeno, não uma comunidade) continua de pé e fica coerente com "5 a 15 famílias"; "dois lotes" não fica |
| 3 | 1.4, 6 | **IMPORTANTE** | A conta trata a produção como espalhada em 250 dias. A manga irrigada é colhida por talhão, em poucas semanas, depois da indução floral. O que limita a câmara é o **pico diário**, não o total anual; isso não aparece na conta e é o que define a regra de cota | Estimativa do revisor: 64 t de um lote colhidas em 3 semanas = cerca de 3 t/dia, três vezes a entrada da câmara. Não achei fonte para a duração da colheita do pequeno produtor | Acrescentar a conta de pico (t/dia na colheita de um lote), marcada [SUPOSTO], e incluir a pergunta de campo "em quantos dias o senhor colhe um talhão?". A pergunta 3 da seção 8 já cobre em parte; ligar as duas coisas |
| 4 | 1.3 (pedúnculo) e 1.4 (última frase) | **IMPORTANTE** | (a) "23 t/dia em todo o Pajeú" é pedúnculo **total**, não fruta de mesa. Caju de mesa é colhido à mão, na árvore; a maior parte do pedúnculo cai e não serve para câmara fria. Falta um fator de aproveitamento. (b) A frase "uma associação de 80 famílias com 25 cajueiros cada é um fornecedor do tamanho da câmara" não tem marcação e mistura duas notícias (25 mudas por agricultor é a distribuição da prefeitura; 80 sócios é uma associação) | Estimativa do revisor: 80 × 25 = 2.000 plantas; a cerca de 200 plantas/ha = 10 ha; sequeiro a cerca de 1 t de castanha/ha = 10 t de castanha = cerca de 100 t de pedúnculo; em 120 dias = **0,8 t/dia bruto**, se todas as mudas de 2019 estiverem vivas e produzindo e se 100% do pedúnculo for colhido. Com aproveitamento de mesa de 10% a 30% [SUPOSTO do revisor], 0,1 a 0,25 t/dia. Não é "do tamanho da câmara" | Marcar a frase como [SUPOSTO], aplicar fator de aproveitamento de mesa (com fonte da Embrapa Agroindústria Tropical) às três contas de pedúnculo e refazer a faixa "2 a 5 t/dia num raio de 30 km" |
| 5 | 1.5 e 7 (meses de uso — caju) | **IMPORTANTE** | Os meses de safra do caju vão para a tabela de interface como "[FONTE 33]", mas a FONTE 33 é um site de auditório (`auditorioibirapuera.com.br`) e um artigo de jornal sobre a "chuva do caju", com link declarado incerto e não específico de Pernambuco. O próprio rodapé das fontes manda tratar 29, 31, 33 e 58 como [SUPOSTO], mas as tabelas 1.5 e 7 as exibem como [FONTE] | Minha busca não achou calendário de caju específico do sertão pernambucano (nem IPA, nem Embrapa). Não confirmado | Trocar a marcação para [SUPOSTO] nas tabelas 1.5 e 7 (caju, manga de sequeiro, "manga o ano todo" da FONTE 31) e buscar o calendário no Sistema de Produção do Caju da Embrapa ou no IPA |
| 6 | 1.1, candidato B | MENOR | Belém do São Francisco entra apoiado em dois blogs e sem a área | IBGE confirma 179.200 t em 6.400 ha (28 t/ha) em 2024 | Trocar a fonte pelo SIDRA e completar a área. Continua faltando dizer se a manga de Belém é de empresa ou de pequeno: sem isso as notas 3 em "organização" e 4 em "raio de coleta" do candidato B são chute |
| 7 | 4.2 (pontuação) | **IMPORTANTE** | As somas estão certas, mas a tabela tem defeitos de construção: (a) o critério 4 junta duas perguntas diferentes ("duas frutas" e "encaixe de escala") numa nota só; (b) o critério 3 dá nota 5 a Petrolina por volume, quando o próprio documento mostra que volume acima de 1 t/dia não acrescenta nada à câmara e é justamente o problema de escala; (c) os critérios 1, 2, 3, 8 e 11 (58 pontos) medem todos "estar num polo desenvolvido" e favorecem A em bloco; (d) segurança (5) e Starlink (2) têm a mesma nota para todos: 7 pontos que não discriminam; (e) "já existir frio disponível", "ninguém aceitar operar" e "comprador não pagar mais" aparecem em 4.3 como fatores que **derrubam** a recomendação, mas na tabela valem só 10 pontos cada ou nem entram. Critério que derruba não é critério aditivo | Refiz com outros pesos, mantendo as notas do autor. Pesos iguais nos 11 critérios: A 81,8; B 69,1; C 69,1; E 63,6; D 61,8. Pesos voltados à necessidade (critérios 4 e 6 com 20 cada; 1, 2, 3 e 5 com 10; 11 com 3): **C 72,0; A 71,6**; D e E 66,4; B 62,4. Reescalando só o critério 4 e os demais em proporção, C só passa A com o critério 4 acima de 37,5% do peso total. Baixando um ponto nas notas de A nos critérios 4, 5 e 6: A cai para 77,6 e continua em primeiro | Separar o critério 4 em dois; tratar frio existente, operador e comprador como **eliminatórios** (sim/não, respondidos em campo), fora da soma; dizer no texto que, com as notas dadas, Petrolina vence com quase qualquer peso e só perde se "necessidade/duas frutas" pesar mais de um terço — e que o "empate" do teste foi obtido tirando peso justamente dos três critérios em que A tem nota 5 |
| 8 | 4.2 (notas), 3 (critérios 6 e 7) | **IMPORTANTE** | Notas dadas sem dado nenhum, embora a definição da tarefa peça o levantamento: concorrência de câmaras existentes (não pesquisada; a nota 5 de C, D e E vem de "provável ausência [SUPOSTO]"); irradiação solar (não obtida; mesmo assim A e B levam 5 e E leva 3); segurança (3 para todos) | O documento reconhece as três lacunas em "O que não consegui verificar" | Deixar explícito na tabela quais notas não têm dado (por exemplo com asterisco) e recalcular o total só com as notas apoiadas em fonte, para o dono ver quanto do resultado é dado e quanto é opinião |
| 9 | 7 (temperatura de projeto) e 9 (decisão 3) | **IMPORTANTE** | "40 °C mantida. Fica acima do recorde encontrado" está errado. O recorde usado é de **um mês** (novembro de 2015, site secundário, convertido de Fahrenheit). Há registro oficial maior | A Apac registrou **41,0 °C em Petrolina** em 2021, a maior temperatura do ano em Pernambuco (https://www.folhape.com.br/noticias/com-41oc-petrolina-bate-recorde-de-temperatura-registrada-em/198898/, trecho de busca). Outra notícia cita 38 °C em outubro de 2024 (Diario de Pernambuco) | Corrigir a frase: 40 °C **não** está acima do recorde; é excedido em dias extremos. Manter ou não a premissa é do engenheiro térmico e do dono, não da logística: retirar "decisão 3" da lista de decisões e passar como dado de interface com a ressalva |
| 10 | 6 e 7 x `01-projeto-termico.md` seção 3.4 | **IMPORTANTE** (conflito, ver abaixo) | Horário de recepção incompatível entre documentos. O 09 propõe portão das 7h às 14h e "caso de projeto: 1 t entre 10h e 14h", com manga chegando das 10h às 15h. O 01 recomenda "fruta nova entra até as 10 h" e dimensionou o gelo de 400 kg para esse caso (700 kg sem regra de horário). Dentro do próprio 09 a chegada da manga (até 15h) passa da janela (até 14h) | 01, linhas 24, 194 e 281; 09, seções 6 e 7 | Não resolver sozinho: registrar o conflito (bloco "Conflitos" abaixo). Corrigir a incoerência interna 14h x 15h |
| 11 | 7 (temperatura da fruta) x 01 | **IMPORTANTE** | O 09 entrega "30 a 35 °C" como temperatura de chegada; o 01 calculou com 30 °C. A diferença não é pequena | 1.000 kg × 3,77 kJ/kg·K × 5 K = 18.850 kJ = **5,2 kWh de frio por dia a mais** (cerca de 7% da carga de 70 a 80 kWh/dia do 01) | Dar um único valor de projeto com marcação, ou avisar o autor do 01 da faixa. Manter a medição com termômetro na visita |
| 12 | 6 e 7 x 01 seção 2 | **IMPORTANTE** (conflito, ver abaixo) | O 09 recomenda "começar só com manga; caju ausente no local". O 01 projetou **duas zonas** e dimensionou tudo para o caso "câmara inteira a 5 °C, 1 t/dia de caju". Além disso, o 01 descarta a operação alternada porque "as duas colhem no segundo semestre", e o 09 diz que no polo irrigado a alternância caberia (manga o ano todo, caju de setembro a dezembro) | 01, linhas 26, 113, 124; 09, seções 1.5 e 6 | Registrar como conflito para o dono. O custo de projetar para caju num local sem caju deve ser mostrado pelo autor do 01 |
| 13 | 7 (embalagem) x 01 | MENOR | Caixa de 22 a 27 kg e "1 t ≈ 40 caixas" no 09; caixa de 20 kg, 50 caixas por tonelada e 250 caixas para 5 t no 01. E o dado do 09 só vale para manga: o caju de mesa vai em bandeja de camada única com filme (o 01 cita os ensaios da Embrapa com bandeja e PVC), o que ocupa muito mais volume por quilo e reduz a capacidade de 5 t | 01, linhas 84, 135 e 629. Embrapa: 5 °C e 85–90% de umidade, cerca de 20 dias em bandeja com PVC (https://www.redalyc.org/pdf/1953/195320033013.pdf, trecho de busca) | Unificar a caixa com o 01 e escrever que a embalagem do caju é outra, com efeito na capacidade [SUPOSTO até cotar] |
| 14 | 6 (permanência do caju) | MENOR | "10 a 15 dias a 5 °C" no 09; "10 a 25 dias" no 01; a busca mostra cerca de 20 dias (Embrapa) | Mesma fonte do achado 13 | Alinhar os dois documentos na mesma fonte |
| 15 | 1.1, 2 | **IMPORTANTE** | O estudo para na divisa do estado, mas o local recomendado vende do outro lado da ponte. Juazeiro-BA teria colhido 417,5 mil t de manga em 2024, mais que Petrolina, e Casa Nova-BA 196.161 t; o próprio Projeto Nilo Coelho se estende a Casa Nova. Isso pesa na concorrência por comprador e na oferta de frio existente, e não aparece | Canal Rural, reportagem de 2026 citando Embrapa/IBGE (https://www.canalrural.com.br/alem-do-agro/?p=7820) e Movimento Econômico/Sudene; trechos de busca, não conferidos no IBGE | Acrescentar uma linha sobre o lado baiano do polo (produção, cooperativas, câmaras) pelo menos como contexto do candidato A |
| 16 | 2, 4.3 | **IMPORTANTE** | Não há **nenhum preço** no documento: nem da manga na roça, nem no Mercado do Produtor, nem na CEASA-PE (a FONTE 26 é uma página de cotação e foi usada só para o peso da caixa), nem do PNAE. Sem diferença de preço não se sabe se "tirar 1 t/dia do circuito vende na roça" compensa — e o próprio texto diz que a câmara "só se paga se a fruta sair para um mercado que pague pela qualidade" | Não levantei preços; aponto a ausência | Buscar cotações (CEASA-PE, Prohort/Conab, Cepea/Hortifruti Brasil para manga do Vale) com data, ou escrever "preço não encontrado" como manda a regra 2 das premissas |
| 17 | 2.4 (conta de bolso do PNAE) | MENOR | "10 famílias × R$ 40.000 = R$ 400.000 por ano" é teto legal, não demanda. Nada indica que uma prefeitura compre esse valor em manga | A R$ 3/kg [SUPOSTO do revisor], R$ 400.000 seriam 133 t/ano, cerca de 0,5 t por dia letivo: mais da metade da câmara só em merenda de manga | Dizer que é teto e remeter à pergunta 25 da seção 8 |
| 18 | 2.1 | MENOR | "CEASA em Petrolina — não pesquisado a fundo" e "Central em Serra Talhada — não encontrei": a definição pedia as centrais de Petrolina/Juazeiro. Feiras e cooperativas compradoras quase não aparecem | — | Pesquisar a central de abastecimento de Petrolina e as feiras da agricultura familiar, ou declarar a lacuna na lista final (hoje não está) |
| 19 | 1 (fontes exigidas) | MENOR | A definição cita IPA e Adagro como fontes para produção e calendário; nenhuma das duas foi usada para isso (Adagro só para sanidade). Produtos parecidos (Ecofrost, ColdHubs), citados na regra 1 das premissas, não foram consultados para o modelo de operação (taxa por caixa, tempo de permanência) | — | Buscar ao menos o modelo de cobrança do ColdHubs (taxa diária por caixa) como referência para a "taxa por caixa" da seção 6 |
| 20 | 5.1 e bloco de segurança | **IMPORTANTE** | (a) "Os painéis podem servir de telhado" sobre o contêiner e a recepção: afirmação estrutural sem marcação e sem aviso de vento, de ventilação do condensador e de gás inflamável sob cobertura. O 01 põe os resfriadores a propano do lado de fora, a 3 m da porta e de ralos. (b) A área de 300 a 500 m² foi suposta sem conhecer o porte que o 01 pede (11 a 12 kWp e tanque de gelo de 800 kg). (c) O bloco de segurança não fala de CO₂ e falta de oxigênio com a câmara fechada (o 01 fala), nem de vento sobre a estrutura dos painéis, nem de raio/aterramento em campo aberto | 12 kWp ocupam cerca de 55 a 65 m² de módulos [estimativa do revisor], contra cerca de 15 m² de teto de um contêiner de 20 pés: os painéis não cabem sobre o contêiner | Marcar a frase do telhado como [VALIDAR COM PROFISSIONAL HABILITADO] (estrutura, vento, afastamento do gás); refazer a área com os números do 01; completar o bloco de segurança |
| 21 | 2.4 | MENOR | A Resolução FNDE nº 04/2026 foi alterada pela Resolução CD/FNDE nº 17, de 22/10/2026. O limite de R$ 40 mil foi mantido, segundo a imprensa | https://www.canalrural.com.br/politica/resolucao-do-pnae-redefine-compras-da-agricultura-familiar/ (trecho de busca) | Citar a alteração e mandar conferir o texto vigente |
| 22 | 1.2 | MENOR | "12.520 ha ÷ 1.954 lotes = 6,4 ha" divide área de uma fonte por lotes de 2012 de outra; a tabela também traz 2.326 lotes e 84,5% de pequenos (= 1.965). O autor avisa que mistura anos, mas marca [CALCULADO] | 2.326 × 0,845 = 1.965 lotes; 12.520 ÷ 1.965 = 6,4 ha. O valor se mantém | Manter, citando a segunda conta como conferência |
| 23 | 1.3 (linha "666,1 mil t") | MENOR | Número descartado pelo autor permanece na tabela. Um leigo pode lê-lo como dado | — | Tirar da tabela e deixar só em nota |
| 24 | 5.2 e 6 | MENOR | Leigo não consegue contratar a operação só com o texto: não há minuta do termo de cessão, valor de referência da taxa por caixa, nem quem responde por fruta perdida se o equipamento falhar. São pendências legítimas, mas não estão na lista de pendências | — | Incluir na seção 9 "responsabilidade por perda de fruta" e "valor da taxa" como pendências |
| 25 | Geral | MENOR | Ponto positivo que deve ser preservado: o documento declara que não abriu nenhuma página, separa fonte fraca de boa e lista o que não verificou. O problema é que as marcações das tabelas nem sempre acompanham essa honestidade (achados 2, 4, 5) | — | Alinhar as marcações das tabelas com o aviso do início |

## Respostas diretas às perguntas da tarefa

1. **Produção por município.** Refeita no IBGE. Manga: cinco dos sete municípios conferem; **Lagoa Grande está errada** (30.000 t, não 10.000) e o **total do estado está errado** (560.977 t, não 540.977). Caju: o documento não tinha a tabela; o IBGE mostra **Buíque com 81%** e o Pajeú com 3,8%.
2. **Conta de escala.** Aritmética certa, hipótese errada. O resultado honesto é uma faixa de cerca de 2 a 6 lotes, com valor central perto de 4, e falta a conta de pico de colheita.
3. **Pontuação.** Somas certas. A primeira posição de Petrolina é robusta a pesos; o "empate" depende de uma troca de pesos escolhida. As notas de C, D e E precisam ser refeitas com o IBGE: Buíque (E) foi rebaixado por "fonte fraca" e é, de longe, o maior polo de caju; o Pajeú (C) recebeu nota de caju que o dado não sustenta. O segundo lugar (C 66,0 contra B 65,4) já era empate técnico.
4. **Manga e caju não coexistem.** Sustenta-se para volume comercial, com a exceção de São José do Belmonte. O autor chegou perto da resposta certa sem ter o dado; a frase precisa ser reescrita com ele (achado 1b).
5. **Horários e meses.** Horários de chegada são [SUPOSTO] declarado e conflitam com o projeto térmico. Meses do caju estão com marcação de fonte que o próprio autor desautoriza.
6. **Links.** Fora o SIDRA, não abri nenhum. Fontes que, pelo que o próprio documento diz, não sustentam o número: 14 (blog; acertou Buíque, errou o total), 25, 29, 31, 33, 58. As FONTES 2 e 3 devem ser trocadas pelo SIDRA; a FONTE 3 ou o trecho lido dela dá um total do estado diferente do IBGE.
7. **Calculado que é suposição.** Achados 2, 3, 4, 22, 27 e a frase sem marcação da seção 1.4.
8. **O que falta da definição.** Calendário específico de PE; central de Petrolina e feiras; concorrência de câmaras; irradiação; preços; e todo o levantamento de Buíque.

## Conflitos para o dono mediar (não são erro simples)

### Conflito A — horário de entrada da fruta (09 x 01)

| | Posição do 09 (logística) | Posição do 01 (térmico) |
|---|---|---|
| Regra | Recepção das 7h às 14h; carga típica entre 10h e 14h; manga chega das 10h às 15h [SUPOSTO] | Fruta nova entra até as 10h; depois disso espera à sombra até a manhã seguinte, ou entra meia carga |
| Base | Colheita de manga do amanhecer ao fim da manhã; costume local não verificado | Carga noturna de 53,3 kWh com fruta às 17h contra 29,3 kWh com fruta às 7h [CALCULADO no 01] |
| Custo ou risco | Se valer a janela até 14h, o gelo de 400 kg não basta; o 01 pede 700 a 800 kg | Se valer o limite das 10h, a manga colhida na manhã fica um dia fora da câmara, e o caju (que "não espera") teria de ser colhido e entregue em 2 a 3 horas |

O revisor não decide. Dado que resolveria: horário real de colheita e entrega, medido na visita (pergunta 4 da seção 8).

### Conflito B — projetar para caju num local sem caju (09 x 01)

| | Posição do 09 | Posição do 01 |
|---|---|---|
| Regra | Petrolina, só manga para começar; caju só se aparecer oferta | Duas zonas (caju a 5 °C, manga a 12 °C); equipamento dimensionado para câmara inteira a 5 °C com 1 t/dia de caju |
| Custo ou risco | Equipamento mais simples e uma zona só, mas não atende o pedido do dono (as duas frutas) | Atende as duas frutas, mas a carga de projeto sobe de cerca de 66,6 para 79,5 kWh/dia e a capacidade prática cai para cerca de 4 t, num local onde o caju pode nunca chegar |

### Conflito C — a alternativa do caju fica fora do sertão (decisão do dono, não do revisor nem do autor)

As premissas dizem "sertão de Pernambuco". O IBGE mostra que o caju do estado está em Buíque e Tupanatinga, que são Agreste. Não é erro de ninguém: é uma escolha.

| | Manter "sertão" | Aceitar o Agreste para o caju |
|---|---|---|
| Local de caju | São José do Belmonte (151 t de castanha, e também 400 t de manga) ou Carnaíba–Flores (92 t) | Buíque–Tupanatinga (2.686 t de castanha) |
| A favor | Respeita a premissa; Belmonte é o único município com as duas frutas | Volume de caju cerca de 18 vezes o de Belmonte; mais perto de Caruaru e do Recife |
| Contra | Volume pequeno: a oferta de caju de mesa pode não chegar a 1 t/dia; uso de poucos meses | Sem manga; clima de altitude diferente dos 40 °C das premissas (a conferir); o documento não levantou nada sobre associações, estradas e compradores de lá |

## Veredito

**APROVADO COM CORREÇÕES**, com um item bloqueante.

- A recomendação principal (**Petrolina, manga**) sai **reforçada** pela conferência no IBGE e pode seguir como referência provisória de local e de clima, depois de corrigidos os achados 9, 10 e 11.
- A parte do **caju não pode ser usada como está**: a alternativa "Pajeú" não se sustenta no IBGE (achado 1). Enquanto a seção 1.3 e os candidatos C, D e E não forem refeitos com a PAM, o dono não deve decidir entre manga e caju com base neste documento.
- Os achados 1b, 2 a 5, 7, 8, 15, 16, 20, 26 e 27 devem ser corrigidos na próxima versão. Os conflitos A, B e C vão ao dono.
