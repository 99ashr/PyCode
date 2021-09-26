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

awk 'BEGIN{FS=";";max_tax=0}{
    tax=$3*.1
    if(tax>max_tax){
        max_tax=tax
    }
}
END{
    print(max_tax)
}' emp_details.txt