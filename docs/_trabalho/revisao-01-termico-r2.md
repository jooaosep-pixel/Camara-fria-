# Parecer de revisão, rodada 2 — `docs/01-projeto-termico.md` (anteprojeto, versão 2)

Revisor técnico independente. Data: 17/11/2026.
Base: `docs/00-premissas.md` com as decisões D1 a D6; parecer da rodada 1 em `docs/_trabalho/revisao-01-termico.md`.
Minhas contas: `docs/_trabalho/revisao_termico.py`, **parte C** (rodada 2), com a saída em `docs/_trabalho/revisao_termico_saida.txt`. O script continua independente do `termico.py` do autor.
Acesso à web: nesta rodada não tentei abrir sites de novo (na rodada 1 todos falharam por bloqueio de rede). Nada foi conferido na fonte por mim; vale o que digo na seção 0 do parecer da rodada 1.

## 1. Contas: revisor x autor (só manga a 12 °C, 5 t, recepção até 14 h, dia de 27 a 41 °C)

| Grandeza | Revisor (parte C) | Autor | Diferença | Explicação |
|---|---|---|---|---|
| Frio diário com folga de 10 % (UA 33, ar novo 10 m³/h) | **75,7 kWh** (79,4 com 25 m³/h de ar novo) | **82,2 kWh** | autor +8 % | Quase toda a diferença está na respiração (eu 12,9 kWh, ele 19,1). O meu modelo retira os lotes já frios da conta da respiração e por isso subestima um pouco; o dele é mais conservador. Invólucro (18,1), calor de campo (24,9 x 24,2) e porta batem. **Conta do autor aceita.** |
| Frio diário, recepção até 10 h | 74,7 kWh | 73,1 kWh | −2 % | Concordam. |
| Gelo gasto das 17 h às 7 h, recepção até 14 h | 30,7 kWh (constante de tempo de 6 h); 32,8 (8 h) | 35,9 kWh | autor +9 a +17 % | Constante de tempo da fruta, respiração e folga de 10 %. |
| COP, arquitetura (b), R513A, expansão direta, −7/+51 °C | 2,27 | 1,98 | autor −13 % | Os dois são estimativas sem catálogo; a do autor é mais conservadora. |
| COP, arquitetura (a), glicol, −10,5/+51 °C, com perda do inversor | 1,91 | 1,70 | autor −11 % | Idem. |
| **kWp mínimo, (b)** | **8,7** (irradiação de 5,8) a **10,7** (4,7) | **10** (+500 kg) | dentro da faixa | Concordam. |
| **kWp mínimo, (a)** | **10,3 a 12,7** | **12** (+500 kg) | dentro da faixa | Concordam. |
| **Gelo mínimo, recepção até 14 h** | **390 kg** (com 85 % de fração útil); 410 kg com 25 m³/h de ar novo | **500 kg** mínimo; **700 kg** de referência | autor +28 % | Mais noite (35,9 x 30,7 kWh) e o critério do autor de fechar em regime com o banco nunca vazio. Diferença de premissa, não de conta. |
| Banco (b), grades de cobre | 2,72 kg/m × 260 m = **706 kg**; 24 L de volume interno | 700 kg; 25 a 38 L | — | Bate. |

**Resultado: as duas contas convergem.** Arquitetura (b): 9 a 11 kWp e 400 a 500 kg; arquitetura (a): 10 a 13 kWp e 400 a 500 kg. O conjunto de referência do autor (12 kWp + 700 kg) tem folga real nas duas.

## 2. Situação dos achados da rodada 1 (conferida no texto e no script, não só na tabela 15.5)

