instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan',
               'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']


def find_index(arr, name):
    output = []
    recursiveSearch(0, arr, name, output)
    return output

def recursiveSearch(index, arr, name, output):
  if index >= len(arr):
    return

  elif arr[index] == name and len(output) == 0:
    output.append(index)

  elif arr[index] != name and len(output) == 1:
    output.append(index - 1)

  index += 1
  recursiveSearch(index, arr, name, output)

print(find_index(instructors, 'Braus'))
# ----------------------------------------------------------------

digits = {"2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "qprs",
          "8": "tuv",
          "9": "wxyz", }

# def keypadConversion(input, output, outputString = "", index = 0):
#   if index == len(input):
#     output.append(outputString)
#     return output

def keypad(index, input, result = []):
  if len(input) == len(digits):
    result.append(input)
    return

  for char in digits[input[index]]:
    print(char)
    input(index + 1, input + char)


keypad(0, "34")
