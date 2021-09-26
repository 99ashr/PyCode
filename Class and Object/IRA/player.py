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
class Player:
    def __init__(self, matches, goal, rating, name):
        self.matches = matches
        self.goal = goal
        self.rating = rating
        self.name = name


class FootballLeague:
    def __init__(self, leagueName, playerList):
        self.leagueName = leagueName
        self.playerList = playerList

    def findMaximumPlayerByRating(self):
        ratingList = []
        for i in playerList:
            ratingList.append(i.rating)
        maxobj = max(ratingList)
        # print(maxobj)

        if maxobj != 0:
            return maxobj
        else:
            return None

    def sortPlayerByGoals(self):
        goalsList = []
        for i in playerList:
            goalsList.append(i.goal)
        x = sorted(goalsList)
        # print(x)
        if len(x) != 0:
            return x
        else:
            return None


playerList = []
n = int(input())
for i in range(n):
    matches = int(input())
    goals = int(input())
    rating = int(input())
    name = input()
    playerList.append(Player(matches, goals, rating, name))
r = FootballLeague.findMaximumPlayerByRating(playerList)

if r == None:
    print("No Data Found.")
else:
    for i in playerList:
        if i.rating == r:
            print(i.matches)
            print(i.goal)
            print(i.rating)
            print(i.name)

g = FootballLeague.sortPlayerByGoals(playerList)

if g == None:
    print("No Data Found.")
else:
    for i in g:
        print(i)
