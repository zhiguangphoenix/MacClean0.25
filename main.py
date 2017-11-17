from flask import Flask, render_template, jsonify, request, url_for, redirect
import os
import json

from data_processing import  post_data_info, get_num_d, get_ds, get_aofds

app = Flask(__name__)
UPLOAD_FOLDER = 'file'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['basefiledir'] = os.path.join(basedir, 'file')
app.config['rdf'] = os.path.join(app.config['basefiledir'], 'rdf')
app.config['data'] = os.path.join(app.config['basefiledir'], 'data')
app.config['detail'] = os.path.join(app.config['basefiledir'], 'detail')

@app.route('/', methods=['GET', 'POST'])
def init():


    data_info=post_data_info(app,'data.csv')

    threshold=1

    num_d=get_num_d(app)

    ds=get_ds(app)

    fd=ds[0]
    ofd=ds[1]

    num_fd=num_d[0]
    num_ofd=num_d[1]

    aofds = get_aofds(app)

    result={
            'DATA':data_info[0],
            'NUM_ROW':data_info[1],
            'NUM_COL':data_info[2],
            'ATTRIBUTES':data_info[3],
            'THRESHOLD':threshold,
            'NUM_FD':num_fd,
            'NUM_OFD':num_ofd,
            'FD':fd,
            'OFD':ofd,
            'AOFD':aofds
           }

    result=json.dumps(result)
    return render_template("output.html",result=result)



@app.route('/test', methods=['GET', 'POST'])
def test():
    data = [{'ID': 000,
             'TYPE': 0,
             'FD': 'disease, medicine, status --> countrycode',
             'ATTRIBUTES':['id','countrycode','country','disease','medicine','status','study_design'],
             'VIOLATION':
                 [
                     {
                         "VID": 000,
                         "PATTERN": 'Anemia,Epoetin,active',
                         "ERROR_COL": 4,
                         "ERROR_TUPPLES":
                             [
                                 {"ROW": 13,
                                  "CELLS": [13, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research'],
                                  "REPAIR_CANDIDATE":['test']
                                  },
                                 {"ROW": 15,
                                  "CELLS": [15, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research'],
                                  "REPAIR_CANDIDATE": ['test']
                                  }
                             ],
                         "CORRECT_TUPPLES":
                             [
                                 {"ROW": 19,
                                  "CELLS": [19, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research']
                                  },
                                 {"ROW": 20,
                                  "CELLS": [20, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research']
                                  }
                             ]
                     }
                 ]
             },
            {'ID': 1,
             'TYPE': 0,
             'FD': 'TESTING',
             'ATTRIBUTES': ['id', 'countrycode', 'country', 'disease', 'medicine', 'status', 'study_design'],
             'VIOLATION':
                 [
                     {
                         "VID": 000,
                         "PATTERN": 'Anemia,Epoetin,active',
                         "ERROR_COL": 4,
                         "ERROR_TUPPLES":
                             [
                                 {"ROW": 13,
                                  "CELLS": [13, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research'],
                                  "REPAIR_CANDIDATE": ['test']
                                  },
                                 {"ROW": 15,
                                  "CELLS": [15, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research'],
                                  "REPAIR_CANDIDATE": ['test']
                                  }
                             ],
                         "CORRECT_TUPPLES":
                             [
                                 {"ROW": 19,
                                  "CELLS": [19, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research']
                                  },
                                 {"ROW": 20,
                                  "CELLS": [20, 'IND', 'India', 'Anemia', 'Epoetin', 'active', 'research']
                                  }
                             ]
                     }
                 ]
             }
            ]

    out = json.dumps(data)

    return render_template("test.html", result=out)
if __name__ == '__main__':
    app.run(debug=True)
