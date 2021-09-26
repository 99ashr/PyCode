# Copyright 2021 gaura
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

awk 'BEGIN{FS="#";OFS=",";c=0;g=0}{
    if(substr($4,4,4)=='2017'){
        print($1,$2,$3,$4)
        ++g
    }
    if($3>20){
        ++c
    }
}
END{
    if(g==0){
        print("No Data Found")
    }
    if(c!=0){
        print(c" Players have played more than 20 games globally!")
    }
    else{
        print("All are rookies!!!")
    }
}' playerDetails.txt