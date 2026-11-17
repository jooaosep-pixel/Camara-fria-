# 11 — Importação da China x compra no Brasil (FASE 1 — preliminar)

Autor: agente de importação. Data da pesquisa: 17/11/2026.
Estado: **fase 1**. O projeto térmico (01), o elétrico (02) e o de controle (03) ainda não existem, então a lista de componentes é por **categoria**, não por modelo. A fase 2 fecha item a item (ver seção 8).

## Como ler este documento

- Marcas usadas: **[CALCULADO]** (conta feita aqui, conferível), **[SUPOSTO]** (hipótese de trabalho, sem fonte), **[VALIDAR COM DESPACHANTE]** (alíquota ou regra que não consegui confirmar em fonte oficial), **[VALIDAR COM PROFISSIONAL HABILITADO]**.
- Os números entre colchetes, como [F7] ou [P3], remetem à lista de fontes no fim.
- "FOB" é o preço da mercadoria embarcada no porto chinês, sem frete, seguro nem impostos brasileiros. "Custo posto" é quanto ela custa já liberada no Brasil.

### Limites desta pesquisa (leia antes de confiar nos números)

1. **Não consegui abrir nenhuma página.** Neste ambiente só a busca na web funcionou; a abertura direta das páginas foi bloqueada (os endereços canalsolar.com.br, dhl.com, normasbrasil.com.br, guiatributario.net, mercadoeconsumo.com.br e blog.econeteditora.com.br falharam). Todos os números vêm dos **trechos exibidos nos resultados da busca**. Nenhuma lei, portaria ou anúncio foi lido na íntegra.
2. **As alíquotas por NCM vêm de sites particulares de consulta** (buscadorncm, fazcomex, remessaonline), não da tarifa oficial. Em 2026 o governo mexeu em mais de mil alíquotas de máquinas e eletrônicos (seção 2.3), e não achei uma lista consolidada. **Toda alíquota deste documento precisa ser conferida por um despachante no dia do embarque.**
3. **Preço de vitrine (Alibaba, Made-in-China e parecidos) é indicativo.** Não é cotação. Costuma valer para grandes quantidades, omitir a especificação real e mudar ao pedir orçamento. Em vários casos o resumo da busca não deixou claro qual preço pertence a qual anúncio; isso está dito item a item.
4. Vários sites mostram datas de 2026 no cabeçalho de textos que parecem mais antigos. Onde a data da informação não ficou clara, está dito.

---

## Resumo em uma página

1. **Para 1 protótipo, importar quase nada.** A importação formal tem custos fixos (despachante, taxas, armazenagem, frete interno) que não dependem do tamanho da compra, e os itens mais baratos na China são justamente os que têm barreira de certificação no Brasil (módulos, baterias, inversores).
2. **Multiplicador típico** do preço FOB em dólar para o custo posto, antes dos custos fixos: **1,8 a 2,1 vezes** para máquinas e eletrônicos; 1,9 a 2,4 para módulos; perto de 3 para itens volumosos e baratos (painéis isotérmicos, contêiner usado), por causa do frete [CALCULADO, seção 2.5].
3. **Onde importar pode valer:** a unidade condensadora (ou o compressor) de velocidade variável em R290 **se** o projeto concluir que não existe equivalente à venda no Brasil; e o conjunto todo, num lote de 10. Para esses, a via recomendada é **importação por conta e ordem através de uma importadora (trading)**, com CNPJ.
4. **Onde não vale:** módulos fotovoltaicos, bateria, contêiner reefer usado, painéis isotérmicos e CLP. Motivos: Inmetro, lítio como carga perigosa, licença para bem usado, frete, e manutenção local.
5. **O que pode barrar:** registro no Inmetro (módulos, inversores, controladores e baterias de sistemas fotovoltaicos); controle do Ibama sobre gases HFC (regra para equipamento que já vem carregado: não confirmada); licença para importar bem usado (reefer); homologação da Anatel para qualquer coisa com Wi-Fi; carga perigosa no navio (gás inflamável e lítio).
6. **Não achei nenhum fabricante chinês que venda, pronta, a câmara do projeto** (acionamento direto pelos painéis, com banco de gelo no lugar de baterias). Os "solar cold room" anunciados usam baterias ou não dizem.

---

## 1. Como se importa, para um leigo

### 1.1 Três caminhos

| Caminho | O que é | Serve para | Limite |
|---|---|---|---|
| **Remessa internacional** (correio ou courier; inclui o programa Remessa Conforme) | Encomenda que chega pela transportadora, com imposto simplificado | Peças pequenas e baratas: sensores, placas eletrônicas, um drive pequeno | Até US$ 3.000 por remessa, segundo as fontes [F24]. Não serve para carga perigosa nem para máquina pesada |
| **Importação formal direta** | A sua empresa registra a declaração de importação (hoje chamada DUIMP) e paga cada imposto separadamente | Lote de 10 ou mais; quem vai importar com frequência | Exige habilitação na Receita (Radar) e, na prática, CNPJ e despachante |
| **Importação por uma importadora (trading)** | Uma empresa já habilitada importa para você. "Por conta e ordem": a mercadoria é sua desde a origem e a importadora presta serviço. "Por encomenda": a importadora compra com o dinheiro dela e revende a você [F25] | **Primeira importação e protótipo** | Paga-se a taxa da importadora. Percentual típico: **não encontrado**; pedir proposta |

### 1.2 Pessoa física x empresa

- **Pessoa física pode importar para uso próprio**, sem revenda. Fontes jurídicas dizem que nesse caso ela fica dispensada da habilitação no Radar; outras fontes dizem que o Radar é sempre exigido para registrar a declaração [F23][F26]. **Divergência não resolvida** [VALIDAR COM DESPACHANTE].
- **A Receita pode reter a mercadoria se entender que a finalidade é comercial** [F26]. Uma câmara fria para atender produtores, com intenção de fazer mais dez, tem cara de atividade comercial. Recomendo tratar o projeto como **empresa (CNPJ)** desde o início.
- **O que na prática exige CNPJ:** habilitação Radar de empresa; registro de produto no Inmetro; cadastro e licenças no Ibama; contratar importadora por conta e ordem; aproveitar créditos de impostos; emitir nota para vender ou alugar a câmara depois. [VALIDAR com contador qual tipo de empresa e regime tributário.]

### 1.3 Habilitação no Radar/Siscomex

- É o cadastro na Receita Federal que autoriza a empresa a importar. Norma citada: IN RFB nº 1.984/2020 [F23].
- Três modalidades [F23]: **Expressa** (entrada, em regra automática; uma fonte cita teto de US$ 50 mil por semestre), **Limitada** (até US$ 150 mil por semestre) e **Ilimitada** (acima disso, conforme a capacidade financeira estimada pela Receita). Os tetos valem só para importação.
- Desde 15/01/2026 a habilitação exige CNPJ e CPF dos representantes regulares de forma permanente [F23]. Para o protótipo, mesmo a modalidade de entrada sobra.
- Se usar importadora por conta e ordem, a sua empresa ainda precisa estar habilitada e vinculada à importadora [VALIDAR COM DESPACHANTE].

### 1.4 Remessa internacional e Remessa Conforme (situação em 2026)

Regras mudaram em 2026. O que as fontes dizem [F24]:

- Compra de **até US$ 50** em site certificado: imposto de importação **zero** desde 12/05/2026 (Medida Provisória nº 1.357, convertida na Lei nº 15.502, de 10/09/2026).
- **De US$ 50 a US$ 3.000:** imposto de importação de **60%**, com desconto fixo de **US$ 30** no imposto. Uma fonte diz que a nova lei permite ao Ministério da Fazenda fixar até 30% nessa faixa; não achei confirmação de que os 60% tenham sido reduzidos [VALIDAR COM DESPACHANTE].
- Em site **não** certificado: 60% sem desconto.
- **ICMS sempre incide.** Para remessas, a Sefaz-PE informou 17% (notícia de 14/05/2026) [F14].
- Conta de exemplo, drive de US$ 328: imposto = 0,60 × 328 − 30 = US$ 166,80; ICMS "por dentro" de 17%: (328 + 166,80) ÷ 0,83 = US$ 596,14; em reais, × 5,65 = **R$ 3.368**, ou 1,82 vez o preço [CALCULADO].
- Não vale para: bateria de lítio avulsa (carga perigosa), produto que exige licença (Inmetro, Anatel, Ibama) sem a licença, nem para revenda.

### 1.5 Incoterms: quem paga o quê

| Sigla | O vendedor entrega | Você paga e organiza | Comentário |
|---|---|---|---|
| EXW | Na porta da fábrica | Tudo, inclusive transporte dentro da China | Evitar na primeira compra |
| **FOB** | A bordo do navio no porto chinês | Frete marítimo, seguro, impostos, liberação | **O mais usado para comparar preços**; você escolhe o agente de carga |
| CIF | No porto brasileiro, frete e seguro pagos | Impostos, liberação, taxas do porto | Cômodo, mas o vendedor escolhe o frete e as taxas no destino costumam vir altas |
| DDP | Na sua porta, impostos pagos | Nada | Desconfiar: para o Brasil quase nunca é feito de forma regular; quem promete DDP em carga formal pode estar subfaturando [SUPOSTO] |

