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
* [pyranges](https://github.com/pyranges/pyranges) - Fast genomic interval operations in pure Python. Like pybedtools, but implemented with pandas for speed. Better to use [pyranges_1](https://github.com/pyranges/pyranges_1.x).
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


## More obscure & esoteric Python libraries used in biology

### Genomics & Sequencing

* [dnaio](https://github.com/marcelm/dnaio/) - Fast FASTA/FASTQ reader/writer used under the hood by cutadapt.
* cutadapt (Python API) - Adapter trimming library - most people use the CLI, but it has a Python API.
* python-edlib -  Ultra-fast library for edit distance / approximate sequence alignment (bindings for Edlib C library).
* parasail-python - Bindings to the Parasail SIMD-accelerated pairwise alignment routines.
* mappy - Python bindings to minimap2 for ultra-fast genome mapping.
* pyfaidx - FASTA indexing and fast random access (like samtools faidx, but in Python).
* screed - Indexed FASTA/FASTQ reader optimized for streaming very large datasets.
* sourmash - Implements MinHash comparisons for genomic sketching, metagenomics, and large-scale sequence similarity.
* khmer - K-mer counting, compression, and probabilistic data structures for huge genomes.
* xopen - Handles compressed files (bgzip, gz) more efficiently than standard Python readers; used in many seq tools.

### Neuroscience & Neurobiology
* neo - Data model library for electrophysiology experiment formats.
* elephant - Statistical analysis for spiking neural data (built on Neo).
* PyNWB / HDMF - Work with the Neurodata Without Borders (NWB) data standard.
* brian2 - Spiking neural network simulator used in theoretical neuroscience.
* pyabf - Reading Axon Binary File (ABF) electrophysiology files.
* pylake - Control and analysis for optical tweezer experiments (LUMICKS instruments)

### Structural biology / Chemical biology
* PyEMMA - Markov state modeling for protein conformational dynamics.
* MSMBuilder - Machine learning library for analyzing molecular dynamics trajectories.
* MDtraj - Specialized molecular dynamics trajectory analysis toolkit.
* pyrosetta.distributed - The Python interface to Rosetta in cluster / distributed computing contexts.
* molecool - Small library for manipulating molecular structures intended for teaching but used in niche workflows.
* pdbfixer - Automatically fix missing atoms/residues in PDB files - used before MD simulations.

### Systems biology & Modelling
* cobra-me - For modeling macromolecular expression models ("ME models") - very specialized.
* PEtab / pyPESTO - Parameter estimation for systems biology models.
* sbnet (Systems Biology Notebook) - Experimental toolkit for rule-based modeling workflows.
* Bionetgen Python API - Bindings for BioNetGen rule-based modeling platform.

### Microbiology / Metagenomics
* anvi'o (Python API) - High-dimensional microbial & metagenomic analysis framework.  CLI is famous; the Python API is lesser known.
* genomeview - Python library for visualizing aligned reads and annotations directly from BAM/VCF/FASTA.
* anvi-snakemake / anvio-structure - Extensions for structural metagenomics
* mmgenome2 (Python parts) - Toolkit for metagenome binning; consists partly of Python libraries.

### Population genetics
* allel (scikit-allel) - Analysis of large-scale population genetics data (VCF, Zarr-based).
* fwdpy11 - Forward-time evolutionary simulations (selection, demography).
* moments - Demographic inference from site-frequency spectra.
* dadi - Another demographic inference tool (Diffusion Approximations for Demographic Inference).

### Proteomics
* pyteomics - Parsing MS/MS mass spectrometry formats (mzML, mzXML, MGF).
* alphapept - End-to-end proteomics pipeline with a Python engine.
* ms_deisotope - Deisotoping + charge state deconvolution for mass spec signals.
* GlyPy - Glycoinformatics library - glycan structures & mass spec data.

### Phylogenetics
* biopython-phylip - Sxtensions for interacting with PHYLIP tools.
* augur (Nextstrain) - Python API for phylogenetic pipelines (used heavily in genomic epidemiology).
* phylopandas - Integrates phylogenetic sequences & metadata into a pandas-like API.
* pastml - Phylogenetic ancestral state reconstruction in Python.

### Microscopy / Image analysis
* aicsimageio - Read microscopy data from proprietary formats (CZI, OME-TIFF, etc.).
* czifile - Read Zeiss CZI microscopy images.
* cellpose (Python API) - Deep learning-based cell segmentation.
* napari (with bioimage-specific plugins) - Interactive viewer - not strictly a “biology" library, but most of its ecosystem is microscopy-oriented.

### Animal tracking / Behavioral biology
* dlc (DeepLabCut) - Pose estimation software used for tracking animal behavior.
* SLEAP - Multi-animal pose tracking using deep learning.

### Plant biology
* PlantCV - Computer vision toolkit for plant phenotyping.

### Bioinformatics adjacent / "Strange but real"
* skmer - Genome distance estimation without assembly using spectral k-mer methods.
* phylter - Detect suspicious sequences in phylogenetic datasets (contaminants and outliers).
* pyslim - Manipulate tree sequences produced by SLiM evolutionary simulations.
* pp-sketchlib - MinHash sketches for petabase-scale genomics (used by BIGSI databases).
* pyswift - Machine-learning-based annotation for Schizosaccharomyces pombe datasets
* pyrosetta.bindings - Bindings for Rosetta energy functions only - used almost nowhere outside protein design labs.
