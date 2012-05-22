from operator import itemgetter

#This app will show fans who to root for in NFL games when thier team isnt playing. 
#It will give the games more context and add a narrative
#Make dictionary of teams into a 8 lists of dictionaries for each division

#OVERVIEW
NFCEast = ['Cowboys', 'Giants' , 'Eagles' , 'Redskins']
Cowboys = {"Games Played" : 16.000, "Team": "Dallas Cowboys", "Wins" : 8, "Losses" : 8, "Ties" : 0, "Division Wins" : 4, "Division Losses" : 2, "Division Ties": 0}
Eagles = {"Games Played" : 16.000, "Team": "Philadelphia Eagles", "Wins" : 8, "Losses" : 8, "Ties" : 0, "Division Wins" : 4, "Division Losses" : 2, "Division Ties": 0}
Giants = {"Games Played" : 16.000, "Team": "New York Giants", "Wins" : 9, "Losses" : 7, "Ties" : 0, "Division Wins" : 4, "Division Losses" : 2, "Division Ties": 0}
Redskins = {"Games Played" : 16.000, "Team": "Washington Redskins", "Wins" : 5, "Losses" : 11, "Ties" : 0, "Division Wins" : 4, "Division Losses" : 2, "Division Ties": 0}


NFCNorth = ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings']

NFCSouth = ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers']

NFCWest = ['Arizona Cardinals', 'St. Louis Rams', 'San Francisco 49ers', 'Seattle Seahawks']

AFCEast = ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets']

AFCNorth = ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers']

AFCSouth = ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans']

AFCWest = ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
afcwest_wins = {"broncos": 8.000, "chargers": 8.000, "raiders": 8.000, "chiefs": 7.000}
afcwest_div_wins = {"broncos" : 3.000, "chargers" : 3.000, "raiders" : 3.000, "chiefs" : 3.000}


NFC = NFCEast + NFCNorth + NFCSouth + NFCWest

AFC = AFCEast + AFCNorth + AFCSouth + AFCWest

NFL = NFC + AFC


#LEAGUE WINS
leaguewins = {"patriots" : 13.000, "jets":8.000, "dolphins" : 6.000, "bills": 6.000, 
"ravens" : 12.000 , "steelers": 12.000, "bengals": 9.000, "browns": 4.000, 
"texans": 10.000, "titans": 9.000 , "jaguars": 5.000 , "colts": 2.000 , 
"broncos": 8.000, "chargers": 8.000, "raiders": 8.000, "chiefs": 7.000,
"eagles" : 8.000, "giants" : 9.000, "cowboys" : 8.000, "redskins" : 5.000, 
"packers": 15.000, "lions": 10.000, "bears": 8.000, "vikings": 3.000, 
"saints": 13.000, "falcons": 10.000, "panthers": 6.000, "buccaneers": 4.000,
"49ers": 13.000, "cardinals": 8.000, "seahawks": 7.000, "rams": 2.000, 
 }

#LEAGUE LOSSES
leaguelosses = {"patriots" : 3.000 , "jets": 8.000, "dolphins" : 10.000, "bills": 10.000, 
"ravens" : 4.000, "steelers": 4.000, "bengals": 7.000, "browns": 12.000, 
"texans": 6.000, "titans": 7.000, "jaguars": 11.000, "colts": 14.000, 
"broncos": 8.000 , "chargers": 8.000, "raiders": 8.000, "chiefs": 9.000, 
"packers": 1.000, "lions": 8.000, "bears": 8.000, "vikings": 11.000, 
"saints": 1.000, "falcons": 6.000, "panthers": 8.000, "buccaneers": 13.000,
"49ers": 3.000, "cardinals": 6.000, "seahawks": 10.000, "rams": 12.000, 
"eagles" : 8.000 , "giants" : 7.000, "cowboys" : 9.000 , "redskins" : 14.000, 
}


#WIN PERCENTAGE
nfceast_wins = {"giants" : leaguewins["giants"], "eagles" : leaguewins["eagles"], "cowboys" : leaguewins["cowboys"], "redskins" : leaguewins["redskins"]}
nfceast_losses = {"giants" : leaguelosses["giants"], "eagles" : leaguelosses["eagles"], "cowboys": leaguelosses["cowboys"], "redskins": leaguelosses["redskins"]}
nfceast_gp = {"giants" : nfceast_wins["giants"] + nfceast_losses["giants"], "eagles" : nfceast_wins["eagles"] + nfceast_losses["eagles"], "cowboys" : nfceast_wins["cowboys"] + nfceast_losses["cowboys"], "redskins" : nfceast_wins["redskins"] + nfceast_losses["redskins"]}
nfceast_pct = {"giants" : nfceast_wins["giants"] / nfceast_gp["giants"], "eagles" : nfceast_wins["eagles"] / nfceast_gp["eagles"], "cowboys" : nfceast_wins["cowboys"] / nfceast_gp["cowboys"], "redskins" : nfceast_wins["redskins"] / nfceast_gp["redskins"]}
nfceast_Prob_torank = sorted(nfceast_pct.items(), reverse=True, key=itemgetter(1))
nfceast_champ = nfceast_Prob_torank[0]

