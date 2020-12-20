"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    nu1 = float(input('Digite o primeiro número:'))
    nu2 = float(input('Digite o segundo número:'))
    nu3 = float(input('Digite o terceiro número:'))
    if nu1>nu2 and nu1>nu3:
      maior=nu1
    if nu2>nu1 and nu2>nu3:
      maior=nu2
    if nu3>nu1 and nu3>nu2:
      maior=nu3
    print(f'{maior}') 


if __name__ == '__main__':
    main()
