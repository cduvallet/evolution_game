# The game

This game was developed for the [Young Leaders in STEM](http://www.scienceclubforgirls.org/teen-programs-overview) summer program led by the [Cambridge Science Club for Girls](http://www.scienceclubforgirls.org/).

It was developed as part of a 3-day lesson on bacteria and the human microbiome to teach concepts about mutation, diversity, selection, and evolution.

It can be simulated using this code or played with a classroom of students.

# Simulating the game

# Playing the game

## Materials
* Students, to be divided into 3 groups
* 2 6-faced die per student
  * Game can also be played with 3 die. This makes the evolutionary dynamics different. Empirically (from this code), I prefer using 2 die.
* Writing materials

## Starting the game

All students start with the same 12 base pair sequence. I've tested this code with the starting sequence `ATGGTACGATCG` and it seems to work pretty well.

## Part 1: Diversity generation

Have each student roll their die twice. 
* The first roll indicates which base pair location will be mutated. 
* The second roll decides what happens to that base pair. Use the following table to determine what happens to the base pair:
  | Die roll | Action       |
  |----------|--------------|
  | 2        | mutate to `A`|
  | 3        | mutate to `T`|
  | 4-10     |    nothing   |
  | 11       | mutate to `C`|
  | 12       | mutate to `G`|

###### Note: this decision table is encoded in `p_mut` in the `load_data.py` module. There is also a decision table available for 3-die games.

After N rounds of mutation, ask the students to write their sequences on the board and ask them to count how many unique sequences now exist.

#### Learning outcome

Even though mutations are relatively rare, they lead to a lot of diversity!

## Part 2: Selection

Before starting Part 2, talk to your students about how DNA codes for proteins and show them a [DNA codon table](https://en.wikipedia.org/wiki/DNA_codon_table).

Split the class into three groups, and place each group into *soil*, *ocean*, or *gut* environments.

Have the students translate their sequences into proteins. Have them use the following tables to determine whether their microbe can survive in its new environment.

###### Note: these survival 'rules' are encoded in `die_dict` and `save_dict` in the `load_data` module.

If any of the codons are the STOP codon, the bacteria does not survive.

##### Gut

| Position | Function           | Amino acids   | Specific function                                | Fate                                                                        |
|----------|--------------------|---------------|--------------------------------------------------|-----------------------------------------------------------------------------|
| 1        | growth rate        | S, P, T, A    | Persistence, bacteria can go into 'dormant' mode | Bacteria that don't have antibiotic resistance but do have this can survive |
| 2        | protection         | H, N, Q, V, Y | Antibiotic resistance                            | Bacteria without this don't survive                                         |
| 3        | metabolism         |               |                                                  | All bacteria can survive - there's lots of food in the gut! :D              |
| 4        | oxygen requirement | H, K, D, E    | Aerobic, bacteria needs oxygen to survive        | Bacteria with this don't survive                                            |

##### Soil

| Position | Function           | Amino acids            | Specific function                                                                   | Fate                                                                |
|----------|--------------------|------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 1        | growth rate        | F, L, I, V             | High growth rate, gives bacteria the ability to adapt quickly to new open niches    | Bacteria without this don't survive                                 |
| 2        | protection         | A, E, D, F, I, L, V    | Cell wall anti-phage protein                                                        | Bacteria without this don't survive                                 |
| 3        | metabolism         | D, E, Y, V, C, S, K, R | Allows the bacteria to eat a very specific nutrient (that other bacteria can't eat) | Bacteria that don't have a high growth but do have this can survive |
| 4        | oxygen requirement | T, S, Y, Q, N          | Strict anaerobe, bacteria can only survive in no-oxygen conditions                  | Bacteria with this don't survive                                    |

##### Ocean

| Position | Function           | Amino acids         | Specific function                                                                    | Fate                                                                        |
|----------|--------------------|---------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 1        | growth rate        | F, I, L, V          | low growth rate, bacteria doesn't need a lot of energy to survive                    | Bacteria without this don't survive                                         |
| 2        | protection         |                     |                                                                                      | All bacteria survive - predators are dilute enough that bacteria can escape |
| 3        | metabolism         | F, K, N, P, S, T    | broad metabolism, bacteria can eat a wide variety of things                          | Bacteria without this don't survive                                         |
| 4        | oxygen requirement | F, L, I, M, V, A, P | facultative anaerobe, bacteria can surive in both aerobic and anaerobic environments | Bacteria that don't have broad metabolism but do have this can survive      |

## Part 2: Selection
Questions for class
- Does it take more or less time for diversity to be generated when you add selection? Why?
	- More time, because much of the diversity generated does not surive
- Which protein locations seem to be most diverse? Which ones are least diverse? Why?
	- Proteins which provide bacteria an essential function are least diverse, because if a microbe is missing that specific protein then it dies and does not reproduce.
	- Proteins which give bacteria an additional function (i.e. can save it from death due to a lacking protein elsewhere) are intermediate diverse - in most cases, they don't matter, but in some, they matter a lot.
	
- environments with selective pressures limit the types of organisms that can grow
- diversity is generated, but much slower
	- and diversity is limited to non-essential functions
	- or ones that give the bug an advantage