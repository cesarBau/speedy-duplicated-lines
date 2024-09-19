from client_redis import init_conection, create_reg, get_all_reg
import datetime


file_name = '60'


def read_file_lines(file_lines):
    unique_line = []
    with open(f'{file_lines}.txt', encoding='UTF-8') as archive:
        for line in archive:
            values = line.rstrip('\n')
            process = values.split('|')
            unique_line.append(process[0])
    return unique_line


def write_lile(name, values):
    with open(f'output-{name}.txt', 'w', encoding='UTF-8') as archive:
        for line in values:
            value = int(line)
            archive.write(str(value))
            archive.write('\n')


def main():
    print('Cargando la lista de errores 60')
    lines = read_file_lines(file_name)
    print('Carga terminada')
    print('Registramos las lineas con errores 60')
    for line in lines:
        create_reg(line, datetime.datetime.now().isoformat())
    print('Registro concluido')
    print('Obtenemos las lineas')
    results = get_all_reg()
    write_lile(file_name, results)
    print('proceso terminado')


init_conection()
main()
