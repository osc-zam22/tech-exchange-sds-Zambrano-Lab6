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

answer_key = {
    "New York" : "Albany" ,
    "Florida" : "Tallahassee" ,
    "California" : "Sacramento" ,
    "Texas" : "Austin",
    "Hawaii" : "Honolulu"
    }

def checkDicts(userDict):
    result_dict = {
        "New York" : True,
        "Florida" : True,
        "California" : True,
        "Texas" : True,
        "Hawaii" : True
    }
    for key in userDict.keys():
        if userDict[key].lower() != answer_key[key].lower():
            result_dict[key] = False
    return result_dict


