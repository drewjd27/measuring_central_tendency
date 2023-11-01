import numpy as np
from scipy import stats

jlh_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# CARI MEAN
mean = jlh_kucing.mean()
# CARI MEDIAN
median = np.median(jlh_kucing)
# CARI MODUS
modus = stats.mode(jlh_kucing)[0]

# CETAK NILAI
print("mean: " + str(mean))
print("median: " + str(median))
print("modus: " + str(modus))