nfcnorth_wins = {"bears" : leaguewins["bears"], "lions" : leaguewins["lions"], "packers" : leaguewins["packers"], "vikings" : leaguewins["vikings"]}
nfcnorth_losses = {"bears" : leaguelosses["bears"], "lions" : leaguelosses["lions"], "packers": leaguelosses["packers"], "vikings": leaguelosses["vikings"]}
nfcnorth_gp = {"bears" : nfcnorth_wins["bears"] + nfcnorth_losses["bears"], "lions" : nfcnorth_wins["lions"] + nfcnorth_losses["lions"], "packers" : nfcnorth_wins["packers"] + nfcnorth_losses["packers"], "vikings" : nfcnorth_wins["vikings"] + nfcnorth_losses["vikings"]}
nfcnorth_pct = {"bears" : nfcnorth_wins["bears"] / nfcnorth_gp["bears"], "lions" : nfcnorth_wins["lions"] / nfcnorth_gp["lions"], "packers" : nfcnorth_wins["packers"] / nfcnorth_gp["packers"], "vikings" : nfcnorth_wins["vikings"] / nfcnorth_gp["vikings"]}
nfcnorth_Prob_torank = sorted(nfcnorth_pct.items(), reverse=True, key=itemgetter(1))
nfcnorth_champ = nfcnorth_Prob_torank[0]

nfcsouth_wins = {"falcons" : leaguewins["falcons"], "panthers" : leaguewins["panthers"], "saints" : leaguewins["saints"], "buccaneers" : leaguewins["buccaneers"]}
nfcsouth_losses = {"falcons" : leaguelosses["falcons"], "panthers" : leaguelosses["panthers"], "saints": leaguelosses["saints"], "buccaneers": leaguelosses["buccaneers"]}
nfcsouth_gp = {"falcons" : nfcsouth_wins["falcons"] + nfcsouth_losses["falcons"], "panthers" : nfcsouth_wins["panthers"] + nfcsouth_losses["panthers"], "saints" : nfcsouth_wins["saints"] + nfcsouth_losses["saints"], "buccaneers" : nfcsouth_wins["buccaneers"] + nfcsouth_losses["buccaneers"]}
nfcsouth_pct = {"falcons" : nfcsouth_wins["falcons"] / nfcsouth_gp["falcons"], "panthers" : nfcsouth_wins["panthers"] / nfcsouth_gp["panthers"], "saints" : nfcsouth_wins["saints"] / nfcsouth_gp["saints"], "buccaneers" : nfcsouth_wins["buccaneers"] / nfcsouth_gp["buccaneers"]}
nfcsouth_Prob_torank = sorted(nfcsouth_pct.items(), reverse=True, key=itemgetter(1))
nfcsouth_champ = nfcsouth_Prob_torank[0]

nfcwest_wins = {"cardinals" : leaguewins["cardinals"], "49ers" : leaguewins["49ers"], "seahawks" : leaguewins["seahawks"], "rams" : leaguewins["rams"]}
nfcwest_losses = {"cardinals" : leaguelosses["cardinals"], "49ers" : leaguelosses["49ers"], "seahawks": leaguelosses["seahawks"], "rams": leaguelosses["rams"]}
nfcwest_gp = {"cardinals" : nfcwest_wins["cardinals"] + nfcwest_losses["cardinals"], "49ers" : nfcwest_wins["49ers"] + nfcwest_losses["49ers"], "seahawks" : nfcwest_wins["seahawks"] + nfcwest_losses["seahawks"], "rams" : nfcwest_wins["rams"] + nfcwest_losses["rams"]}
nfcwest_pct = {"cardinals" : nfcwest_wins["cardinals"] / nfcwest_gp["cardinals"], "49ers" : nfcwest_wins["49ers"] / nfcwest_gp["49ers"], "seahawks" : nfcwest_wins["seahawks"] / nfcwest_gp["seahawks"], "rams" : nfcwest_wins["rams"] / nfcwest_gp["rams"]}
nfcwest_Prob_torank = sorted(nfcwest_pct.items(), reverse=True, key=itemgetter(1))
nfcwest_champ = nfcwest_Prob_torank[0]

afceast_wins = {"patriots" : leaguewins["patriots"], "jets" : leaguewins["jets"], "dolphins" : leaguewins["dolphins"], "bills" : leaguewins["bills"]}
afceast_losses = {"patriots" : leaguelosses["patriots"], "jets" : leaguelosses["jets"], "dolphins": leaguelosses["dolphins"], "bills": leaguelosses["bills"]}
afceast_gp = {"patriots" : afceast_wins["patriots"] + afceast_losses["patriots"], "jets" : afceast_wins["jets"] + afceast_losses["jets"], "dolphins" : afceast_wins["dolphins"] + afceast_losses["dolphins"], "bills" : afceast_wins["bills"] + afceast_losses["bills"]}
afceast_pct = {"patriots" : afceast_wins["patriots"] / afceast_gp["patriots"], "jets" : afceast_wins["jets"] / afceast_gp["jets"], "dolphins" : afceast_wins["dolphins"] / afceast_gp["dolphins"], "bills" : afceast_wins["bills"] / afceast_gp["bills"]}
afceast_Prob_torank = sorted(afceast_pct.items(), reverse=True, key=itemgetter(1,))
afceast_champ = afceast_Prob_torank[0]

afcnorth_wins = {"steelers" : leaguewins["steelers"], "ravens" : leaguewins["ravens"], "bengals" : leaguewins["bengals"], "browns" : leaguewins["browns"]}
afcnorth_losses = {"steelers" : leaguelosses["steelers"], "ravens" : leaguelosses["ravens"], "bengals": leaguelosses["bengals"], "browns": leaguelosses["browns"]}
afcnorth_gp = {"steelers" : afcnorth_wins["steelers"] + afcnorth_losses["steelers"], "ravens" : afcnorth_wins["ravens"] + afcnorth_losses["ravens"], "bengals" : afcnorth_wins["bengals"] + afcnorth_losses["bengals"], "browns" : afcnorth_wins["browns"] + afcnorth_losses["browns"]}
afcnorth_pct = {"steelers" : afcnorth_wins["steelers"] / afcnorth_gp["steelers"], "ravens" : afcnorth_wins["ravens"] / afcnorth_gp["ravens"], "bengals" : afcnorth_wins["bengals"] / afcnorth_gp["bengals"], "browns" : afcnorth_wins["browns"] / afcnorth_gp["browns"]}
afcnorth_Prob_torank = sorted(afcnorth_pct.items(), reverse=True, key=itemgetter(1))
afcnorth_champ = afcnorth_Prob_torank[0]

