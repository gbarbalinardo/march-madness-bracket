__author__ = 'giuseppe'
import numpy as np
import json


class Match:

    def __init__(self, team1, team2, has_draw):
        self.team1 = team1
        self.team2 = team2
        self.has_draw = has_draw
        self.winner = None
        self.goal_scored_team1 = 0
        self.goal_scored_team2 = 0
        self.play_match()

    def play_match(self):
        k = 1
        avgScoredByTeam1 = self.team1.attack / self.team2.defense * k
        avgScoredByTeam2 = self.team2.attack / self.team1.defense * k
        while True:
            self.goal_scored_team1 = np.random.poisson(avgScoredByTeam1)
            self.goal_scored_team2 = np.random.poisson(avgScoredByTeam2)
            if self.goal_scored_team1 > self.goal_scored_team2:
                self.team1.points += 3
                self.team1.won += 1
                self.team2.lost += 1
                self.winner = self.team1
                break
            elif self.goal_scored_team1 < self.goal_scored_team2:
                self.team2.points += 3
                self.team2.won += 1
                self.team1.lost += 1
                self.winner = self.team2
                break
            else:
                if self.has_draw is True:
                    self.team1.points += 1
                    self.team2.points += 1
                    self.team1.drawn += 1
                    self.team2.drawn += 1
                    break
        self.team1.scored += self.goal_scored_team1
        self.team2.scored += self.goal_scored_team2
        self.team1.conceded += self.goal_scored_team2
        self.team2.conceded += self.goal_scored_team1
        self.team1.difference += self.goal_scored_team1-self.goal_scored_team2
        self.team2.difference += self.goal_scored_team2-self.goal_scored_team1
        # self.printMatch()

    def printMatch(self):
        print self.team1.name + " - " + self.team2.name + " => " + self.winner.name

class Team:

    def __init__(self, name, data):
        self.points = 0
        self.won = 0
        self.lost = 0
        self.drawn = 0
        self.scored = 0
        self.conceded = 0
        self.difference = 0
        self.name = name.lower()
        for result in data:
            if self.name in result[0].lower():
                self.attack = result[1]
                self.defense = result[2]
                break
        if self.attack is None:
            print "error" + name + "is not a team"

def repeat_match(team1, team2, repetitions, with_output):
    winners = {}
    for i in range(0, repetitions):
        winner = Match(team1, team2, False).winner
        if winners.has_key(winner.name):
            winners[winner.name] += 1
        else:
            winners[winner.name] = 1

    if with_output:
        for key in sorted(winners, key=winners.get, reverse=True):
            print key + ": " + str(winners[key]) + "/" + str(repetitions) + "\t",
        print
    if len(winners.keys()) == 1:
        return winner
    else:
        if winners[team1.name] > winners[team2.name]:
            return team1
        else:
            return team2


            
