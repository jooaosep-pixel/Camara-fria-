# Premissas do projeto (base comum a todos os subagentes)

Dados do dono do projeto. Ele não é engenheiro: os números são estimativas
iniciais e DEVEM ser refeitos e corrigidos.

## Produto
- Câmara fria fora da rede elétrica para pequenos produtores de fruta, sertão de Pernambuco.
- Base: contêiner de 20 pés (ver "em aberto"). Capacidade: 5 t de fruta, 5 a 10 °C.
- Ambiente: 40 °C à sombra.
- Cerca de 5 kWp de painéis acionando direto um compressor de velocidade variável.
- O frio vai primeiro para a câmara; a sobra vira gelo (estimativa inicial: 200 kg),
  que deve manter a câmara por 14 horas sem sol.
- Só uma bateria pequena para ventiladores, bomba e controle à noite.
- Entrada de até 1 t de fruta por dia a 30 °C.
- Telemetria: o local terá internet por Starlink (não contar com 4G). A antena
  Starlink é uma carga elétrica de 24 h que entra no dimensionamento da bateria.

## Em aberto (o dono ainda não decidiu): tratar assim
| Item | Como tratar |
|---|---|
| Cidade | O agente de logística vai recomendar o local (`docs/09-logistica-e-local.md`). Até lá, usar Petrolina-PE como referência de clima e irradiação; mostrar a sensibilidade para outro ponto do sertão pernambucano. |
| Fruta | DEFINIDA pelo dono: manga e caju (pedúnculo, fruta fresca). Pesquisar a temperatura e a umidade ideais de cada uma; as duas podem não ser compatíveis na mesma câmara (manga sofre dano por frio abaixo de cerca de 10 °C; caju pede temperatura mais baixa). Dizer claramente como resolver: temperatura de compromisso, operação alternada por safra, ou divisória com duas zonas, com o efeito na carga térmica e na vida útil de cada fruta. |
| Horário de entrada e saída da fruta | Calcular o pior caso (1 t entrando no fim da tarde) e o melhor (de manhã cedo) e recomendar uma regra de operação. |
| Contêiner | Comparar: reefer usado (isolado de fábrica), contêiner seco + isolamento, câmara de painéis isotérmicos. Recomendar o que combina mais, com preço encontrado. |
| Gás | O engenheiro compara (R290, R600a, R134a/R513A, R404A/R448A/R449A/R452A, R744 etc.) e escolhe, com a segurança pesando. |
| Orçamento | Sem teto. Mostrar custo e indicar alternativas mais baratas. |
| Controlador | O programador compara CLP industrial x placa tipo ESP32 e recomenda. Deve ser mantível por um eletricista. |

## Conta rápida do orquestrador (sem fonte; conferir, não copiar)
- 200 kg de gelo × 334 kJ/kg ≈ 18,6 kWh de frio.
- Carga noturna estimada 1,2 a 1,5 kW → 17 a 21 kWh em 14 h: gelo no limite.
- Resfriar 1 t de 30 a 7 °C ≈ 24 kWh/dia. Total ≈ 55 a 60 kWh de frio/dia.
- Uma especificação pública indiana para câmara solar de 6 t pede no mínimo
  6,9 kWp e 200 MJ de armazenamento (UPNEDA) — bem acima dos 67 MJ de 200 kg de gelo.

## Regras para todos
1. Pesquisar na web antes de afirmar: catálogos de fabricantes, normas
   brasileiras aplicáveis, artigos técnicos, produtos parecidos (Ecozen Ecofrost,
   ColdHubs). Citar a fonte de CADA número com link. Só citar página que você
   realmente abriu ou que apareceu no resultado da busca; nunca inventar link.
2. Componentes: dar sempre a opção à venda no Brasil (modelo, fabricante, link,
   preço encontrado e data; sem preço: escrever "preço não encontrado"). O dono
   autorizou IMPORTAR DA CHINA para montar aqui: para cada item principal,
   escrever também uma "especificação para cotação" genérica (capacidade, tensão,
   gás, dimensões, certificações exigidas), para o agente de importação cotar o
   equivalente importado. A comparação Brasil x China é do agente de importação
   (`docs/11-importacao.md`); os projetistas não escolhem entre os dois.
3. Marcar cada número ou decisão como [CALCULADO], [SUPOSTO] ou
   [VALIDAR COM PROFISSIONAL HABILITADO].
4. Mostrar as contas com unidades, passo a passo, conferíveis por outra pessoa.
5. Segurança em destaque (blocos "⚠ SEGURANÇA"): gás inflamável, alta pressão,
   tensão contínua dos painéis, espaço fechado.
6. Português do Brasil, linguagem direta. O leitor final é um leigo que vai
   contratar um frigorista e um eletricista apenas para executar.
7. Não ter acesso a uma página (bloqueio, PDF ilegível) deve ser dito, não contornado com chute.
8. Ao final, listar: decisões tomadas, pendências para humanos e os dados de
   interface que as outras disciplinas precisam.

## Conflitos entre agentes: o dono é o mediador
- Quando dois agentes discordarem (autor x revisor, ou duas disciplinas com
  exigências incompatíveis), nenhum agente nem o orquestrador decide.
- O agente registra o conflito sem resolvê-lo: as duas posições, os números e
  fontes de cada uma, e o que cada escolha custa ou arrisca.
- O orquestrador leva o conflito ao dono em linguagem simples e espera a decisão.
  A decisão fica registrada em `docs/07-revisao.md`.
- Não é conflito: erro de conta ou de fonte que o autor reconhece e corrige.
