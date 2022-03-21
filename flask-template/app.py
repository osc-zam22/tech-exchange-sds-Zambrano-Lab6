# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import *
from collections import defaultdict

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "Form is empty"
    
    answers = [] 
    userDict = {} 
    results = []

    # creating userDict for checkDicts()
    for item in request.form:
        userDict[item] = request.form[item]

    # answers from answer_key to display in results.html
    for val in answer_key.values():
        answers.append(val)
    
    # putting items from the dict returned from checkDicts() into a list because dictionarys cant be passed into 'render_templates' 
    for key, val in checkDicts(userDict).items():
        results.append({key: val})

    return render_template('results.html', results = results, answers = answers)       

if __name__ == "__main__":
    app.run(debug=True)