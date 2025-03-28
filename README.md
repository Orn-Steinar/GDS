# Group Project

Our solution to the projet was done in parts, with separate files implementing different parts of the project. Intermediate results were saved to disc and loaded back up to be used in subsequent steps. Below is an overview of the files included in our submission, what they use as inputs and what they produce as outputs.

### How to run the submission
1. Preprocessing.py has to be run before anything else.
2. With the output from Preprocessing.py, part 2 and part 3 of the project can be run as well as the exploratory data analysis part of Part 1.
       - Exploratory Data Analysis: 
       - Part 2:
       - Part 3:
3. With the results from part 2 and 3, part 4 can be run.

#### Part 1
- **Preprocessing.py:**
    - Input: The 955K.csv file
    - This script implements the preprocessing part of Part 1 and outputs a pandas dataframe containing the preprocessed documents and labels to a
    - pkl file.
- **exploratory_data_analysis.ipynb**
    - Input: The pkl file outputted by Preprocessing.py
    - Implements the exploratory data analysis part of Part 1
#### Part 2
- **one-hot-encoding.ipynb:**
      - Input: The pkl file outputted by Preprocessing.py
      - Implements one-hot encoding of the preprocessed dataset and outputs the results to a pkl file.
- **tf_idf**
- **logistic_regression.ipynb**
#### Part 3
- **naive_bayes.ipynb:** Implementerer del 3.

#### Part 4
- **model_evaluation**

#### Other files
- **Functions.ipynb:** Samling af functioner brugt i projektet
- **LIAR**
