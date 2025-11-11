# Data Analytics Fundamentals - Assessment 1 playground

Jupyter Notebook playground for BPP course year 1, term 1.

See ```L4_Data_Analytics_Fundamentals_assessment_1.docx``` and ```L4_Data_Analytics_Fundamentals_assessment_1.txt```

```workings.ipynb``` is my workbook for answering the first questions  in the first assessment:

1. What is the average age of customers who have not churned? (Rounded)
2. What percentage of customers have an International Plan?
3. What is the median monthly charges for all customers?
4. Generate a bar chart showing the count of customers who churned vs. those who did not. Which group is larger?
5. What is the average number of customer service calls for customers who churned?
6. Create a histogram - What is the most common tenure range shown in the histogram? (Adjust the bins if needed)
7. For the fields 'Gender', 'Senior', and 'Contract', determine if they are qualitative or quantitative and identify the specific data types. Which statement is correct?
8. Which state has the second-highest average number of local calls made?
9. Which states had 90 customers churning?
10. Create a line chart showing the average international minutes used per month over different ages. Describe the overall trend. Select all the apply
11. True or False: Males Under 30 churned more than Females under 30

N.B. This project expanded and now includes assessment part 2 questions. They are not listed here but can be found in the part2.ipynb file.

## Virtual environment and dependencies

The virtual environment for this project uses Python 3.14 and was set up by PyCharm.

To create a venv manually, ```python3.14 -m venv .venv```

To activate the venv, ```source .venv/bin/activate```

The project has a number of dependencies that need to be installed.

Start by updating pip, ```pip install --upgrade pip```

And install other packages needed:
```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install scipy
pip install statsmodels
pip install -U pip setuptools wheel
pip install -U scikit-learn
```

Running, ```pip freeze > requirements.txt``` copies the installed dependencies, and their versions, to the ```requirements.txt``` file.

If this repo is then used on another machine, run:
```bash
python3.14 -m venv .venv
pip install -r requirements.txt
```
