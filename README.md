# Optimal Graph Edit Distance Approach (using NetworkX) for Pattern Recognition

<p align="center"> 
<img src="https://github.com/zeinaabuaisheh/Anytime_Graph_Edit_Distance/blob/master/logo-lifat.jpg">
</p>

## Requirements

python 3.6
NetworkX



## Introduction

This repository illustrated the usage of the NetworkX functions (```graph_edit_distance``` and ```optimal_edit_paths```) in Pattern Recognition. 

- ```graph_edit_distance``` returns the distance between two graphs (G1 and G2) which results in transforming the source graph (G1) into the target graph (G2) through the following operations: Deletions, insertions and substitutions of vertices and/or edges.

- ```optimal_edit_paths``` returns all the possible paths whose distance is the minimum (i.e. the optimal distance). Note that most graph edit distance datasets have one and only one solution. However, there are few datasets that could have one or more possible paths with the same minimum or optimal distance.

To be able to use such functions for Pattern Recognition purposes, one needs to define a cost function which is suitable to the graph dataset type (i.e., attributes). In this repository, we show you how to define your cost function and pass it as an input to these NetworkX functions.


## Reference
This optimal graph edit distance approach, referred to as Depth-First Search(DF), has been proposed by Zeina Abu-Aisheh et al:

[Zeina Abu-Aisheh, Romain Raveaux and Jean-Yves Ramel. "Graph Edit Distance for Solving Pattern Recognition Problems." *ICPRAM.* 2015](http://www.rfai.li.univ-tours.fr/PagesPerso/zabuaisheh/documents/icpram.pdf). Please cite:
 
 
```
@inproceedings{DBLP:conf/icpram/Abu-AishehRRM15,
  author    = {Zeina Abu{-}Aisheh and
               Romain Raveaux and
               Jean{-}Yves Ramel and
               Patrick Martineau},
  title     = {An Exact Graph Edit Distance Algorithm for Solving Pattern Recognition
               Problems},
  booktitle = {{ICPRAM} 2015 - Proceedings of the International Conference on Pattern
               Recognition Applications and Methods, Volume 1, Lisbon, Portugal,
               10-12 January, 2015.},
  pages     = {271--278},
  year      = {2015},
  crossref  = {DBLP:conf/icpram/2015-1},
  timestamp = {Tue, 15 Sep 2015 17:18:51 +0200},
  biburl    = {https://dblp.org/rec/bib/conf/icpram/Abu-AishehRRM15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## Inputs

The inputs of this code are graphs whose format is [GXL](http://www.gupro.de/GXL/Introduction/background.html). The first selected dataset in this repository is called GREC and can be downloaded from [here](https://iapr-tc15.greyc.fr/IAM/download-the-iam-graph-database.html). Note that the GREC cost function is defined in ```grec_cost_functions.py```


## Run the Code:

To run the code:

 ``` python GED.py --g1 [THE_PATH_OF_THE_SOURCE_GRAPH] --g2 [THE_PATH_OF_THE_TARGET_GRAPH] ```


## Last but not Least

Please feel free to contribute to this repository and to include more cost functions and datasets for Pattern Recognition purposes