### 1.6 Despachante aduaneiro

- É o profissional que registra a declaração, classifica a mercadoria (escolhe a NCM, o código que define os impostos), obtém as licenças e libera a carga.
- Não há tabela oficial; o preço é livre [F21]. Um site de consultoria estima **R$ 2.500 a R$ 4.500 por declaração marítima** e, acima de US$ 100 mil, 0,5% a 1,5% do valor [F21]. Tratar como ordem de grandeza.
- **Peça a ele, antes de pagar o fornecedor:** a NCM de cada item, a lista de licenças exigidas e uma planilha de custo posto.

### 1.7 Prazos porta a porta até Pernambuco

| Etapa | Prazo | Fonte |
|---|---|---|
| Fabricação e despacho na China | 20 dias em um anúncio de bateria; equipamento sob encomenda costuma levar mais | [P8]; resto [SUPOSTO] |
| Navio China → Nordeste | Cerca de **30 dias** na linha direta Ásia–Pecém (CE), contra cerca de 60 dias antes dela. **Suape não aparece como escala dessa linha.** Suape teve linha semanal para a Ásia via Singapura aberta em novembro de 2024; não confirmei se continua em 2026 | [F37] |
| Liberação na alfândega | **Não encontrado.** Dias quando não há licença; semanas quando há exigência de Inmetro, Ibama ou conferência física | [SUPOSTO] |
| Suape → Petrolina por caminhão | Não levantado nesta fase | pendência |
| **Total** | **75 a 120 dias** depois do pagamento do sinal | [SUPOSTO] — confirmar com agente de carga |

Tempo de trânsito China–Suape: **não encontrado**. Um agente de carga precisa cotar Suape e Pecém.

---

## 2. Custo posto no Brasil

### 2.1 O método, passo a passo

Regra em vigor em novembro de 2026 (antes da troca de impostos de 2027, seção 2.4).

1. **Valor aduaneiro (VA)** = (FOB + frete internacional + seguro) × câmbio do dia do registro. [Se a taxa de descarga no porto entra ou não: VALIDAR COM DESPACHANTE.]
2. **Imposto de Importação (II)** = VA × alíquota da NCM.
3. **IPI** = (VA + II) × alíquota da NCM.
4. **PIS-Importação** = VA × 2,1%. **Cofins-Importação** = VA × 9,65%. Juntos, 11,75% [F9][F27].
5. **AFRMM** (adicional de frete da marinha mercante) = 8% do frete marítimo [F17].
6. **Taxa Siscomex**: valor fixo por declaração. As fontes divergem: R$ 185,00 + R$ 29,50 por adição, ou R$ 115,67 + R$ 38,56 por adição [F20]. Usei R$ 214,50 [VALIDAR COM DESPACHANTE].
7. **ICMS de Pernambuco**, cobrado "por dentro": base = (VA + II + IPI + PIS + Cofins + AFRMM + taxas e despesas aduaneiras) ÷ (1 − alíquota); ICMS = base × alíquota [F15]. Alíquota geral de PE: **20,5%** desde 01/01/2024 (Lei estadual nº 18.305/2023) [F13].
8. **Custos fixos por embarque:** despachante, taxas do terminal (descarga, desova de carga fracionada, armazenagem), transporte até o local.
9. **Custo posto** = soma de tudo.

Fórmula resumida da parte que varia com o valor [CALCULADO]:

> multiplicador sobre o VA = (1 + II + IPI × (1 + II) + 0,1175) ÷ (1 − 0,205)

Tabela pronta do multiplicador sobre o valor aduaneiro (ICMS de 20,5%) [CALCULADO]:

| II ↓ / IPI → | 0% | 3,25% | 9,75% | 11,25% | 13% |
|---|---|---|---|---|---|
| 0% | 1,41 | 1,45 | 1,53 | 1,55 | 1,57 |
| 12,6% | 1,56 | 1,61 | 1,70 | 1,72 | 1,75 |
| 14% | 1,58 | 1,63 | 1,72 | 1,74 | 1,77 |
| 18% | 1,63 | 1,68 | 1,78 | 1,80 | 1,83 |
| 25% | 1,72 | 1,77 | 1,87 | 1,90 | 1,93 |

Leitura: mesmo com imposto de importação zero, a mercadoria chega 41% mais cara que o valor aduaneiro, por causa de PIS, Cofins e ICMS.

### 2.2 Hipóteses usadas nos exemplos

| Hipótese | Valor | Marcação |
|---|---|---|
| Câmbio | R$ 5,65 por dólar (taxa de referência do Banco Central de 13/11/2026, segundo um portal; em 09/11 estava em R$ 5,51) | [F22] — usar o câmbio do dia |
| Frete marítimo em carga fracionada | US$ 150 por m³, incluindo taxas na origem. Fonte brasileira cita US$ 40 a 90 por m³ para Santos; em fevereiro de 2026 houve relato de frete a US$ 10.000 por contêiner | [SUPOSTO] sobre [F18][F19] |
| Frete de contêiner inteiro de 20 pés | US$ 2.150 a 4.800 (rota para Santos) | [F18] |
| Seguro | 0,5% de (FOB + frete) | [SUPOSTO] |
| Custos fixos de um embarque pequeno | Despachante R$ 3.500 + taxas de terminal e armazenagem R$ 4.000 + Siscomex R$ 214,50 = **R$ 7.714,50** | despachante [F21]; terminal [SUPOSTO] — **valor não encontrado** |

### 2.3 Alíquotas por NCM

A NCM de cada item é **provável**; quem define é o despachante, e ela muda o imposto.

| Categoria | NCM provável | II | IPI | Fonte e observação |
|---|---|---|---|---|
| Módulo fotovoltaico | 8541.43.00 | **25%** (Resolução Gecex nº 666) | não encontrado; usei 0% | [F1][F2][F3]. Existe cota a 9,6% (US$ 403,2 milhões, de 16/07/2026 a 15/07/2027, Portaria Secex nº 522/2026), mas é distribuída por empreendimento e a anterior era para usinas acima de 5 MW: **não contar com ela**. ICMS: isento pelo Convênio ICMS 101/97, prorrogado até 31/12/2028 [F16]; se a isenção vale na importação em PE: [VALIDAR COM DESPACHANTE] |
| Unidade condensadora até 30.000 frigorias/h (cerca de 35 kW) | 8418.69.40 | 18% | 13% | [F27]. Um site cita redução a 0,02% por regime especial (Resolução Gecex nº 553/2024): não confirmado |
| Compressor hermético abaixo de 4.700 frigorias/h (5,5 kW de frio) | 8414.30.11 | 18% | 3,25% | [F27] |
| Compressor hermético, outros (acima de 4.700 frigorias/h) | 8414.30.19 | 0% | 0% | [F27]. **A capacidade do compressor muda o imposto de 18% para zero.** Dado para a fase 2 |
| Evaporador (forçador de ar) | 8418.99.00 (partes) ou outra | **não encontrado** | **não encontrado** | [VALIDAR COM DESPACHANTE]. Para ordem de grandeza, ver tabela 2.1 |
| Conversor de frequência (drive) | 8504.40.50 | 14% (um site) ou 12,6% (dois sites) | 9,75% | [F27]. Há ex-tarifários (reduções para itens sem similar nacional) citados com 0%. Um "drive solar" pode cair em 8504.40.90 (outros conversores) |
| Inversor fotovoltaico | 8504.40.90 | 12,6%; aumento para 20% foi aprovado em 2026 mas, segundo o Canal Solar, **ficou fora da lista publicada** | não levantado | [F4][F5] — situação instável |
| Bateria de íon de lítio (inclui LiFePO4) | 8507.60.00 | 18% | 11,25% | [F27]. Aumento de "sistemas de baterias" de 16% para 20% foi noticiado em 2026 com o mesmo desfecho incerto [F5] |
| Controlador programável (CLP) | 8537.10.20 | 12,6% | 9,75% | [F27] |
| Painel isotérmico de aço com núcleo de poliuretano | 7308.90.90 (Solução de Consulta Cosit nº 98.443, segundo site de comentários) | **não encontrado** | **não encontrado** | [F28]. Para painel de isopor a Receita decidiu de outro jeito: classificação discutível |
| Contêiner (inclusive frigorífico) | 8609.00.00 | 14% (um site) ou 12,6% (outros); possível redução a 0% não confirmada | 0% | [F27]. Se o reefer com máquina cai mesmo nesta NCM: [VALIDAR COM DESPACHANTE] |
| Câmara fria completa / equipamento de refrigeração não especificado | 8418.69.99 | 12,6% | 9,75% | [F27] (um site só) |

