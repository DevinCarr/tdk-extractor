from extractor import *
from mlcc_commercial_general_parser import MLCC_Commercial_General_Parser
from math import floor
import argparse

def write_file(data_row, filename):
    with open(filename, 'a') as file:
        file.write(','.join(data_row) + '\n')

def read_part_numbers(filename):
    part_numbers = []
    with open(filename, 'r') as file:
        for part_no in file:
            if len(str(part_no)) > 0:
                part_numbers.append(part_no.replace('\n', ''))
    return part_numbers

def part_parser(part_no):
    if MLCC_Commercial_General_Parser.valid(part_no):
        return MLCC_Commercial_General_Parser(part_no)
    return None

def filter_dcbias(data):
    voltages = ['0', '1', '2', '4', '6.3', '10', '16', '25', '30', '35', '40', '50', '65', '80', '100']
    result = []
    for col in voltages:
        val = list(filter(lambda x: x[0] == col, data))
        if len(val) == 0: 
            result.append([col, ''])
            continue
        result.append(val[0])
    return result

def filter_temp(data):
    currents = [x * 0.1 for x in range(5, 80, 5)]
    length = len(data)
    ptr = 0
    result = []
    tfloor = lambda x, y: float(floor(x)) if y % 1.0 == 0.0 else float(floor(x + 0.5) - 0.5)
    for col in currents:
        while ptr < length:
            if tfloor(float(data[ptr][0]), col) == col:
                break
            else:
                #print('{}\t{}:{} ({})'.format(ptr, col, tfloor(float(data[ptr][0]), col), float(data[ptr][0])))
                ptr += 1
        if ptr >= length:
            result.append([str(col), ''])
            continue
        result.append(data[ptr])
        ptr += 1
    return result

def get_row_data(part_no):
    parser = part_parser(part_no)
    graphs = get_part_graph(part_no)
    if graphs is None:
        return None
    dcbias_data, temp_data = graphs
    return parser.row_output() + list(map(lambda x: str(x[1]), filter_dcbias(dcbias_data))) + list(map(lambda x: str(x[1]), filter_temp(temp_data)))

def main():
    parser = argparse.ArgumentParser(description='Extract part values from part catalog')
    parser.add_argument('--input', type=str, required=True, help='input file of part numbers (one per line)')
    parser.add_argument('--output', type=str, default='output.csv',
                        help='output file (csv)')
    args = parser.parse_args()
    
    part_numbers = read_part_numbers(args.input)
    for part_no in part_numbers:
        print('Fetching part: {}'.format(part_no))
        row = get_row_data(part_no)
        if row is None:
            print('Error fetching part data: {}'.format(part_no))
            continue
        write_file(row, args.output)
    print('Wrote to file: {}'.format(args.output))

if __name__ == '__main__':
    main()