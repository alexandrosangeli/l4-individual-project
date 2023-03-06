# Supervisor meetings

## 04/10/22

### Questions
- How will the project be different from FUpred (Folding Unit Predictor) ? (from W. Zheng et al)
  - Not a clear answer but contact maps could be looked into as part of the project.
- What exactly are we predicting?
  - The domain that amino acids belong to. For example, input data could be "A,E,S,L,E,L,S..." and the output "D1,D1,D1,D2,D2,D2,D2..".
- What is the input data? Contact information? (from paper)
  - A sequence of amino acids could be the input data. Contact maps can be looked into and be utilised in the project.
- Ask for email to add to GitLab/GitHub.
- Is the server necessary?
  - Depends on what we what to emphasize on - i.e. Machine Learning only or a combination of software engineering and Machine Learning.

### Minutes
- Went over proteins - structures, domains, disordered proteins etc.
- Discussed GraphQL and how building a Django server could be part of the project.
- Protein Domain prediction is not *really* solved yet, there could be some different methods and techniques that could be used.
- As a L4 project, it doesn't have to be very unique (and would also be difficult to make something very unique), so approaches found in literature could be used.
- Next meeting: Monday 10th, 14:30-15:30.
  
---

## 10/10/22

### Questions

- Discuss if the prossible improvements mentioned in FUpred can be utilised. (combination of threading alignments and contact map info for composite domain prediction).
  - Will look this later into the project - time may not suffice.
- Discuss what the server part is exactly and if not doing it could impact the grade.
  - The server part is not necessary.
- Discuss the following features: glass transition temperature, melting point, isoelectric point, molecular weight, secondary structure, solubility, surface hydrophobicity and emulsification.
  - Not much time - if still relevant can discuss later.
- Where can I find data? For which features is easiest to find data for.
  - PDB, CATH, UniProt
- Discuss the papers found.
- RNN question: where is the output from t-1 fed to in t?
  - Will leave technical questions for later.

### Minutes
- A clearer idea of how the project will go has been set:
  - Start with benchmarking AlphaFold using CATH - part of the pipeline that can be used later to evaluate results.
  - FUpred results will later be reproduced. If time allows, the possible improvements mentioned in the paper (FUpred) may be considered.
- Until next time:
  - Investigate how CATH will be used to evaluate AlphaFold.
  - Read some more of the paper, understand it better, write down questions.
- Next meeting: Monday 17th, 14:30-15:30.

---
  
## 17/10/22

### Questions
- Where can the models descrbied in the paper be found? Do they have to be implemented?
  - Instead of implementing, benchmark datasets can be utilised.
- I'm worried that the dissertation will be mostly paraphrasing the paper. What will the writing involve?
  - The dissertation will require me understanding the paper and processes used during the project and then writing about those. More details (than the FUpred paper) can be elaborated such as the DeepMSA process. In general, the attempt is to reproduce the results from the paper but given that data used will not be the same, it will be very hard to reproduce them. Nevertheless, some changes may be made in the process that will constitute a more "original" work which they will also be elaborated in the project.

### Minutes
- A possible addition could be to use a Convolutional Neural Network (CNN) do improve the contact map that's used in the pipeline described in the paper.
- Until next week, I will look further into the CATH database and come up with potential ways to convert its format to AlphaFold's data, in order to evaluate AlphaFold's performance in Domain Prediction.
- Next meeting: Monday 24th, 14:30-15:30.

---
  
## 24/10/22