def play_tournament(allResults, repetitions, with_output):

    kentucky_1 = Team("Kentucky 1", allResults)
    arizona_2 = Team("Arizona 2", allResults)
    wisconsin_1 = Team("Wisconsin 1", allResults)
    virginia_2 = Team("Virginia 2", allResults)
    villanova_1 = Team("Villanova 1", allResults)
    gonzaga_2 = Team("Gonzaga 2", allResults)
    duke_1 = Team("Duke 1", allResults)
    utah_5 = Team("Utah 5", allResults)
    oklahoma_3 = Team("Oklahoma 3", allResults)
    notre_dame_3 = Team("Notre Dame 3", allResults)
    kansas_2 = Team("Kansas 2", allResults)
    northern_iowa_5 = Team("Northern Iowa 5", allResults)
    iowa_st_3 = Team("Iowa St. 3", allResults)
    wichita_st_7 = Team("Wichita St. 7", allResults)
    baylor_3 = Team("Baylor 3", allResults)
    north_carolina_4 = Team("North Carolina 4", allResults)
    michigan_st_7 = Team("Michigan St. 7", allResults)
    louisville_4 = Team("Louisville 4", allResults)
    smu_6 = Team("SMU 6", allResults)
    texas_11 = Team("Texas 11", allResults)
    ohio_st_10 = Team("Ohio St. 10", allResults)
    georgetown_4 = Team("Georgetown 4", allResults)
    butler_6 = Team("Butler 6", allResults)
    iowa_7 = Team("Iowa 7", allResults)
    west_virginia_5 = Team("West Virginia 5", allResults)
    xavier_6 = Team("Xavier 6", allResults)
    san_diego_st_8 = Team("San Diego St. 8", allResults)
    providence_6 = Team("Providence 6", allResults)
    arkansas_5 = Team("Arkansas 5", allResults)
    vcu_7 = Team("VCU 7", allResults)
    davidson_10 = Team("Davidson 10", allResults)
    maryland_4 = Team("Maryland 4", allResults)
    cincinnati_8 = Team("Cincinnati 8", allResults)
    stephen_f_austin_12 = Team("Stephen F. Austin 12", allResults)
    georgia_10 = Team("Georgia 10", allResults)
    oklahoma_st_9 = Team("Oklahoma St. 9", allResults)
    north_carolina_st_8 = Team("North Carolina St. 8", allResults)
    dayton_11 = Team("Dayton 11", allResults)
    ucla_11 = Team("UCLA 11", allResults)
    st_johns_9 = Team("St. John's 9", allResults)
    lsu_9 = Team("LSU 9", allResults)
    mississippi_11 = Team("Mississippi 11", allResults)
    oregon_8 = Team("Oregon 8", allResults)
    purdue_9 = Team("Purdue 9", allResults)
    indiana_10 = Team("Indiana 10", allResults)
    buffalo_12 = Team("Buffalo 12", allResults)
    valparaiso_13 = Team("Valparaiso 13", allResults)
    georgia_st_14 = Team("Georgia St. 14", allResults)
    harvard_13 = Team("Harvard 13", allResults)
    new_mexico_st_15 = Team("New Mexico St. 15", allResults)
    wofford_12 = Team("Wofford 12", allResults)
    uc_irvine_13 = Team("UC Irvine 13", allResults)
    wyoming_12 = Team("Wyoming 12", allResults)
    northeastern_14 = Team("Northeastern 14", allResults)
    uab_14 = Team("UAB 14", allResults)
    north_florida_16 = Team("North Florida 16", allResults)
    albany_14 = Team("Albany 14", allResults)
    eastern_washington_13 = Team("Eastern Washington 13", allResults)
    coastal_carolina_16 = Team("Coastal Carolina 16", allResults)
    belmont_15 = Team("Belmont 15", allResults)
    north_dakota_st_15 = Team("North Dakota St. 15", allResults)
    lafayette_16 = Team("Lafayette 16", allResults)
    hampton_16 = Team("Hampton 16", allResults)


    # Play first stage
    a1 = repeat_match(kentucky_1, hampton_16, repetitions, with_output)
    a2 = repeat_match(cincinnati_8, purdue_9, repetitions, with_output)
    a3 = repeat_match(west_virginia_5, buffalo_12, repetitions, with_output)
    a4 = repeat_match(maryland_4, valparaiso_13, repetitions, with_output)
    a5 = repeat_match(butler_6, texas_11, repetitions, with_output)
    a6 = repeat_match(notre_dame_3, northeastern_14, repetitions, with_output)
    a7 = repeat_match(wichita_st_7, indiana_10, repetitions, with_output)
    a8 = repeat_match(kansas_2, new_mexico_st_15, repetitions, with_output)
    a9 = repeat_match(wisconsin_1, coastal_carolina_16, repetitions, with_output)
    a10 = repeat_match(oregon_8, oklahoma_st_9, repetitions, with_output)
    a11 = repeat_match(arkansas_5, wofford_12, repetitions, with_output)
    a12 = repeat_match(north_carolina_4, harvard_13, repetitions, with_output)
    a13 = repeat_match(xavier_6, mississippi_11, repetitions, with_output)
    a14 = repeat_match(baylor_3, georgia_st_14, repetitions, with_output)
    a15 = repeat_match(vcu_7, ohio_st_10, repetitions, with_output)
    a16 = repeat_match(arizona_2, texas_11, repetitions, with_output)
    a17 = repeat_match(villanova_1, lafayette_16, repetitions, with_output)
    a18 = repeat_match(north_carolina_st_8, lsu_9, repetitions, with_output)
    a19 = repeat_match(northern_iowa_5, wyoming_12, repetitions, with_output)
    a20 = repeat_match(louisville_4, uc_irvine_13, repetitions, with_output)
    a21 = repeat_match(providence_6, dayton_11, repetitions, with_output)
    a22 = repeat_match(oklahoma_3, albany_14, repetitions, with_output)
    a23 = repeat_match(michigan_st_7, georgia_10, repetitions, with_output)
    a24 = repeat_match(virginia_2, belmont_15, repetitions, with_output)
    a25 = repeat_match(duke_1, north_florida_16, repetitions, with_output)
    a26 = repeat_match(san_diego_st_8, st_johns_9, repetitions, with_output)
    a27 = repeat_match(utah_5, stephen_f_austin_12, repetitions, with_output)
    a28 = repeat_match(georgetown_4, eastern_washington_13, repetitions, with_output)
    a29 = repeat_match(smu_6, ucla_11, repetitions, with_output)
    a30 = repeat_match(iowa_st_3, uab_14, repetitions, with_output)
    a31 = repeat_match(iowa_7, davidson_10, repetitions, with_output)
    a32 = repeat_match(gonzaga_2, north_dakota_st_15, repetitions, with_output)

    # Play second stage
    b1 = repeat_match(a1, a2, repetitions, with_output)
    b2 = repeat_match(a3, a4, repetitions, with_output)
    b3 = repeat_match(a5, a6, repetitions, with_output)
    b4 = repeat_match(a7, a8, repetitions, with_output)
    b5 = repeat_match(a9, a10, repetitions, with_output)
    b6 = repeat_match(a11, a12, repetitions, with_output)
    b7 = repeat_match(a13, a14, repetitions, with_output)
    b8 = repeat_match(a15, a16, repetitions, with_output)
    b9 = repeat_match(a17, a18, repetitions, with_output)
    b10 = repeat_match(a19, a20, repetitions, with_output)
    b11 = repeat_match(a21, a22, repetitions, with_output)
    b12 = repeat_match(a23, a24, repetitions, with_output)
    b13 = repeat_match(a25, a26, repetitions, with_output)
    b14 = repeat_match(a27, a28, repetitions, with_output)
    b15 = repeat_match(a29, a30, repetitions, with_output)
    b16 = repeat_match(a31, a32, repetitions, with_output)

    # Play third stage
    c1 = repeat_match(b1, b2, repetitions, with_output)
    c2 = repeat_match(b3, b4, repetitions, with_output)
    c3 = repeat_match(b5, b6, repetitions, with_output)
    c4 = repeat_match(b7, b8, repetitions, with_output)
    c5 = repeat_match(b9, b10, repetitions, with_output)
    c6 = repeat_match(b11, b12, repetitions, with_output)
    c7 = repeat_match(b13, b14, repetitions, with_output)
    c8 = repeat_match(b15, b16, repetitions, with_output)

    # Play forth stage
    d1 = repeat_match(c1, c2, repetitions, with_output)
    d2 = repeat_match(c3, c4, repetitions, with_output)
    d3 = repeat_match(c5, c6, repetitions, with_output)
    d4 = repeat_match(c7, c8, repetitions, with_output)

    # Play semifinal stage
    e1 = repeat_match(d1, d2, repetitions, with_output)
    e2 = repeat_match(d3, d4, repetitions, with_output)

    # Play final
    winner = repeat_match(e1, e2, repetitions, with_output)

    return winner


def main():

    # Team Name, Attack, Defence
    json_data = open('input_value.json')
    allResults = json.load(json_data)
    json_data.close()
    repetitions = 100

    # Simulate all the matches
    print "\n\nSINGLE MATCHES"
    play_tournament(allResults, repetitions, True)


    # Simulate the full tournament
    winners = {}
    for i in range(0, 1000):

        winner = play_tournament(allResults, 1, False)

        if winners.has_key(winner.name):
            winners[winner.name] += 1
        else:
            winners[winner.name] = 1


    print "\n\nFULL TOURNAMENT"
    for key in sorted(winners, key=winners.get, reverse=True):
        print key + ": " + str(winners[key])

if __name__ == '__main__':
    main()