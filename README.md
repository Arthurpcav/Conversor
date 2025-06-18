# Conversor de Temperaturas

---

## Sobre o Projeto

Este é um programa Python simples para converter temperaturas de **Celsius** para **Fahrenheit**, **Kelvin** e **Rankine**. O objetivo do projeto é demonstrar o uso de testes de unidade e a integração contínua (CI/CD) com GitHub Actions.

---

## Funcionalidades

* Converte Celsius para Fahrenheit.
* Converte Celsius para Kelvin.
* Converte Celsius para Rankine.
* Interface de usuário via terminal.

---

## Como Usar

Para executar o conversor, siga os passos abaixo:

1.  **Clone o repositório**:
    ```sh
    git clone https://github.com/Arthurpcav/Conversor.git
    cd Conversor
    ```

2.  **Execute o programa**:
    ```sh
    python conversor.py
    ```
    O programa apresentará um menu interativo no terminal.

---

## Testes

O projeto inclui testes de unidade para as funções de conversão. Para executá-los:

```sh
python -m unittest test_conversor.py
```

---

## CI/CD com GitHub Actions

Este projeto utiliza **GitHub Actions** para automação de CI/CD. Os testes são executados automaticamente a cada *commit* na branch \`main\`. Os testes são realizados em diferentes sistemas operacionais (**Ubuntu**, **macOS**, **Windows**) e em múltiplas versões do **Python** (3.10 e 3.12).

Você pode acompanhar o status dos builds e testes na aba \"Actions\" do repositório no GitHub.

---
