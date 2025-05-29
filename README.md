
# 🧾 Automação de Lançamento de Ajustes de ICMS – Sistema Dexion

Este script automatiza o processo de lançamento de **ajustes de ICMS** no sistema **Dexion**, utilizando dados provenientes de uma planilha Excel. Ele foi desenvolvido para **otimizar o tempo de trabalho de contadores**, reduzindo erros manuais e acelerando tarefas repetitivas.

---

## 📌 Funcionalidades

- Leitura de planilhas Excel com dados fiscais.
- Navegação automatizada pela interface do sistema Dexion via `pyautogui`.
- Preenchimento automático dos campos: Participante, Modelo, Série, NF, Data de Emissão, Valor e ICMS.
- Tentativas inteligentes de preenchimento do código do participante, com verificação por imagem.
- Alertas ao final do processo.
- Economia significativa de tempo nos ajustes de ICMS.

---

## 🛠️ Requisitos

- Python 3.8+
- Sistema Dexion aberto e pronto para inserção dos dados.
- Resolução de tela compatível com as coordenadas definidas no script.
- Imagem `participante_nao_cadastrado.png` salva na mesma pasta do script.

### Bibliotecas necessárias:

```bash
pip install pandas pyautogui openpyxl
```

> Obs.: A biblioteca `openpyxl` é necessária para leitura de arquivos `.xlsx`.

---

## 📄 Estrutura da Planilha

A planilha Excel utilizada deve conter as seguintes colunas (sem acentos ou espaços no nome do cabeçalho):

| PARTICIPANTE | MODELO | SERIE | NF | EMISSAO | VALOR | ICMS |
|--------------|--------|-------|----|---------|--------|------|

---

## 🚀 Como Usar

1. **Abra o sistema Dexion** e vá até a tela de ajustes de ICMS onde os dados devem ser lançados.
2. **Execute o script Python**:
   ```bash
   python automacao_icms_dexion.py
   ```
3. Insira os dados solicitados no terminal:
   - Número da empresa
   - Mês no formato `MM/AAAA`
   - Nome do arquivo Excel (com a extensão `.xlsx`)
4. Aguarde a automação concluir o processo.

> ⚠️ **Não mexa no mouse ou teclado durante a execução da automação**, pois isso pode comprometer o funcionamento.

---

## 🔍 Reconhecimento de Participante

Caso o participante não seja reconhecido, o script realiza tentativas automáticas com os seguintes formatos:
- `1`
- `01`
- `001`

Se nenhuma tentativa for bem-sucedida, o campo será preenchido com o valor `1`.

---

## 📷 Requisitos Visuais

O script utiliza verificação por imagem com a seguinte imagem:

- `participante_nao_cadastrado.png`: Imagem que aparece na tela do sistema Dexion quando um código de participante é inválido.

Certifique-se de que a imagem:
- Esteja na **mesma resolução de tela** usada no desenvolvimento (ou ajuste as coordenadas no script).
- Tenha boa qualidade e esteja recortada corretamente.

---

## ✅ Benefícios

- ⏱️ Economia de tempo
- 📉 Redução de erros manuais
- 💼 Aumento da produtividade da equipe contábil
- 🤖 Processo automatizado e confiável

---

## 🧠 Desenvolvedor

**Elias - Morpho Automações**  
🔗 [GitHub: elias2031](https://github.com/elias2031)

---

## 📌 Observações Finais

- A automação é sensível a mudanças na interface do sistema Dexion. Qualquer alteração visual pode exigir ajustes nas coordenadas e imagens usadas.
- Recomenda-se utilizar em máquinas com o sistema já configurado e atualizado para evitar incompatibilidades.

---
