# Homology Modeling
This tutorial aims to model modeling the structure of Siglec-7 using the [MODELLER](https://salilab.org/modeller). You can download by clicking in Code --> Download Zip. Unzip this file and go inside modeller directory. 

## Template Selection: 
PDB database and search for protein ID: [1O7S](https://www.rcsb.org/structure/1O7S) (The second letter is O as in Oxford and not zero) or [1O7V](https://www.rcsb.org/structure/1O7V). 1O7S is 1.7 A resolution structure of human Siglec-7, a sialic acid lectin. Siglec-7 is N-glycosylated at N107, and it binds with sialic acids and their analogs (See Fig. below)
![fig-1-hSig7-complex](https://user-images.githubusercontent.com/10772897/112083562-47527780-8b55-11eb-9143-99b7cb9a0d91.png)

## Searching human Siglec-7 Homologs: 
First, it is required to save the sequence of Siglec-7  into the PIR format readable by MODELLER (file "query.ali"). We will be referring Siglec-7 sequence as a query sequence and given the name 'Query' through this tutorial and in the script scripts.

```
>P1;Query
sequence:Query:::::::0.00: 0.00
GQKSNRKDYSLTMQSSVTVQEGMCVHVRCSFSYPVDSQTDSDPVHGYWFRAGNDISWKAPVATNNPAWAVQEETR
DRFHLLGDPQTKNCTLSIRDARMSDAGRYFFRMEKGNIKWNYKYDQLSVNVT*
```

The first line contains the sequence name, in the format ">P1;name". The second line with ten fields separated by colons generally contains information about the structure file, if applicable. Only two of these fields are used for sequences, "sequence" and "Query" (the model file name). The rest of the file contains the Query sequence, with "*" marking its end. The standard one-letter amino acid codes (upper case) are used.

A search for potentially homolos sequences of known structure can be performed by the running [NCBI BLAST Webpage](https://blast.ncbi.nlm.nih.gov/Blast.cgi)
Choose Protein Blast, paste query sequence in "Enter Query Sequence" box, and select protein databank proteins in section "database". Let the other parameters be in default (to learn only) and run Blast. We will get results showing the top 10 hits ranked based on their E-value (expected value) in a few seconds. We can see that almost all the homologous hits are sialic acid-binding lectins, molecules from the same class and binding to similar molecules.

The first two hits with nearly 100% sequence identity are naturally the structures of Siglec-7. We have selected a protein with a known structure so that we can compare the homology modeling results at the end. However, we will NOT be using Siglec-7 structural information to model our homology model. Thus, it must be used as template structures. 

Select three hits (Siglec 3, Siglec-5 and Siglec-8). Siglec-3 (another name CD33), Siglec-5 (CD170), Siglec-7 (CD328), and Siglec-8 are all CD33 related Siglecs and have similar structure and functions. In this tutorial, we will choose structures of Siglec-3 (PDB ID: 6D48), Siglec-5 (PDB ID: 2ZG2), and Siglec-8 (2N7A) to build the structure of Siglec-7.


## Align Template Sequences:
Download structures of the above three from the protein data bank webpage and save them inside modeller direcotry. If you have program wget installed (Linux/Mac), structures can also be downloaded using the terminal:

```
wget https://files.rcsb.org/view/6D48.pdb
wget https://files.rcsb.org/view/2ZG2.pdb
wget https://files.rcsb.org/view/2N7A.pdb
wget https://files.rcsb.org/view/1O7V.pdb
```

Now place the script 1_salign.py into the same directory and run:
```
#mod9.25 script 1_salign.py
```

Upon successful completion, this program will align all three structures, their sequences and creates five new files:
```
-rw-r--r--  1 sushil  staff   92982 Mar 22 13:22 2N7A_fit.pdb
-rw-r--r--  1 sushil  staff  134157 Mar 22 13:22 2ZG2_fit.pdb
-rw-r--r--  1 sushil  staff   80105 Mar 22 13:22 6D48_fit.pdb
-rw-r--r--  1 sushil  staff    2286 Mar 22 13:22 fm00495.ali
-rw-r--r--  1 sushil  staff    1256 Mar 22 13:22 fm00495.pap
-rw-r--r--  1 sushil  staff     539 Mar 22 13:22 fm00495.tree
```

The first three files are the aligned structures of the templates. fm00495.ali contains FASTA sequences of these three templates and fm00495.pap contains multiple sequence alignment (MSA) of the three template sequences.

```
_aln.pos         10        20        30        40        50        60
2ZG2A     --------SVYELQVQKSVTVQEGLCVLVPCSFSYPWRSWYSSPPLYVYWFRDGEIPYYAEVVATNNP 
6D48E     -------DPNFWLQVQESVTVQEGLCVLVPCTFFHPIPYYDKNSPVHGYWFREGAIISRDSPVATNKL 
2N7AA     MEGDRQYGDGYLLQVQELVTVQEGLSVHVPCSFSYPQDGWTDSDPVHGYWFRAGDRPYQDAPVATNNP 
 _consrvd             ****  ******* * *** *  *        *   **** *        ****

 _aln.p   70        80        90       100       110       120       130
2ZG2A     DRRVKPETQGRFRLLGDVQKKNCSLSIGDARMEDTGSYFFRVERGRDVKYSYQ------QNKLNLEVT 
6D48E     DQEVQEETQGRFRLLGDPSRNNCSLSIVDARRRDNGSYFFRMERGS-TKYSYK------SPQLSVHVT 
2N7AA     DREVQAETQGRFQLLGDIWSNDCSLSIRDARKRDKGSYFFRLERGS-MKWSYKSQLNYKTKQLSVFVT 
 _consrvd *  *  ****** ****     ***** ***  * ****** ***   * **          *   **

 _aln.pos  140       150       160       170       180       190       200
2ZG2A     ALIEKPDIHFLEPLESGRPTRLSCSLPGSCEAGPPLTFSWTGNALSPLDPETTRSSELTLTPRPEDHG 
6D48E     DLT----------------------------------------------------------------- 
2N7AA     ALTHG--------------------SLVPR-------------------------------------- 
 _consrvd  *

 _aln.pos    210       220
2ZG2A     TNLTCQMKRQQVTTERTVQLNVSL 
6D48E     ------------------------ 
2N7AA     ------------------------ 
 _consrvd

```


## Aligning Query Sequence with Templates:
Now we have to align our query sequence (file _Query.ali_) with the template sequences' MSA. This can be done by running the second script:
```
mod9.25 2_align_2d_mult.py 
```
Two new files, query-mult.ali and _query-mult.pap_ will be created. This step will append previous 'ali' and 'pap' files and add aligned sequences for our query sequences. 
```
2ZG2A     --------SVYELQVQKSVTVQEGLCVLVPCSFSYPWRSWYSSPPLYVYWFRDGEIPYYAEVVATNNP 
6D48E     -------DPNFWLQVQESVTVQEGLCVLVPCTFFHPIPYYDKNSPVHGYWFREGAIISRDSPVATNKL 
2N7AA     MEGDRQYGDGYLLQVQELVTVQEGLSVHVPCSFSYPQDGWTDSDPVHGYWFRAGDRPYQDAPVATNNP 
Query     GQKSNRKDYSLTMQSSVTVQEGMCVHVRCSFSYPVDSQTDSDPVHGYWFRAGNDISWKAPVATNNPAW 
 _consrvd              *    *       *

 _aln.p   70        80        90       100       110       120       130
2ZG2A     DRRVKPETQGRFRLLGDVQKKNCSLSIGDARMEDTGSYFFRVERGRDVKYSYQQNKLNLEVTALIEKP 
6D48E     DQEVQEETQGRFRLLGDPSRNNCSLSIVDARRRDNGSYFFRMERGS-TKYSYK-------SPQLSVHV 
2N7AA     DREVQAETQGRFQLLGDIWSNDCSLSIRDARKRDKGSYFFRLERGS-MKWSYK-SQLNYKTKQLSVFV 
Query     AVQEETRDRFHLLGDPQTKNCTLSIRDARMSDAGRYFFRMEKGNIKWNYKYDQ-LSVNVT-------- 
 _consrvd                        *

 _aln.pos  140       150       160       170       180       190       200
2ZG2A     DIHFLEPLESGRPTRLSCSLPGSCEAGPPLTFSWTGNALSPLDPETTRSSELTLTPRPEDHGTNLTCQ 
6D48E     -------------------------------------------------------------------- 
2N7AA     -------------------------------------------------------------------- 
Query     -------------------------------------------------------------------- 
 _consrvd

 _aln.pos    210       220
2ZG2A     MKRQQVTTERTVQLNVSL 
6D48E     -------TDLT------- 
2N7AA     -------TALTHGSLVPR 
Query     ------------------ 
 _consrvd


```

## Model Siglec-7 Structure:
Now you can run the third script 3_model_protein.py to start homology modeling. 

```
$ mod9.25 3_model_protein.py
```

For learning, this script will generate only 20 models, but that can be changed by changing the value of a.ending_model in the script. In about ~ 10 minutes, the Modeller will generate 10 models and print their dope scores at the end of 3_model_protein.log file. 


##Loop modeling



## Acknowledgment:
This tutorial had been adopted from Modeller tutorials. Please look into MODELLER tutorials for details. https://salilab.org/modeller/tutorial/ 



