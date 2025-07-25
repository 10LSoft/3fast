# 3Fast

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/10LSoft/3Fast)](https://github.com/10LSoft/3Fast/issues)

> Framework web full stack em Python, inspirado no Django.  
> Utiliza **FastAPI**, **FastHTML**, **FastCSS** e **Tortoise ORM**, com abordagem monolítica e produtiva.

---

## ✨ Visão Geral

**3Fast** é um framework web full stack minimalista e poderoso, que une
backend e frontend em um único app, com uma arquitetura moderna e familiar para
quem já conhece Django. Ele foi criado para acelerar o desenvolvimento de
aplicações web com Python moderno e componentes reutilizáveis.

### Principais tecnologias:

- ⚡️ FastAPI — servidor web rápido e moderno
- 🧩 FastHTML — sistema de componentes e templates com Python puro
- 🎨 FastCSS — utilitários CSS para produtividade (escrita localmente)
- 🐢 Tortoise ORM — ORM assíncrono inspirado no Django ORM
- 🛠 CLI com Typer — comandos para scaffold e dev experience

---

## 🚀 Primeiros passos

### Clone o projeto

```bash
git clone https://github.com/10LSoft/3Fast
cd 3Fast
```

No momento é importante entender que o framework está em case alfa teste e os
avanços são implantados no corpo do framework /fasts após correta implementação
no /dev (um projeto exemplo e já gerado pelo 3Fast via CLI). Trata-se de uma
implementação recursiva e a versão final do pacote não terá o diretório dev
nela.

Implementações relacionadas ao corpo do framework deverão ser adicionadas no
diretório /fasts e submetidas via PR para avaliação (se você estiver
interessado em apoiar o desenvolvimento).

### Rodando o pack /dev (aplicação exemplo para desenvolvimento)

O projeto está sendo implementado usando poetry:
[Poetry Project](https://python-poetry.org)

```bash
poetry install
poetry shell
uvicorn dev.configs.server:back_app
```

## 🧱 Estrutura básica:

```
3Fast/
├── fasts/              # Núcleo do framework
├── dev/                # Projeto de exemplo ou dev environment
├── LICENSE
├── README.md
└── pyproject.toml
```

## 📜 Licença

Este projeto está licenciado sob a MIT License — sinta-se livre para usar, modificar e contribuir!

## 🙌 Contribuindo

Contribuições são muito bem-vindas!
Veja a lista de issues, envie uma pull request, ou abra uma ideia nova.

## 📫 Contato

Criado por Genese Lessa (10LSoft) • © 2025
Dúvidas, sugestões ou colaborações? Me chama por aqui mesmo no GitHub ou abra uma issue!


#### Feito com 🧡 para desenvolvedores Python que gostam de produtividade e elegância.
