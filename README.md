# intelligent-team-building-recommendation-system

> A team building recommender system for researchers who have similar overlapping research interests and can collaborate to work on a particular problemstatement.  Given a dataset of researchers who have worked on different areas of research and coupling it with their collaboration and citation network. The project intends to select researchers and recommend the most favourable group that can work together.

## Data Preprocessing
We preprocessed the data from AANDEC dataset to extract topics from publication papers andquery-document matching. We divide the preprocessing stage into further stages,

- Extraction of noun phrases
- Removing unacceptable words
- Fixing broken words
- Filter noun phrases using Named Entity Recognition
- Stop Words Elimination
- Stemming
- Coreference Resolution
- Cleaning Collaboration Network
- Generating Similarity Matrix
