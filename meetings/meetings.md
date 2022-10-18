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
- I'm potentiall worried that the dissertation will be mostly paraphrasing the paper. What will the writing involve?
  - The dissertation will require me understanding the paper and processes used during the project and then writing about those. More details (than the FUpred paper) can be elaborated such as the DeepMSA process. In general, the attempt is to reproduce the results from the paper but given that data used will not be the same, it will be very hard to reproduce them. Nevertheless, some changes may be made in the process that will constitute a more "original" work which they will also be elaborated in the project.

### Minutes
- A possible addition could be to use a Convolutional Neural Network (CNN) do improve the contact map that's used in the pipeline described in the paper.
- Until next week, I will look further into the CATH database and come up with potential ways to convert its format to AlphaFold's data, in order to evaluate AlphaFold's performance in Domain Prediction.
- Next meeting: Monday 24th, 14:30-15:30.