Para todos: PIS 2,1% + Cofins 9,65% [F27] e ICMS-PE 20,5% [F13].

**Mudanças de 2026 que afetam esta tabela:**

- **Resolução Gecex nº 852/2026** (publicada em 05/02/2026): aumentou o imposto de importação de mais de mil códigos de máquinas e eletrônicos, alguns até 20%. Houve recuos parciais (105 produtos zerados em 27/02/2026; Resolução nº 866/2026). **Não encontrei lista consolidada do que ficou** [F6][F7][F8]. Compressores, drives e CLPs são exatamente esse tipo de bem.
- **Lei Complementar nº 224/2025 e IN RFB nº 2.305/2026** (em vigor desde 01/04/2026): cortaram 10% de benefícios fiscais, inclusive de PIS/Cofins na importação. A alíquota padrão de 11,75% segue como referência [F9].
- **China:** fim da devolução de imposto na exportação de módulos a partir de 01/04/2026, com previsão de alta de preço [P4].

### 2.4 Reforma tributária: o que muda se a compra escorregar para 2027

- **2026 é ano de teste:** CBS de 0,9% e IBS de 0,1%, abatidos de PIS/Cofins. Não aumenta o custo [F10][F11].
- **2027:** PIS-Importação e Cofins-Importação deixam de existir e entra a CBS cheia (estimativa citada: 8,7%, a confirmar); o IBS segue em 0,1% e o ICMS continua [F10][F12]. Como fica o IPI em 2027: **não levantado** [VALIDAR com contador].
- **Consequência:** as contas deste documento valem para registro da importação até 31/12/2026. Depois disso, refazer.

### 2.5 Exemplos calculados, por categoria [CALCULADO]

Câmbio R$ 5,65; frete, seguro e alíquotas conforme 2.2 e 2.3. **Sem** os custos fixos do embarque.

| Item de exemplo | FOB (US$) | Frete (US$) | Valor aduaneiro (R$) | II | IPI | PIS+Cofins | ICMS | **Custo posto (R$)** | Multiplicador sobre FOB em reais |
|---|---|---|---|---|---|---|---|---|---|
| 14 módulos de 550 W a US$ 58,85, ICMS isento | 824 | 300 | 6.382 | 1.595 | 0 | 750 | 0 | **8.863** (R$ 633 cada) | 1,90 |
| Os mesmos, se a isenção de ICMS não valer | 824 | 300 | 6.382 | 1.595 | 0 | 750 | 2.285 | **11.148** (R$ 796 cada) | 2,39 |
| Unidade condensadora inverter de 5 HP | 1.380 | 150 | 8.688 | 1.564 | 1.333 | 1.020 | 3.268 | **15.941** | 2,04 |
| Drive solar de 5,5 kW | 328 | 15 | 1.948 | 273 | 216 | 229 | 689 | **3.362** | 1,81 |
| Bateria LiFePO4 51,2 V 100 Ah | 768 | 45 | 4.616 | 831 | 613 | 542 | 1.708 | **8.331** | 1,92 |
| CLP de US$ 200 | 200 | 5 | 1.164 | 147 | 128 | 136 | 407 | **1.984** | 1,76 |
| Compressor de US$ 1.000 acima de 4.700 frigorias/h | 1.000 | 30 | 5.849 | 0 | 0 | 687 | 1.689 | **8.238** | 1,46 |
| Compressor de US$ 1.000 abaixo de 4.700 frigorias/h | 1.000 | 30 | 5.849 | 1.053 | 224 | 687 | 2.018 | **9.845** | 1,74 |
| Reefer usado de 20 pés | 5.000 | 3.500 | 48.265 | 6.757 | 0 | 5.672 | 16.058 | **78.334** | 2,77 |
| Conjunto "solar cold room" de US$ 15.000 em contêiner próprio | 15.000 | 4.800 | 112.429 | 14.166 | 12.343 | 13.210 | 39.793 | **194.111** | 2,29 |

Os valores incluem o AFRMM (8% do frete), que não tem coluna própria. O FOB do conjunto de US$ 15.000 é [SUPOSTO], escolhido dentro da faixa de US$ 8.000 a 60.000 citada em [P12].

**Embarque consolidado de protótipo** (módulos com ICMS isento + condensadora + drive + bateria): R$ 36.496 de mercadoria e impostos + R$ 7.714,50 de custos fixos = **R$ 44.211** [CALCULADO]. Os custos fixos pesam 17% e não incluem o caminhão até Petrolina.

---

## 3. Exigências que podem barrar a importação

> **⚠ O QUE PODE BARRAR.** Barrar significa: a carga fica retida no porto pagando armazenagem, volta para a China, ou entra mas não pode ser usada nem vendida legalmente. Confirmar cada linha **antes de pagar o fornecedor**.

| # | Exigência | Atinge | O que achei | Risco |
|---|---|---|---|---|
| 1 | **Registro no Inmetro** — Portaria nº 140/2022, alterada pela nº 515/2023 | Módulos acima de 5 W; inversores ligados à rede, isolados e híbridos até 75 kW; controladores de carga; **baterias, inclusive de lítio** | Registro obrigatório, com ensaio em laboratório [F29]. Se a alfândega exige o registro já na entrada, e se um importador novo pode usar o registro que o fabricante já tem no Brasil: **não confirmado** | **Alto.** Módulo ou bateria de fabricante sem registro no Brasil não deve ser importado. Registrar um modelo por conta própria para 14 módulos não compensa [SUPOSTO] |
| 2 | Inmetro para o **drive solar** (conversor de frequência alimentado por painéis) | Drive do compressor | A busca não trouxe nada sobre drives de bombeamento ou de compressor na Portaria 140. Pode ser entendido como "inversor isolado" | **Médio, indefinido** [VALIDAR COM DESPACHANTE e com o Inmetro] |
| 3 | **Ibama — gases HFC** (R134a, R404A, R449A, R452A, R513A etc.) | Gás em cilindro; possivelmente equipamento que já vem carregado | Instrução Normativa do Ibama de 18/12/2023 (o portal do governo a chama de nº 29; um site a publica como nº 251) controla a importação de HFC e misturas por **cota anual em toneladas de CO2 equivalente**: 90% para quem já importava, 10% de reserva para novos. Exige certificado de regularidade e licença de importação no sistema do Ibama [F30]. **Se alcança equipamento pré-carregado: não encontrado** | **Alto para gás avulso** (quem não tem cota não importa). **Indefinido para equipamento carregado** [VALIDAR COM DESPACHANTE e com o Ibama] |
| 4 | Ibama — gases HCFC (R22) | Reefer antigo | Importação controlada e em eliminação; a reserva técnica de R22 de 2025 se esgotou [F30] | Não importar nada com R22 |
| 5 | **R290 (propano)** como fluido | Unidade em R290 | Não é substância controlada pelo Protocolo de Montreal; o controle do Ibama encontrado é sobre CFC, HCFC e HFC [F31]. Regra da ANP para importar propano em cilindro: **não encontrada** | Baixo para o equipamento. Para o gás: **comprar no Brasil** |
| 6 | **Transporte marítimo de gás inflamável** | Unidade pré-carregada com R290 | Código marítimo de cargas perigosas (IMDG): "máquinas frigoríficas com gás inflamável", UN 3358, classe 2.1. Máquina com **menos de 12 kg** de gás fica fora das exigências do código (disposição especial 291) [F32] | Baixo se a carga for pequena. Mesmo assim, **pedir a unidade sem gás**, com carga de nitrogênio para manter seca, e carregar aqui: evita a declaração de carga perigosa e a dúvida do item 3 |
| 7 | **Transporte de bateria de lítio** | Bateria LiFePO4 | UN 3480, classe 9. Exige ensaio UN 38.3 e declaração de carga perigosa; no navio vai em contêiner fechado ou sob o convés [F33]. Sobretaxa em carga fracionada: **não encontrada** | **Médio/alto para uma unidade só**: muitos consolidadores recusam ou cobram caro [SUPOSTO] |
| 8 | **Anatel** | Qualquer coisa com Wi-Fi, Bluetooth ou celular: placa ESP32, CLP com Wi-Fi, modem | Homologação obrigatória. Em março de 2026 a Anatel autuou empresa cujo Wi-Fi estava desligado por programa: **basta o rádio existir na placa**. Novo ato (nº 18.086, em vigor desde 25/05/2026) cobre importação para venda e para uso próprio, com checagem automática na alfândega. Módulos ESP32 da Espressif têm certificado Anatel publicado [F34] | **Médio.** Comprar no Brasil o que tem rádio, ou exigir o número de homologação. A antena Starlink compra-se aqui |
| 9 | **Licença para importar bem usado** | Contêiner reefer usado | Portaria Secex nº 249/2023: bem de capital usado depende de licença (art. 29) e, em regra, de verificação de que não há produção nacional (art. 30); a lista de bens usados foi alterada em 2025 [F36]. Regra específica para contêiner: **não encontrada** | **Alto** — mais um motivo para comprar o reefer usado já no Brasil |
| 10 | **NR-13 — vasos de pressão** | Tanque de líquido, separadores | Vale para vasos com P×V acima de 8 (pressão em kPa, volume em m³). Fontes do setor dizem que **vasos com fluido inflamável entram na norma qualquer que seja o tamanho** [F35]. A norma pede documentação do vaso (prontuário, placa, válvula de segurança) | **Médio.** Vaso chinês sem documentação aceita no Brasil pode ter de ser trocado [VALIDAR COM PROFISSIONAL HABILITADO] |
| 11 | **Frequência e tensão** | Motores de ventilador, contatores, fontes | A China usa 50 Hz; o Brasil, 60 Hz. Motor de 50 Hz ligado em 60 Hz gira mais rápido e pode aquecer [SUPOSTO] | Exigir no pedido: **60 Hz** ou ventiladores eletrônicos (EC) ou em corrente contínua; a tensão será dada pelo projeto elétrico |
| 12 | Conexões e tomadas | Tubulação e painel | Conexões frigoríficas chinesas podem vir em milímetros; no Brasil o comum é polegada [SUPOSTO]. Tomadas no padrão brasileiro (NBR 14136) | Baixo. Pedir desenho com as bitolas antes de fechar |
| 13 | **Garantia e assistência** | Tudo | Garantia de fabricante chinês, na prática, é envio de peça; a mão de obra e a nova importação da peça são suas [SUPOSTO] | Comprar junto um jogo de sobressalentes (placa do drive, ventiladores, sensores) |

