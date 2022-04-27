class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, unwanted_columns, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        # unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        # df.drop(unwanted_rows , inplace=True)
        # df = df[df['polarity'] != 'polarity']

        df.drop(axis=0, columns=unwanted_columns, inplace=True) 
        return df

    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df.drop_duplicates(inplace=True)
        return df

    def convert_to_datetime(self, datetime_columns, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        for column in datetime_columns:
            df[column] = pd.to_datetime(df[column], format='%Y%m%d : %H%M%S')
        
        # df = df[df['created_at'] >= '2020-12-31' ]
        
        return df
    
    def convert_to_numbers(self, numbers_columns, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        for column in numbers_columns:
            df[column] = pd.to_numeric(df[column], errors='ignore')    
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df.drop(df[df['lang']]!='')
        
        return df