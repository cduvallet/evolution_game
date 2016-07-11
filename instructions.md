# The game

This game was developed for the [Young Leaders in STEM](http://www.scienceclubforgirls.org/teen-programs-overview) summer program led by the [Cambridge Science Club for Girls](http://www.scienceclubforgirls.org/).

It was developed as part of a 3-day lesson on bacteria and the human microbiome to teach concepts about mutation, diversity, selection, and evolution.

# Playing the game

## Starting the game

All students start with the same 12 base pair sequence. I've tested this with the starting sequence `ATGGTACGATCG` and it seems to work pretty well.

### Part 1: Diversity generation

Roll your die twice. 
* The first roll indicates which base pair location will be mutated. 
* The second roll decides what happens to that base pair. Use the following table to determine what happens to the base pair:

| Die roll | Action        |
|----------|---------------|
| 2        | Mutate to `A` |
| 3        | Mutate to `T` |
| 4-10     | Do nothing    |
| 11       | Mutate to `C` |
| 12       | Mutate to `G` |

Do this for 10-15 rounds.

##### Learning outcome

Even though mutations are relatively rare, they lead to a lot of diversity!

### Part 2: Selection

Split the class into three groups, and place each group into *soil*, *ocean*, or *gut* environments.

Translate your sequences into proteins. Then, use the following tables to determine whether your microbe can survive in its new environment. If any of the codons are the STOP codon, the bacteria does not survive.

#### Gut

| Position | Function           | Amino acids   | Specific function                                | Fate                                                                        |
|----------|--------------------|---------------|--------------------------------------------------|-----------------------------------------------------------------------------|
| 1        | growth rate        | S, P, T, A    | Persistence, bacteria can go into 'dormant' mode | Bacteria that don't have antibiotic resistance but do have this can survive |
| 2        | protection         | H, N, Q, V, Y | Antibiotic resistance                            | Bacteria without this don't survive                                         |
| 3        | metabolism         |               |                                                  | All bacteria can survive - there's lots of food in the gut! :D              |
| 4        | oxygen requirement | H, K, D, E    | Aerobic, bacteria needs oxygen to survive        | Bacteria with this don't survive                                            |

#### Soil

| Position | Function           | Amino acids            | Specific function                                                                   | Fate                                                                |
|----------|--------------------|------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 1        | growth rate        | F, L, I, V             | High growth rate, gives bacteria the ability to adapt quickly to new open niches    | Bacteria without this don't survive                                 |
| 2        | protection         | A, E, D, F, I, L, V    | Cell wall anti-phage protein                                                        | Bacteria without this don't survive                                 |
| 3        | metabolism         | D, E, Y, V, C, S, K, R | Allows the bacteria to eat a very specific nutrient (that other bacteria can't eat) | Bacteria that don't have a high growth but do have this can survive |
| 4        | oxygen requirement | T, S, Y, Q, N          | Strict anaerobe, bacteria can only survive in no-oxygen conditions                  | Bacteria with this don't survive                                    |

#### Ocean

| Position | Function           | Amino acids         | Specific function                                                                    | Fate                                                                        |
|----------|--------------------|---------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 1        | growth rate        | F, I, L, V          | low growth rate, bacteria doesn't need a lot of energy to survive                    | Bacteria without this don't survive                                         |
| 2        | protection         |                     |                                                                                      | This one isn't so important - predators are dilute enough that bacteria can escape |
| 3        | metabolism         | F, K, N, P, S, T    | broad metabolism, bacteria can eat a wide variety of things                          | Bacteria without this don't survive                                         |
| 4        | oxygen requirement | F, L, I, M, V, A, P | facultative anaerobe, bacteria can surive in both aerobic and anaerobic environments | Bacteria that don't have broad metabolism but do have this can survive      |

If a your bacteria does not survive, replace your sequence with one from your group which did survive. If no bacteria in the entire group (environment) survived, make a sequence up that would survive and go with that.

Go through 15 more rounds of mutation and selection. Like in Part 1, roll the die to decide the location and type of mutation to happen. Then, translate the sequence into amino acids, and determine the fate of your new bacteria.

##### Questions for the the class
- Does it take more or less time for diversity to be generated when you add selection? Why?
- Which protein locations seem to be most diverse? Which ones are least diverse? Why?

##### Learning outcomes	
- Environments with selective pressures limit the types of organisms that can survive
- Diversity is still generated, but at a much slower rate than just random mutations
	- The most diverse proteins are those that have non-essential functions
	- Or ones that give the bug an advantage
- Bonus question: how do we define bacterial species?

# Simulating the game

You can find a python script to simulate the game at www.github.com/cduvallet/evolution_game

Run `python play_game.py`. 

You can change the starting sequence (`-s`), the number of students in the class (`-n`), the number of rounds of mutation in Part 1 (`-m`), the number of rounds of mutation/selection in Part 2 (`-x`), and the number of die (`-d`) from the command line.

You can change whether and how a base pair is mutated in `load_p_mut` and the selection rules in `load_selection_dict` in `load_data.py`.

## Example

```text
$ python play_game.py
---------------------
ROUND ONE - MUTATION
---------------------
After 1 rounds of mutation, there are 3 unique sequences
After 2 rounds of mutation, there are 4 unique sequences
After 3 rounds of mutation, there are 5 unique sequences
After 4 rounds of mutation, there are 5 unique sequences
After 5 rounds of mutation, there are 6 unique sequences
After 6 rounds of mutation, there are 8 unique sequences
After 7 rounds of mutation, there are 10 unique sequences
After 8 rounds of mutation, there are 10 unique sequences
After 9 rounds of mutation, there are 10 unique sequences
After 10 rounds of mutation, there are 10 unique sequences
---------------------
ROUND TWO - SELECTION
---------------------
After 0 rounds of selection, this is what we have:
        gut: MERS, MVRS
        soil: MVRC
        ocean: MVRS, MVPP, MVCS
After 1 rounds of selection, this is what we have:
        gut: IVRS, MERS, MVRS
        soil: MVRC
        ocean: MVRS, MVPP, MVCS
After 2 rounds of selection, this is what we have:
        gut: IVRS, MERS, MVRS
        soil: MVRC, MVPC
        ocean: MVRS, MVPP, MVCS
After 3 rounds of selection, this is what we have:
        gut: IVRS, MERS, MVRS, KERS
        soil: MVRC, MVPC
        ocean: MVRS, MVPP, MVCS
After 4 rounds of selection, this is what we have:
        gut: IVRS, MERP, MVLS, MVRS, KERS
        soil: MVRC, MVPC, MLRC
        ocean: MVRS, MVPP
```
