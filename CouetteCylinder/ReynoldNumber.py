import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np

waterKVis = 0.000001
oilKVis = 0.00005
aveL = 0.03
waterReyNums = []
minOilReyNums = []
velWaterList = []
velOilList = []
velWater = 0
velMinOil = 0
reyNum = 0
reyNumOil = 0

while reyNum < 10000:
    reyNum = (velWater * aveL) / waterKVis
    waterReyNums.append(reyNum)
    velWaterList.append(velWater)
    velWater = velWater + .01

while reyNumOil < 10000:
    reyNumOil = (velMinOil * aveL) / oilKVis
    minOilReyNums.append(reyNumOil)
    velOilList.append(velMinOil)
    velMinOil = velMinOil + 1


plt.subplot(121)
plt.scatter(velWaterList, waterReyNums)
plt.plot(velWaterList, waterReyNums)
plt.title("Water")
plt.ylabel("Reynold's Number")
plt.xlabel("Velocity")
plt.subplot(122)
plt.scatter(velOilList, minOilReyNums)
plt.plot(velOilList, minOilReyNums)
plt.title("Mineral Oil")

table = [["Water: Re", "Velocity", "Mineral Oil: Re", "Velocity"],
         [waterReyNums], [velWaterList], [minOilReyNums], [velOilList]]

print(waterReyNums)
print(velWaterList)
print(minOilReyNums)
print(velOilList)
plt.show()

# model = np.poly1d(np.polyfit(velList, waterReyNums, 1))
# line = np.linspace(1, len(velList), 100)
# plt.plot(line, model(line))

'''def calcReyNumDV(self, fluidDensity, flowVelocity, linearDimension, dynamicViscosity):
    reynoldNumber = (fluidDensity * flowVelocity * linearDimension) / dynamicViscosity
    return reynoldNumber

def calcReyNumKV(flowVelocity, linearDimension, kinematicViscosity):
    reynoldNumber = (flowVelocity * linearDimension) / kinematicViscosity
    return reynoldNumber'''








