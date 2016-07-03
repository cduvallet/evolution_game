# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 21:04:16 2016

@author: Claire
"""


def load_codontable():
    codontable = {'TTT': 'F',
                  'TTC': 'F',
                  'TTA': 'L',
                  'TTG': 'L',
                  'CTT': 'L',
                  'CTC': 'L',
                  'CTA': 'L',
                  'CTG': 'L',
                  'ATT': 'I',
                  'ATC': 'I',
                  'ATA': 'I',
                  'ATG': 'I',
                  'GTT': 'V',
                  'GTC': 'V',
                  'GTA': 'V',
                  'GTG': 'V',
                  'TCT': 'S',
                  'TCC': 'S',
                  'TCA': 'S',
                  'TCG': 'S',
                  'CCT': 'P',
                  'CCC': 'P',
                  'CCA': 'P',
                  'CCG': 'P',
                  'ACT': 'T',
                  'ACC': 'T',
                  'ACA': 'T',
                  'ACG': 'T',
                  'GCT': 'A',
                  'GCC': 'A',
                  'GCA': 'A',
                  'GCG': 'A',
                  'TAT': 'Y',
                  'TAC': 'Y',
                  'TAA': '_',
                  'TAG': '_',
                  'CAT': 'H',
                  'CAC': 'H',
                  'CAA': 'Q',
                  'CAG': 'Q',
                  'AAT': 'N',
                  'AAC': 'N',
                  'AAA': 'K',
                  'AAG': 'K',
                  'GAT': 'D',
                  'GAC': 'D',
                  'GAA': 'E',
                  'GAG': 'E',
                  'TGT': 'C',
                  'TGC': 'C',
                  'TGA': '_',
                  'TGG': 'W',
                  'CGT': 'R',
                  'CGC': 'R',
                  'CGA': 'R',
                  'CGG': 'R',
                  'AGT': 'S',
                  'AGC': 'S',
                  'AGA': 'R',
                  'AGG': 'R',
                  'GGT': 'G',
                  'GGC': 'G',
                  'GGA': 'G',
                  'GGG': 'G'}
    return codontable

def load_p_mut(num_die=2):
    if num_die == 3:
        p_mut = {2: 'A',
                 3: 'T',
                 4: 'nothing',
                 5: 'nothing',
                 6: 'nothing',
                 7: 'nothing',
                 8: 'nothing',
                 9: 'nothing',
                 10: 'nothing',
                 11: 'nothing',
                 12: 'nothing',
                 13: 'nothing',
                 14: 'nothing',
                 15: 'C',
                 16: 'G',
                 17: 'G',
                 18: 'C'}
    else:
        p_mut = {2: 'A',
                 3: 'T',
                 4: 'nothing',
                 5: 'nothing',
                 6: 'nothing',
                 7: 'nothing',
                 8: 'nothing',
                 9: 'nothing',
                 10: 'nothing',
                 11: 'C',
                 12: 'G'}
    return p_mut
    
def load_selection_dict():
    ## Need to figure out (1) how to encode die/live/die only if don't have this other thing
    ## Need to figure out which codons to assign to which thing!
    die_dict = {'soil': {1: ['A', 'C', 'E', 'D', 'G', 'H', 'K', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'Y', '_'],
                         2: ['C', 'G', 'H', 'K', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'Y', '_'],
                         3: ['_'],
                         4: ['T', 'S', 'Y', 'Q', 'N', '_']
                         },
                'gut': 
                        {1: ['_'],
                         2: ['A', 'C', 'E', 'D', 'G', 'F', 'I', 'K', 'L', 'P', 'S', 'R', 'T', 'W', '_'],
                         3: ['_'],
                         4: ['H', 'K', 'D', 'E', '_']
                         },
                'ocean': 
                        {1: ['A', 'C', 'E', 'D', 'G', 'H', 'K', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'Y', '_'],
                         2: ['_'],
                         3: ['A', 'C', 'E', 'D', 'G', 'I', 'H', 'L', 'Q', 'R', 'W', 'V', 'Y', '_'],
                         4: ['_']
                         }
                }
                
    save_dict = {'soil': {1: [],
                          2: [],
                          3: ['D', 'E', 'Y', 'V', 'C', 'S'], 
                          4: []},
                 'gut': { 1: ['S', 'P', 'T', 'A', 'M',' Y'],
                          2: [],
                          3: [],
                          4: []},
                 'ocean': {1: [],
                           2: [],
                           3: [],
                           4: ['F', 'L', 'I', 'M', 'V', 'A', 'P']}
                 }
                 
    return die_dict, save_dict
#def load_p_transition():
#    p_trans = {'A': 
#                {'A': 
#                 'T':
#                 'C': }
#        }