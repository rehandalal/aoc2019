from utils import get_input_data_comma_separated


data = [int(i) for i in get_input_data_comma_separated('2.txt')]


def compute(intcode):
    i = 0
    while i < len(intcode):
        opcode = intcode[i]
        if opcode == 99:
            break
        elif opcode < 1 or opcode > 2:
            raise Exception('Invalid opcode.')
        else:
            p1 = intcode[i + 1]
            p2 = intcode[i + 2]
            p3 = intcode[i + 3]
            if opcode == 1:
                result = intcode[p1] + intcode[p2]
            else:
                result = intcode[p1] * intcode[p2]
            intcode[p3] = result
        i += 4
    return intcode


fixed_data = data[:1] + [12, 2] + data[3:]
computed = compute(fixed_data)

print(f'Primary Result: {computed[0]}')

TARGET = 19690720
for noun in range(0, 99):
    fixed_data = data[:1] + [noun, 0] + data[3:]
    computed = compute(fixed_data)
    if TARGET - computed[0] < 99:
        verb = TARGET - computed[0]
        break

print(f'Secondary Result: {(100 * noun) + verb}')

