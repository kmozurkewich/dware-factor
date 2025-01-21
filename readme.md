# D-Wave Quantum Factoring

Quantum factorization using D-Wave's quantum annealing computer.

## Setup

1. Create virtual environment:
```bash
python -m venv quantum-env
source quantum-env/bin/activate  # Windows: quantum-env\Scripts\activate
```

2. Install requirements:
```bash
pip install dwave-ocean-sdk
```

3. Configure D-Wave:
```bash
dwave config create  # Enter your API token when prompted
```

## Usage

Run with a number to factor:
```bash
python factor_d.py 77
```

Optional arguments:
```bash
python factor_d.py 77 --max-bits 12  # For larger numbers
```

## Requirements

- Python 3.8+
- D-Wave Leap account (free tier available at cloud.dwavesys.com/leap)

## Notes

- Maximum input size is limited by quantum hardware constraints
- Results are probabilistic due to quantum annealing nature