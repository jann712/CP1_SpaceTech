from util.analise_autonomia_agua import analise_autonomia_agua
from util.analise_bateria import analise_bateria
from util.analise_reservatorio import analise_reservatorio
from util.analise_solar import analise_solar

def main():
    
    analise_solar()
    analise_bateria()
    analise_reservatorio()
    analise_autonomia_agua()


if __name__ == "__main__":
    main()

 