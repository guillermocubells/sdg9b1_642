#%% Importing 9.b.1 and defining variables
innovation_9b1 = open('Indicators_9_6.csv','r' , encoding = 'utf-8' , errors= 'ignore') 
innovation_9b1.readline()

indicator= []
geocode = []
geoarea = []
timeperiod= []
value = []

    
for line in innovation_9b1:
    try:
        if len(line) > 3500:
            continue 
        _, _, i, _, _, g, a, tp, v, _, _, _, _, _, _, _, _, _ = line.strip().split(',')
        indicator.append(i) 
        geocode.append(g)
        geoarea.append(a)
        timeperiod.append(tp)
        value.append(v)
    except:
        break
    
    relevant_data = [timeperiod ,indicator, geocode, geoarea, value]
    print(relevant_data)
    #print(geoarea)
    
#%%
    
#%%
for year in timeperiod:
    if year == 2015:
        continue
    print (year)
    
    
    