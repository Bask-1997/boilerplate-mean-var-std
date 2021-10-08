import numpy as np

def calculate(list):
  number = np.array([list[0:3],list[3:6],list[6:]])

  #'mean: '
  mean1 = [number[:,0].mean(),number[:,1].mean(),number[:,2].mean()]
  mean2 = [number[0,:].mean(),number[2,:].mean(),number[2,:].mean()]
  meanall = number.mean()
  meanlist = [mean1,mean2, meanall]

  #'variance : '
  var1 = [number[:,0].var(), number[:,1].var(), number[:,2].var()]
  var2 = [number[0,:].var(), number[2,:].var(), number[2,:].var()]
  varall = number.var()
  varlist = [var1,var2, varall]

  #'standard deviation : '
  std1 = [number[:,0].std(), number[:,1].std(), number[:,2].std()]
  std2 = [number[0,:].std(), number[2,:].std(), number[2,:].std()]
  stdall = number.std()
  stdlist = [std1,std2, stdall]

  #max
  max1 = [number[:,0].max(), number[:,1].max(), number[:,2].max()]
  max2 = [number[0,:].max(), number[2,:].max(), number[2,:].max()]
  maxall = number.max()
  maxlist = [max1,max2, maxall]

  #min
  min1 = [number[:,0].min(), number[:,1].min(), number[:,2].min()]
  min2 = [number[0,:].min(), number[2,:].min(), number[2,:].min()]
  minall = number.min()
  minlist = [min1,min2, minall]

  #sum
  sum1 = [number[:,0].sum(), number[:,1].sum(), number[:,2].sum()]
  sum2 = [number[0,:].sum(), number[2,:].sum(), number[2,:].sum()]
  sumall = number.sum()
  sumlist = [sum1, sum2, sumall]

  
  
  calculations = {'mean' : meanlist,
  'variance' : varlist,
  'standard deviation' : stdlist,
  'max' : maxlist,
  'min' : minlist,
  'sum' : sumlist}
  return calculations
