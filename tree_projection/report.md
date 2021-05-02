# TREE PROJECTION
## _REPORT_

I implemented a naive implementation of tree projection. For each target token, a source head is copied if no cycle will be created. Additionally, the source sentence is traversed in a BFS manner.

I also ensure the tree is rooted and there is exactly one root (during copying of DEPREL from source, I track which token is the root in target; only the last assigned root is the root in the final tree) and all nodes have a head (I check the nodes and assign them root as head if they do not have one).

## Tree projection

Few results (see `results` file for all results):

### CS <-> EN

| source | target |        HEAD        |        DEPREL       |         LAS        |
|:------:|:------:|:------------------:|:-------------------:|:------------------:|
|   en   |   cs   | 0.3320795271359484 | 0.39145620634067707 | 0.1890918860827512 |
|   cs   |   en   | 0.2853702304495655 | 0.38061956932376273 | 0.1785039667548167 |

### SV <-> EN (best)

| source | target |        HEAD        |       DEPREL       |         LAS        |
|:------:|:------:|:------------------:|:------------------:|:------------------:|
|   en   |   sv   | 0.5675264758309742 | 0.6353675159903533 | 0.4431687113348013 |
|   sv   |   en   | 0.4931054023422743 | 0.6221666037023045 | 0.3894030978466188 |

## Delexicalized parsing

I reuse delexicalized parsers from the previous assignment.

| source   |  parser  |          results         |
|----------|:--------:|:------------------------:|
| cs delex | cs delex | UAS: 80.37%, LAS: 73.84% |
| cs delex | en delex | UAS: 54.25%, LAS: 47.44% |
| en delex | en delex | UAS: 80.36%, LAS: 77.59% |
| en delex | cs delex | UAS: 63.25%, LAS: 56.19% |

| source   |  parser  |          results         |
|----------|:--------:|:------------------------:|
| en delex | sv delex | UAS: 64.58%, LAS: 58.61% |
| sv delex | en delex | UAS: 74.52%, LAS: 65.34% |


We see that the naive implementation of tree projection is significantly worse compared with the delexicalized parsing.    