| Nº | Gravidade (r1) | Situação | O que conferi |
|---|---|---|---|
| 1 | BLOQUEANTE | **Resolvido** | Seção 7.3: sem purgador, alívio ou vaso do glicol dentro da câmara; corte por evaporação a −13 °C; chave de fluxo; refratômetro; detector dentro da câmara se o aparelho usar R290. Na (b) só entra água na câmara e o gás não é inflamável. |
| 2 | BLOQUEANTE | **Resolvido no princípio, com erro novo** (N2) | Conta de 8 % em uma noite, ar novo, sensor, luz na porta e ventilação antes de entrar estão no texto, na carga (2,4 kWh) e nos testes. Mas a lógica dos setpoints não bate com a carga somada (N2). |
| 3 | BLOQUEANTE | **Aberto, agora declarado** | Ainda não há COP de catálogo, modelo de compressor nem orçamento (preço só em 5 de 16 linhas). O documento passou a se chamar anteprojeto e diz que não serve para contratar. Isso basta para um anteprojeto; para a execução continua bloqueante. |
| 4 | BLOQUEANTE | **Resolvido**, com ressalva (N3) | O script limita a potência da serpentina (K de 900 W/K com água a 3 °C) e a tabela 5.4 mostra o ar no máximo a 12,1 °C. Com uma serpentina só, ar a 12 °C e água a 3 °C, a capacidade de 8,5 kW é coerente com o pico de 6,0 kW. Ressalva: a água a 5–7 °C prometida à noite (11.1) não está no modelo. |
| 5 | BLOQUEANTE | **Resolvido no nível de anteprojeto** | Grades de cobre: 13 × 10 passes de 2 m, passo de 90 mm, vão de 27 mm entre cilindros, ancoragem (63 kgf), estrutura do tanque, base (cerca de 5,8 kPa no solo, valor baixo). Espirais de PE-RT: comprimento de 38,9 m por camada confere, raio mínimo de 150 mm. Detalhe em N5. O executivo fica com o engenheiro (seção 14.2), como deve ser. |
| 6 | IMPORTANTE | Resolvido | 8,7 kW na (a), declarado como insuficiente para o pico. |
| 7 | IMPORTANTE | Resolvido, com conflito revisto (seção 4) | — |
| 8 | IMPORTANTE | Resolvido | Na (b) não há P1; na (a), separador hidráulico; P2 com 8 m. |
| 9 | IMPORTANTE | Resolvido | Tanque de líquido com válvula de segurança na (b). |
| 10 | IMPORTANTE | Resolvido | Pressões em bar relativo com a saturação ao lado; válvula obrigatória; pressões de teste. Falta só a tabela do R513A (pendência 10, declarada). |
| 11 | IMPORTANTE | Resolvido por D3 | Detector junto ao aparelho; fontes de ignição a 1 m ou mais. |
| 12, 13 | IMPORTANTE | Resolvidos por D1 e D2 | — |
| 14 | IMPORTANTE | Resolvido | Marcação [CALCULADO sobre SUPOSTO] e faixas no resumo. |
| 15 | IMPORTANTE | Resolvido | Material de tubo definido por arquitetura. |
| 16 | IMPORTANTE | Resolvido | Motor de 220 V com inversor da classe 380 V; 400 V CC no mínimo; correntes. |
| 27 | IMPORTANTE | **Resolvido no que cabe a um anteprojeto** | Implantação, escopo por profissional e 12 testes de aceitação com critério. |
| 17 a 26 | MENOR | Resolvidos | Conferi 18 e 19 (63 L para 700 kg), 20 (12 °C em todo o texto), 21 (83 W/t) e 23 (ColdHubs retirado). |

## 3. Achados novos (introduzidos pela reescrita ou só visíveis agora)

