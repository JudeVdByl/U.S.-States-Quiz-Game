
# U.S. States Quiz Game

![Game board](blank_states_img.gif)

A lightweight Python turtle-graphics game that challenges you to name all 50 U.S. states.

## How it works
Run the program and a blank U.S. map appears. Type the name of a state into the prompt. If you’re correct, the name is written on the map at the proper location and your score increases. Type `Exit` at any time to end the session and see which states you missed.

## Prerequisites
- Python 3.9 or later  
- pandas

## Installation
1. Clone or download this repository.  
2. Install the required package:

   ```
   pip install pandas

## Running the game

From the project directory, execute:

```
python main.py
```

## Project files

| File                   | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| `main.py`              | Core game logic                              |
| `50_states.csv`        | State names with screen coordinates          |
| `learning_states.csv`  | Auto-generated list of states still to learn |
| `blank_states_img.gif` | Map image used as the game board             |

## License

Distributed under the MIT License.
