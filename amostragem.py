import pandas as pd
from random import sample

def get_sample_size(n, z="95", e="5"):
    '''
    Define o tamanho da amostra, dada uma determinada população n. 
    Confiança (z) default = 95%
    Margem de erro (e) default = 5%
    '''
    q = {"80": 1.28,
        "85": 1.44,
        "90": 1.65,
        "95": 1.96,
        "99": 2.58}

    z = q[z] 
    e = float(e)/100
    p= 0.5

    amostra = ((z**2)*p*(1-p)/e**2)/(1+(((z**2)*p*(1-p))/(e**2*n)))

    return(round(amostra))

def sample_extractor(logs_df, sample_size):
    '''
    Retorna um DataFrame de amostras extraído do DataFrame logs_df do tamanho sample_size.
    '''
    sample_df = pd.DataFrame(columns=["input", "intent_CM", "intent_watson", "confidence", "bot_message", "score", "check", "log_id"])
    sample_index = sample(range(0, len(logs_df)), sample_size)
    for index in sample_index:
        row = logs_df.loc[index]
        line = [row['input'], '', row['intent'], row['confidence'], row['bot_message'], '', '', row['log_id']]
        sample_df = sample_df.append(pd.Series(line, index=sample_df.columns), ignore_index=True)
    return sample_df