# Epidemic symulation

## Prerequisites

Python >=3.8  
List of all required packages can be found in [here](./requirements.txt)

## Creating environment

### pip

```bash
python3 -m venv <nazwa_env>
source /env/bin/activate
pip install -r requirements.txt
```

### conda

```bash
conda env create -f environment.yml
```

## Running simultation

In order to run the simulation simply type

```bash
python main.py
```

Program is executed in user-friendy GUI.  
Available options:

* import data
* start simulation
* stop simulation

> Model: https://holko.pl/public/documents/1-s2.0-S0957417415005631-main.pdf

## Code description

### State  

    type: str [S, E, I, R]  
    S - susceptible  
    E - exposed  
    I - infected  
    R - recovered  
    day: int >= 0
    n: str

### StateVector

    a: int >=0 Exposed period
    b: int >=0 Infected period
    beta: str Contact rate
    [init_data]: Initial data in np.array format

### CA (Cellular Automate)

    cell_size: int >=0
    C: Cell matrix
