# -*- coding: utf-8 -*-
import re, locale

purchases = [float(i.replace(',', '.')) for i in re.findall(u'(?:Grand Total:|Gesamt)\s*([0-9]{1,},[0-9]{2,2}).*?EUR', open("emails.txt").read())]
total_sum = sum(purchases)
count = len(purchases)

print ('You\'ve spent a total of ' + str(total_sum) + ' EUR on ' + str(count) + ' purchases from Blizzard.')
