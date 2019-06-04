from flask import Flask, jsonify,request
from flask_restful import Api, Resource, reqparse
from data import init_jobs,init_bids
from sort import sel_sort,sel_sort_date

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS']= False

jobs = [
    {
        "id": 1,
        "origin" : "Solo",
        "Destination": "Semarang",
        "budget" : 5400000,
        "shipment_date" : "2019-04-18 05:48:18",
        "distance" : 100
    },
    {
        "id": 2,
        "origin" : "Surabaya",
        "Destination": "Jember",
        "budget" : 1300000,
        "shipment_date" : "2019-04-10 05:48:18",
        "distance" : 200
    }
    
]
init_jobs(jobs)

bids = [
    {
        "id":1,
        "job_id":1,
        "transporter_name":"david wildan",
        "transporter_rating":4.5,
        "price":4500000,
        "vehicle_name":"Tronton"
    },
    {
        "id":1,
        "job_id":2,
        "transporter_name":"david beng",
        "transporter_rating":4,
        "price":1500000,
        "vehicle_name":"Fuso"
    }
]
init_bids(bids)

@app.route('/jobs',methods=['GET'])
def get_jobs():
    return jsonify({'jobs': jobs})

@app.route('/bids',methods=['GET','POST'])
def get_bids():
    if(request.method=='GET'):
        return jsonify({'bids': bids})
    elif(request.method=='POST'):
        job_id=int(request.args.get('job_id'))
        bids_new=[]
        for bid in bids:
            if(bid['job_id']==job_id):
                bids_new.append(bid)
        return jsonify({'bids(job_id : '+str(job_id)+')':bids_new})

@app.route('/sort',methods=['POST'])
def sort_data():
    parameters=request.args
    data=parameters.get('data')
    field=parameters.get('field')
    sort_type=parameters.get('type')
    if(data=='jobs'):
        if(field!="shipment_date"):
            jobs_sorted=sel_sort(jobs,field,sort_type)
        else:
            jobs_sorted=sel_sort_date(jobs,field,sort_type)
        return jsonify({'jobs (sorted-'+field+'-'+sort_type+')' : jobs_sorted})
    else : #data=='bids' 
        bids_sorted=sel_sort(bids,field,sort_type)
        return jsonify({'bids (sorted-'+field+'-'+sort_type+')' : bids_sorted})



if __name__=='__main__':
    app.run(debug=True)
#api.add_resource(Job, "/user/<string:name>")

#app.run(debug=True)
    
