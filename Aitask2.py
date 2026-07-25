Q.1 In a college:
20% of students know Python.
80% of students know Java.
90% of Python students get placed.
40% of Java students get placed.
A randomly selected student is placed.
Find:
Probability that the student knows Python.
Probability that the student knows Java.
Probability that a placed student knows Python.
CODE:
# Probabilities
P_Python = 0.20
P_Java = 0.80
P_Placed_Python = 0.90
P_Placed_Java = 0.40
# Total probability of being placed
P_Placed = (P_Placed_Python * P_Python) + (P_Placed_Java * P_Java)
# Bayes Rule
P_Python_Placed = (P_Placed_Python * P_Python) / P_Placed
P_Java_Placed = (P_Placed_Java * P_Java) / P_Placed
print("Probability student knows Python:", P_Python)
print("Probability student knows Java:", P_Java)
print("Probability placed student knows Python:", round(P_Python_Placed, 4))
print("Probability placed student knows Java:", round(P_Java_Placed, 4))
print("Soham Acharekar T001")

Q.2 In a city:
85% of taxis are Green.
15% are Blue.
A witness correctly identifies the taxi color 80% of the time.
A witness claims the taxi involved in an accident was Blue. What is the probability that the taxi was actually Blue?
CODE:
# Probabilities
P_Blue = 0.15
P_Green = 0.85
P_Correct = 0.80
P_Wrong = 0.20
# Probability witness says Blue
P_Witness_Blue = (P_Correct * P_Blue) + (P_Wrong * P_Green)
# Bayes Rule
P_Blue_WitnessBlue = (P_Correct * P_Blue) / P_Witness_Blue
print("Probability taxi was actually Blue:", round(P_Blue_WitnessBlue, 4))
print("Soham Acharekar T001")