afcsouth_wins = {"titans" : leaguewins["titans"], "jaguars" : leaguewins["jaguars"], "texans" : leaguewins["texans"], "colts" : leaguewins["colts"]}
afcsouth_losses = {"titans" : leaguelosses["titans"], "jaguars" : leaguelosses["jaguars"], "texans": leaguelosses["texans"], "colts": leaguelosses["colts"]}
afcsouth_gp = {"titans" : afcsouth_wins["titans"] + afcsouth_losses["titans"], "jaguars" : afcsouth_wins["jaguars"] + afcsouth_losses["jaguars"], "texans" : afcsouth_wins["texans"] + afcsouth_losses["texans"], "colts" : afcsouth_wins["colts"] + afcsouth_losses["colts"]}
afcsouth_pct = {"titans" : afcsouth_wins["titans"] / afcsouth_gp["titans"], "jaguars" : afcsouth_wins["jaguars"] / afcsouth_gp["jaguars"], "texans" : afcsouth_wins["texans"] / afcsouth_gp["texans"], "colts" : afcsouth_wins["colts"] / afcsouth_gp["colts"]}
afcsouth_Prob_torank = sorted(afcsouth_pct.items(), reverse=True, key=itemgetter(1))
afcsouth_champ = afcsouth_Prob_torank[0]

afcwest_wins = {"chargers" : leaguewins["chargers"], "broncos" : leaguewins["broncos"], "raiders" : leaguewins["raiders"], "chiefs" : leaguewins["chiefs"]}
afcwest_losses = {"chargers" : leaguelosses["chargers"], "broncos" : leaguelosses["broncos"], "raiders": leaguelosses["raiders"], "chiefs": leaguelosses["chiefs"]}
afcwest_gp = {"chargers" : afcwest_wins["chargers"] + afcwest_losses["chargers"], "broncos" : afcwest_wins["broncos"] + afcwest_losses["broncos"], "raiders" : afcwest_wins["raiders"] + afcwest_losses["raiders"], "chiefs" : afcwest_wins["chiefs"] + afcwest_losses["chiefs"]}
afcwest_pct = {"chargers" : afcwest_wins["chargers"] / afcwest_gp["chargers"], "broncos" : afcwest_wins["broncos"] / afcwest_gp["broncos"], "raiders" : afcwest_wins["raiders"] / afcwest_gp["raiders"], "chiefs" : afcwest_wins["chiefs"] / afcwest_gp["chiefs"]}
afcwest_Prob_torank = sorted(afcwest_pct.items(), reverse=True, key=itemgetter(1))
afcwest_champ = afcwest_Prob_torank[0]

#DIVINSIONAL WIN PERCENTAGE
nfceast_div_wins = {"giants" : 3.000, "eagles" : 5.000, "cowboys" : 2.000, "redskins" : 2.000}
nfceast_div_losses = {"giants" : 3.000, "eagles" : 1.000, "cowboys": 4.000, "redskins": 4.000}
nfceast_div_gp = {"giants" : nfceast_div_wins["giants"] + nfceast_div_losses["giants"], "eagles" : nfceast_div_wins["eagles"] + nfceast_div_losses["eagles"], "cowboys" : nfceast_div_wins["cowboys"] + nfceast_div_losses["cowboys"], "redskins" : nfceast_div_wins["redskins"] + nfceast_div_losses["redskins"]}
nfceast_div_pct = {"giants" : nfceast_div_wins["giants"] / nfceast_div_gp["giants"], "eagles" : nfceast_div_wins["eagles"] / nfceast_div_gp["eagles"], "cowboys" : nfceast_div_wins["cowboys"] / nfceast_div_gp["cowboys"], "redskins" : nfceast_div_wins["redskins"] / nfceast_div_gp["redskins"]}


