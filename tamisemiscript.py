#! /usr/bin/python3
print('welcome to my data cleaning script prepared by Johanes Petro during Tamisemi Data cleaning')
import difflib
gn ='/home/johanes/Desktop/TAMISEMI/GNconcate.txt'
shapefile = '/home/johanes/Desktop/TAMISEMI/shapefile.txt'
ogn=open(gn).readlines()
oshapefile = open(shapefile).readlines()
comparison = difflib.HtmlDiff().make_file(oshapefile,ogn, shapefile,gn)
report= open('/home/johanes/Desktop/TAMISEMI/report2.html', 'w')
report.write(comparison)
report.close()