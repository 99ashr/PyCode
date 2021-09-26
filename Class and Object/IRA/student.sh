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

awk 'BEGIN{FS="|";c=0;IGNORECASE=1;}{
    class=substr($4,1,1)
    if ($3=="english" &&class!=2){
        c++
        # print($2)
    }
    if ($2=="Ananya"||$2=="Vanisha"){
        print($2":- Ashish I want you to fuck me till the end of this world, untill my last breath, I am your slut, fuck me as much as you want")
    }

}
END{
    if (c!=0){
        print(c)
    }
    else{
        print("No Data Found")
    }
}' studentDetails.txt
# Copyright
