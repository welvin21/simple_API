def isSmaller(date1,date2):
    date1=date1[0:date1.find(' ')]
    date2=date2[0:date2.find(' ')]
    if(int(date1[0:4])<int(date2[0:4])):
        return True
    elif(int(date1[0:4])>int(date2[0:4])):
        return False
    else:
        if(int(date1[5:7])<int(date2[5:7])):
            return True
        elif(int(date1[5:7])>int(date2[5:7])):
            return False
        else:
            if(int(date1[8:])<int(date2[8:])):
                return True
            else:
                return False
        
def sel_sort(data,field,sort_type):
    #implement selection sort
    data_sorted=data.copy()
    if(sort_type=='ascending'):
        for i in range(0,len(data_sorted)):
            key=data_sorted[i][field]
            index=i
            for j in range(i+1,len(data_sorted)):
                if(data_sorted[j][field]<=key):
                    key=data_sorted[j][field]
                    index=j
            temp=data_sorted[i]
            data_sorted[i]=data_sorted[index]
            data_sorted[index]=temp
    else : #sort_type=='descending'
        for i in range(0,len(data_sorted)):
            key=data_sorted[i][field]
            index=i
            for j in range(i+1,len(data_sorted)):
                if(data_sorted[j][field]>=key):
                    key=data_sorted[j][field]
                    index=j
            temp=data_sorted[i]
            data_sorted[i]=data_sorted[index]
            data_sorted[index]=temp
    return data_sorted

#define selection sort function for special field (date)
def sel_sort_date(data,field,sort_type):
    #implement selection sort
    data_sorted=data.copy()
    if(sort_type=='ascending'):
        for i in range(0,len(data_sorted)):
            key=data_sorted[i][field]
            index=i
            for j in range(i+1,len(data_sorted)):
                if(isSmaller(data_sorted[j][field],key)):
                    key=data_sorted[j][field]
                    index=j
            temp=data_sorted[i]
            data_sorted[i]=data_sorted[index]
            data_sorted[index]=temp
    else : #sort_type=='descending'
        for i in range(0,len(data_sorted)):
            key=data_sorted[i][field]
            index=i
            for j in range(i+1,len(data_sorted)):
                if(not isSmaller(data_sorted[j][field],key)):
                    key=data_sorted[j][field]
                    index=j
            temp=data_sorted[i]
            data_sorted[i]=data_sorted[index]
            data_sorted[index]=temp
    return data_sorted
