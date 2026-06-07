import pandas as pd, random
from datetime import datetime, timedelta

rows=[]
start=datetime.now()-timedelta(days=28)
countries=['Brazil','Mexico','Colombia','Argentina']
methods=['PIX','OXXO','PSE','Rapipago','Card']
processors=['ProcessorA','ProcessorB','ProcessorC']

for i in range(12000):
    ts=start+timedelta(minutes=i*3)
    country=random.choice(countries)
    method=random.choice(methods)
    processor=random.choice(processors)
    amount=random.randint(20,800)
    customer=random.choice(['new','returning'])
    use3ds=random.random()<0.35

    approved=random.random()<0.87
    decline=''

    if ts > start+timedelta(days=7):
        if country=='Mexico' and method=='Card' and use3ds:
            approved=random.random()<0.43
            if not approved: decline='3ds_failed'
        elif country=='Brazil' and processor=='ProcessorC':
            approved=random.random()<0.55
            if not approved: decline='timeout'

    if not approved and not decline:
        decline=random.choice(['insufficient_funds','do_not_honor','processor_error'])

    rows.append([ts,country,method,processor,amount,customer,use3ds,'approved' if approved else 'declined',decline])

pd.DataFrame(rows,columns=['timestamp','country','payment_method','processor','amount','customer_type','three_ds','status','decline_code']).to_csv('data/transactions.csv',index=False)