> **⚠ SEGURANÇA.** R290 é propano: inflamável. Equipamento em R290 comprado sem ficha técnica confiável (carga de gás, componentes elétricos próprios para atmosfera inflamável, ensaio de estanqueidade) **não deve ser instalado em contêiner fechado** sem a análise do engenheiro de refrigeração. O preço baixo da vitrine não compra essa segurança. [VALIDAR COM PROFISSIONAL HABILITADO]

---

## 4. Item a item — PRELIMINAR, por categoria

Sem o projeto, comparo categorias e ordens de grandeza. Para cada uma: preço FOB encontrado, equivalente no Brasil, custo posto do exemplo (seção 2.5) e recomendação provisória. "Recomendação" aqui é sobre **origem da compra**, não sobre a escolha técnica.

### 4.1 Módulos fotovoltaicos de cerca de 550 W (9 a 14 unidades)

- **China (FOB):** referência de mercado para módulos TOPCon abaixo de 645 W: **US$ 0,107 por watt** FOB China (índice OPIS, notícia de 23/10/2026) [P1], ou US$ 58,85 por módulo de 550 W [CALCULADO]. Vitrines do Alibaba: US$ 0,08 a 0,13 por watt, com pedido mínimo de 5.000 a 20.700 W (9 a 38 módulos) [P3].
- **Brasil:** OSDA 550 W por **R$ 869,99** à vista (Pichau) [P4]; Jinko 550 W por R$ 1.140 (classificado); Maxeon 550 W por R$ 1.350 (Mercado Livre) [P4]. Datas dos anúncios não informadas; vistos em 17/11/2026.
- **Custo posto do exemplo:** R$ 633 por módulo com ICMS isento; R$ 796 sem a isenção. Ganho possível em 14 módulos: R$ 1.000 a R$ 3.300, menor que os custos fixos do embarque (R$ 7.714,50).
- **Barreiras:** Inmetro (item 1 da seção 3). II de 25%.
- **Prazo:** Brasil, pronta entrega; China, 75 a 120 dias [SUPOSTO].
- **Recomendação: COMPRAR NO BRASIL.** Já vem com registro no Inmetro, nota fiscal e garantia local.

### 4.2 Unidade condensadora ou compressor de velocidade variável, 3 a 8 kW de frio

- **China (FOB), preços de vitrine:**
  - Unidade condensadora "full DC inverter" de 5 HP, marca FLAND: **US$ 1.250 a 1.380**. O trecho **não confirma o gás** [P5].
  - Unidades inverter de 2 a 7 HP para câmara: **US$ 1.143 a 8.000** por conjunto, FOB (Made-in-China); gás não informado [P5].
  - Unidade de velocidade fixa em R404A, para comparação: US$ 1.677 a 1.899 [P5].
  - Unidade pequena em corrente contínua 12/24/48 V, R134a ou R290 (RIGID): US$ 390. Muito menor que o necessário [P5].
  - Fabricante chinês com unidade condensadora externa em R290 exposta em feira (Boyard): existe, **sem preço** [P5].
- **Não encontrei** anúncio que reúna tudo: R290 + inverter + 3 a 8 kW + alimentação pelos painéis + preço.
- **Brasil:** unidades de velocidade fixa: Danfoss OP-HJZ019, 220 V trifásico, **R$ 5.069,90**; Danfoss HJZ064, 5,5 HP, R22/R404A, **R$ 9.882,72** (Magazine Luiza) [P5]. Unidade inverter ou em R290 à venda no Brasil (Danfoss Optyma Inverter, Embraco, Elgin): **preço não encontrado**; disponibilidade em R290 a confirmar pelo engenheiro.
- **Custo posto do exemplo:** FOB US$ 1.380 → **R$ 15.941**, mais custos fixos.
- **Barreiras:** gás (itens 3, 5 e 6); vaso de pressão (item 10); 60 Hz (item 11); assistência.
- **Recomendação: INDEFINIDO — é o único item em que importar pode se justificar.** Depende de o projeto térmico achar ou não um equivalente nacional. Se importar: pedir sem gás, com nitrogênio; exigir ficha técnica do compressor (marca, curva de capacidade) e do drive; comprar sobressalentes; via importadora por conta e ordem.

### 4.3 Drive solar (conversor de frequência com rastreador de máxima potência), 3 a 7,5 kW

- **China:** drive de bombeamento solar trifásico de 5,5 kW: **US$ 328,08** (loja inverter.com, preço de varejo); 5,5 kW "M-driver": **US$ 138 a 156**, saída trifásica 220 V, entrada recomendada de 450 a 600 V em corrente contínua [P6]. Modelos de 7,5 kW e 380 V (Veikong, RSI): sem preço; faixa de entrada de 486 a 750 V.
- **Brasil:** a WEG tem o CFW500 Solar Drive (catálogo) [P6]; **preço não encontrado**. Mercado Livre: kit de bombeamento solar de 7,5 cv com inversor de 380 V por R$ 3.569; de 5,5 cv por R$ 2.814 (marca SGV; o trecho não diz o que o kit inclui) [P6].
- **Custo posto do exemplo:** US$ 328 → **R$ 3.362** por importação formal; R$ 3.368 por remessa.
- **Atenção técnica (não é decisão minha):** esses drives são feitos para **bomba d'água**. Usá-los em compressor frigorífico exige confirmação do engenheiro e do fabricante do compressor.
- **Barreiras:** Inmetro indefinido (item 2).
- **Recomendação: INDIFERENTE no preço; preferir BRASIL** pela assistência e para fugir da dúvida do Inmetro. Se a condensadora importada vier com drive próprio, o drive vem junto.

### 4.4 Evaporador de teto para câmara

- **China:** preços de vitrine **não confiáveis**. Apareceram US$ 150 a 250 para um modelo "DL40" e US$ 6.690 a 14.600 para evaporadores "DD/DL/DJ" de um mesmo fornecedor, sem capacidade informada [P7]. A diferença de 50 vezes mostra que não servem de referência.
- **Brasil:** fabricantes nacionais com linha própria: Elgin (FXB+, de −35 a 10 °C, 1 a 6 ventiladores) e Mipal [P7]. **Preço não encontrado**.
- **NCM e alíquotas:** não encontradas.
- **Recomendação: COMPRAR NO BRASIL**, salvo se vier no mesmo embarque e do mesmo fabricante da condensadora. Há fabricação nacional, a peça é volumosa e frágil, e precisa de motor em 60 Hz.

### 4.5 Bateria LiFePO4 pequena (1 a 5 kWh)

- **China:** 51,2 V 100 Ah (5,12 kWh), de rack: **US$ 768** de 1 a 9 peças (SunPlus, Alibaba); **US$ 399 a 999** (Joypo); € 523 em catálogo europeu [P8]. Um fabricante exige pedido mínimo de 50 unidades [P8].
- **Brasil:** existem Elgin BAT-48V-5KWH (5 kWh, 5 anos de garantia), Unipower UPLFP48-100 e Intelbras EBL 4800 [P8]. **Preço não encontrado.** Registro no Inmetro desses modelos: não confirmado; a GoodWe anunciou registro de um modelo de 51,2 V [P8].
- **Custo posto do exemplo:** US$ 768 → **R$ 8.331**, sem a sobretaxa de carga perigosa.
- **Barreiras:** Inmetro (item 1) e lítio (item 7).
- **Recomendação: COMPRAR NO BRASIL.**