### Questions
- How to interpret `cath-alphaflow` from GitHub (for protein domain detection from AlphaFold's predicted PDB data).
  - Will be using SWORD instead. 
- What metrics to be used for evaluating AlhaFold's predictions?
  - number of domains predicted (exact, RMS)
  - cut point prediction (+- 10 residuals)
  - maximum overlap
- Is it feasible to create/approximate a timeline for the project's progress now?
  - Not an exact but it'd be good if some rough deadlines were put down. 
- Are timelogs assessed? Is it okay that the start is slow (i.e. few hours have been logged so far). 
  - Timelogs are not assessed. 
- Where is the threshhold parameter that needs tuning?

### Minutes
- Evaluation at the end can include: testing of code, evlauation of benchmarking, development of accuracy measures
- Put down rough deadlines, good to have a plan but difficult to predict how the process will go (Especially for non SE projects)
- Next meeting: Monday 31st, 14:30-15:30.

---

## 31/10/22

### Questions
- Where to access literature about methods for measuring accuracy of domain boundary prediction?
  - Papers have been added on the teams channel
- What to do with alternative outputs of SWORD2?
  - Can use all of them since domain boundaries are not very well defined yet in bioinformatics (could depend on the task)
- What to do with the slow processing of SWORD2? 
  - Built a prototype, test on a few datapoints and when the pipeline works, run it on the entire (few thousand) datapoints

### Minutes
- Different methods for measuring accuracy have been discussed. Will read on my own time more thoroughly.

### Objectives
- Continue with the pipeline
- Implement at least one function for measuring the accuracy until Monday
- If there is time, come up with some soft deadlines regarding the project

---

## 07/11/22

### Questions
- No questions but need some more guidance and discussion on the pipeline

### Minutes
- Use CATH pdb files to find what the upper bound of the score between AlphaFold's prediction and CATH's data will be using Sword2

---

## 14/11/22 (No meeting)

---

## 21/11/22

### Questions
- What to do with missing residues or linkers?
  - For example, consider x = [1, 1, 1, 0, 1] (where the 0 is a linker) and y = [0, 1, 1, 0, 1] (where the first 0 is a linker and the second 0 is a missing residue). How to treat the naive accuracy function (correct predictions / total residues) ? 
  - Is it 3 / 5 or 3 / 4 ?
- Step 2 in CASP6 scoring: why is the third number the horizontal score (82) positive?
  - Why isn't it negative?

### Minutes


---

## 7/12/22

### Questions
 - General discussion of the future of the project which involves the deep learning part.

### Minutes
 - Discussed utilising CNNs and RNNs for the prediction.
 - One-hot encoding for each amino acid.
 - 20 channels input (each channel is the one hot encoding for each amino acid).
 - CNN would be fully convolutional since the size of each protein varies.
 - RNN is a good fit since it can take variable sized inputs.

---

## 15/12/22

### Questions
 - General discussion of the future of the project which involves the deep learning part.

### Minutes
  - Changed the scope of the project from domain prediction to protein domain *boundary* prediction.
  - Discontinuous proteins would be a big issue.
  - Future work could include utilising contact maps for discontinuous proteins.

## Next meeting

### Questions
 - How many sequences is a good number?
 - Should I use all chains from a protein? If yes, is the data fair/balanced if some proteins have many chains and others few?
 - ~~How big the margin should be for the target data? (e.g. [0,0,1,1,0,0] vs [0,1,1,1,1,0])~~
   - This can vary. Different papers have used different margins (+-8, +-20 residues etc.) 
 - What to do about variable sized inputs? Cannot batch them together.
 - What loss is best? Loss now seems very low (0.017) but its because the arrays are mostly zero anyway. Discuss Res-Dom loss. (Maybe use a different loss for innovation?)
 - Using 20 layers vs unsqueezing data making them 1 dimensional ?
 - What to do with research that already exists? Since this isn't unique. 40% is on research quality which includes innovation (moodle slides)
 - "...were normalized to 700. Sequences longer than 700 were truncated and those shorter than 700 were padded with zeros." Should I do something similar?
 - Can this be "translated" into a classification problem where each residue is classified as 1 or 0?
 - How to include/write about AlphaFold in the dissertation?
 - "Because the true domain boundary definitions have not been universally accepted, we assigned all residues within ±20 residues from each true domain boundary " What to do about overlaps? assign back to 0?
 - Coming up with a new method instead of evaluating different architectures? E.g. extracting features using CNNs and feeding those in a bi-LSTM.
 - Would it be okay if the status report's timeline is not accurate?
 - Do I need to provide background on CNN, RNN etc. in the dissertation or background on their (relevant) applications? 
 - Dissertation preview?
 - Sources for the challenges in experimentally predicting proteins' structures. 
 - Can I use this citation style? "...they use a bi-LSTM (Paper's Author, Year)
 - hybrid of Template-based and ab initio method as my argument? (no need to predict other features such as secondary structure makes it faster)
 - what are similarity thresholds and should I use something similar?
  
## 19/01/23

### Questions
- See questions above

### Minutes
- Need to do stratified random sampling instead of uniform.
- Could utilize a pretrained model to generate embeddings instead of just one-hot encoding.
- Some backround for DL/CNNs/RNNs could be good.

## 26/01/23

### Minutes
- A bit more detailed needed for the AlphaFold sections since it is part of my project + maybe a diagram.
- Restructure dissertation: Intro (incl. Background), Methods (Data, techniques, architecture etc), Result, Discussion, Conclusion
- Use Mathew's Correlation Coefficient too for a metric.
- Dont include multiple 1s (a margin around boundaries) in the prediction. Need to re-do some helper methods.

## 02/02/23

### Minutes


## 09/02/23

### Questions

- Is 1024 vs 480 fair? Since it needs more computing power to train one over the other. But the number of trainable parameters are the same in their respective models.
  - discuss how carp uses less processing to generate features but more to train because of 1024
  - would need to discuss and elaborate the caveat and tradeoff in the dissertation
- Why do PDB files not have some chains? (that are found in cath)
- what if I combine the embeddings?
- what does "If the domain boundary has a linker, the whole linker is regarded as the domain boundary" mean?
  - not going to be assessed on this
- colab pro re-imbursement
- how much to talk about helper functions? a lot of programming is involved (BASH scripting, parsing CATH, identifying linkers/boundaries/non-boundaries, metrics, median, amplifying)
  - maybe discuss briefly in the implementation
- a further point if they are within three, and so on up to eight residues. A prediction two residues away from the correct boundary would therefore have 7 points. If the boundary is perfectly predicted, does it get 8 or 9 (8+1) points?

### Minutes
- STD deviation/variance of results & standard error
- fix dataset, also change the boundaries as discussed in the meeting (2 domain would have just one boundary)
- for dbd and 1 domain (so 0 predictions) use 1.0 for 0/0 but 0.0 for 0/x
- add domain and key to dataset to see how good the predition is for every category (1 domain, 2 domain etc.)
- k fold vaidaton for my model and explain the importance of the thi good practice
- plot metrics against number of samples
- discuss the uniprot pdb mapping in diss
- write about helper because someone not involved in the field may not be aware of the complexity
- alphafold + sword2 against sequence based boundary prediction methods
- lit review about esm vs carp

## 16/02/23

### Questions
- How does AF predict the A chain of IDs that have no A chain (e.g. P00800)
  - will just use those that have an A chain
- is there a way to find the number of domains from a uniprot?
<!-- - should linkers be boundaries? -->
- no literature on how boundaries are defined. Can keep the code as is and manually remove first and last boundary and test both methods
- when i tried to use -u UNIPROT and -p PDB the chains were of different size of atoms.
- Is it safe to use the mapping (many to many) to get the PDB and check against CATH for the true boundaries?

### Minutes
- Check sequence similarity and filter
- this can introduce bias because some chains are filtered out
- discuss that some pdb structures dont match UNiprots that likely due to chains being modified -> thus the algorithms
- bioinfomatics data are messy, maybe they dont agree, discuss
- exclude discontinuous from dataset, find the number
- if exclude disctoninuous ->

## 23/02/23

### Questions
- Double check that training and testing are correct (model.eval(), no gradient stuff)
- ~~check metrics (should I replace the 1 in the MCC - different scores are obtained with th two methods)~~
- ~~discuss new metrics with the two passes instead of 1~~
- do i need a glossary? (contact maps, residue)
- does my diagram need to be accurate (e.g. is it ok if it resmebles a fully and end-to-end process if it's not?)
- ~~is chain A ok?~~
- ~~iid?~~
- general advice for succeeding in academia (is work experience relevant?)
- residuals and skip connections
- ~~AlphaFold seems to have solved the foldingp problem, even with a low MCC, if goal of boundary prediction is to better predict structure and AF already does that, where's the benefit?~~


### Minutes
- reference some numbers
- knowing the domains helps experimentalists because it helps split he protein and crytalize it
- if alphafold is good in domain prediction then maybe split protein into domains first, apply alphafold on domains and then put everything together
- add to intro something about crystalizastion
- dbd must change too
- iid - take into consideration - mmseq
- state assumption of iid in diss

## 02/03/23

### Questions
- should i time the generation of encodings?
- can i perform hyperparam tuning on one fold only ? will it be a good indicator?
- ~~roc for best threshold implications?~~
  - use entire datasaet
  - point that maximises mcc
- play with losses
- can i mention that i tried out different hyperparams without evidence?
  - ~~yes but is good to have some~~
- skip connections between lstm blocks?
- ~~7000 data for around 1000 features?~~
  - Latent space is < 1000
- how complex can the network be given 1000 features and 7000 data points?
- how important is source code and timelog?
- measuring time taken - how to compare with different hardware? colab assigns different hardware sometimes. Also some code is not optiimsed

## 09/03/23

### Questions
- Considering boundaries at the start as well.Rationale: the model can learn when a domain starts better? (is this valid?)
- can i describe this as an end-to-end system (which is possible if I add the encoding part in the middle just slower) even if it's not technically end-to-end?
- total confusion matrix yields better MCC than mean MCC