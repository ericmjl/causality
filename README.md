---
pagetitle: ericmjl/causality
---

![](https://travis-ci.org/ericmjl/causality.svg?branch=master)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ericmjl/causality/master)

# causality

A small repo in which I play with the ideas of causal modelling.

# why this repo exists

I'm interested in causal modelling; having read Judea Pearl's [The Book of Why: The New Science of Cause and Effect](https://www.amazon.com/Book-Why-Science-Cause-Effect-ebook/dp/B075CR9QBJ/ref=cm_cr_arp_d_product_top?ie=UTF8), I then followed up with Jonas Peters' [mini-course on causality](https://www.youtube.com/playlist?list=PLW01hpWnEtbTcuY0a0jhZyanHX3GPImAy). Pearl's book is a good layman's introduction to the history of causal inference research, even if mostly written from the viewpoint of one deeply invested in the field. Peters' lecture series turns out to be a great follow-up to the book.

# getting started

## installation

To get started, install the packages as specified in the `environment.yml` conda specification file.

```
$ conda env create -f environment.yml
```

If you prefer to install by pip, install the packages listed there manually. (They are all available on PyPI.)


## running the notebooks

There are two options for running the notebooks. The first one is the simplest: just click on the Binder icon below.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ericmjl/causality/master)

The second way assumes you've cloned the repository locally, or have downloaded and unzipped it from GitHub. In your terminal (or command prompt), run the following commands:

```
$ source activate causality
$ jupyter lab
```

# contributing

If you are an expert on causal modelling, and see issues with my notebooks, I would love to hear about them! Please post it as an [issue](https://github.com/ericmjl/causality/issues). I would also love to accept a pull request.
