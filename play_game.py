# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 21:11:57 2016

@author: Claire
"""

import load_data
import numpy as np
import argparse
import copy


def roll_die(size=None, num_die=2):
    if num_die == 3:
        return np.random.randint(1,7, size=size) + np.random.randint(1,7, size=size) + np.random.randint(1,7, size=size)
    else:
        return np.random.randint(1,7, size=size) + np.random.randint(1,7, size=size)

def mutate_seq(seq, loc, mut, p_mut):
    # Mutate one sequence at location loc given mutationg mut and probability of
    # mutations p_mut (dict)
    if p_mut[mut] != 'nothing':
        seq = seq[:loc] + p_mut[mut] + seq[loc+1:]
    return seq

def mutate_seqs(seqs, loc_rolls, mut_rolls, p_mut):
    # Given a list of seqs, a list of rolls to determine location to mutate,
    # a list of rolls to determine what mutation to make, and a dictionary
    # indicating what roll gives what mutation, mutate the array of sequences.
    # seqs, loc_rolls, and mut_rolls should all be same lengths
    for i in range(0, len(seqs)):
        seq = seqs[i]
        # Get bp location to mutate
        loc = loc_rolls[i] - 1
        # Get the roll for the 'mutation' decision
        mut = mut_rolls[i]
        seq = mutate_seq(seq, loc, mut, p_mut)
        seqs[i] = seq
    return seqs

def translate_seq(seq, codontable):
    # codontable is a dict of {codon: aa}
    prot = ''
    for i in range(0, len(seq)/3):
        c = seq[3*i:3*(i+1)]
        prot += codontable[c]
    return prot 
    
def translate_seqs(seqs, codontable):
    prots = []
    for i in range(0, len(seqs)):
        prots.append(translate_seq(seqs[i], codontable))
    return prots

def select_prots(prots, environments, die, save):
    newprots = copy.copy(prots)
    
    for i in range(0, len(prots)):
        env = environments[i]
        prot = prots[i]
        for j in range(0,len(prot)):
            if prot[j] in die[env][j+1]:
                if prot[j] not in save[env][j+1]:
                    prot = "dead"
                    break
        newprots[i] = prot
    
    return newprots

def update_prots(prots, env2s, s2env):
    for p in range(0, len(prots)):
        if prots[p] == 'dead':
            for p2 in env2s[s2env[p]]:
                if prots[p2] != 'dead':
                    prots[p] = prots[p2]
                    seqs[p] = seqs[p2]
                    break
    return prots, seqs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='starting sequence. Should be length 12', default='ATCGTACGATCC')    
    parser.add_argument('-n', help='number of students in class.', default=15, type=int) 
    parser.add_argument('-m', help='number of rounds of mutation (part 1: generate diversity)', default=10, type=int)
    parser.add_argument('-x', help='number of rounds of mutation between each selection event (part 2: selection)', default=5, type=int)
    parser.add_argument('-d', help='number of die. accepts 2 or 3', default=2, type=int)
    args = parser.parse_args()
    
    # Initialize all students with same sequence
    seqs = np.array(args.n * [args.s])
    
    ## Load up dict with probablity of mutation given roll    
    p_mut = load_data.load_p_mut(num_die=args.d)
    
    ## Part 1: Generating diversity
    print('----------------\nROUND ONE - MUTATION\n----------------')
    # After m rounds of mutation, how many unique sequences does the class have?
    for i in range(0, args.m):
        loc_rolls = roll_die(seqs.shape)
        mut_rolls = roll_die(seqs.shape, num_die=args.d)
        seqs = mutate_seqs(seqs, loc_rolls, mut_rolls, p_mut)        
        print('After {} rounds of mutation, there are {} unique sequences'.format(i+1, len(set(seqs))))
    
    ## Part 2: Selecting for function
    print('----------------\nROUND TWO - SELECTION\n----------------')

    codontable = load_data.load_codontable()

    ## Split the class into 3 groups, put them in environments
    env2s = {'soil': range(0, len(seqs))[::3],
                    'gut': range(0,len(seqs))[1::3],
                    'ocean': range(0, len(seqs))[2::3]}
    s2env = {i: 'soil' for i in range(0, len(seqs))[::3]}
    s2env.update({i: 'gut' for i in range(0, len(seqs))[1::3]})
    s2env.update({i: 'ocean' for i in range(0, len(seqs))[2::3]})
    
    
    ## Select, mutate, select, etc...
    die, save = load_data.load_selection_dict()    

    for i in range(0, args.x):    
        # Translate proteins        
        prots = translate_seqs(seqs, codontable)
        # Select proteins according to environment and die/save rules
        prots = select_prots(prots, s2env, die, save)
        # Get the sequences and proteins that survived
        # Student whose bacteria died get a remaining sequence from their same environment
        prots, seqs = update_prots(prots, env2s, s2env)
        
        # Count number of unique organisms in each environment
        print('After {} rounds of selection, this is what we have:'.format(i))
        print('\tgut: ' + ', '.join(set([prots[i] for i in env2s['gut']])))      
        print('\tsoil: ' + ', '.join(set([prots[i] for i in env2s['soil']])))
        print('\tocean: ' + ', '.join(set([prots[i] for i in env2s['ocean']])))
        
        # Mutate sequences again
        loc_rolls = roll_die(seqs.shape)
        mut_rolls = roll_die(seqs.shape, num_die=args.d)
        seqs = mutate_seqs(seqs, loc_rolls, mut_rolls, p_mut)