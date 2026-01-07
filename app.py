from misc.parser_estadao import EstadaoSpider

# -------------------------------------------------------------------------------- #
# BLOCO DE TESTE DO SPIDER

# Aqui podemos passar quantas URLs quisermos
lista_urls = ["https://www.estadao.com.br/internacional/por-dentro-da-disputa-pela-politica-externa-do-maga/",
            "https://www.estadao.com.br/politica/prefeito-de-diadema-e-condenado-por-ligar-assessor-de-lula-a-marcola-e-crime-organizado-npr/",
            "https://www.estadao.com.br/politica/lula-diz-que-dinheiro-e-influencia-nao-pararao-a-pf-e-que-combate-a-faccoes-chegou-ao-andar-de-cima/",
            "https://www.estadao.com.br/saude/adultos-podem-tomar-a-vacina-contra-hpv-especialistas-tiram-duvidas-sobre-o-imunizante-nprm/",
            "https://www.estadao.com.br/link/empresas/ricacos-do-vale-do-silicio-miram-algoritmos-e-ciencia-de-dados-para-gerarem-os-bebes-perfeitos/",
            "https://www.estadao.com.br/brasil/serial-killer-da-rotatoria-foge-de-prisao-de-seguranca-maxima-governo-ve-elo-de-detento-com-o-pcc-npr/",
            "https://www.estadao.com.br/economia/negocios/de-postos-de-gasolina-a-fintechs-como-o-crime-se-infiltrou-no-dia-a-dia-dos-negocios-no-brasil/",
            "https://www.estadao.com.br/politica/prefeito-de-diadema-e-condenado-por-ligar-assessor-de-lula-a-marcola-e-crime-organizado-npr/",
            "https://www.estadao.com.br/sao-paulo/operacao-da-pm-na-favela-do-moinho-deixa-suspeito-morto-apos-troca-de-tiros-npr/",
            "https://www.estadao.com.br/economia/correios-ainda-precisam-captar-r-8-bi-para-fechar-conta-diz-presidente-da-estatal/",
            "https://www.estadao.com.br/politica/se-tiver-filho-meu-metido-nisso-sera-investigado-diz-lula-sobre-esquema-de-fraude-no-inss/",
            "https://www.estadao.com.br/politica/em-balanco-tarcisio-diz-que-tirou-do-papel-tunel-santos-guaruja-mas-contrato-sequer-foi-assinado-npr/",
            "https://www.estadao.com.br/brasil/prescricao-de-processo-contra-marcola-e-mais-lideres-do-pcc-e-falha-do-estado-diz-desembargadora/",
            "https://www.estadao.com.br/sao-paulo/marcola-e-cupula-do-pcc-se-livram-de-maior-processo-contra-a-faccao-jamais-poderia-ter-acontecido/",
            "https://www.estadao.com.br/politica/blog-do-fausto-macedo/avanco-do-crime-organizado-no-mercado-faz-pf-fechar-acordo-de-cooperacao-com-bndes-e-febraban/",
            "https://www.estadao.com.br/brasil/homem-preso-suspeita-matar-namorada-simular-acidente-carro-mg-npr/",
            "https://www.estadao.com.br/brasil/empresaria-40-anos-morre-acidente-carro-luxo-balneario-camboriu-motorista-presa-npr/",
            "https://www.estadao.com.br/cultura/cinema/o-que-se-sabe-sobre-a-morte-de-rob-reiner-nprec/",
            "https://www.estadao.com.br/brasil/policia-prende-12-integrantes-do-nucleo-operacional-do-comando-vermelho-na-zona-norte-do-rio-npr/",
            "https://www.estadao.com.br/brasil/promotor-fala-de-acao-contra-o-pcc-e-marcola-que-prescreveu-apos-12-anos-sem-sentenca/",
            "https://www.estadao.com.br/brasil/delegado-que-teve-perna-amputada-apos-ficar-ferido-em-operacao-no-rj-tem-alta-apos-45-dias-internado-npr/"]

# Dicionário de configurações do scraper 
CONFIGS_BOT = {'KEYWORD':'pcc'}

def executar():
    print("Iniciando bot do portal Estadão...")
    EstadaoSpider(keyword=CONFIGS_BOT["KEYWORD"], list=lista_urls)

if __name__ == "__main__":
    executar()