### 4.6 Controlador (CLP ou placa)

- **China:** preço de CLP chinês **não levantado** nesta fase.
- **Brasil:** preço **não encontrado**. Referência europeia: Siemens LOGO! 8 por € 132 a 148 [P9]; a linha LOGO! 9 foi anunciada para 01/04/2026.
- **Custo posto do exemplo:** CLP de US$ 200 → R$ 1.984.
- **Barreiras:** Anatel se tiver Wi-Fi (item 8).
- **Recomendação: COMPRAR NO BRASIL.** O valor é pequeno e a premissa do projeto pede que um eletricista local consiga manter. Se o programador escolher placa ESP32, usar módulo com homologação Anatel [F34].

### 4.7 Painéis isotérmicos de poliuretano

- **China (FOB):** 100 mm: em geral **US$ 8,50 a 25 por m²**; alguns anúncios, US$ 19 a 40. Pedidos mínimos de 100 m² a 20.000 m² [P10].
- **Brasil:** referência de orçamento público de Sergipe (ORSE): painel de poliuretano de 100 mm para câmara, **R$ 610,98 por m²** de material (data não informada); referência nacional SINAPI de maio de 2026 para painel de parede de 70/80 mm: **R$ 292,61 por m²** [P10]. Fabricantes: Dânica (FrigoPainel, 50 a 200 mm), Kingspan Isoeste [P10]. Preço de fabricante: não encontrado.
- **Conta de exemplo** [CALCULADO sobre hipóteses]: caixa do tamanho de um contêiner de 20 pés, 6,0 × 2,4 × 2,6 m: paredes 2 × (6,0 + 2,4) × 2,6 = 43,7 m²; teto 14,4 m²; piso 14,4 m²; total 72,5 m². A US$ 20 por m²: US$ 1.450. Volume com embalagem: 10 m³ [SUPOSTO] × US$ 150 = US$ 1.500 de frete. **O frete custa tanto quanto a mercadoria.** Com II entre 12,6% e 14% e IPI entre 0% e 5% [SUPOSTO — alíquotas não encontradas]: R$ 27.000 a 28.600, ou **R$ 373 a 394 por m²**, mais custos fixos.
- **Recomendação: COMPRAR NO BRASIL.** O preço importado cai dentro da faixa brasileira, com risco de avaria e sem assistência.

### 4.8 Contêiner reefer de 20 pés

- **Usado, no Brasil:** anúncios no MF Rural: **R$ 20.000** (Arealva-SP, precisa de revisão no motor) e **R$ 30.000** (Santos-SP, revisado), frete por conta do comprador; faixa geral de um vendedor de Santos: R$ 9.900 a R$ 40.000 [P11]. Nenhum anúncio em Recife ou Suape apareceu.
- **Usado, no exterior:** US$ 3.500 a 6.500 (página do Alibaba, sem data); na Alemanha, € 5.250 (Daikin 2013) e € 8.950 (Carrier 2017) [P11].
- **Novo:** na Alemanha, **€ 19.700 a 21.500** (2026, máquina Thermo King) [P11]. Preço FOB China de reefer novo: **não encontrado**.
- **Custo posto do exemplo (usado importado):** US$ 5.000 + US$ 3.500 de frete → **R$ 78.334**, contra R$ 20.000 a 30.000 no Brasil.
- **Barreiras:** licença de bem usado (item 9); gás da máquina (itens 3 e 4).
- **Recomendação: COMPRAR NO BRASIL.** Um reefer usado à venda aqui já foi nacionalizado. Exigir do vendedor a nota fiscal e a comprovação de nacionalização [VALIDAR COM DESPACHANTE].
- Observação para os projetistas: se o projeto usar só a **caixa isolada** do reefer e trocar a máquina, o gás original precisa ser recolhido por profissional. [VALIDAR COM PROFISSIONAL HABILITADO]

### 4.9 Conjunto pronto de "solar cold room"

Ver seção 5.

### 4.10 Quadro-resumo preliminar

| Categoria | Multiplicador FOB → posto | Brasil x China (ordem de grandeza) | Barreira principal | Recomendação provisória |
|---|---|---|---|---|
| Módulos | 1,9 a 2,4 | R$ 870 a 1.350 x R$ 633 a 796 | Inmetro, II de 25% | Brasil |
| Condensadora / compressor inverter | 2,0 (1,5 a 1,7 para compressor avulso) | Fixa: R$ 5.070 a 9.883; inverter: não encontrado x R$ 15.941 | Gás, NR-13, assistência | **A decidir na fase 2** |
| Drive solar | 1,8 | R$ 2.800 a 3.600 (kits) x R$ 3.362 | Inmetro indefinido | Brasil (indiferente no preço) |
| Evaporador | não calculado | não encontrado | 60 Hz, volume | Brasil |
| Bateria LiFePO4 | 1,9 + sobretaxa | não encontrado x R$ 8.331 | Inmetro, lítio | Brasil |
| CLP | 1,8 | não encontrado | Anatel, manutenção | Brasil |
| Painéis PU | cerca de 3,3 | R$ 293 a 611/m² x R$ 373 a 394/m² | Frete, avaria | Brasil |
| Reefer usado | 2,8 | R$ 20.000 a 30.000 x R$ 78.334 | Licença de usado, gás | Brasil |
| Conjunto pronto | 2,3 | sem equivalente x cerca de R$ 194.000 (hipótese) | Tudo acima, junto | Só para lote; ver seção 5 |

---

## 5. Alternativa "conjunto pronto"

### 5.1 O que os chineses anunciam

| Anúncio | Preço de vitrine | O que o trecho diz | Fonte |
|---|---|---|---|
| "20ft container solar power mobile cold room" (Alibaba) | US$ 1.566 (1 a 2 conjuntos) a US$ 1.488 (6 ou mais) | Preço baixo demais para incluir painéis e baterias; provavelmente só a câmara ou só a máquina | [P12] |
| CSCPOWER "solar cold room" | US$ 3.500; US$ 3.100 para 3 ou mais | Não diz se inclui o sistema solar | [P12] |
| Câmara modular 20FT/40HQ (Bestsuppliers) | US$ 8.899 (1), US$ 6.880 (5), US$ 5.660 (10) | Não menciona solar | [P12] |
| Guia de mercado | US$ 8.000 a 60.000 ou mais | Faixa geral para contêiner frigorífico solar, conforme painéis e baterias | [P12] |
| Century Sea, Jialiang, Sino-Cold, Hugecool | sem preço | Câmaras solares com compressores Copeland, Bitzer etc.; uma com monobloco "full DC inverter" de 1,5 HP | [P12] |
| Henan Hongtu | sem preço | Com **baterias** para a noite | [P12] |
| Haier Medical HWIC-10M | sem preço | "Solar direct driven", para vacinas | [P12] |

A ligação entre cada preço e cada anúncio foi feita pelo resumo da busca e pode estar trocada. **Conferir abrindo os anúncios.**

### 5.2 O que não achei

- **Nenhum fornecedor que declare usar banco de gelo no lugar de baterias** com acionamento direto pelos painéis. O que existe publicado sobre isso é pesquisa universitária chinesa (Universidade Normal de Yunnan) [P12].
- Nenhum preço de unidade condensadora solar em corrente contínua na faixa de 3 a 8 kW de frio com especificação completa.

### 5.3 Conjunto pronto x montar por componentes

| Critério | Conjunto pronto da China | Montar aqui |
|---|---|---|
| Atende à ideia do projeto (gelo, sem banco grande de baterias) | Não encontrado | Sim, é o próprio projeto |
| Preço | Vitrine de US$ 3.000 a 60.000; custo posto por volta de 2,3 vezes; exemplo de US$ 15.000 → R$ 194.000 [CALCULADO sobre hipótese] | A fechar na fase 2 |
| Barreiras | **Todas ao mesmo tempo:** módulos, inversor e bateria precisam de Inmetro; gás; lítio; Anatel. Um item irregular pode reter o contêiner inteiro [SUPOSTO] | Cada item resolvido na compra |
| Classificação fiscal | Itens diferentes dentro do contêiner são declarados cada um na sua NCM [VALIDAR COM DESPACHANTE] | — |
| Ficha técnica | Em geral fraca; capacidade declarada sem a condição de teste (40 °C lá fora?) | Projeto com contas conferíveis |
| Assistência | Nenhuma no sertão | Frigorista e eletricista locais |
| Prazo | 75 a 120 dias [SUPOSTO] | Depende do item mais demorado |

