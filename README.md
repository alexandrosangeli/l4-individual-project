# Protein domain boundary prediction based on deep neural networks

### Quick setup and validation of code
To run the code that evaluates the model on CASP13 simply open `casp13_test.ipynb` and run all cells.

# Code
The `src/notebooks` directory provides the code used to download data, process data, the code for the implementation of the evaluation metrics, pre-processing functions, post processing functions and neural network implementation.
The `src/clean` directory provides a clean version of every common function we used for post-processing, pre-processing and evaluation.

## Main notebooks 
The main notebooks used for training and generating the matrix representations of sequences are downloaded from Google Colab and are the following:
- `data_generation.ipynb` is used to create the training data using the CASP13 data, our custom dataset and the three encoding mechanisms. The requirement to run is `carp_38M.pt` in `data/data_generation/` which can be downloaded from https://github.com/microsoft/protein-sequence-models [READY TO RUN - Requires CUDA support]
- `casp13_test.ipynb` [READY TO RUN]
- `baseline.ipynb` (used to compare ESM, CARP and one hot)

The main notebooks used to sample the data from CATH, extract sequences, evaluate AlphaFold and create the dataset are:
- `alpha_fold_eval.ipynb`
- `alphafold_pre_eval.ipynb`
- `alphafold_evaluation_preprocess.ipynb`
- `create_dataset.ipynb` requires an enormous amount of 70,000 PDB files in order to create the final list of PDB IDs which is found in `data/list_of_final_chains.txt` [Requirement: Biopython library]

The rest of the notebooks provide an evidence of our process and failures.

`prot_to_vec.ipynb` provides a very short code snippet that shows how CARP generates matrix representations of amino acids.

`carp13_test.ipynb` is ready to run. The training part is commented out so that the pre-trained model loads and is evaluated. `data_generation.ipynb` is also ready to run and create the datasets if needed. However, the models require CUDA as they are too big to run on CPU.
The rest of the notebooks cannot run as the required data were not pushed to the repository and require too much disk space. Just the CARP representations is 5GBs.


# Data
- The `.pdb` files were downloaded using the `bulk_download.sh` script in the `pdb` directory
- The data including the true domain boundaries are under `cath`
- The data for many-to-many sequence searching are in `cath/iid/mmseqs` 
- The data AlphaFold data was downloaded using `SWORD2.py`
- `cath/cath_domain_boundaries.json` provides the necessary data used to sample the chains and to extract structural information
- `sword2/final_results/valid_pairs.txt` includes the PDB to UniProt mapping used to test AlphaFold
- The CASP13 dataset is found at `data/casp13/casp13_data.josn`
To download the required PDB files you can run the following command in `data/`:
```
`./batch_download.sh -f list_of_final_chains.txt -p`
```



# Pre-trained-models
The pre-trained models (our models, not CARP or ESM) can be found in the GitHub repository at https://github.com/alexandrosangeli/l4-individual-project
