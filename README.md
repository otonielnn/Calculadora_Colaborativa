# Calculadora Colaborativa
> Uma simples calculadora criada com o objetivo de estudar git e colaborar com os colega da turma do Start By Proa.

## Ferramentas
- Git
- GitHub
- Python
- Pytest

## Diagrama das classes do projeto
```mermaid
classDiagram
  class calculadora {
    + numero1 : float
    + numero2 : float
  }

  class soma {
    + somar()
  }
  class subtracao {
    + subtrair()
  }
  class multiplicacao {
    + multiplicar()
  }
  class divisao {
    + dividir()
  }

  soma --> calculadora
  subtracao --> calculadora
  multiplicacao --> calculadora
  divisao --> calculadora
```