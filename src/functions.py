


import pandas as pd



def lowercase_headers_and_replace_spaces(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the column headers of a DataFrame to lowercase and replace empty spaces with underscores.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - DataFrame with lowercase headers and spaces replaced by underscores
    """
    
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def delete_unamed_column(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function takes a Pandas DataFrame as input, and creates an internal copy.
    Then on the interal copy it checks wheter or not contains a column named "Unnamed: 0".
    If it exists, deletes the column and returns the modified DataFrame, otherwise returns
    the original DataFrame.

    Inputs:
    df: Pandas DataFrame

    Output:
    Modified Pandas DataFrame
    '''
    
    if "unnamed:_0" in df.columns:
        df = df.drop("unnamed:_0", axis=1)

    return df

def convert_st_to_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the column header 'st' to 'state' if present in the DataFrame.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - DataFrame with 'st' header replaced by 'state' if 'st' is present
    """
    st_variations=["st","ST","sT"]
    
    for col in df.columns:
        if col in st_variations:
            df.rename(columns={'st': 'state'}, inplace=True)
    return df

def dropna_column(df: pd.DataFrame,col="customer") -> pd.DataFrame:
    """
    This function drops NaN values of a column
    
    Parameters:
    - df: pandas DataFrame
    - column name: string, if not given applies to the column "customer"

    Returns:
    - Returns df with no NaN on the selected column
    """
    df.dropna(subset=[col], inplace=True)
    return df

def convert_st_to_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the column header 'st' to 'state' if present in the DataFrame.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - DataFrame with 'st' header replaced by 'state' if 'st' is present
    """
    st_variations=["st","ST","sT"]
    
    for col in df.columns:
        if col in st_variations:
            df.rename(columns={'st': 'state'}, inplace=True)
    return df

def clean_gender(df: pd.DataFrame, col_name="gender") -> pd.DataFrame:
    '''
    This function will take a Pandas DataFrame as an input and it will replace the values in
    the specified column (default is "GENDER") in such a way that any gender which is not 
    "Male" or "Female" will be replaced by "U". If the gender starts with "M" or "F", it 
    will be replaced by the respective uppercase letter.

    Inputs:
    df: Pandas DataFrame
    col_name: str, the name of the column to clean (default is "GENDER")

    Outputs:
    A pandas DataFrame with the values in the specified column cleaned.
    '''
    uni = []
    for x in df[col_name]:
        if pd.isna(x):
            uni.append("U")
        elif x[0].upper() in ["M", "F"]:
            uni.append(x[0].upper())
        else:
            uni.append(x)
            # x=x[0].upper()

    df[col_name] = uni
    return df

def remove_perc_symbol(df: pd.DataFrame,col="customer_lifetime_value") -> pd.DataFrame:
    
    """
    Remove symbols from numerical values in a DataFrame.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - DataFrame with symbols removed from numerical values
    """
    df[col]=df[col].astype(str)
    df[col] = df[col].str.replace("%","")
    return df

def middle_value_slashes(df: pd.DataFrame,col="number_of_open_complaints") -> pd.DataFrame:
    """
    pics the value in the middle if a cell contains 2 slashes,e.g. X/Y/Z

    Parameters:
    - df: pandas DataFrame

    Returns:
    - Returns value in the middle.
    """
    col2 = []
    df[col]=df[col].astype(str)
    for x in df[col]:
        if "/" in x:
            col2.append(x.split('/')[1])
        else:
            col2.append(x)
    df[col] = col2
    return df

def fillna_median(df: pd.DataFrame,col:"string") -> pd.DataFrame:
    '''
    This function fills the NaN values with the median of the column
    
    Parameters:
    df: dataframe
    col: column name to be applied on
    
    Returns:
    
    df with NaN values replace by the median.
    '''
    median_col = df[col].median()
    df[col]=df[col].fillna(median_col)
    return df

def clean_bachelor(df: pd.DataFrame,col="education") -> pd.DataFrame:
    ''''
    This function removes the tail "s" from "Bachelors"
    
    Parameters:
    
    input: 
    
    Dataframe
    column name optional, if not provided education will be defined.
    '''
    col2 = []
    for word in df[col]:
        if word == "Bachelors":
            col2.append(word[:-1])
        else:
            col2.append(word)
    df[col] = col2
    return df

def replace_with_luxury(df: pd.DataFrame,col="vehicle_class") -> pd.DataFrame:
    

    luxury_types = ["Sports Car", "Luxury SUV", "Luxury Car"]
    col2 = []
    for v_class in df[col]:
        if v_class in luxury_types:
            col2.append("Luxury")
        else:
            col2.append(v_class)
    df[col] = col2
    return df

def state_abbrev(df: pd.DataFrame,col="state") -> pd.DataFrame:
    '''
    This function replaces the abbreviations for specific states with the full names
    
    Parameters:
    
    Dataframe
    Column: if not provided takes state as optional
    
    Returns: dataframe
    
    '''
    vals_to_replace = {"AZ":"Arizona","Cali":"California","WA":"Washington"}
    df["state"]=df["state"].replace(vals_to_replace)
    return df
  

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function will take a Pandas DataFrame and it will apply the previous functions in the library
    to clean some columns of the dataframe

    Inputs: 
    df: Pandas DataFrame

    Outputs:
    Another DataFrame
    '''
  
    df = delete_unamed_column(df)
    df = lowercase_headers_and_replace_spaces(df)
    df = convert_st_to_state(df)
    df = dropna_column(df)
    df = clean_gender(df)
    df = middle_value_slashes(df)
    df = remove_perc_symbol(df)
    df = clean_bachelor(df)
    df = replace_with_luxury(df)
    df = state_abbrev(df)
    return df
