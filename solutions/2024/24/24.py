from aocd import get_data, submit

def parse_input(data):
    sections = data.strip().split('\n\n')
    
    wires = {}
    for line in sections[0].split('\n'):
        if(not line.strip()):
            continue
        name, value = line.split(': ')
        wires[name] = int(value)
    
    input_bit_count = len(wires) // 2
    
    gates = []
    for line in sections[1].split('\n'):
        if(not line.strip()):
            continue
        inputs, output = line.strip().split(' -> ')
        a, op, b = inputs.split(' ')
        gates.append({'a': a, 'op': op, 'b': b, 'output': output})
        
        if(a not in wires):
            wires[a] = None
        if(b not in wires):
            wires[b] = None
        if(output not in wires):
            wires[output] = None
            
    return wires, gates, input_bit_count

def is_direct(gate):
    return gate['a'].startswith('x') or gate['b'].startswith('x')

def is_output(gate):
    return gate['output'].startswith('z')

def is_gate_type(type):
    return lambda gate: gate['op'] == type

def has_output(output):
    return lambda gate: gate['output'] == output

def has_input(input):
    return lambda gate: gate['a'] == input or gate['b'] == input

def find_swapped_wires(data):
    _, gates, input_bit_count = parse_input(data)
    flags = set()
    
    ## (XOR gates connected directly to inputs)
    fa_gate0s = [g for g in gates if is_direct(g) and g['op'] == 'XOR']
    for gate in fa_gate0s:
        a, b, output = gate['a'], gate['b'], gate['output']
        
        is_first = a == 'x00' or b == 'x00'
        if(is_first):
            if(output != 'z00'):
                flags.add(output)
            continue
        elif(output == 'z00'):
            flags.add(output)
            
        if(is_output(gate)):
            flags.add(output)
    
    ## (indirect XOR gates)
    fa_gate3s = [g for g in gates if not is_direct(g) and g['op'] == 'XOR']
    for gate in fa_gate3s:
        if(not is_output(gate)):
            flags.add(gate['output'])

    output_gates = [g for g in gates if is_output(g)]
    for gate in output_gates:
        is_last = gate['output'] == f"z{str(input_bit_count).zfill(2)}"  # z45
        if(is_last):
            ## The last gate (z45) should be an OR gate (it's the carry bit) (in my case this was a false positive)
            if(gate['op'] != 'OR'):
                flags.add(gate['output'])
            continue
        ## All other z outputs should be XOR gates (they're sum bits)
        elif(gate['op'] != 'XOR'):
            flags.add(gate['output'])

    check_next = []
    for gate in fa_gate0s:
        output = gate['output']
        
        if(output in flags):
            continue
            
        if(output == 'z00'):
            continue
            
        matches = [g for g in fa_gate3s if has_input(output)(g)]
        if(not matches):
            check_next.append(gate)
            flags.add(output)

    for gate in check_next:
        a, output = gate['a'], gate['output']
        
        intended_result = f"z{a[1:]}"
        matches = [g for g in fa_gate3s if has_output(intended_result)(g)]
        
        if(len(matches) != 1):
            raise Exception("Your input is probably dogshit")
            
        match = matches[0]
        to_check = [match['a'], match['b']]
        
        or_matches = [g for g in gates if g['op'] == 'OR' and any(g['output'] == t for t in to_check)]
        
        if(len(or_matches) != 1):
            raise Exception("Fuck, you may have a false positive")
            
        or_match_output = or_matches[0]['output']
        correct_output = next(t for t in to_check if t != or_match_output)
        flags.add(correct_output)
    
    if(len(flags) != 8):
        raise Exception("Fuck, you may have a false positive")
    
    return ','.join(sorted(flags))

def simulate_circuit(wires, gates):
    while(any(wires[gate['output']] is None for gate in gates)):
        for gate in gates:
            if(wires[gate['output']] is not None):
                continue
                
            a_val = wires[gate['a']]
            if(a_val is None):
                continue
                
            b_val = wires[gate['b']]
            if(b_val is None):
                continue
            
            if(gate['op'] == 'AND'):
                wires[gate['output']] = a_val & b_val
            elif(gate['op'] == 'OR'):
                wires[gate['output']] = a_val | b_val
            elif(gate['op'] == 'XOR'):
                wires[gate['output']] = a_val ^ b_val

def get_z_value(wires):
    z_wires = sorted([k for k in wires.keys() if k.startswith('z')])
    result = 0
    for wire in reversed(z_wires):
        result = (result << 1) | wires[wire]
    return result

def part1(data):
    wires, gates, _ = parse_input(data)
    simulate_circuit(wires, gates)
    result = get_z_value(wires)
    print(f"Part 1: {result}")
    return result

def part2(data):
    result = find_swapped_wires(data)
    print(f"Part 2: {result}")
    return result

if(__name__ == "__main__"):
    data = get_data(day=24, year=2024)
    
    submit(part1(data), part="a", day=24, year=2024)
    
    submit(part2(data), part="b", day=24, year=2024)
