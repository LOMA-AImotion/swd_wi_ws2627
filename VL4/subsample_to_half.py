werte = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
# nehme jeden zweiten Wert und das nur bis zur Hälfte
# z.B. 3.2, 2.8, 6.4
downsampling = werte[:len(werte)//2 + 1:2]
print(downsampling)