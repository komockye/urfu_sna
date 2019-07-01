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
        users = api.users.get(v='5.87', user_ids=ids, fields='personal')
        
        
        for user in users:
                    try:
                        ids = user['id']
                        ids = str(ids)
                        first_name = user['first_name']
                        last_name = user['last_name']                
                        personal = user['personal']
                        alcohol = personal.get("alcohol", 'none')
                        
                        inspired_by = personal.get("inspired_by", 'none')
                        langs = personal.get("langs", 'none')
                        life_main = personal.get("life_main", 'none')
                        people_main = personal.get("people_main", 'none')
                        political = personal.get("political", 'none')
                        religion = personal.get("religion", 'none')
                        smoking = personal.get("smoking", 'none')
                        df = df.append({'ids': ids, 
                                        'first_name': first_name, 
                                        'last_name':last_name, 
                                        'alcohol':alcohol, 
                                        'inspired_by':inspired_by, 
                                        'langs':langs,
                                        'life_main':life_main, 
                                        'people_main':people_main, 
                                        'political':political, 
                                        'religion':religion, 
                                        'smoking':smoking}, ignore_index=True)
                    except: pass
                
    except:
        pass
    
end = time.time()
print(end - start)

df.to_csv('personal.csv', sep=';', mode='a', index=True, header=True)