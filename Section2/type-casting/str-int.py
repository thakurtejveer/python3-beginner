# string - integer
score_eng = "90"
score_math = "95"
score_chem = "85"

# convert strings to integers 

# int :: built in fucntions
score_eng = int(score_eng)
score_math = int(score_math)
score_chem = int(score_chem)

average_score = (score_chem+score_eng+score_math)/3

print(average_score)