| Nº | Documento / seção | Gravidade | O que está errado | Minha conta ou fonte | O que o autor deve fazer |
|---|---|---|---|---|---|
| N1 | 6.2–6.4, 12.3, "As três rotas" (Rota B) | **IMPORTANTE** | A bateria de apoio de 5 kWh "alimenta o compressor" (12.3), e a seção 6 calcula o frio que ela entrega com COP de 2,9. Mas na Rota B o compressor é acionado por um inversor de bombeamento que recebe 400 a 750 V CC dos painéis, enquanto a bateria citada é de 48 V (Elgin BAT-48V-5KWH). **Não existe caminho elétrico entre os dois** sem um inversor de 48 V para 220 V CA de pelo menos 2 a 4 kW (e um inversor de bombeamento que aceite entrada CA), ou um conversor elevador CC/CC. Esse equipamento não está na Rota B, nem no custo da seção 6.3, nem na interface. A conclusão "pouca bateria" fica mais forte com esse custo, mas a recomendação de 5 kWh pressupõe um hardware que não foi descrito. | Script C5. | Descrever o caminho bateria → compressor na Rota B (ou admitir que nela a bateria só cobre as cargas de 24 h), incluir o inversor no custo da seção 6.3 e na tabela 15.7, e refazer a comparação gelo x painel x bateria. |
| N2 | 11.2, 12.3, 3.1 | **IMPORTANTE** | Incoerência entre a lógica do CO₂ e a carga. Com 10 m³/h o equilíbrio é **0,89 %** (o próprio texto diz 0,9 %); o setpoint manda o ventilador ao máximo acima de 0,39 %. Logo o ventilador fica perto de 30 m³/h quase o tempo todo (equilíbrio de 0,32 %), e a luz da porta fica vermelha sempre que estiver em 10 m³/h. A carga soma só 10 m³/h (2,4 kWh/dia); com 25 a 30 m³/h são **5,5 a 6,6 kWh/dia** (+3 a +4 kWh). | Script C3. | Escolher: ou vazão de projeto de 25 a 30 m³/h contínuos (somar à carga e refazer kWp e gelo; meu efeito: +3,5 kWh/dia e cerca de +20 kg de gelo), ou 10 m³/h com luz por limiar de entrada e ventilação forçada só antes de entrar. As duas versões têm que bater no texto, na carga e nos setpoints. |
| N3 | 11.1 x script (`T_AGUA = 3,0`) | **IMPORTANTE** | O texto promete água a 5–7 °C à noite para não secar o ar (manga a 85–90 %). O modelo usa 3 °C o tempo todo. Com 5–7 °C a diferença ar–água cai de 9 K para 5 a 7 K: a vazão de ar sobe na mesma proporção e a potência do ventilador com o cubo (até cerca de 3 vezes). Os 79 a 109 W e o 1,22 kWh por noite saem do caso de 3 °C. De dia, com água a 3 °C e superfície da serpentina abaixo do ponto de orvalho (cerca de 10 °C), a serpentina seca o ar e tira água da fruta; nenhuma conta de umidade foi feita. | Script do autor, linha 35; 11.1. | Rodar o modelo com a água a 5–7 °C à noite e mostrar o consumo noturno e a umidade resultantes. O valor de interface de 150 W médios e 300 W de pico fica de pé (ver seção 4), mas tem que vir dessa conta. |
| N4 | "As três rotas", 9.2, 12.1 (Rota A) | IMPORTANTE | A Rota A, recomendada como de menor risco, usa unidades condensadoras de **rotação fixa** (Elgin UCMB/UCM0, Danfoss Optyma) num inversor híbrido. Partida direta de compressor puxa várias vezes a corrente nominal [de memória, 4 a 7 vezes]; o inversor híbrido de 8 a 10 kW precisa suportar esse pico, e com duas unidades a partida tem que ser intertravada. A tabela 12.1 só cobre a Rota B, e não há interface elétrica para a Rota A. Além disso, o candidato da arquitetura (a) (Elgin EcoTherm Duo, "aquecimento e resfriamento") não tem capacidade nem gás publicados: a recomendação "(a) + Rota A" se apoia num aparelho que pode nem ter o porte ou a temperatura de glicol necessários. O autor condiciona a recomendação à ficha, o que é correto. | — | Acrescentar uma tabela 12.1 para a Rota A (potência, corrente de partida ou exigência de soft-starter, intertravamento das partidas, tensão). Manter a recomendação condicionada à ficha. |
| N5 | 8.3 | MENOR | "Curvas em U de catálogo com 90 mm entre centros" para tubo de cobre de 1/2": não confirmei que esse entre-centros exista pronto. Se a curva de catálogo tiver outro entre-centros, o passo das grades e o vão de 27 mm mudam. | — | [VALIDAR] com o fornecedor de conexões, ou curvar o tubo na obra com curvador e gabarito. |
| N6 | 7.2, 9.1 (arquitetura (b)) | MENOR | Na (b), se a serpentina do banco furar, o R513A e o **óleo do compressor** vão para a água do tanque, que é bombeada para a serpentina dentro da câmara. O texto trata só do gás. | — | Prever filtro na água e procedimento de troca da água após vazamento; óleo POE na água não é risco à saúde, mas suja a serpentina e o tanque. |
| N7 | 6.3 | MENOR | A conclusão "gelo é a reserva mais barata" depende de R$ 1.000 a 2.000 por 100 kg de gelo, [SUPOSTO] e sem fonte. | — | Manter a marcação em destaque e refazer com cotação (pendência 4). |
| N8 | 5.3, 5.4 | MENOR | O mínimo de 10 kWp + 500 kg supõe que quase todo o gelo pode ser derretido (35,9 kWh de 46,4 kWh, 77 %). Com fusão externa a fração útil costuma ser de 80 a 90 % [de memória]: o mínimo fica no fio. | — | Dizer a fração útil adotada. O conjunto de referência (700 kg) não é afetado. |
| N9 | "As três rotas" | MENOR | O COP da (a) desconta 6 % do inversor, mas na Rota A a energia que passa pela bateria perde também 5 a 10 % na ida e volta [de memória]. | — | Incluir a perda ou dizer que é desprezível no balanço diário. |

