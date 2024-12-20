
# 📦 Gerador de Códigos de Barras EAN-13

Este repositório contém uma solução para gerar códigos de barras **EAN-13** (GTIN-13) com base nas regras do  **GS1 Brasil** . O código de barras gerado é compatível com leitores de código de barras e pode ser utilizado em sistemas de gestão de estoque, vendas e controle de produtos.

## 📜 Índice

* [🚀 Visão Geral](#-visão-geral)
* [📚 O que é o GTIN EAN-13?](#-o-que-é-o-gtin-ean-13)
* [🇧🇷 Regras do GS1 Brasil](#-regras-do-gs1-brasil)
* [⚙️ Como Funciona](#️-como-funciona)
* [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
* [💼 Gerar ZPL e Excel](#-gerar-zpl-e-excel)
* [🎯 Contribuições](#-contribuições)
* [📞 Contato](#-contato)

## 🚀 Visão Geral

Este projeto permite a geração de códigos de barras **EAN-13** para produtos, seguindo as regras do **GTIN** (Global Trade Item Number). Os códigos gerados podem ser usados para impressão, controle de estoque e integração com sistemas de automação.

Ele também gera **arquivos ZPL** para impressão em impressoras térmicas e **um arquivo Excel** contendo todos os códigos gerados, permitindo fácil rastreamento e importação.

## 📚 O que é o GTIN EAN-13?

O **GTIN-13** (Global Trade Item Number) é um sistema de numeração padronizado utilizado para identificar produtos comercializados globalmente. No Brasil, o sistema de códigos de barras **EAN-13** segue as diretrizes estabelecidas pela  **GS1 Brasil** .

### Estrutura do Código EAN-13

O código EAN-13 é composto por 13 dígitos, sendo:

1. **Prefixo do País (3 dígitos)** : Identifica o país de origem do produto. No Brasil, o prefixo é  **789** .
2. **Código da Empresa (4 a 7 dígitos)** : Identifica a empresa que comercializa o produto. Este código é obtido através da  **GS1 Brasil** , a organização responsável pela emissão dos códigos de barras.
3. **Código do Produto (4 dígitos)** : Identifica o produto específico dentro da empresa.
4. **Dígito Verificador (1 dígito)** : Calculado a partir dos outros 12 dígitos para garantir que o código de barras seja lido corretamente.

## 🇧🇷 Regras do GS1 Brasil

A **GS1 Brasil** é uma organização sem fins lucrativos responsável pela gestão e emissão dos códigos de barras no Brasil. Para obter um **código de empresa** (parte do EAN-13), a empresa precisa se registrar junto à GS1 Brasil e seguir as normas e processos estabelecidos.

### Passos para obter um código de empresa:

1. **Cadastro na GS1 Brasil** : A empresa deve se cadastrar no site oficial da GS1 Brasil ([https://www.gs1br.org/](https://www.gs1br.org/)).
2. **Emissão do Código de Empresa** : A GS1 Brasil fornecerá um código único de empresa, que será utilizado para gerar os códigos de barras EAN-13.
3. **Uso do Prefixo Nacional** : O prefixo brasileiro para os códigos EAN-13 é  **789** , e a empresa deve complementar este prefixo com seu código exclusivo.

## ⚙️ Como Funciona

1. O sistema gera um código de barras EAN-13 utilizando o código da empresa e um código de produto aleatório.
2. O dígito verificador é calculado para garantir a integridade do código EAN-13.
3. Um **arquivo ZPL** é gerado para impressão em impressoras térmicas compatíveis.
4. Todos os códigos gerados são armazenados em um  **arquivo Excel** , que pode ser usado para consulta ou importação em sistemas de gestão.

## 🛠️ Tecnologias Utilizadas

* **Python 3** 🐍
* **Barcode** (biblioteca de código de barras) 📦
* **openpyxl** (para gerar o arquivo Excel) 📊
* **ZipFile** (para compactar os arquivos) 📦
* **Zebra Programming Language (ZPL)** para impressão de etiquetas 🖨️

## 💼 Gerar ZPL e Excel

O processo de geração de códigos de barras envolve:

1. **Geração do Código EAN-13** : Um código único é gerado com base no código da empresa e no código do produto.
2. **Geração do Arquivo ZPL** : Para impressão em impressoras térmicas, o código é convertido para o formato ZPL.
3. **Arquivo Excel** : Todos os códigos gerados são salvos em um arquivo Excel, com o índice e o código EAN.
4. **Arquivos ZIP** : Todos os arquivos ZPL e o Excel são compactados em um único arquivo ZIP para fácil distribuição.

## 🎯 Contribuições

Contribuições são bem-vindas! Se você encontrar algum bug ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir um Pull Request ou criar uma Issue.

### Como Contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para sua funcionalidade: `git checkout -b feature/nova-funcionalidade`.
3. Faça suas alterações e adicione commits.
4. Envie um Pull Request.

## 📞 Contato

Caso tenha dúvidas ou sugestões, entre em contato:

Email: [ikauedeveloper@gmail.com](mailto:ikauedeveloper@gmail.com)

LinkedIn: [https://www.linkedin.com/in/ikauematos/](https://www.linkedin.com/in/ikauematos/)

---

Este README fornece uma visão geral do projeto, explicando como ele gera os códigos de barras EAN-13, com base nas regras do **GTIN** e da  **GS1 Brasil** . Ele também detalha as tecnologias usadas e como contribuir para o projeto.
