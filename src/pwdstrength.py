def Has_Upper(pwd):
    has_upper = False
    for char in pwd:
      if char.isupper():
         has_upper=True
         break
      else:
         continue
    return has_upper

passwords = ["beyond2013", "Beyond2013", "beyoNd2013"]

for pwd in passwords:
    print(pwd, Has_Upper(pwd))
