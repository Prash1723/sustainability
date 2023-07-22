# Linux terminal dashboard for calculating the carbon footprint for individuals

**Aim** : To calculate the carbon footprint for an individual's monthly activities. The methodology is based on the formula in "The Environment Equation", the link to the resource is given below

Steps in the calculations :
1. Electric bill * 105
2. Gas bill * 105
3. Oil usage * 113
4. Total fuel consumption * 0.79
5. Flight hours (4 hours or less) * 1100
6. Flight hours (4 hours or more) * 4400
7. Add 184 if you dont recycle newspaper
8. Add 166 if you dont recycle aluminium and tin
9. Add 1-8 together for total carbon footprint

Note : All the metrics are in pounds

**Author** : Praveen Shekar

**Tool** : Python 3.9.12

**Resource** : https://justenergy.com/blog/how-to-calculate-your-carbon-footprint/

**Output** : Report.txt

**Modules used** : Rich