#COMMON GAMES RECORD
patriots_CG = {"jets":[1.000+1.000,0.000+0.000, 30+37,21+16], "dolphins" : [1.000+1.000,0.000+0.000,38+24,24+27], "bills": [0.000+1.000,1.000+0.000,31+49,34+21], 
"ravens" : [], "steelers": [ 0.000,1.000,17,25,], "bengals": [], "browns": [], 
"texans": [], "titans": [], "jaguars": [], "colts": [1.000,0.000,31,24], 
"broncos": [1.000,0.000, 41,23], "chargers": [1.000,0.000,21,35], "raiders": [1.000,0.000,31,19], "chiefs": [1.000,0.000, 34,3],
"eagles" : [1.000,0.000, 38,20], "giants" : [0.000, 1.000, 20,24], "cowboys" : [1.000,0.000,20,16], "redskins" : [1.000,0.000, 34,27], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }


 
jets_CG = {"patriots" : [0.000+0.000, 1.000+1.000, 21+16, 30+37, ],"dolphins" : [1.000+0.000, 0.000+1.000, 24+17, 6+19], "bills": [1.000+1.000, 0.000+0.000,27+28,11+24],  
"ravens" : [0.000, 1.000, 17,34] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [1.000, 0.000, 32,3] , "colts": [] , 
"broncos": [0.000, 1.000, 13,17], "chargers": [1.000, 0.000, 27,21], "raiders": [0.000, 1.000, 24,34], "chiefs": [1.000, 0.000, 37,10],
"eagles" : [0.000, 1.000, 19,45], "giants" : [0.000, 1.000, 14,29], "cowboys" : [1.000, 0.000, 27,24], "redskins" : [1.000, 0.000, 34,19], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }

 
dolphins_CG = {"patriots" : [0.000+0.000, 1.000+1.000, 24+24,38+27] ,"jets":[0.000+1.000, 1.000+0.000,6+19,24+17], "bills": [1.000+1.000,0.000+0.000,35+30,8+23],  
"ravens" : [] , "steelers": [], "bengals": [], "browns": [0.000, 1.000, 16,17], 
"texans": [0.000, 1.000, 13,23], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [0.000, 1.000, 15,18 ], "chargers": [0.000, 1.000, 16,26], "raiders": [1.000, 0.000, 34,14], "chiefs": [1.000, 0.000, 31,3],
"eagles" : [0.000, 1.000, 10,26], "giants" : [0.000, 1.000, 17,20], "cowboys" : [0.000, 1.000, 19,20], "redskins" : [1.000, 0.000, 20,9], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
bills_CG = {"patriots" : [1.000+0.000, 0.000+1.000, 34+21, 31+49], "jets":[0.000+0.000, 1.000+1.000, 11+24, 27+28], "dolphins" : [0.000+0.000, 1.000+1.000, 8+23, 35+30] , 
"ravens" : [] , "steelers": [], "bengals": [0.000, 1.000, 20, 23], "browns": [], 
"texans": [], "titans": [0.000, 1.000, 17, 23] , "jaguars": [] , "colts": [] , 
"broncos": [1.000, 0.000, 40, 14], "chargers": [0.000, 1.000, 10, 37], "raiders": [1.000, 0.000, 38, 35], "chiefs": [1.000, 0.000, 41, 7],
"eagles" : [1.000, 0.000, 31, 24], "giants" : [0.000, 1.000, 24, 27], "cowboys" : [0.000, 1.000, 7, 44], "redskins" : [1.000, 0.000, 23, 0], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
ravens_CG = {"patriots" : [], "jets":[1.000, 0.000, 34, 17], "dolphins" : [], "bills": [], 
"steelers": [1.000+1.000, 0.000+0.000, 35+23, 7+ 20 ],"bengals": [1.000+1.000, 0.000+0.000, 31+24, 24+16], "browns": [1.000+1.000, 0.000+0.000, 24+20,10+14], 
"texans": [1.000, 0.000, 29, 14], "titans": [0.000, 1.000, 13, 26] , "jaguars": [0.000, 1.000, 7, 12] , "colts": [1.000, 0.000, 24,10] , 
"broncos": [], "chargers": [0.000, 1.000, 14,34], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [1.000, 0.000, 16,6], "cardinals": [1.000, 0.000, 30, 27], "seahawks": [0.000, 1.000, 17, 22], "rams": [1.000, 0.000, 37, 7], 
 }
 
steelers_CG = {"patriots" : [1.000, 0.000, 25,17], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [0.000+0.000, 1.000+ 1.000, 7+20,35+ 23], "bengals": [1.000+1.000, 0.000+0.000, 24+35,17+7], "browns": [1.000+1.000, 0.000+0.000, 14+13,3+9], 
"texans": [0.000, 1.000, 10,17], "titans": [1.000, 0.000, 38,17] , "jaguars": [1.000, 0.000, 17,13] , "colts": [1.000, 0.000, 23,20] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [1.000, 0.000, 13,9],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [0.000, 1.000, 3,20], "cardinals": [1.000, 0.000, 32,20], "seahawks": [1.000, 0.000, 24,0], "rams": [1.000, 0.000, 27,0], 
 }

bengals_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [1.000, 0.000, 23,20], 
"ravens" : [0.000+0.000, 1.000+1.000, 24+16, 31+24], "steelers": [0.000+0.000, 1.000+1.000, 17+7, 24+35] , "browns": [1.000+1.000, 0.000+0.000, 27+23,17+20] , 
"texans": [0.000, 1.000, 19,20], "titans": [1.000, 0.000, 24,17] , "jaguars": [1.000, 0.000, 30,20] , "colts": [1.000, 0.000, 27,17] , 
"broncos": [0.000, 1.000, 22,24], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [0.000, 1.000, 8,13], "cardinals": [1.000, 0.000, 23,16], "seahawks": [1.000, 0.000, 34,12], "rams": [1.000, 0.000, 20,13], 
 }
 
browns_CG = {"patriots" : [], "jets":[], "dolphins" : [1.000, 0.000, 17,16], "bills": [], 
"ravens" : [0.000+0.000, 1.000+1.000, 10+14, 24+20] , "steelers": [0.000+0.000, 1.000+1.000, 3+9, 14+13] , "bengals": [0.000+0.000, 1.000+1.000, 17+20, 27+23],    
"texans": [0.000, 1.000, 12,30], "titans": [0.000, 1.000, 13,31] , "jaguars": [1.000, 0.000, 14,10] , "colts": [1.000, 0.000, 27,19] , 
"broncos": [], "chargers": [], "raiders": [0.000, 1.000, 17,24], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [0.000, 1.000, 10,20], "cardinals": [0.000, 1.000, 17,20 ], "seahawks": [1.000, 0.000, 6,3], "rams": [0.000, 1.000, 12,13], 
 }
 
texans_CG = {"patriots" : [], "jets":[], "dolphins" : [1.000, 0.000, 23,13], "bills": [], 
"ravens" : [0.000, 1.000, 14,29] , "steelers": [1.000, 0.000, 17,10], "bengals": [1.000, 0.000, 20,19], "browns": [1.000, 0.000, 30,12], 
"titans": [1.000+0.000, 0.000+1.000, 41+22, 7+23] , "jaguars": [1.000+1.000, 0.000+0.000, 24+20, 14+13] , "colts": [1.000+0.000, 0.000+1.000, 34+16, 7+19], 
"broncos": [], "chargers": [], "raiders": [0.000, 1.000, 20,25], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [0.000, 1.000, 33,40], "falcons": [1.000, 0.000, 17,10], "panthers": [0.000, 1.000, 13,28], "buccaneers": [1.000, 0.000, 37,9],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
titans_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [1.000, 0.000, 23,17], 
"ravens" : [1.000, 0.000, 26,13] , "steelers": [0.000, 1.000, 17,38], "bengals": [0.000, 1.000, 17,24], "browns": [1.000, 0.000, 31,13], 
"texans": [0.000+1.000, 1.000+0.000, 7+23, 41+22] , "jaguars": [0.000+1.000,  1.000+0.000, 14+23, 16+17] , "colts": [1.000+0.000, 0.000+1.000, 27+13, 10+ 27] , 
"broncos": [1.000, 0.000, 17,14], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [0.000, 1.000, 17,22], "falcons": [0.000, 1.000, 17,23], "panthers": [1.000, 0.000, 30,3], "buccaneers": [1.000, 0.000, 23,17],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
jaguars_CG = {"patriots" : [], "jets":[0.000, 1.000, 3,32], "dolphins" : [], "bills": [], 
"ravens" : [1.000, 0.000, 12,7] , "steelers": [0.000, 1.000, 13,17], "bengals": [0.000, 1.000, 20,30], "browns": [0.000, 1.000, 10,14], 
"texans": [0.000+0.000, 1.000+1.000, 14+13, 24+20] , "titans": [1.000+0.000, 0.000+1.000, 16+17, 14+23]  , "colts": [1.000+1.000, 0.000+0.000, 17+19, 3+13] , 
"broncos": [], "chargers": [0.000, 1.000, 14,38], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [0.000, 1.000, 10,23], "falcons": [0.000, 1.000, 14,41], "panthers": [0.000, 1.000, 10,16], "buccaneers": [1.000, 0.000, 41,14],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
colts_CG = {"patriots" : [0.000, 1.000, 24,31], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [0.000, 1.000, 10,24] , "steelers": [0.000, 1.000, 20,23], "bengals": [0.000, 1.000, 17,27], "browns": [0.000, 1.000, 19,27], 
"texans": [0.000+1.000, 1.000+0.000, 7+19, 34+16], "titans": [0.000+1.000, 1.000+0.000, 10+27, 27+13] , "jaguars": [0.000+0.000, 1.000+1.000, 3+13, 17+19] ,  
"broncos": [], "chargers": [], "raiders": [], "chiefs": [0.000, 1.000, 24,28],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [], "lions": [], "bears": [], "vikings": [], 
"saints": [0.000, 1.000, 7,62], "falcons": [0.000, 1.000, 7,31], "panthers": [0.000, 1.000, 19,27], "buccaneers": [0.000, 1.000, 17,24],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
broncos_CG = {"patriots" : [0.000, 1.000, 23,41], "jets":[1.000, 0.000, 17,13], "dolphins" : [1.000, 0.000, 18,15 ], "bills": [0.000, 1.000, 14,40], 
"ravens" : [] , "steelers": [], "bengals": [1.000, 0.000, 24,22], "browns": [], 
"texans": [], "titans": [0.000, 1.000, 14,17] , "jaguars": [] , "colts": [] , 
"chargers": [0.000+1.000, 1.000+0.000, 24+16, 29+13] , "raiders": [0.000+1.000, 1.000+0.000, 20+38, 23+24] , "chiefs": [1.000+0.000, 0.000+1.000, 17+3, 10+7] ,
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [0.000, 1.000, 23,49], "lions": [0.000, 1.000, 10,45], "bears": [1.000, 0.000, 13,10 ], "vikings": [1.000, 0.000, 35,32], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
chargers_CG = {"patriots" : [0.000, 1.000, 21,35], "jets":[0.000, 1.000, 21,27], "dolphins" : [1.000, 0.000, 26,16], "bills": [1.000, 0.000, 37,10], 
"ravens" : [1.000, 0.000, 34,14] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [1.000, 0.000, 38,14] , "colts": [] , 
"broncos": [1.000+0.000, 0.000+1.000, 29+13, 24+16], "raiders": [0.000+1.000, 1.000+0.000, 17+38, 24+26], "chiefs": [1.000+0.000, 0.000+1.000, 20+20,17+23] ,
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [0.000, 1.000, 38,45], "lions": [0.000, 1.000, 10,38], "bears": [0.000, 1.000, 20,31], "vikings": [1.000, 0.000, 24,17], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
raiders_CG = {"patriots" : [0.000, 1.000, 19,31], "jets":[1.000, 0.000, 34,24], "dolphins" : [0.000, 1.000, 14,34], "bills": [0.000, 1.000, 35,38], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [1.000, 0.000, 24,17], 
"texans": [1.000, 0.000, 25,20], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [1.000+0.000, 0.000+1.000, 23+24, 20+38] , "chargers": [1.000+0.000, 0.000+1.000, 24+26, 17+38], "chiefs": [0.000+1.000, 1.000+0.000, 0+16, 28+13],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [0.000, 1.000, 16,46], "lions": [0.000, 1.000, 27,28], "bears": [1.000, 0.000, 25,20], "vikings": [1.000, 0.000, 27,21], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
chiefs_CG = {"patriots" : [0.000, 1.000, 3,34], "jets": [0.000, 1.000, 10,37], "dolphins" : [0.000, 1.000, 3,31], "bills": [0.000, 1.000, 7,41], 
"ravens" : [] , "steelers": [0.000, 1.000, 9,13], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [1.000, 0.000, 28,24] , 
"broncos": [0.000+1.000, 1.000+0.000, 10+7, 17+3] , "chargers": [0.000+1.000, 1.000+0.000, 17+23, 20+20] , "raiders": [1.000+0.000, 0.000+1.000, 28+13,0+16], 
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [1.000, 0.000, 19,14], "lions": [0.000, 1.000, 3,48], "bears": [1.000, 0.000, 10,3], "vikings": [1.000, 0.000, 22,17], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
eagles_CG = {"patriots" : [0.000, 1.000, 20,38], "jets":[1.000, 0.000, 45,19], "dolphins" : [1.000, 0.000, 26,10], "bills": [0.000, 1.000, 24,31], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"giants" : [0.000+1.000, 1.000+0.000, 16+17, 29+10] , "cowboys" : [1.000+1.000, 0.000+0.000, 34+20, 7+7] , "redskins" : [1.000+1.000, 0.000+0.000, 20+34, 13+10] , 
"packers": [], "lions": [], "bears": [0.000, 1.000, 24,30], "vikings": [], 
"saints": [], "falcons": [0.000, 1.000, 31,35], "panthers": [], "buccaneers": [],
"49ers": [0.000, 1.000, 23,24], "cardinals": [0.000, 1.000, 17,21], "seahawks": [0.000, 1.000, 14,31], "rams": [1.000, 0.000, 31,13], 
 }
 
giants_CG = {"patriots" : [1.000, 0.000, 24,20], "jets":[1.000, 0.000, 29,14], "dolphins" : [1.000, 0.000, 20,17], "bills": [1.000, 0.000, 27,24], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [1.000+0.000, 0.000+1.000, 29+10, 16+17], "cowboys" : [1.000+1.000, 0.000+0.000, 37+31, 34+14], "redskins" : [0.000+0.000, 1.000+1.000, 14+10, 28+23] , 
"packers": [0.000, 1.000, 35,38], "lions": [], "bears": [], "vikings": [], 
"saints": [0.000, 1.000, 24,49], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [0.000, 1.000, 20,27], "cardinals": [1.000, 0.000, 31,27], "seahawks": [0.000, 1.000, 25,36], "rams": [1.000, 0.000, 28,16], 
 }
 
cowboys_CG = {"patriots" : [0.000, 1.000, 16,20], "jets":[0.000, 1.000, 24,27], "dolphins" : [1.000, 0.000, 20,19], "bills": [1.000, 0.000, 44,7], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [0.000+0.000, 1.000+1.000, 7+7,34+20]  , "giants" : [0.000+0.000, 1.000+1.000, 34+ 14,37+31], "redskins" : [1.000+1.000, 0.000+0.000, 18+27, 16+24] , 
"packers": [], "lions": [0.000, 1.000, 30,34], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [1.000, 0.000, 31,15],
"49ers": [1.000, 0.000, 27,24 ], "cardinals": [0.000, 1.000, 13,19], "seahawks": [1.000, 0.000, 23,13], "rams": [1.000, 0.000, 34,7], 
 }
 
redskins_CG = {"patriots" : [0.000, 1.000, 27,34], "jets":[0.000, 1.000, 19,34], "dolphins" : [0.000, 1.000, 9,20], "bills": [0.000, 1.000, 0,23], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [0.000+0.000, 1.000+1.000, 13+10, 20+34], "giants" : [1.000+1.000, 0.000+0.000, 28+23, 14+10] , "cowboys" : [0.000+0.000, 1.000+1.000, 16+24, 18+27] ,
"packers": [], "lions": [], "bears": [], "vikings": [0.000, 1.000, 26,33], 
"saints": [], "falcons": [], "panthers": [0.000, 1.000, 20,33], "buccaneers": [],
"49ers": [0.000, 1.000, 11,19], "cardinals": [1.000, 0.000, 22,21], "seahawks": [1.000, 0.000, 23,17], "rams": [1.000, 0.000, 17,10], 
 }
 
packers_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [1.000, 0.000, 49,23], "chargers": [1.000, 0.000, 45,38], "raiders": [], "chiefs": [0.000, 1.000, 14,19],
"eagles" : [], "giants" : [1.000, 0.000, 38,35], "cowboys" : [], "redskins" : [], 
"lions": [1.000+1.000, 0.000+0.000, 27+45, 15+41]  , "bears": [1.000+1.000, 0.000+0.000, 27+35, 17+21] , "vikings": [1.000+1.000, 0.000+0.000, 33+45, 27+7], 
"saints": [1.000, 0.000, 42,34], "falcons": [1.000, 0.000, 25,14], "panthers": [1.000, 0.000, 30,23], "buccaneers": [1.000, 0.000, 35,26],
"49ers": [], "cardinals": [], "seahawks": [], "rams": [1.000, 0.000, 24,3], 
 }
 
lions_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [1.000, 0.000, 45,10], "chargers": [1.000, 0.000, 38,10], "raiders": [1.000, 0.000, 28,27], "chiefs": [1.000, 0.000, 48,3],
"eagles" : [], "giants" : [], "cowboys" : [1.000, 0.000, 34,30], "redskins" : [], 
"packers": [0.000+0.000, 1.000+1.000, 15+41, 27+45], "bears": [1.000+0.000, 0.000+1.000, 24+13, 13+37], "vikings": [1.000+1.000, 0.000+0.000, 26+34, 23+28] , 
"saints": [0.000, 1.000, 17,31], "falcons": [0.000, 1.000, 16,23], "panthers": [1.000, 0.000, 49, 35] , "buccaneers": [1.000, 0.000, 27,20],
"49ers": [0.000, 1.000, 19,25], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
bears_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [0.000, 1.000, 10,13 ], "chargers": [1.000, 0.000, 31,20], "raiders": [0.000, 1.000, 20,25], "chiefs": [0.000, 1.000, 3,10],
"eagles" : [1.000, 0.000, 30,24], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [0.000+0.000, 1.000+1.000, 17+21, 27+35], "lions": [0.000+1.000, 1.000+0.000, 13+37, 24+13] , "vikings": [1.000+1.000, 0.000+0.000, 39+17, 10+13] , 
"saints": [0.000, 1.000, 13,30], "falcons": [1.000, 0.000, 30,12], "panthers": [1.000, 0.000, 34,29], "buccaneers": [],
"49ers": [], "cardinals": [], "seahawks": [0.000, 1.000, 14,38], "rams": [], 
 }
 
vikings_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [0.000, 1.000, 32,35], "chargers": [0.000, 1.000, 17,24], "raiders": [0.000, 1.000, 21,27], "chiefs": [0.000, 1.000, 17,22],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [0.000+0.000,  1.000+1.000, 27+7, 33+45] , "lions": [0.000+0.000, 1.000+1.000,  23+28, 26+34 ] , "bears": [0.000+0.000, 1.000+1.000, 10+13, 39+17] ,
"saints": [0.000+1.000, 1.000+0.000, 20+33, 42+26] , "falcons": [0.000, 1.000, 14,24], "panthers": [1.000, 0.000, 24,21], "buccaneers": [0.000, 1.000, 20,24],
"49ers": [], "cardinals": [1.000, 0.000, 34,10], "seahawks": [], "rams": [], 
 }
 
saints_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [1.000, 0.000, 40,33], "titans": [1.000, 0.000, 22,17] , "jaguars": [1.000, 0.000, 23,10] , "colts": [1.000, 0.000, 62,7] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [1.000, 0.000, 49,24], "cowboys" : [], "redskins" : [], 
"packers": [0.000, 1.000, 34,42], "lions": [1.000, 0.000, 31,17], "bears": [1.000, 0.000, 30,13], "vikings": [1.000, 0.000, 42,20], 
"falcons": [1.000+1.000, 0.000+0.000, 26+45, 23+16 ]  , "panthers": [1.000+1.000, 0.000+0.000, 30+45, 27+17], "buccaneers": [0.000+1.000, 1.000+0.000, 20+27, 26+16]  ,
"49ers": [], "cardinals": [], "seahawks": [], "rams": [0.000, 1.000, 21,31], 
 }
 
falcons_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [0.000, 1.000, 10,17], "titans": [1.000, 0.000, 23,17] , "jaguars": [1.000, 0.000, 41,14] , "colts": [1.000, 0.000, 31,7] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [1.000, 0.000, 35,31], "giants" : [], "cowboys" : [], "redskins" : [], 
"packers": [0.000, 1.000, 14,25], "lions": [1.000, 0.000, 23,16], "bears": [0.000, 1.000, 12,30], "vikings": [1.000, 0.000, 24,14], 
"saints": [0.000+0.000, 1.000+1.000, 23+16, 26+45], "panthers": [1.000+1.000, 0.000+0.000, 31+31, 17+23] , "buccaneers": [0.000+1.000, 1.000+0.000, 13+45, 16+24] ,
"49ers": [], "cardinals": [], "seahawks": [1.000, 0.000, 30,28], "rams": [], 
 }
 
panthers_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [1.000, 0.000, 28,13], "titans": [0.000, 1.000, 3,30] , "jaguars": [1.000, 0.000, 16,10] , "colts": [1.000, 0.000, 27,19] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [], "redskins" : [1.000, 0.000, 33,20], 
"packers": [0.000, 1.000, 23,30], "lions": [0.000, 1.000, 35,49], "bears": [], "vikings": [0.000, 1.000, 21,24], 
"saints": [0.000+0.000, 1.000+1.000, 27+17, 30+45], "falcons": [0.000+0.000, 1.000+1.000, 17+23, 31+31] , "buccaneers": [1.000+1.000, 0.000+0.000, 38+48, 19+16],
"49ers": [], "cardinals": [0.000, 1.000, 21,28], "seahawks": [], "rams": [], 
 }
 
buccaneers_CG  = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [] , "steelers": [], "bengals": [], "browns": [], 
"texans": [0.000, 1.000, 9,37], "titans": [0.000, 1.000, 17,23] , "jaguars": [0.000, 1.000, 14,41] , "colts": [1.000, 0.000, 24,17] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [], "giants" : [], "cowboys" : [0.000, 1.000, 15,31], "redskins" : [], 
"packers": [0.000, 1.000, 26,35], "lions": [0.000, 1.000, 20,27], "bears": [0.000, 1.000, 18,24], "vikings": [1.000, 0.000, 24,20], 
"saints": [1.000+0.000, 0.000+ 1.000,  26+16, 20+27], "falcons": [1.000+0.000, 0.000+1.000, 16+24, 13+45] , "panthers": [0.000+0.000, 1.000+1.000, 19+16, 38+48]  ,
"49ers": [0.000, 1.000, 3,48], "cardinals": [], "seahawks": [], "rams": [], 
 }
 
forty9ers_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [0.000, 1.000, 6,16] , "steelers": [1.000, 0.000, 20,3], "bengals": [1.000, 0.000, 13,8], "browns": [1.000, 0.000, 20,10], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [1.000, 0.000, 24,23], "giants" : [1.000, 0.000, 27,20], "cowboys" : [0.000, 1.000, 24,27], "redskins" : [1.000, 0.000, 19,11], 
"packers": [], "lions": [1.000, 0.000, 25,19], "bears": [], "vikings": [], 
"saints": [], "falcons": [], "panthers": [], "buccaneers": [1.000, 0.000, 48,3],
"cardinals": [1.000+0.000, 0.000+1.000, 23+19, 7+21] , "seahawks": [1.000+1.000, 0.000+0.000, 33+19, 17+17] , "rams": [1.000+1.000, 0.000+0.000, 26+34,0+27] , 
 }
 
