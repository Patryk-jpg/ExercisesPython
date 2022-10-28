

import operator
operators={
    "+": operator.add,
    "-": operator.sub,
}
def arithmetic_arranger(problems, ShowAnswers = False):
  temp = []
  firstrow = ''
  secondrow = ''
  thirdrow = ''
  scorerow = ''
  for problem in problems:
    problem = problem.split()    
    temp.append(problem)
  for i in temp:
    if len(i[0]) > len(i[2]): 
      firstrow += ' '*2 +i[0] 
      secondrow += i[1]+  ' '*(1+len(i[0]) - len(i[2])) + i[2] 
      thirdrow += '-'*(len(i[0])+2)
    else:  
      firstrow +=' '*(2+(len(i[2])-len(i[0])))  + i[0] 
      secondrow += i[1]+  ' ' + i[2]
      thirdrow += '-'*(len(i[2])+2)
    firstrow += ' '*4
    secondrow += ' '*4
    thirdrow += ' '*4
    if ShowAnswers == True:
      score = str(operators[i[1]](int(i[0]),int(i[2])))
      scorelen = len(score)
      if len(i[0]) > len(i[2]):
        scorerow += ' '*(2+(len(i[0])-scorelen)) + score
      else: scorerow += ' '*(2+(len(i[2])-scorelen)) + score
    scorerow += ' '*4
  if ShowAnswers == True:
        arranged_problems = firstrow+'\n'+secondrow +'\n'+thirdrow + '\n' + scorerow 
  else: arranged_problems =  firstrow+'\n'+secondrow +'\n'+thirdrow 
  arranged_problems = arranged_problems.rstrip()
  print(arranged_problems)
  return arranged_problems
