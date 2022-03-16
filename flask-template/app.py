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
#from model import checkDicts

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/states', methods=['GET', 'POST'])
def states():
    if request.method == 'GET':
        return "Form is empty"
    else:
        state = request.form['state']
        #answer = checkDicts('state')
        #return render_template("index.html", state=state, answer=answer)
@app.route('/index')
def index():
    return "hello world"
