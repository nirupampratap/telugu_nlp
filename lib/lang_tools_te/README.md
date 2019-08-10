# Telugu Part of Speech (POS) Tagger

## Usage:

We support only UNIX based systems. There is nothing to do to install.

To tag the sample file given in this software, run this command

>     make tag

The sample file provided with the tool is [telugu.input.txt](https://bitbucket.org/sivareddyg/telugu-part-of-speech-tagger/src/master/telugu.input.txt). When you run the command, a file named `telugu.output.txt` will be created. For more tagging options, modify the Makefile.

For a sample output, see [telugu.sample.out.txt](https://bitbucket.org/sivareddyg/telugu-part-of-speech-tagger/src/master/telugu.sample.out.pdf).

## Output Format:

The output format contains the following columns separated by tab space.

| word | lemma |  **POS tag** | suffix | coarse pos | gender | number | case marker |
| :------: |:-----:| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | 
|మీకోసం |మీరు | **NN** | కోసం | pn | any | pl | 2 |  |

You probably require only the first 3 columns. The main pos tag is highlighted in bold.

## Tagset:

We use IIIT Tagset described in [posguidelines.pdf](https://bitbucket.org/sivareddyg/telugu-part-of-speech-tagger/src/master/posguidelines.pdf) (Bharati et al., 2006). 


```

Fine Grained Tags ~~300 discarding low frequent tags.
Main POS Tag        25     CC, JJ, NN, VM, . . .
Coarse POS Tag      9      adj, n, num, unk . . .
Gender              6      any, f, m, n, punc, null
Number              4      any, pl, sg, null
Person              5      1, 2, 3, any, null
Case                3      d, o, null

```


## Citation:

Please cite either [http://sivareddy.in/downloads](http://sivareddy.in/downloads) or the reference below. Paper can be downloaded from: http://sivareddy.in/papers/clia2011IndianCrossLang.pdf

```

@InProceedings{reddy-sharoff:2011:CLIA5,
  author    = {Reddy, Siva  and  Sharoff, Serge},
  title     = {Cross Language POS Taggers (and other Tools) for Indian Languages: An Experiment with Kannada using Telugu Resources},
  booktitle = {Proceedings of the Fifth International Workshop On Cross Lingual Information Access},
  month     = {November},
  year      = {2011},
  address   = {Chiang Mai, Thailand},
  publisher = {Asian Federation of Natural Language Processing},
  pages     = {11--19},
  url       = {http://www.aclweb.org/anthology/W11-3603}
}

```

This work is supported by Intellitext [1] project and Lexical Computing Ltd [2] (Sketch Engine)
[1] http://corpus.leeds.ac.uk/it/
[2] http://www.sketchengine.co.uk/?page=Website/Company

## Description

The tagger is similar to Model 5 described in Table 2 of (Reddy and Sharoff 2011), but with a focus on Telugu. Short synopsis is presented below. 

Large web corpora of Telugu is downloaded and cleaned, and tagged with with a high precision but low recall tagger. Morph analyzer is also run on this data. The tagger learns morphological analysis and pos tagging at the same time, there by pos tagging getting befitted from morphological analysis and vice versa. Since the tagger is trained on large data, the tagger is expected to handle large vocabulary, and also predicting the tags of unknown words using known words.

Current tagger is based on TnT tagger. TnT Tagger is well known for its robustness and speed, however it initially loads lex and trigram files which make take time to load. Once the loading is finished, we expect the tagger to be very fast.

## License:

The model files are distributed under GNU GPL license. Feel free to use, modify, and redistribute the files as necessary. But the TnT tagger binary files are free only for research purposes (Get a license of TnT from http://www.coli.uni-saarland.de/~thorsten/tnt/)

This work is supported by [Intellitext](http://corpus.leeds.ac.uk/it/) project and [Lexical Computing Ltd (Sketch Engine)](http://www.sketchengine.co.uk/?page=Website/Company)

## Contact:

For additional corpora and tools for other languages, please email your queries to siva@sivareddy.in

## Training Details:

Trained on a corpus containing 3,152,199 tokens.

Lexicon contains 365591 tokens.

## Evaluation Results of Main POS tag:

```

Equal	 :   19463 /  21452 ( 90.73%)
Different:    1989 /  21452 (  9.27%)

Tag  Freq   Prec         Rec        F-Measure
=============================================   
NN  6754    0.837423    0.944922    0.887930
SYM 4963    0.999526    0.850494    0.919007
VM  4469    0.925830    0.960841    0.943011
PRP 1075    0.977591    0.973953    0.975769
NNP 677 0.817787    0.556869    0.662566
NST 546 0.951493    0.934066    0.942699
JJ  458 0.884444    0.868996    0.876652
RB  424 0.847599    0.957547    0.899225
QC  335 0.950292    0.970149    0.960118
WQ  327 0.945161    0.896024    0.919937
PSP 276 0.925676    0.992754    0.958042
DEM 254 0.988327    1.000000    0.994129
UT  191 0.974093    0.984293    0.979167
INTF    156 0.847561    0.891026    0.868750
QF  137 0.906977    0.854015    0.879699
RP  118 0.876106    0.838983    0.857143
CC  88  0.766355    0.931818    0.841026
RDP 46  0.833333    0.326087    0.468750
INJ 38  0.916667    0.578947    0.709677
CL  12  1.000000    0.916667    0.956522
QO  9   1.000000    1.000000    1.000000

```

## Acknowledgements:

[Avinesh PVS](http://www.avineshpvs.com/)

## References:

Bharati, Akshar, Rajeev Sangal, Dipti Misra Sharma, and Lakshmi Bai. "Anncorra: Annotating corpora guidelines for pos and chunk annotation for indian languages." LTRC-TR31 (2006).

Reddy, Siva, and Serge Sharoff. "Cross language POS taggers (and other tools) for Indian languages: An experiment with Kannada using Telugu resources." Cross Lingual Information Access (2011): 11.