from flask import jsonify
import random
import json

fstream = open("name.txt")
name=fstream.read().split('\n')
fstream.close()

city = ["Jakarta","Bandung","Surabaya","Medan","Makassar","Jayapura","Manokwari"
          ,"Tangerang","Semarang","Solo","Pekanbaru","Manado","Padang","Bogor","Bekasi",
        "Lombok","Bali","Aceh","Kupang","Pontianak","Samarinda","Palangkaraya"]

vehicle=["Tronton","Fuso","Mitsubishi","Honda","Toyota","Kawasaki","Suzuki","Daihatsu"]

def init_jobs(jobs):
    for i in range (3,251):
        new_job = {}
        new_job["id"]=i
        new_job["origin"]=random.choice(city)
        new_job["Destination"]=random.choice(city)
        while(new_job["origin"]==new_job["Destination"]):
            new_job["Destination"]=random.choice(city)
        new_job["budget"]=random.randint(1,100)*100000
        year='2019-'
        month=str(random.randint(1,12))+'-'
        date=str(random.randint(1,30))+' '
        hour=str(random.randint(0,23))+':'
        minute=str(random.randint(0,59))+':'
        second=str(random.randint(0,59))
        if(len(month)<3):
            month='0'+month
        if(len(date)<3):
            date='0'+date
        new_job["shipment_date"]=year+month+date+hour+minute+second
        new_job["distance"]=random.randint(1,11)*100
        jobs.append(new_job)

#one job can have many bids
def init_bids(bids):
    pivot={}
    for i in range(3,1001):
        new_bid={}
        new_bid["job_id"]=random.randint(3,250)
        if(new_bid["job_id"] not in pivot):
            pivot[new_bid["job_id"]]=[]
            pivot[new_bid["job_id"]].append(1)
            new_bid["id"]=1
        else:
            new_bid["id"]=pivot[new_bid["job_id"]][-1]+1
            pivot[new_bid["job_id"]].append(new_bid["id"])
        first=random.choice(name).lower()
        last=random.choice(name).lower()
        while(first==last):
            last=random.choice(name).lower()
        new_bid["transporter_name"]=first+' '+last
        new_bid["transporter_rating"]=random.randint(30,50)/10
        new_bid["price"]=random.randint(1,100)*100000
        new_bid["vehicle_name"]=random.choice(vehicle)
        bids.append(new_bid)



    



