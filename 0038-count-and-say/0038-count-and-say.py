class Solution:
  def __init__(self):
    pass

  #THIS IS LEETCODE
  def  countAndSay(self,n:'int')->'string':
    ## NOTHING CAN BE CHANGED HERE
    return self._alg_integer(n)

  def  countAndSayString(self,n:'string')->'string':
    #Nothing can be changed here
    return self._alg_string(n) 

  ### YOU CAN HAVE ANY NUMBER OF FUNCTIONS AND CLASSES BELOW


  ## n is str here
  def _alg_string(self,n:'string')->'string':
    # print("WRITE CODE  BELOW")
    '''
    Checking if previous number is same as the current number and incrementing count accordingly.
    '''
    previous_character = ""
    count = 0
    result = ""
    for current_character in n:      
      if previous_character == current_character:                 
        count+= 1
      else: 
        if previous_character != "":
          result += str(count) 
          result += str(previous_character)
        previous_character = current_character
        count = 1
    return result + str(count)+str(previous_character)
    

  ## n is int here
  def _alg_integer(self,n:'int')->'string':
    # print("WRITE CODE  BELOW")
    '''
    The code below iterates upto n-1 appending ouput values for each iteration in the result list.
    '''
    result = ['1']
    for i in range(n-1):
        i = 0
        last_output = result[-1]
        curr_str = ''
        j = 0
        while i<len(last_output):
            count = 0
            while j<len(last_output) and last_output[i] == last_output[j]:
                count+=1
                j+=1
            curr_str += str(count)
            curr_str += str(last_output[i])
            i = j
        # print(curr_str)
        result.append(curr_str)
    
    return result[-1]