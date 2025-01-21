import dwavebinarycsp as dbc
from dwave.system import DWaveSampler, EmbeddingComposite
import numpy as np
from collections import defaultdict

def factor_77():
    # Initialize the D-Wave sampler
    sampler = EmbeddingComposite(DWaveSampler())
    
    # Create constraint satisfaction problem for factoring
    csp = dbc.factories.multiplication_circuit(7)  # Need 7 bits for factors of 77
    
    # Convert to binary quadratic model
    bqm = dbc.stitch(csp, min_classical_gap=.1)
    
    # Fix the product variables to represent 77 in binary (1001101)
    p_vars = ['p0', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']
    fixed_variables = dict(zip(reversed(p_vars), "{:07b}".format(77)))
    fixed_variables = {var: int(x) for (var, x) in fixed_variables.items()}
    
    # Fix product qubits
    for var, value in fixed_variables.items():
        bqm.fix_variable(var, value)
    
    # Sample from the quantum computer
    num_reads = 1000  # Increased for better sampling
    sampleset = sampler.sample(bqm,
                              num_reads=num_reads,
                              label='Factor-77')
    
    # Process results
    a_vars = ['a0', 'a1', 'a2', 'a3']  # Variables for first factor
    b_vars = ['b0', 'b1', 'b2', 'b3']  # Variables for second factor
    
    # Use defaultdict to accumulate occurrences
    results_dict = defaultdict(int)
    
    for sample, occurrences in sampleset.data(['sample', 'num_occurrences']):
        # Convert binary to decimal for both factors
        a = int(sum(sample[v] << i for i, v in enumerate(reversed(a_vars))))
        b = int(sum(sample[v] << i for i, v in enumerate(reversed(b_vars))))
        
        # Convert numpy types to Python int
        a, b = int(a), int(b)
        
        # Store results by sorted tuple to avoid duplicates of (7,11) and (11,7)
        if a * b == 77:
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

if __name__ == '__main__':
    print("Factoring 77 using D-Wave quantum computer...")
    results = factor_77()
    
    print("\nResults:")
    print("-" * 40)
    for result in sorted(results, key=lambda x: x['occurrences'], reverse=True):
        print(f"Factors: {result['factors']}")
        print(f"Occurrences: {result['occurrences']} ({result['percentage']:.2f}%)")
        print("-" * 40)