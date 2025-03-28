# Group Project

Our solution to the projet was done in parts, with separate files implementing different parts of the project. Intermediate results were saved to disc and loaded back up to be used in subsequent steps. Below is an overview of the files included in our submission, what they use as inputs and what they produce as outputs.

### How to run the submission

#### Part 1
- **Preprocessing.py:**
    - Input: The 955K.csv file
    - This script implements the preprocessing part of Part 1 and outputs a pandas dataframe containing the preprocessed documents and labels to a
    - pkl file.
- **exploratory_data_analysis.ipynb**
    - Input: The pkl file outputted by Preprocessing.py
    - Implements the exploratory data analysis part of Part 1
#### Part 2
- **one-hot-encoding_sparse.ipynb:**
    - Input: The pkl file outputted by Preprocessing.py
    - Implements one-hot encoding of the preprocessed dataset and outputs the results as a sparse matrix to a pkl file.
- **idfidf_weighting.ipynb:**
    - Input: The pkl file outputted by Preprocessing.py
    - Implements tf_idf encoding of the preprocessed dataset and outputs the results as a sparse matrix to a pkl file.
- **logistic_regression.ipynb**
    - Input: Uses the one-hot encoded sparse matrix dataset for the data samples as well as the non-sparse matrix for the labels.
    - Implements the Logistic regression model and outputs the trained model along with the test set to pkl files.
#### Part 3
- **naive_bayes.ipynb**
    - Input: Uses the tfidf encoded sparse matrix dataset for the data samples as well as the non-sparse matrix for the labels.
    - Implements the Naive Bayes model and outputs the trained model along with the test set to pkl files.
#### Part 4
- **model_evaluation**
    - Input: Uses the trained models and test sets from part 2 and 3, as well as the onehot encoded LIAR dataset.
    - Implements the model evaluation part of the assignment.
- **LIAR**
    - Folder containing slightly modified versions of the preprocessing and one-hot files used to preprocess the LIAR dataset
