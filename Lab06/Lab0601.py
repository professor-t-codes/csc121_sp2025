##
# Richard Tillies
# December 20, 2024
# Nested lists: students and assignment scores
#
# students = ['Ashley', 'Barb', 'Carl']
# a_list = [90, 83, 95]
# b_list = [100, 78, 89, 87, 90]
# c_list = [57, 82, 85, 89]
a_list = []
b_list = []
c_list = []

# Get scores for Ashley
print("Please enter Ashley's scores one by one.")
for a in range(3):
    a_list.append(int(input("Enter a score: ")))

print("Ashley's scores:", a_list, end='\n\n')

# Get scores for Barb
print("Please enter Barb's scores one by one.")
for b in range(5):
    b_list.append(int(input("Enter a score: ")))

print("Barb's scores:", b_list, end='\n\n')

# Get scores for Carl
print("Please enter Carl's scores one by one.")
for c in range(4):
    c_list.append(int(input("Enter a score: ")))
print("Carl's scores:", c_list, end='\n\n')

# Create copy of individual list as a nested list
all_scores = [a_list[:], b_list[:], c_list[:]]
print("All scores:", all_scores)

# Add 5% extra credit to each score
for i in range(len(all_scores)):
    for j in range(len(all_scores[i])):
        all_scores[i][j] = int(all_scores[i][j] * 1.05)

print("All scores after extra credit:", all_scores)

# Score spreads
score_spreads = []
for i in all_scores:
    score_spreads.append(max(i) - min(i))

print("Score spreads:", score_spreads)

# Print original scores
print()
print("Original Scores")
print("Ashley's scores:", a_list)
print("Barb's scores:", b_list)
print("Carl's scores:", c_list)