**Caminho intermediário, a levar ao dono:** pedir a um fabricante chinês apenas a **parte frigorífica** (condensadora inverter + evaporador + quadro, sem gás, sem módulos e sem bateria), feita sob a especificação do projeto, e comprar no Brasil tudo o que tem barreira. Isso tira do embarque os itens com Inmetro e lítio.

---

## 6. Um protótipo x lote de 10

| Assunto | 1 protótipo | Lote de 10 |
|---|---|---|
| Via | Comprar no Brasil; se algo vier de fora, importadora por conta e ordem, ou remessa para peça pequena | Importação formal própria ou por importadora, em contêiner fechado |
| Custos fixos | R$ 7.700 [SUPOSTO] sobre uma compra de R$ 15.000 a 40.000: pesam 17% ou mais | Os mesmos custos divididos por 10 |
| Frete | Carga fracionada, por m³, mais manuseio e risco de avaria | Contêiner de 20 ou 40 pés: US$ 2.150 a 8.300 [F18] |
| Quantidade mínima | Muitos fabricantes não vendem uma unidade, ou vendem como "amostra" mais cara. Exemplos: baterias, 50 unidades; painéis, 100 m² ou mais; módulos, 5.000 W ou mais [P3][P8][P10] | Atendida |
| Módulos (140 unidades, 77 kWp) | Brasil | Ainda Brasil, provavelmente: II de 25% e Inmetro continuam; a cota de 9,6% não é para esse porte [F3]. Pedir preço de distribuidor por palete |
| Parte frigorífica | A decidir (4.2) | Aqui a importação passa a fazer sentido: dá para pedir fabricação sob especificação e inspeção na fábrica |
| Painéis isotérmicos | Brasil | Reavaliar: 725 m² enchem um contêiner |
| Certificações | Não compensa certificar nada | Pode compensar registrar no Inmetro um modelo próprio [VALIDAR] |
| Redução de imposto | Não | Pedido de ex-tarifário (redução do II para bem sem similar nacional) passa a valer a pena. Prazo e chance: não levantados |
| Habilitação | Modalidade de entrada | Dez conjuntos de US$ 15.000 chegam ao teto de US$ 150 mil por semestre da modalidade Limitada [F23] |
| Câmbio | Risco pequeno em valor | Risco relevante |
| Imposto estadual | — | Verificar com contador incentivos de Pernambuco para importação por Suape. **Não levantado** |

**Regra prática proposta:** o protótipo serve para descobrir **o que importar no lote**. Comprar aqui agora, anotar preço e prazo de cada item, e só então cotar o lote com a especificação já testada.

---

## 7. Riscos e como reduzir

| Risco | Como aparece | Como reduzir |
|---|---|---|
| **Ficha técnica não confiável** | Capacidade dada sem a condição (temperatura externa e de evaporação); "inverter" que é só partida suave; gás diferente do anunciado | Exigir folha de dados com marca e modelo do compressor e a curva na condição do projeto (40 °C externos); exigir relatório de teste da unidade antes do embarque |
| **Qualidade de fabricação** | Solda fria, vazamento, fiação subdimensionada, motor de 50 Hz | Inspeção antes do embarque por empresa independente (SGS, Bureau Veritas, TÜV ou similar; custo não levantado); comprar amostra antes do lote |
| **Peça de reposição** | Placa do drive queima e a câmara para na safra | Comprar sobressalentes no mesmo embarque; preferir compressor e controles de marca com distribuidor no Brasil |
| **Câmbio** | O dólar foi de R$ 5,51 para R$ 5,65 em quatro dias de novembro de 2026 [F22]; todos os impostos são calculados sobre o valor em reais do dia do registro | Reservar 10% de folga [SUPOSTO]; fechar câmbio junto com o pagamento |
| **Mudança de imposto no meio do caminho** | 2026 teve aumento, recuo e cotas; 2027 troca PIS/Cofins pela CBS | Refazer a conta com o despachante na semana do embarque |
| **Retenção na alfândega** | Falta de licença, NCM errada, valor declarado abaixo do real | Classificação e licenças definidas pelo despachante **antes** do embarque; fatura com o valor real; nunca aceitar proposta de "declarar mais barato" |
| **Golpe** | Fornecedor some após o sinal; troca de conta bancária por e-mail falso; mercadoria diferente da amostra | Verificar a empresa (licença comercial, tempo de plataforma, chamada de vídeo na fábrica); usar a garantia de pagamento da plataforma; pagamento em duas partes (sinal de 30% e saldo contra documentos de embarque) [SUPOSTO — prática comum]; nunca pagar a conta de pessoa física |
| **Avaria no transporte** | Evaporador amassado, painel riscado | Embalagem em caixa de madeira; seguro de carga; conferir e fotografar no recebimento |
| **Garantia que não se executa** | Fabricante responde, mas não paga a nova importação | Tratar garantia chinesa como desconto: só importar o que continua vantajoso sem ela |
| **Equipamento irregular em operação** | Bateria ou inversor sem registro; rádio sem homologação; vaso sem documentação | Seção 3: resolver antes da compra |

---

## 8. O que falta para a fase 2

Para fechar item a item (opção Brasil x opção importada, custo posto, prazo, risco e a tabela final de compras), preciso dos seguintes dados dos documentos de projeto.

**Do projeto térmico (01):**
1. Capacidade frigorífica de projeto (kW) e a condição: temperatura externa, temperatura de evaporação e de condensação.
2. **Gás escolhido** e carga estimada em kg (define Ibama, carga perigosa e NR-13).
3. Tipo de máquina: unidade condensadora completa, compressor avulso para montar, ou monobloco. Faixa de rotação.
4. **Capacidade do compressor em frigorias/h ou kW**: acima ou abaixo de 4.700 frigorias/h (5,5 kW) muda o imposto de importação de zero para 18% [F27].
5. Evaporador: capacidade, vazão de ar, espaçamento de aletas, tipo de degelo, tensão dos ventiladores.
6. Banco de gelo: tipo (serpentina em tanque, placas), volume, materiais, se há bomba e trocador.
7. Volume e pressão de cada vaso de pressão.
8. Envoltória escolhida: reefer usado, contêiner seco isolado ou painéis; área e espessura.
9. Modelo, fabricante e preço de cada opção brasileira encontrada, e a "especificação para cotação".

**Do projeto elétrico (02):**
10. Número e potência dos módulos; tensão da fileira (define a faixa de entrada do drive).
11. Drive: potência, tensão de saída, se é o do fabricante do compressor ou genérico.
12. Bateria: tensão, capacidade (kWh), química; cargas de 24 h (inclui Starlink).
13. Há inversor comum para cargas auxiliares? Potência e tensão.
14. Proteções, cabos, estrutura de fixação: lista com quantidades.

**Do projeto de controle (03):**
15. CLP ou ESP32; modelo; se tem Wi-Fi ou outro rádio (Anatel).
16. Lista de sensores, válvulas (expansão eletrônica?), contatores, interface.

**Do dono:**
17. Vai abrir **empresa (CNPJ)** para o projeto? Sem isso, importação formal e certificações ficam praticamente fora.
18. Intenção de lote: é para planejar 10 unidades ou só o protótipo?
19. Aceita **prazo de 3 a 4 meses** para os itens importados?
20. Aceita equipamento sem assistência técnica no Brasil na peça central (compressor e drive)?

**O que eu farei na fase 2 com esses dados:** pedir a despachante a classificação e as licenças de cada item; cotar por escrito pelo menos três fornecedores chineses para os itens em que a importação seguir de pé; cotar frete para Suape e Pecém; montar a tabela final (item, origem, modelo, fabricante, quantidade, preço posto, link, prazo) e a lista de pendências para humanos.

---

## 9. Fechamento da fase 1

### Decisões tomadas (provisórias, sobre origem da compra)

- Protótipo: comprar no Brasil módulos, bateria, CLP, evaporador, painéis e reefer usado.
- Único item em aberto para importação no protótipo: unidade condensadora ou compressor de velocidade variável.
- Se houver importação: por importadora (conta e ordem), sem gás, com CNPJ.

### Conflitos entre agentes

Nenhum registrado nesta fase: os outros projetos ainda não existem. Dois pontos **podem virar conflito** e ficam anotados para o dono mediar quando surgirem:
1. Se o engenheiro de refrigeração especificar uma máquina que só existe importada, ou o equivalente importado tiver gás, tensão ou capacidade diferente da especificada.
2. Se o integrador solar especificar módulo, inversor ou bateria de modelo sem registro no Inmetro.

### Pendências para humanos

