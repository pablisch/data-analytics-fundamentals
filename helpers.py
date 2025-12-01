import pandas as pd

def is_significant(p_value, alpha=0.05):
    if p_value < alpha:
        print(f"✅ The difference is significant\nThe p-value: {p_value} is {alpha - p_value} less than the alpha: {alpha}\nThe null hypothesis is rejected")
        return True
    elif p_value > alpha:
        print(f"❌ The difference is not significant\nThe p-value: {p_value} is {p_value - alpha} more than the alpha: {alpha}\nThe null hypothesis is NOT rejected")
        return False
    else:
        print(f"❓The p-value: {p_value} is equal to the alpha: {alpha}\nI am not sure what this means in terms of rejecting the null hypothesis")
        return False

def clean_bpp_5_dataframes(df: pd.DataFrame):
    df.columns = df.columns.str.strip() # removes leading and trailing whitespace
    df = df.dropna(axis=1, how="all") # drops any columns that ONLY contain NaN values
    year_cols = [col for col in df.columns if col.isdigit()] # list comprehension for Years - contains only digits
    df_melted = df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Value"
    ) # Pandas melt method unpivots the df from wide to long format
    # args:
    # id_vars are the columns to leave as they are
    # value_vars are the columns to unpivot into rows - the year cols
    # var_name is the name for the new col in place of the year columns
    # value_name is the name of the new col in place of the values that were in the year columns
    df_melted["Year"] = pd.to_numeric(df_melted["Year"], errors="coerce") # the "Year" col values are converted to numeric format and any exceptions become NaN
    df_melted = df_melted.dropna(subset=["Year", "Value"]) # drops any row where "Value" OR "Year" is NaN

    return df_melted

def run_sql_query(query, cursor):
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    return df
