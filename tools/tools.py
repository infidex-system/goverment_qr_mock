from linebot.models import (
    BoxComponent,
    TextComponent,
    SeparatorComponent
)

def box_gen(data):
    print(data)
    boxComponent = []
    for d in data:
        if d[0]=="moving":
            title = "本日のお手続き"
            body = "転出届け"
        elif d[0]=="moving_1":
            title = "転出日"
            body = convert_date(d[1])
        elif d[0]=="moving_2": #住所は個別に処理を行う。
            title = "お引越し先のご住所"
            zipcode,streetAddress,address = d[1].split(",")
            ele = BoxComponent(
                layout = 'vertical',
                contents= [
                    #TextComponent(d[1],size = 'sm',align = 'end',color = '#111111'),
                    TextComponent(title,size = 'sm',flex = 1,color = '#555555'),
                    TextComponent("〒"+zipcode,size = 'sm',align = 'end',color = '#111111'),
                    TextComponent(streetAddress + address,size = 'sm',align = 'end',color = '#111111'),
                    SeparatorComponent(margin = 'lg'),
                ]
            )
            boxComponent.append(ele)
            continue

        elif d[0]=="moving_3":
            title = "市役所予約日時"
            body = convert_datetime(d[1])


        ele = BoxComponent(
            layout = 'vertical',
            contents= [
                TextComponent(title,size = 'sm',flex = 1,color = '#555555'),
                TextComponent(body,size = 'sm',align = 'end',color = '#111111'),
                SeparatorComponent(margin = 'lg'),
            ]
        )

        boxComponent.append(ele)
    return boxComponent

def convert_datetime(d):
    year = d[:4]
    month =d[5:7]
    day = d[8:10]
    time =d[-5:]
    return year+"年 "+month+"月 "+day+" 日 "+time 

def convert_date(d):
    year = d[:4]
    month =d[5:7]
    day = d[8:10]
    
    return year+"年 "+month+"月 "+day+" 日 " 
    