# Quantum Factoring with D-Wave

This project demonstrates quantum factoring using D-Wave's quantum annealing computer. The implementation specifically factors the number 77 using quantum annealing techniques.

## Prerequisites

- Python 3.8 or higher
- A D-Wave Leap account (free tier available)
- D-Wave Ocean SDK

## Installation

1. First, create and activate a virtual environment (recommended):
```bash
python -m venv quantum-env
source quantum-env/bin/activate  # On Windows, use: quantum-env\Scripts\activate
```

2. Install the required packages:
```bash
pip install dwave-ocean-sdk
```

3. Configure your D-Wave credentials:
   
   a. Sign up for a [D-Wave Leap account](https://cloud.dwavesys.com/leap/signup/)
   
   b. Get your API token from the D-Wave Leap dashboard
   
   c. Configure your environment:
   ```bash
   dwave config create
   ```
   Follow the prompts to enter your API token.

## Project Structure

```
quantum-factoring/
├── README.md
├── factor_77.py
```

## Usage

Run the factoring program:
```bash
python factor_77.py
```

The program will:
1. Connect to D-Wave's quantum computer
2. Set up the factoring problem for the number 77
3. Run the quantum annealing process
4. Display the results, showing the factors found and their frequencies

## Expected Output

The program will output something like:
```
Factoring 77 using D-Wave quantum computer...

Results:
----------------------------------------
Factors: (7, 11)
Occurrences: 423 (42.30%)
----------------------------------------
```

Note: Due to the probabilistic nature of quantum annealing, the exact occurrences and percentages may vary between runs.

## How It Works

The program uses quantum annealing to solve a factoring problem by:
1. Converting the factoring problem into a binary quadratic model
2. Embedding the problem onto D-Wave's quantum architecture
3. Running multiple annealing cycles
4. Processing the results to identify valid factors

Unlike Shor's algorithm, which runs on gate-based quantum computers, this implementation uses quantum annealing, which is specifically designed for optimization problems.

## Troubleshooting

Common issues and solutions:

1. **API Token Issues**
   - Ensure your D-Wave API token is correctly configured
   - Verify your Leap account is active
   ```bash
   dwave ping
   ```

2. **Connection Problems**
   - Check your internet connection
   - Verify firewall settings aren't blocking the connection
   - Try running with debug logging:
   ```bash
   python factor_77.py --log-level debug
   ```

3. **Installation Problems**
   - Make sure you have Python 3.8 or higher:
   ```bash
   python --version
   ```
   - Try upgrading pip:
   ```bash
   pip install --upgrade pip
   ```

## Resources

- [D-Wave System Documentation](https://docs.dwavesys.com/docs/latest/index.html)
- [Ocean SDK Documentation](https://docs.ocean.dwavesys.com/en/stable/)
- [D-Wave Leap](https://cloud.dwavesys.com/leap/)
