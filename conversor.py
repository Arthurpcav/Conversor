import sys # sys sair do programa

def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    """Converte temperatura de Celsius para Kelvin"""
    return celsius + 273.15

def celsius_para_rankine(celsius):
    """Converte temperatura de Celsius para Rankine"""
    # primeiro Fahrenheit e depois para Rankine
    fahrenheit = celsius_para_fahrenheit(celsius)
    return fahrenheit + 459.67

def exibir_menu():
    """Mostra as opções de conversão para o usuário."""
    print("\n--- Conversor de Temperaturas ---")
    print("---------------------------------")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Celsius para Rankine")
    print("4. Sair")
    print("---------------------------------")

def main():
    """Função principal do programa."""
    while True:
        exibir_menu() # opções
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '4':
            print("Saindo do conversor. Até mais!")
            sys.exit() # sair

        try:
            graus_celsius_str = input("Quantos graus Celsius deseja converter? ")
            graus_celsius = float(graus_celsius_str.replace(',', '.')) # Permite usar vírgula como separador decimal
        except ValueError:
            print("\nOps! Valor inválido para a temperatura. Por favor, digite um número.")
            continue # Volta para o início do loop

        print("\n--- Resultado da Conversão ---")
        if escolha == '1':
            resultado = celsius_para_fahrenheit(graus_celsius)
            print(f"{graus_celsius:.2f}°C equivalem a {resultado:.2f}°F")
        elif escolha == '2':
            resultado = celsius_para_kelvin(graus_celsius)
            print(f"{graus_celsius:.2f}°C equivalem a {resultado:.2f}K")
        elif escolha == '3':
            resultado = celsius_para_rankine(graus_celsius)
            print(f"{graus_celsius:.2f}°C equivalem a {resultado:.2f}°R")
        else:
            print("Opção inválida. Por favor, tente novamente.")
        print("------------------------------\n")

# garante que a função 'main' só rode quando o script for executado diretamente
if __name__ == "__main__":
    main()