class StringUtility():
  def __init__(self, string = ''):
    self.word = string
  
  def __str__(self):
    return self.word
 
  def vowels(self):
    '''
    Counting number of vowels in isntance of string
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for i in range(len(self.word)):
      if self.word[i] in vowels:
        num_vowels += 1
    if num_vowels >= 5:
      num_vowels = 'many'
    return str(num_vowels)
  
  def bothEnds(self):

    if len(self.word) > 1:
      new_word = self.word[0] + self.word[1] + self.word[-2] + self.word[-1]
      if len(new_word) <= 2:
        return ''
      else:
        return str(new_word)
    else:
      return str(self.word)
  
  def fixStart(self):
    
    if len(self.word) > 1:
      start_letter = self.word[0]
      new_string = start_letter
      for i in range(1, len(self.word)):
        if self.word[i] == start_letter:
          new_string += '*'
        else:
          letter= self.word[i]
          new_string += letter
      return str(new_string)
    else:
      return str(self.word)
  
  def asciiSum(self):
    '''
    adds the ASCII value 
    '''
    num = 0
    for i in range(len(self.word)):
      num += ord(self.word[i])
    return num
  
  def cipher(self):
    '''
    shifts the characters of a string by the length of the string
    '''
    new_cipher = ''
    length = (len(self.word) % 26)
    for i in range(len(self.word)):
      
      
      if ord(self.word[i]) == 32:#ASCII num for blank space
        new_cipher += (' ')
      
      
      
      
      elif ord(self.word[i]) <= 90:#where capital letters end
        letter = ord(self.word[i])
        letter += length
        if letter > 90:
          letter -= 26
        new_cipher += chr(letter)
      
      
      
      else:
        print(ord(self.word[i]))
        letter = ord(self.word[i])
        letter += length
        if letter > 122:
          letter -= 26
        converted = chr(letter)
        print(converted)
        new_cipher += converted
        print(new_cipher)
        
      
    return str(new_cipher)