# ch20_43.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock
import lxml

#mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體

stock2330 = twstock.Stock("2330")
print(stock2330.price)
# plt.title(u"台積電", fontsize=24)
# plt.plot(stock2330.price)
# plt.show()