cardinals_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [0.000, 1.000, 27,30] , "steelers": [0.000, 1.000, 20,32], "bengals": [0.000, 1.000, 16,23], "browns": [1.000, 0.000, 20,17 ], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [1.000, 0.000, 21,17], "giants" : [0.000, 1.000, 27,31], "cowboys" : [1.000, 0.000, 19,13], "redskins" : [0.000, 1.000, 21,22], 
"packers": [], "lions": [], "bears": [], "vikings": [0.000, 1.000, 10,34], 
"saints": [], "falcons": [], "panthers": [1.000, 0.000, 28,21], "buccaneers": [],
"49ers": [0.000+1.000, 1.000+0.000, 7+21, 23+19], "seahawks": [0.000+1.000, 1.000+0.000, 10+23, 13+20], "rams": [1.000+1.000, 0.000+0.000, 19+23, 13+20] , 
 }
 
seahawks_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [1.000, 0.000, 22,17] , "steelers": [0.000, 1.000, 0,24], "bengals": [0.000, 1.000, 12,34], "browns": [0.000, 1.000, 3,6], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [1.000, 0.000, 31,14], "giants" : [1.000, 0.000, 36,25], "cowboys" : [0.000, 1.000, 13,23], "redskins" : [0.000, 1.000, 17,23], 
"packers": [], "lions": [], "bears": [1.000, 0.000, 38,14], "vikings": [], 
"saints": [], "falcons": [0.000, 1.000, 28,30], "panthers": [], "buccaneers": [],
"49ers": [0.000+0.000, 1.000+1.000, 17+17, 33+19] , "cardinals": [1.000+0.000, 0.000+1.000, 13+20, 10+23]   , "rams": [1.000+1.000, 0.000+0.000, 24+30, 7+13], 
 }
 
