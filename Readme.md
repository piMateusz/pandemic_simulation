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