| Pendência | Quem |
|---|---|
| Confirmar NCM e alíquota de cada item na tarifa oficial vigente no dia | Despachante |
| Dizer se equipamento pré-carregado com HFC precisa de licença e cota do Ibama | Despachante e Ibama |
| Dizer se drive solar para compressor entra na Portaria Inmetro nº 140/2022 | Despachante e Inmetro |
| Dizer se a isenção de ICMS de módulos vale na importação em Pernambuco | Despachante ou contador |
| Pessoa física pode ou não importar sem Radar neste caso | Despachante |
| Tipo de empresa, regime tributário, incentivos de PE, efeitos da reforma em 2027 | Contador |
| Vasos de pressão importados e NR-13; segurança do R290 | Engenheiro habilitado |
| Abrir CNPJ; protótipo ou lote; aceitar prazo e falta de assistência | Dono |
| Cotações de frete China–Suape e China–Pecém, taxas de terminal, caminhão até Petrolina | Agente de carga |

### O que não consegui verificar

- Texto oficial de qualquer norma citada (acesso às páginas bloqueado).
- Lista consolidada das alíquotas após as Resoluções Gecex nº 852, 853 e 866 de 2026.
- Alíquotas de: evaporador (8418.99.00), painel isotérmico (7308.90.90), IPI do módulo.
- Se inversores e baterias tiveram mesmo o imposto de importação elevado para 20% em 2026.
- Regra do Ibama para equipamento pré-carregado; regra da ANP para propano refrigerante.
- Valor atual da Taxa Siscomex; taxas do terminal de Suape; honorários reais de despachante em Pernambuco; taxa de importadora.
- Tempo de trânsito e existência de linha direta China–Suape em 2026.
- Preço no Brasil de: unidade condensadora inverter ou em R290, evaporador, bateria LiFePO4, CLP, drive WEG solar, painel isotérmico de fabricante.
- Preço FOB confiável de: evaporador, reefer novo, CLP chinês, unidade condensadora R290 inverter com especificação completa.
- Qualquer fornecedor chinês de câmara solar com banco de gelo.

### Dados de interface para as outras disciplinas

- **Engenheiro de refrigeração:** informar capacidade do compressor em frigorias/h; carga de gás em kg; volume dos vasos. Se cogitar equipamento importado, especificar "sem gás, com nitrogênio" e "60 Hz".
- **Integrador solar:** escolher módulos, inversores, controladores e baterias **com registro no Inmetro**; informar tensão da fileira para a cotação do drive.
- **Programador:** qualquer placa com rádio precisa de homologação Anatel; preferir módulo já homologado.
- **Logística:** prazo de 75 a 120 dias para qualquer item importado [SUPOSTO]; porto de entrada a definir entre Suape e Pecém.

---

## Fontes

Todas apareceram nos resultados da busca em 17/11/2026. **Nenhuma foi aberta na íntegra.**

**Impostos, regras e logística**

- [F1] Canal Solar — imposto de importação de painéis solares (25%, Resolução Gecex nº 666): https://canalsolar.com.br/imposto-de-importacao-paineis-solares/
- [F2] Canal Solar — cotas do imposto de importação de painéis: https://canalsolar.com.br/cotas-imposto-importacao-paineis-solares/
- [F3] Portaria Secex nº 522, de 14/07/2026 (LegisWeb): https://www.legisweb.com.br/legislacao/?id=498202
- [F4] Canal Solar — aumento para geradores fotovoltaicos; inversores e baterias fora da lista publicada: https://canalsolar.com.br/governo-aumento-imposto-geradores-fotovoltaicos/
- [F5] Canal Solar — aumento do imposto de inversores e baterias: https://canalsolar.com.br/governo-aumento-imposto-importacao-inversores-bess/ e https://canalsolar.com.br/inversores-bess-impactados-novas-aliquotas-importacao/
- [F6] Machado Meyer — Resoluções Gecex 852 e 853/2026: https://www.machadomeyer.com.br/pt/inteligencia-juridica/publicacoes-ij/tributario-ij/resolucoes-gecex-852-e-853-26-pontos-de-atencao-para-importadores
- [F7] Resolução Gecex nº 852/2026 (LegisWeb, DOU de 05/02/2026): https://www.legisweb.com.br/legislacao/?id=490417 ; notícia: https://www.noticiasagricolas.com.br/noticia/415876
- [F8] Recuos parciais: https://tagdlaw.com.br/gecex-concede-ex-tarifarios-bk-e-bit-e-volta-atras-na-elevacao-da-lista-de-excecoes-para-alguns-itens-de-informatica/ ; https://www.mattosfilho.com.br/unico/reducao-tributaria-bens-capital/
- [F9] PIS/Cofins-Importação, LC nº 224/2025 e IN RFB nº 2.305/2026: https://www.legisweb.com.br/noticia/?id=33080 ; https://tagdlaw.com.br/pis-e-cofins-importacao-alteracoes-decorrentes-da-lc-no-224-2025-e-in-rfb-no-2-305-2026/
- [F10] DHL — reforma tributária na importação: https://www.dhl.com/discover/pt-br/assuntos-regulatorios/reforma-tributaria-importacao
- [F11] Contábeis — reforma tributária 2026, fase de transição: https://www.contabeis.com.br/noticias/73889/reforma-tributaria-2026-veja-o-que-muda-na-fase-de-transicao/
- [F12] IOB — transição da reforma: https://noticias.iob.com.br/reforma-tributaria-transicao/
- [F13] Tax Group — ICMS de Pernambuco, 20,5%: https://www.taxgroup.com.br/intelligence/icms-pe-tabela-atualizada/
- [F14] Diario de Pernambuco, 14/05/2026 — ICMS de 17% em compras internacionais: https://www.diariodepernambuco.com.br/economia/2026/05/11714254-taxa-das-blusinhas-chega-ao-fim-mas-icms-nos-estados-continua-entenda.html
- [F15] Fazcomex — ICMS na importação: https://www.fazcomex.com.br/importacao/icms-na-importacao/
- [F16] Convênio ICMS nº 101/97 (LegisWeb): https://www.legisweb.com.br/legislacao/?id=14712
- [F17] Suaid Global — frete China–Brasil, AFRMM de 8%: https://suaidglobal.com/pt-br/insights/china-to-brazil-shipping-cost/
- [F18] Guelcos — faixas de frete marítimo: https://guelcos.com.br/?p=10253
- [F19] MercoPress — frete a US$ 10.000 por contêiner em fevereiro de 2026: https://en.mercopress.com/tags/luigi-ferrini
- [F20] Taxa Siscomex: https://www.fazcomex.com.br/npi/duimp-taxa-de-utilizacao-do-siscomex/ ; https://toexceed.com.br/blog/2026/09/12/taxa-siscomex-na-importacao-o-que-e-como-funciona-e-como-calcular/
- [F21] Despachante: https://toexceed.com.br/blog/?p=9180 ; https://www.dhl.com/discover/pt-br/conselhos-de-logistica/despachante-aduaneiro
- [F22] Câmbio: https://boca.com.br/economia/dolar/cotacao-dolar-hoje-15-11-2026 ; https://brasil61.com/n/dolar-hoje-fecha-em-leve-alta-a-r-5-51-apos-oscilar-entre-queda-e-valorizacao-bras2617447
- [F23] Radar: https://www.dhl.com/discover/pt-br/conselhos-de-logistica/radar-siscomex ; https://taxup.com.br/solucoes/direito-aduaneiro/radar-siscomex/ ; https://diretolegaliza.com/?p=9626 ; https://www.migalhas.com.br/depeso/364476/radar-conheca-suas-modalidades-e-como-se-habilitar-para-importar
- [F24] Remessa Conforme: https://www.dhl.com/discover/pt-br/assuntos-regulatorios/remessa-conforme ; https://blog.econeteditora.com.br/remessa-conforme-o-que-muda-com-a-portaria-mf-1-342-2026/ ; https://www.diariodepernambuco.com.br/colunas/diario-economico/2026/09/11723263-fim-da-taxa-das-blusinhas-vai-alem-extincao-definitiva-da-aliquota-de-20.html
- [F25] Conta e ordem x encomenda: https://www.dhl.com/discover/pt-br/conselhos-de-logistica/importacao-por-conta-e-ordem ; https://toexceed.com.br/blog/2025/12/30/importacao-por-conta-e-ordem-x-encomenda-qual-escolher/
- [F26] Importação por pessoa física: https://www.meucontadoronline.com.br/blog/importacao-pessoa-fisica/ ; https://blog.econeteditora.com.br/como-pessoas-fisicas-podem-importar-mercadorias/
- [F27] Alíquotas por NCM (sites particulares): https://buscadorncm.com.br/ncm/84143011 ; https://buscadorncm.com.br/ncm/84143019 ; https://buscadorncm.com.br/ncm/84186940 ; https://buscadorncm.com.br/ncm/85044050 ; https://buscadorncm.com.br/ncm/85076000 ; https://buscadorncm.com.br/ncm/85371020 ; https://buscadorncm.com.br/ncm/86090000 ; https://ncm.fazcomex.com.br/84186999-outros/ ; https://ncm.fazcomex.com.br/85044050-conversores-eletronicos-de-frequencia-para-variacao-de-velocidade-de-motores-eletricos/
- [F28] Classificação de painéis isolantes (Cosit 98.443): https://tributodevido.com.br/portal/classificacao-fiscal-de-paineis-isolantes-termicos/
- [F29] Inmetro: Portaria nº 140/2022: https://www.legisweb.com.br/legislacao/?id=468088 ; Portaria nº 515/2023: https://www.normasbrasil.com.br/norma/portaria-515-2023_451929.html ; https://canalsolar.com.br/portaria-do-inmetro-regulamenta-inversores-hibridos-no-brasil/
- [F30] Ibama: https://www.normasbrasil.com.br/norma/instrucao-normativa-251-2023_453588.html ; https://www.gov.br/ibama/pt-br/acesso-a-informacao/analise-de-impacto-regulatorio-air/relatorios-de-analise-de-impacto-regulatorio-air/arquivos/20240307_SEI_Ibama_17836111_Nota_Tecnica_79_2023_Corem_CGqua_Diqua.pdf ; https://www.gov.br/ibama/pt-br/assuntos/emissoes-e-residuos/emissoes/arquivos/20230519_Manual_Sistema_Protocolo_Montreal.pdf ; https://www.gov.br/ibama/pt-br/assuntos/notas/2025/comunicado-reserva-tecnica-de-hcfc-22-em-2025-esta-esgotada-no-brasil/20250508_SEI_23268623_Comunicado.pdf
- [F31] Ministério do Meio Ambiente — boletim sobre R-290: https://www.gov.br/mma/pt-br/assuntos/mudanca-do-clima/ozonio/boletim-informativo-aplicao-do-r-290-em-equipamentos-de-refrigerao-comercial.pdf
- [F32] Swire Shipping — máquinas frigoríficas no código IMDG (UN 3358, disposição 291): https://www.swireshipping.com/information/?p=14968
- [F33] Baterias de lítio por mar: https://www.maersk.com/logistics-explained/transportation-and-freight/2024/04/04/shipping-batteries ; https://www.chinaimportal.com/?p=16097
- [F34] Anatel: https://tecnoblog.net/noticias/anatel-regras-homologacao-importados/ ; https://tecnoblog.net/noticias/anatel-avanca-em-alianca-com-receita-contra-celulares-irregulares/ ; https://teletime.com.br/04/03/2026/anatel-apreende-impressoras-parana/ ; certificado de módulo ESP32: https://www.espressif.com/sites/default/files/ESP32-S3-WROOM-1%20Anatel%20Certification.pdf
- [F35] NR-13: https://www.guiatrabalhista.com.br/legislacao/nr/nr13.htm ; https://webarcondicionado.com.br/nr-13-norma-protege-profissionais-de-climatizacao-e-refrigeracao
- [F36] Bens usados: https://www.conjur.com.br/2024-abr-16/importacao-de-bens-usados-tratamento-aduaneiro-e-tributario/ ; https://www.gov.br/siscomex/pt-br/legislacao/PortariaSecex249de2023TextoCompilado.pdf
- [F37] Rotas marítimas para o Nordeste: https://www.autodata.com.br/noticias/2025/05/15/nova-rota-maritima-devera-intensificar-importacoes-da-china/88251/ ; https://www.brasilagro.com.br/conteudo/ceara-e-china-tem-nova-rota-maritima-direta-em-meio-a-guerra-comercial.html ; https://movimentoeconomico.com.br/geral/redacao/2026/05/06/solve-shipping-inicia-mapeamento-logistico-internacional-em-suape/