rams_CG = {"patriots" : [], "jets":[], "dolphins" : [], "bills": [], 
"ravens" : [0.000, 1.000, 7,37] , "steelers": [0.000, 1.000, 0,27], "bengals": [0.000, 1.000, 13,20], "browns": [1.000, 0.000, 13,12], 
"texans": [], "titans": [] , "jaguars": [] , "colts": [] , 
"broncos": [], "chargers": [], "raiders": [], "chiefs": [],
"eagles" : [0.000, 1.000, 13,31], "giants" : [0.000, 1.000, 16,28], "cowboys" : [0.000, 1.000, 7,34], "redskins" : [0.000, 1.000, 10,17], 
"packers": [0.000, 1.000, 3,24], "lions": [], "bears": [], "vikings": [], 
"saints": [1.000, 0.000, 31,21], "falcons": [], "panthers": [], "buccaneers": [],
"49ers": [0.000+0.000, 1.000+1.000, 0+27, 26+34], "cardinals": [0.000+0.000, 1.000+1.000, 13+20, 19+23], "seahawks": [0.000+0.000, 1.000+1.000, 7+13, 24+30],
 }
 


#AFCWEST DIVISION LEADER
#afcwest_champ = max(afcwest_wins.values())
afcwestsort = sorted(afcwest_wins.items(), reverse=True, key=itemgetter(1))
afcwestleaderrec = afcwestsort[0][1]

