import vk
import pandas as pd
import time

df=pd.DataFrame()

start = time.time()

session = vk.AuthSession(app_id='', user_login='', user_password='')
api = vk.API(session)

accounts = pd.read_csv('users.csv', sep=';', encoding='ansi')

for index, row in accounts.iterrows():
    try:
        ids=row['ids']
        time.sleep(0.35)
        subscriptions = api.users.getSubscriptions(user_id=ids, extended='1', v='5.87', count='100')
        subscriptions = subscriptions['items']
        
        for subscription in subscriptions:
                    try:
                        ids = str(ids)
                        group_id = subscription['id']
                        group_id = str(group_id)
                        name = subscription['name']
						
                        df = df.append({'ids': ids, 
                                        'group_id':group_id, 
                                        'name':name}, ignore_index=True)
                    except: pass
                
    except:
        pass
    
end = time.time()
print(end - start)

df.to_csv('subscriptions.csv', sep=';', mode='a', index=True, header=True)