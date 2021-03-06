Installation
============

As *Sargasso* has a number of dependencies on other Python packages, it is **strongly** recommended to install in an isolated environment using the [virtualenv](http://virtualenv.readthedocs.org/en/latest/index.html) tool. The [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html) tool makes managing multiple virtual environments easier.

Create and work in a virtual environment for *Sargasso* using the ``virtualenvwrapper`` tool:

    mkproject sargasso

Then install the latest version of the *Sargasso* package and its Python package dependencies into the virtual environment by running:

    pip install git+https://github.com/statbio/Sargasso.git
    
Note that the *Sargasso* pipeline uses the [Sambamba](http://lomereiter.github.io/sambamba/) alignment processing tool, and either the [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml) read aligner (for reads originating from DNA sequencing), or the short RNA-seq read aligner [STAR](https://github.com/alexdobin/STAR). These should be installed before using *Sargasso* (though, for example, only STAR needs to be installed if only RNA-seq data is intended to be processed).

[Next: Example usage](example_usage.md)
