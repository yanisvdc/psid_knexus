import pandas as pd
import re

def long_to_wide(df):
    """
    Convert a DataFrame from long format to wide format.

    Parameters:
    df (pd.DataFrame): DataFrame in long format with 'ID_indiv' and 'year' columns.

    Returns:
    pd.DataFrame: DataFrame in wide format with features as columns.
    """
    # We use pivot to transform from long to wide
    df_wide = df.pivot(index='ID_indiv', columns='year')

    # Rename the columns to format: feature_87, feature_88, ...
    df_wide.columns = [f'{col[0]}_{int(col[1])}' for col in df_wide.columns]

    # Reset the index if needed
    df_wide = df_wide.reset_index()

    return df_wide

def wide_to_long(df):
    """
    Convert a DataFrame from wide format to long format.

    Parameters:
    df (pd.DataFrame): DataFrame in wide format with features and years as columns.

    Returns:
    pd.DataFrame: DataFrame in long format with 'ID_indiv', 'year', and feature columns.
    """
    # First, we need to melt the dataframe
    df_melt = pd.melt(df, id_vars=['ID_indiv'], var_name='feature_year', value_name='value')

    # Extract feature and year from the 'feature_year' column
    df_melt['feature'] = df_melt['feature_year'].apply(lambda x: re.match(r'(.+)_([0-9]+)', x).group(1))
    df_melt['year'] = df_melt['feature_year'].apply(lambda x: int(re.match(r'(.+)_([0-9]+)', x).group(2)))

    # Now we pivot back to long format, dropping 'feature_year'
    df_long = df_melt.drop('feature_year', axis=1).pivot(index=['ID_indiv', 'year'], columns='feature', values='value').reset_index()

    # Sort the DataFrame by the 'year' and 'ID_indiv' columns
    df_long.sort_values(by=['year', 'ID_indiv'], inplace=True)

    # Define the ordered columns
    ordered_columns = [
        "ID_indiv", "relationship_to_head", "sex", "race", "hispanicity", "region_grewup", 
        "state_grewup", "area_size_grewup", "both_parents_grewup", "year", "age", 
        "father_tot_nb_children", "mother_tot_nb_children", "nb_births_tot", "nb_children_fu", 
        "married", "family_change", "home_type", "housing_status_ownership", 
        "institutionalization", "disability_whether", "work_disability_degree", "physical_health", 
        "veteran_status", "extra_school", "grades_completed", "region_current", "state_current", 
        "religion", "employed_whether", "employment_status_type", "industry", "income_labor_tot", 
        "income_needs_standard_orshansky", "income_needs_standard_census", "vacation_last_year", 
        "person_number", "sample_or_nonsample"
    ]

    # Reorder the dataframe columns
    df_long = df_long[ordered_columns].copy()

    # List of columns to convert to float64
    float_columns = ['income_labor_tot', 'income_needs_standard_orshansky', 'income_needs_standard_census']

    # Determine integer columns
    int_columns = list(set(df_long.columns) - set(float_columns))

    # Convert columns to appropriate data types
    df_long[int_columns] = df_long[int_columns].astype('int64')
    df_long[float_columns] = df_long[float_columns].astype('float64')

    # Reset index in place
    df_long.reset_index(drop=True, inplace=True)

    return df_long

if __name__ == "__main__":
    # Example usage
    # Replace with your actual DataFrame
    # df = pd.read_csv('your_long_format_data.csv')

    # Convert from long to wide
    # df_wide = long_to_wide(df)
    # print(df_wide)

    # Convert from wide to long
    # df_long = wide_to_long(df_wide)
    # print(df_long)
