import pandas as pd

def analyze_csv(path):
    df=pd.read_csv(path)
    overall=(df['status']=='approved').mean()*100

    results=[]
    dims=['country','payment_method','processor','three_ds','customer_type']
    for d in dims:
        grp=df.groupby(d)['status'].apply(lambda s:(s=='approved').mean()*100)
        for k,v in grp.items():
            if v < overall-15:
                results.append({'dimension':d,'value':str(k),'auth_rate':round(v,2),'gap':round(overall-v,2)})

    results=sorted(results,key=lambda x:x['gap'],reverse=True)[:7]

    return {
        'overall_authorization_rate': round(overall,2),
        'top_root_causes': results
    }
