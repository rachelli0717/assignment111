import pandas as pd
import os


def clean_data(input1, input2,output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df1 = df1.rename(columns={'respondent_id': 'id'})
    merge_df = pd.merge(df1, df2, on='id')
    cleaned_df = merge_df.dropna()
    s_df = cleaned_df[~cleaned_df['job'].str.contains('Insurance')]
    ss_df = s_df[~cleaned_df['job'].str.contains('insurance')]

    ss_df.to_csv(output, index=False)


if __name__ == "__main__":
    clean_data( "respondent_contact.csv", "respondent_other.csv", "cleaned_data.csv")