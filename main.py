import keyboard as kb
import time, csv, pandas
from PIL import Image, ImageOps
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.colors import LinearSegmentedColormap

wd = matplotlib.cm.winter._segmentdata  # only has r,g,b
wd['alpha'] = ((0.0, 0.0, 0.3),
               (0.3, 0.3, 1.0),
               (1.0, 1.0, 1.0))

al_winter = LinearSegmentedColormap('AlphaWinter', wd)

t1=time.time()
filename = time.strftime("%Y-%m-%d_%Hh%Mm%Ss")
end=t1+5 #change this number to change the duration(in seconds) of the mapping
log=[]
scan_pressed = []
k_loc = {'1':(46,5,92,50),'59':(170,5,215,50),'60':(225,5,265,50),'61':(278,5,321,50),
        '62':(330,5,375,50),'63':(384,5,427,50),'64':(436,5,481,50),'65':(490,5,532,50),
        '66':(540,5,586,50),'67':(596,5,640,50),'68':(650,5,693,50),'87':(702,5,750,50),
        '88':(755,5,805,50),'55':(845,5,895,50),'70':(900,5,950,50),'69':(950,5,995,50),
        '41':(15,105,65,155),'2':(65,105,115,155),'3':(115,105,165,155),'4':(175,105,225,155),
        '5':(225,105,275,155),'6':(280,105,325,155),'7':(335,105,380,155),'8':(385,105,430,155),
        '9':(435,105,485,155),'10':(490,105,540,155),'11':(540,105,590,155),'12':(595,105,640,155),
        '13':(650,105,695,155),'14':(700,105,800,155),'82':(840,105,890,155),'71':(895,105,940,155),
        '73':(950,105,995,155),'69':(1035,105,1085,155),'53':(1090,105,1135,155),'55':(1145,105,1190,155),
        '74':(1200,105,1245,155),'15':(20,165,75,210),'16':(80,165,125,210),'17':(130,165,180,210),
        '18':(180,165,235,210),'19':(240,165,285,210),'20':(295,165,340,210),'21':(350,165,390,210),
        '22':(400,165,445,210),'23':(450,165,500,210),'24':(505,165,550,210),'25':(560,165,605,210),
        '26':(610,165,655,210),'27':(665,165,710,210),'28':(715,165,800,210),'83':(840,165,890,210),
        '79':(895,165,940,210),'81':(950,165,995,210),'71':(1040,165,1085,210),'72':(1090,165,1140,210),
        '73':(1145,165,1190,210),'78':(1200,165,1245,270),'58':(15,220,90,270),'30':(100,220,145,270),
        '31':(150,220,200,270),'32':(205,220,255,270),'33':(260,220,305,270),'34':(315,220,360,270),
        '35':(370,220,415,270),'36':(420,220,470,270),'37':(475,220,525,270),'38':(530,220,575,270),
        '39':(580,220,630,270),'40':(635,220,680,270),'43':(690,220,735,270),'75':(1035,220,1085,270),
        '76':(1090,220,1140,270),'77':(1145,220,1190,270),'42':(15,275,65,325),'86':(70,275,120,325),
        '44':(130,275,175,325),'45':(180,275,230,325),'46':(235,275,285,325),'47':(290,275,340,325),
        '48':(345,275,395,325),'49':(405,275,450,325),'50':(455,275,505,325),'51':(510,275,560,325),
        '52':(570,275,615,325),'53':(625,275,670,325),'54':(680,275,800,325),'72':(895,275,945,325),
        '79':(1040,275,1085,325),'80':(1090,275,1140,325),'81':(1145,275,1190,325),'28':(1195,275,1245,380),
        '29':(20,335,75,385),'91':(90,335,135,385),'56':(150,335,195,385),'57':(200,335,615,385),
        '541':(630,335,675,385),'92':(695,335,740,385),'93':(695,335,740,385),'29':(755,335,800,385),
        '75':(845,335,890,385),'80':(895,335,940,385),'77':(950,335,995,385),'82':(1035,335,1140,385),
        '83':(1145,335,1190,385)}


def buildHeatmap():
    global k_loc, scan_pressed
    heatmap_array = np.zeros(shape=(404,1250))
    biggest = max(scan_pressed)
    import matplotlib.image as mpimg
    for i in scan_pressed:
        if i not in heatmap_array:
            continue
        heatmap_array[k_loc[i][1]:k_loc[i][3],k_loc[i][0]:k_loc[i][2]] = heatmap_array[k_loc[i][1]:k_loc[i][3],k_loc[i][0]:k_loc[i][2]] + 1
    kb_img = mpimg.imread('./src/keyboard_image.png')
    heat_map = sb.heatmap(heatmap_array, yticklabels=False, xticklabels=False, vmin=0, vmax=biggest, cbar=False, cmap=matplotlib.cm.winter, zorder=2, alpha=.5)
    heat_map.imshow(kb_img, aspect=heat_map.get_aspect(), extent=heat_map.get_xlim() + heat_map.get_ylim(),zorder=1)
    plt.savefig(f'./log/{filename}.png')
    plt.show()
    return True

while True:
    event=kb.read_event(False)
    print(f'{event} pressed {event.name} at {str(event.time - t1)[:5]} with scan code {event.scan_code}')
    Type='down'if('down'in str(event))else'up'
    log.append({'Key':event.name,'Time':str(event.time-t1)[:5],'Type':Type,'Scan code':event.scan_code})
    if Type=='down':
        scan_pressed.append(event.scan_code)
    else:
        continue
    if end<=event.time: 
        with open(f'./log/{filename}.csv',"w") as file:
            columns=['Key','Time','Type','Scan code']
            writer=csv.DictWriter(file,fieldnames=columns)
            writer.writeheader()
            for i in range(0,len(log)):
                writer.writerow(log[i])
        buildHeatmap()
        break
