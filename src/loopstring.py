str = "we are four in this room"
y = ""
for x in str:
	y += x.upper()

print(y)

str2 = """PTI leader Fawad Chaudhry had told media on Wednesday that the ruling coalition would go for a vote of confidence before Jan 11, the day when an LHC bench resumes hearing into a petition by Parvez Elahi challenging the governor's move"""

print(str2.find("Parvez"))

for x in range(7):
  print(str2[190: 190 + x])
