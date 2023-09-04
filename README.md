# Mi primera calculadora

El proyecto consiste en una calculadora que realiza operaciones basicas, medias y avanzadas.
## Estructura del programa

```
my_calculadora
├── modules
│   ├── check_data
│   │   └── check_data.py
│   ├── interfaz
│   │   └── menu.py
│   ├── math_basic
│   │   └── operations_basic.py
│   ├── math_middle
│   │   ├── comparison.py
│   │   ├── factorial.py
│   │   ├── mcd.py
│   │   └── mcm.py
│   ├── math_advanced
│   │   └──fibonacci.py
├── tests
│   ├── test_basic_math.py
│   ├── test_middle.py
│   └── test_advanced.py
├── main.py
└── README.md
```

## Modulos

### `operations_basic`

El modulo contiene las operaciones basicas.

### `comparison.py`

El modulo contiene las operaciones de comparacion.
### `fibonacci.py`

El modulo contiene la operacion de fibonacci.
### `factorial.py`

El modulo contiene la operacion de factorial.
### `mcm.py`

El modulo contiene la operacion de mcm.
### `mcd.py`

El modulo contiene la operacion de mcd.
### `menu.py`

El modulo contiene el menu de la calculadora.
## Utilizar el menu

Para utilizar el menu se debe importar el modulo menu.py.

```python
from my_calculadora.modules import menu