def christmas_tree(height):
    s = ""
    h = height//3
    start = 1
    original_space = h+1
    for i in range(h):
        added_stars = i*2+1
        for j in range(3):
            s+=' '*(original_space-j - i) + "*"*added_stars + '\r\n' 
            added_stars+=2
    if s != "":
        s+=' '*(original_space-1) + "###"
    return s
christmas_tree(17)

"""
Here your task is to Create a (nice) Christmas Tree.

You don't have to check errors or incorrect input values, every thing is ok without bad tricks, only one int parameter as input and a string to return;-)...

So what to do?

First three easy examples: 

Input: 3 and Output:
  *
 ***
*****
 ###
 
 Input 9 and Output:
    *
   ***
  *****
   ***
  *****
 *******
  *****
 *******
*********
   ###
   
 Input 17 and Output:
      *
     ***
    *****
     ***
    *****
   *******
    *****
   *******
  *********
   *******
  *********
 ***********
  *********
 ***********
*************
     ###
     
Really nice trees, or what???! So merry Christmas;-)

You can see, always a root, always steps of hight 3, tree never smaller than 3 (return "") and no difference for input values like 15 or 17 (because (int) 15/3 = (int) 17/3). That's valid for every input and every tree. Lines are delimited by \r\n and no trailing white space allowed. I think there's nothing more to say - perhaps look at the testcases too;-)!

There are some static tests at the beginning and many random tests if you submit your solution.

"""