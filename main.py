import keyboard as kb
import time, csv, pandas

t1=time.time()
filename = time.strftime("%Y-%m-%d_%Hh%Mm%Ss")
end=t1+10 #change this number to change the duration(in seconds) of the mapping
log=[]
i=0

while True:
    event=kb.read_event(False)
    print(f'{event} pressed {event.name} at {str(event.time - t1)[:6]}')
    Type='down'if('down'in str(event))else'up'
    log.insert(i,{'Key':event.name,'Time':str(event.time-t1)[:6],'Type':Type})
    i=i+1
    if end<=event.time: 
        with open(f'./log/{filename}.csv',"w") as file:
            columns=['Key','Time','Type']
            writer=csv.DictWriter(file,fieldnames=columns)
            writer.writeheader()
            for j in range(0,i):
                writer.writerow(log[j])
        df = pandas.read_csv(f'./log/{filename}.csv', index_col='Key')
        print(df)
        break
