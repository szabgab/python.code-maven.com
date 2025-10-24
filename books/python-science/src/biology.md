# Python and Biology

## General Bioinformatics Frameworks

These libraries provide broad biological functionality (sequence analysis, file parsing, etc.):

* [Biopython](https://biopython.org/) - The de facto standard library for bioinformatics in Python.  Tools for parsing FASTA/GenBank, working with sequences, BLAST, alignments, phylogenetics, etc.
* [Scikit-bio](http://scikit-bio.org) - Bioinformatics and computational biology toolkit built on NumPy. Focus on microbiome analysis, sequence data, diversity metrics, and statistics.
* [BioPandas](https://biopandas.github.io/biopandas/) - Extends pandas for structural biology data (PDB, mmCIF). Integrates molecular data frames with protein 3D structure parsing.

## Genomics / Transcriptomics

Libraries for working with genome sequences, reads, and expression data:

* [pysam](https://pysam.readthedocs.io/) - Python interface to SAMtools and BCFtools.  For reading/writing SAM/BAM/VCF files efficiently.
* [pybedtools](https://daler.github.io/pybedtools/) - Python wrapper around BEDTools. For genome interval operations (overlaps, unions, intersections).
* [HTSeq](https://htseq.readthedocs.io//) - For analyzing high-throughput sequencing (RNA-Seq, etc.). Counts reads, annotates features, handles GFF/GTF formats.
* [anndata](https://anndata.readthedocs.io/) - Data structure for annotated data matrices (used in single-cell). Foundation for many single-cell analysis tools (e.g. scanpy).
* [scanpy](https://scanpy.readthedocs.io/) - Analysis toolkit for single-cell RNA-seq data. Supports clustering, visualization, trajectory inference, etc.
* [pyranges](https://github.com/pyranges/pyranges) - Fast genomic interval operations in pure Python. Like pybedtools, but implemented with pandas for speed.
* [cyvcf2](https://brentp.github.io/cyvcf2/) - Fast VCF parser and query tool.

## Proteomics and Structural Biology

Working with proteins, molecular dynamics, and structural data:

* [MDAnalysis](https://www.mdanalysis.org/) - Analyze molecular dynamics trajectories. Supports many formats (GROMACS, AMBER, etc.).
* [ProDy](http://www.bahargroup.org/prody/) - For protein structure and dynamics analysis.
* [PyMOL API](https://pymol.org/) - Python interface to PyMOL for visualizing 3D molecular structures.
* [biotite](https://www.biotite-python.org/) - Structural bioinformatics and sequence analysis; fast and modern.

## Phylogenetics and Evolution

Tools for working with trees, evolutionary analysis, and alignments:

* [ETE Toolkit](https://etetoolkit.org/) - Phylogenetic tree analysis, visualization, and manipulation.
* [DendroPy](https://github.com/jeetsukumaran/DendroPy) - For phylogenetic computing with trees and taxon data.
* [toytree](https://eaton-lab.org/toytree/) - Lightweight and fast tree visualization and manipulation.

## Systems Biology & Pathways

Libraries for metabolic models, pathways, and systems simulation:

* [COBRApy](https://cobrapy.readthedocs.io/) - Constraint-based modeling for metabolic networks.
* [Tellurium](https://tellurium.analogmachine.org/) - Modeling and simulation of biochemical networks.
* [libSBML](https://sbml.org/software/libsbml/) - Work with SBML (Systems Biology Markup Language).
* [PySCeS](https://pysces.sourceforge.net/) - Python Simulator for Cellular Systems.

## Microbiome and Metagenomics

* [QIIME 2 API](https://amplicon-docs.qiime2.org/) - Framework for microbiome analysis and reproducibility.
* [biom-format](http://biom-format.org/) - Read/write BIOM tables (Biological Observation Matrix format).

## Population Genetics

* [msprime](https://tskit.dev/software/msprime.html) - Efficient simulation of population genetic data.
* [tskit](https://tskit.dev/software/tskit.html) - Tree sequence toolkit for storing and analyzing genealogical data.

## Cheminformatics

(Overlaps with computational chemistry, but widely used in drug design and molecular biology)

* [RDKit](https://www.rdkit.org/) - Standard for cheminformatics: molecular fingerprints, descriptors, SMILES parsing.
* [Open Babel (Pybel)](https://open-babel.readthedocs.io/) - Chemical toolbox for converting between molecular file formats.






