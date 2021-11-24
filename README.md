# Blog
<p align="center">
<img src=https://img.shields.io/badge/version-1.0.0-green/>
<img src=https://img.shields.io/badge/Frontend-HTML/CSS-blue?/>
<img src=https://img.shields.io/badge/Backend-Python%20-important?/>
</p>

Modelo de blog, todo backend foi desenvolvido usando flask e os dados são armazenado no banco SQLite.

---
## Começando
Para executar o projeto você vai precisar:

1. Criar um ambiente virtual
2. Entrar no ambiente virtual

Após esse processo na pasta do projeto instale as dependências do projeto. 

```PowerShell
pip install -r requirements.txt
```
---

## Rodar o projeto
Para rodar o projeto você vai precisar:

- Entra no ambiente virtual
- Após esse processo na pasta do projeto execute:

#### PowerShell
```PowerShell
$env:FLASK_APP=flaskr

$env:FLASK_ENV=development

flask run
```

#### CMD
```CMD
set FLASK_APP=flaskr

set FLASK_ENV=development

flask run
```
