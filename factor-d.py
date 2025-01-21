import dwavebinarycsp as dbc
from dwave.system import DWaveSampler, EmbeddingComposite
import numpy as np
from collections import defaultdict
import argparse
import math

def calculate_required_bits(n):
    """Calculate number of bits needed to represent the number and its factors."""
    return math.ceil(math.log2(n)) + 1

def quantum_factor(n):
    """Factor a number using D-Wave quantum annealer."""
    # Calculate required bits for the multiplication circuit
    num_bits = calculate_required_bits(n)
    
    # Initialize the D-Wave sampler
    sampler = EmbeddingComposite(DWaveSampler())
    
    # Create constraint satisfaction problem for factoring
    csp = dbc.factories.multiplication_circuit(num_bits)
    
    # Convert to binary quadratic model
    bqm = dbc.stitch(csp, min_classical_gap=.1)
    
    # Fix the product variables to represent input number in binary
    p_vars = [f'p{i}' for i in range(num_bits)]
    fixed_variables = dict(zip(reversed(p_vars), f'{n:0{num_bits}b}'))
    fixed_variables = {var: int(x) for (var, x) in fixed_variables.items()}
    
    # Fix product qubits
    for var, value in fixed_variables.items():
        bqm.fix_variable(var, value)
    
    # Sample from the quantum computer
    num_reads = 1000
    sampleset = sampler.sample(bqm,
                              num_reads=num_reads,
                              label=f'Factor-{n}')
    
    # Process results
    factor_bits = math.ceil(num_bits/2)
    a_vars = [f'a{i}' for i in range(factor_bits)]
    b_vars = [f'b{i}' for i in range(factor_bits)]
    
    # Use defaultdict to accumulate occurrences
    results_dict = defaultdict(int)
    
    for sample, occurrences in sampleset.data(['sample', 'num_occurrences']):
        # Convert binary to decimal for both factors
        a = int(sum(sample[v] << i for i, v in enumerate(reversed(a_vars))))
        b = int(sum(sample[v] << i for i, v in enumerate(reversed(b_vars))))
        
        # Convert numpy types to Python int
        a, b = int(a), int(b)
        
        # Store results by sorted tuple to avoid duplicates
        if a * b == n:
            factors = tuple(sorted([a, b]))
            results_dict[factors] += occurrences
    
    # Convert to list of results
    results = []
    for factors, occurrences in results_dict.items():
        results.append({
            'factors': factors,
            'occurrences': occurrences,
            'percentage': 100.0 * occurrences / num_reads
        })
    
    return results

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Factor a number using D-Wave quantum computer')
    parser.add_argument('number', type=int, help='The number to factor')
    parser.add_argument('--max-bits', type=int, default=10,
                       help='Maximum number of bits supported (default: 10)')
    return parser.parse_args()

def main():
    """Main program entry point."""
    args = parse_arguments()
    
    # Validate input
    if args.number < 2:
        print("Error: Please enter a number greater than 1")
        return
    
    max_value = 2 ** args.max_bits
    if args.number >= max_value:
        print(f"Error: Number too large. Maximum supported value is {max_value-1}")
        return
        
    print(f"\nFactoring {args.number} using D-Wave quantum computer...")
    results = quantum_factor(args.number)
    
    print("\nResults:")
    print("-" * 40)
    for result in sorted(results, key=lambda x: x['occurrences'], reverse=True):
        print(f"Factors: {result['factors']}")
        print(f"Occurrences: {result['occurrences']} ({result['percentage']:.2f}%)")
        print("-" * 40)

if __name__ == '__main__':
    main()