## 4. As discordâncias da seção 15.4: minha posição revista

| Assunto | Minha posição agora | Argumento |
|---|---|---|
| Consumo noturno: autor 150 W médios; eu 250 a 400 W | **Revejo: aceito 150 W médios e 300 W de pico como valor de interface**, condicionado a N3. Retiro os 250 a 400 W. | Os 250 a 400 W eram para o arranjo da versão 1: duas serpentinas, ar a 5 °C, glicol a +1/+3 °C e diferença de 2 K. Agora há uma serpentina de UA 2.000 W/K, ar a 12 °C e água a 3 °C: a carga noturna de 2 a 3,5 kW sai com 30 a 50 % da vazão de ar. Mesmo com a água a 5–7 °C (N3), minha estimativa fica em 120 a 200 W. O teste 12 fecha a questão. |
| Banco de gelo comercial "de prateleira" | **Revejo: retiro a afirmação de que é produto de prateleira.** Mantenho só que deve ser cotado. | Eu não tinha fonte, e a busca do autor não achou fabricante. O texto atual (duas opções abertas, decidir com cotação) está correto. Não há conflito. |
| 10 x 12 kWp | **Mantenho em parte; o conflito encolheu.** | As contas convergem: (b) 9 a 11 kWp; (a) 10 a 13 kWp. Concordo com o autor em dimensionar estrutura, cabos e inversores para 12 a 14 kWp desde já. Mantenho que a quantidade de módulos da (b) (10 ou 12) só deve ser fechada com o SunData e o COP de catálogo; na (a), 12 kWp já é o mínimo. A diferença em jogo é de cerca de R$ 3,5 mil em módulos: decisão pequena, do dono. |
| Ordem de preferência do gás e da arquitetura | Concordo com a condição do autor. | Sem a ficha do resfriador, a (a) não está demonstrada; a (b) é a única que hoje se dimensiona com peças brasileiras. |

## 5. Seções novas

- **"O que existe pronto e o que é desenvolvimento" (rotas A, B e C):** a melhor seção nova. É clara para o leigo, separa prateleira, integração e desenvolvimento, e diz a quem pedir o quê por escrito. Problemas: N1 (bateria sem caminho na Rota B) e N4 (Rota A sem interface elétrica e com candidato sem ficha). O custo relativo "A maior, B menor" não está quantificado, e o texto admite isso.
- **Gelo x painel x bateria:** o raciocínio está certo. Bateria é a reserva mais cara por kWh de frio, painel repete o benefício todo dia, e a regra "dia nublado, meia carga; terceiro dia, sem fruta" custa zero. Concordo com "só bateria mínima, cerca de 5 kWh" **na Rota B, depois de resolvido N1**. Os custos de gelo são supostos (N7).
- **CO₂ e ar novo:** resolve o bloqueante da rodada 1 (conta, sensor, luz, regra de entrada, teste 9). Falta coerência entre a lógica e a carga (N2). O limite ocupacional está como [VALIDAR com a NR-15], o que é adequado.

## 6. Veredito

**APROVADO COM CORREÇÕES, como anteprojeto de dimensionamento.** Ainda não serve para contratar a execução, e o próprio documento diz isso (achado 3 da rodada 1 continua aberto, por falta de catálogo e cotação, não de conta).

Não resta nenhum BLOQUEANTE de segurança ou de conta. Restam IMPORTANTES:

1. N1: bateria de apoio sem caminho elétrico ao compressor na Rota B, e custo do inversor fora da comparação.
2. N2: lógica do CO₂ x vazão somada à carga (+3 a +4 kWh/dia).
3. N3: água a 5–7 °C à noite não está no modelo; consumo noturno e umidade precisam vir dessa conta.
4. N4: Rota A sem interface elétrica (partida das unidades de rotação fixa) e com candidato sem ficha.

Corrigidos esses quatro pontos, os números de interface podem ser usados pelo integrador e pelo controle: 82 kWh/dia; 10 a 12 kWp; 500 a 700 kg; 150 W médios à noite.
