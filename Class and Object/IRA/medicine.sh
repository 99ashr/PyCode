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

awk 'BEGIN{FS=",";IGNORECASE=1;count=0;}{
    split($1,a,"_")
    if (a[1]=="TB" && a[3]>10){
        print($1)
        ++count
    }
}
END{
    if(count==0){
        print("No medicine found greater than 10 pills")
    }
    else{
        print(count)
    }
}' medicineDetails.txt