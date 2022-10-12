def star_pyramid(): 
  rows = int(input("Enter a number of rows: ")) 
  for i in range(rows): 
    for j in range(i+1):
      print("* ", end="")
    print("\n")
star_pyramid()