#AFCWEST OVERALL WINS TIES
overallwin_ties = [owt for owt in afcwest_wins if afcwest_wins[owt] == afcwestleaderrec]
owtteam1 = overallwin_ties[0]
owtteam2 = overallwin_ties[1]
owtteam3 = overallwin_ties[2]

#AFCWEST DIVISION WINS TIES
afcwestdivwinssort = sorted(afcwest_div_wins.items(), reverse=True, key=itemgetter(1))
afcwestleaderdivrec = afcwestdivwinssort[0][1]
divwin_ties = [dwt for dwt in afcwest_div_wins if afcwest_div_wins[dwt] == afcwestleaderdivrec]
divwinties = [val for val in divwin_ties if val in overallwin_ties]
divteam1 = divwinties[0]
divteam2 = divwinties[1]
divteam3 = divwinties[2]


#AFCWEST COMMON GAMES TIE BREAKER
all_games = {
    divteam1: eval(divteam1 + "_CG"),
	divteam2: eval(divteam2 + "_CG"),
	divteam3: eval(divteam3 + "_CG"),
}

wins = {}
for team, games in all_games.items():
    wins[team] = 0
    for opponent, results in games.items():
        common = True
        #Check if it is genuinely a common opponent
        # As we are never opponents with ourselves, the tied winners are never counted
        for other_team in divwinties:
            if not all_games[other_team].get(opponent):
                common = False
                break
        if common:
            wins[team] += results[0]
			

afcwestcgsort = sorted(wins.items(), reverse=True, key=itemgetter(1))
afcwestcgleader = afcwestcgsort[0]


for afcwest_champ in afcwest_champ:
	afcwest_champ = afcwestsort[0]
	if overallwin_ties:
		afcwest_champ = afcwestleaderdivrec
	if divwin_ties:
		afcwest_champ = afcwestcgleader

print afcwest_champ

"""
#EXPLANATION 
#The _______ are ranked number 2 in their division because _______________________________________. If the ___________ win on ________ they will be 1st.
#nfl_win = 
#wildcards = nflwin1 + nflwin2 if team not nfceast1, nfcwest1, etc.

http://www.nfl.com/standings/tiebreakingprocedures
http://video.about.com/football/How-are-the-NFL-Playoffs-Organized-.htm


class csv.DictReader(csvfile[, fieldnames=None[, restkey=None[, restval=None[, dialect='excel'[, *args, **kwds]]]]])
"""