**Preços**

- [P1] pv magazine, 23/10/2026 — índice OPIS de módulos, US$ 0,107/W FOB China: https://www.pv-magazine.com/2026/10/23/china-solar-module-prices-steady-as-proposed-price-floors-meet-skepticism/
- [P3] Vitrines de módulos de 550 W: https://pt.accio.com/plp/placas-solar-550w-pre%C3%A7o ; https://www.made-in-china.com/products-search/hot-china-products/550w_Half_Solar_Panel.html
- [P4] Módulos no Brasil: https://www.pichau.com.br/painel-solar-fotovoltaico-osda-550w-2279x1134x35mm-oda550-36-mh ; https://lista.mercadolivre.com.br/placas-para-energia-solar-avulsa ; https://www.solutudo.com.br/classificados/painel-solar-fotovoltaico-jinko-550w-607443 ; alta de preços e fim da devolução de imposto chinesa: https://canalsolar.com.br/tag/preco-de-paineis-solar-em-2026/
- [P5] Unidades condensadoras: FLAND 5 HP: https://china.org.ru/product/1600966804570 ; inverter 2 a 7 HP e R404A: https://m.made-in-china.com/hot-china-products/Remote_Condensing_Unit.html ; RIGID: https://www.madeinchina.com/mall/show-Compact-12V-DC-Refrigeration-Condensing-Unit-for-Efficient-Cooling_644684.html ; Boyard R290: https://chillventa.de/en/exhibitors-products/b/boyard-compressor/r290-outdoor-condensing-unit ; Brasil (Danfoss): https://magazineluiza.com.br/busca/unidade+condicionadora
- [P6] Drives solares: https://www.inverter.com/5-5kw-three-phase-solar-pump-inverter ; https://china.org.ru/product/1601192974525 ; https://veikong-electric.com/?p=4550 ; Brasil: https://lista.mercadolivre.com.br/kit-energia-solar-completo-trifasico ; catálogo WEG: https://static.weg.net/medias/downloadcenter/h22/hfd/WEG-solucao-solar-para-agronegocio-catalogo-50123210-pt.pdf
- [P7] Evaporadores: https://www.madeinchina.com/mall/show-Dd-Dl-DJ-Series-Evaporative-Cold-Room-Unit-Air-Cooler_27613.html ; https://china.org.ru/product/62598552415 ; Elgin FXB+: https://www.acrlatinoamerica.com/en/2020060916120/products/refrigeration/low-profile-evaporator.html
- [P8] Baterias: https://www.alibaba.fr/product-detail/SunPlus-SU5-0-X-51-2V_1601662280388.html ; https://joypo-e.company.frbiz.com/p117110263-server-rack-lfp-solar-storage-lithium-battery-pack-48v-100ah-200ah.html ; https://www.enfsolar.com/pv/storage-system-datasheet/14574 ; https://www.redwaypower.com/?p=17258 ; Brasil: https://content.elgin.com.br/assets/arquivos/ELGIN-Datasheet-Elgin-BAT-48V-5KWH.pdf ; https://backend.intelbras.com/pt-br/bateria-recarregavel-li-ion-48-v-100-ah-ebl-4800 ; https://download.aldo.com.br/pdfprodutos/Produto339501IdArquivo28080.pdf ; https://canalsolar.com.br/bateria-lynx-goodwe-registro-inmetro/
- [P9] CLP: https://aio.lv/en/product--siemens-6ed1052-1cc08-0ba2--12464950.md ; https://control.com/news/siemens-introduces-logo-9-next-generation-logic-controllers/
- [P10] Painéis: https://changxue.en.alibaba.com/product/62190173435-210626777/100mm_thick_cold_room_pu_insulated_panel.html ; https://m.made-in-china.com/hot-china-products/Pu_Sandwich_Panel.html ; https://coldroomcn.en.made-in-china.com/product/FOUnyrlEbAkq/China-PU-PUR-PIR-Sandwich-Panel-Price-for-Cold-Storage-Room.html ; https://www.tradekey.com/product_view/100mm-Pu-Insulation-Panel-With-Color-Steel-Sheet-6057030.html ; Brasil: https://orcamentor.com/orse/composicoes/ORSE-9438/ ; https://orcamentor.com/insumo/39518/ ; https://www.aecweb.com.br/produto/frigopainel/34683
- [P11] Reefer: https://www.mfrural.com.br/busca/reefer-20-pes ; https://alibaba.com/showroom/used-refrigerated-containers-for-sales.html ; anúncios na Alemanha: https://www.truckscout24.com/tsp/ts-207-63-242 e https://www.truckscout24.com/tsp/ts-225-55-057
- [P12] Câmaras solares: https://www.thesolarcontainer.com/?p=1356 ; https://www.alibaba.com/product-detail/20ft-container-Price-Solar-Power-Mobile_1601152957257.html ; https://cscpower.en.alibaba.com/product/60405928336-802173885/solar_cold_room_for_fish_meat_vegetable_ice_store_in_big_promotion.html ; https://bestsuppliers.com/products/ueqsomt4loh3/walk-in-chiller-cold-room-solar-powered-cold-store-container-refrigerator ; https://www.cncsc.com/20ft-solar-cold-room-product/ ; https://www.directindustry.com/prod/henan-hongtu-machinery-manufacturing-co-ltd/product-4622252-2850864.html ; https://www.haiermedical.com/cold-freezer-room/solar-direct-driven-cold-room.html ; pesquisa sobre gelo no lugar de baterias: https://www.pv-magazine.com/2024/04/15/photovoltaics-for-cold-storage
