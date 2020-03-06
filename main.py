import keyboard as kb
import time, csv, pandas, datetime

start=time.time()
t1=time.time()
end=t1+5 #change this number to change the duration(in seconds) of the mapping
log=[]
i=0

while True:
    event=kb.read_event(False)
    print(f'{event} pressed {event.name} at {str(event.time - t1)[:6]}')
    start=time.time()
    if 'down' in str(event):
        Type='down'
    else:
        Type='up'
    log.insert(i,{'Key':event.name,'Time':str(event.time-t1)[:6],'Type':Type})
    i=i+1
    if end<=start: 
        with open(f'./log/{t1}.csv',"w") as file:
            columns=['Key','Time','Type']
            writer=csv.DictWriter(file,fieldnames=columns)

            writer.writeheader()
            for j in range(0,i):
                writer.writerow(log[j])
        df = pandas.read_csv(f'./log/{t1}.csv', index_col='Key')
        print(df)
        break
