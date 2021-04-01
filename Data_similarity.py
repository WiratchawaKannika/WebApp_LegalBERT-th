import pandas as pd
data_df = pd.DataFrame(columns=['ID', 'name', 'message','tag', 'time', 'ques_similar1', 'anws_similar1', 'ques_similar2', 'anws_similar2', 'ques_similar3', 'anws_similar3', 'SatisfactionInSearch'])
data_df.to_csv('Data_similarity.csv', index=False)
