# Young Leaders in STEM - Mutation game
> July 11, 2017    
> Claire Duvallet    
> http://github.com/cduvallet/evolution_game

## Materials
* Students, to be divided into 3 groups
* 2 6-faced die per student
  * Game can also be played with 3 die. This makes the evolutionary dynamics different. Empirically (from this code), I prefer using 2 die.
* Writing materials

## Starting the game

All students start with the same 12 base pair sequence:

#### ATGGTACGATCG

### Part 1: Diversity generation

In this part, we will simulate diversity generation through random mutations.

For each round of mutation, you should roll your die twice:
* The first roll indicates which base pair location will be mutated.
* The second roll decides what happens to that base pair. Use the following table to determine what happens to the base pair:

| Die roll | Action        |
|----------|---------------|
| 2        | Mutate to `A` |
| 3        | Mutate to `T` |
| 4-10     | Do nothing    |
| 11       | Mutate to `C` |
| 12       | Mutate to `G` |

After each round of mutation, use the codon table to translate your DNA sequence into a protein.

Write down the DNA sequence and the protein sequence after each round. Do 10 rounds of mutation.

##### Discussion questions and learning outcomes

* How rare are these mutations? How much diversity did they lead to? Is this what you would have expected?
* How does the DNA sequence diversity compare to the protein diversity?

### Part 2: Selection

Now, we'll be adding selection. Not every mutation is equal. Some are beneficial, and help the microbe adapt to a challenging environment. Some are harmful, and cause the bacteria to lose a function or die.

We'll split you into three groups: *soil*, *ocean*, or *gut* environments.

Using your last sequence from Part 1, look at the rules in the tables below to determine whether your microbe will survive in its new environment. If any of the codons are the STOP codon, the bacteria does not survive.

##### Gut

| Position | Function           | Amino acids   | Specific function                                | Fate                                                                        |
|----------|--------------------|---------------|--------------------------------------------------|-----------------------------------------------------------------------------|
| 1        | growth rate        | S, P, T, A    | Sporulation, bacteria can go into 'dormant' mode when they're challenged | Bacteria that don't have antibiotic resistance but do have this can survive |
| 2        | protection         | H, N, Q, V, Y | Antibiotic resistance                            | Humans are constantly taking antibiotics, so bacteria without this don't survive                                         |
| 3        | metabolism         |               |                                                  | All bacteria can survive - there's lots of food in the gut! :D              |
| 4        | oxygen requirement | H, K, D, E    | Aerobic, bacteria needs oxygen to survive        | The human gut doesn't have any oxygen in it, so bacteria with this don't survive                                            |

##### Soil

| Position | Function           | Amino acids            | Specific function                                                                   | Fate                                                                |
|----------|--------------------|------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 1        | growth rate        | F, L, I, V             | High growth rate, gives bacteria the ability to adapt quickly to new open niches    | Soil is a battlefield, bacteria need to be able to adapt quickly to open niches. Bacteria without this don't survive                                 |
| 2        | protection         | A, E, D, F, I, L, V    | Cell wall anti-phage protein                                                        | Soil is teeming with microorganisms, including bacterial viruses! Bacteria without this protein can't fend off virsuses and don't survive                                 |
| 3        | metabolism         | D, E, Y, V, C, S, K, R | Allows the bacteria to eat a very specific nutrient (that other bacteria can't eat) | Bacteria that don't have a high growth but that do have this can survive, because they can eat something that no one else can |
| 4        | oxygen requirement | T, S, Y, Q, N          | Strict anaerobe, bacteria can only survive in no-oxygen conditions                  | Bacteria with this don't survive because soil has oxygen                                    |

##### Ocean

| Position | Function           | Amino acids         | Specific function                                                                    | Fate                                                                        |
|----------|--------------------|---------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 1        | growth rate        | F, I, L, V          | low growth rate, bacteria doesn't need a lot of energy to survive                    | The ocean does not have a lot of nutrients, so bacteria that need a lot of energy (i.e. ones that don't have this) die                                         |
| 2        | protection         |                     |                                                                                      | This one isn't so important - predators are dilute enough that bacteria can escape |
| 3        | metabolism         | F, K, N, P, S, T    | broad metabolism, bacteria can eat a wide variety of things                          | The ocean is very dilute, so bacteria need to be able to eat many different things. Bacteria without this don't survive                                         |
| 4        | oxygen requirement | F, L, I, M, V, A, P | sulfate reduction, bacteria can "breathe" sulfate | Bacteria that don't have a broad metabolism but do have this can survive, because they can make use of something that most other bacteria can't      |

If your bacteria does not survive, you can either replace it with one from your group which did survive, or you can make one up that would have survived and go with that.

Go through 10 more rounds of mutation and selection. Like in Part 1, roll the die to decide the location and type of mutation that happens. After each round of mutation, translate your DNA sequence into amino acids and determine whether your bacteria can survive or not.

Talk with your group: what are some patterns that you notice?

##### Questions for the the class
- What was the difference between parts 1 and 2?
- How does this game relate to evolution? What other aspects of evolution are missing in this game?
- Which protein locations seem to be most diverse? Which ones are least diverse? Why?
