#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:21:45 2020

@author: huangsunchuangyu
"""

import APA7 as apa

a = apa.webpages()
a.Author(['Nick'])
a.Date('2015, July 11')
a.Url('www.google.com')
a.Title('google')
a.ref()

test = apa.webpages()
test.name = 'Victorian Current Acts'
test.Date('2010')
test.Url('http://www8.austlii.edu.au/cgi-bin/viewdoc/au/legis/vic/consol_act/eoa2010250/s71.html')
test.Title('EQUAL OPPORTUNITY ACT 2010 - SECT 71 Discrimination in sport')
test.ref()
apa.dump(test, 'test.html')

ref_4 = apa.newspaper('','Cargo vessel lost 40 containers off NSW','2020', 'May', '26', 'Herald Sun', 'p. 3.')
ref_4.ref()
ref_4.Title('Cargo vessel lost 40 containers off NSW')
apa.dump(ref_4, 'test.html') 
ref_5 = apa.newspaper('','Cargo vessel lost 40 containers off NSW','2020', 'May', '26', 'Herald Sun', 'https://www.heraldsun.com.au/business/breaking-news/shanghai-copper-slips-for-second-day/news-story/ff7855ae8cc61b37e45eed6620be05fe')
ref_5.Author(['Archibald-Binge E'])
ref_5.Public('New York Times')
ref_5.Source('https://www.nytimes.com/2020/05/25/opinion/online-college-coronavirus.html?')
ref_5.Title("The future of college in online, and it's cheaper")
ref_5.ref()        
apa.dump(ref_5, 'test.html')

apa.info()

ref_5 = doi('Noble C', '2019', 'A bibliography of polar medicine related articles', 'Australian Antarctic Data Centre', 'https://data.aad.gov.au/metadata/records/medical_bibliography')
ref_5.Author(['Ayton J', 'Watzl R', 'Rin Sunchuangyu Huang', 'Noble C'])           
         
ref_5.ref()
dump(ref_5, 'test.html')

ref_6 = tables(publisher = 'Melbourne Institute')
ref_6.Copyright('Melbourne Institute')

ref_6.Year_copyright('2019')
ref_6.Source('https://melbourneinstitute.unimelb.edu.au/__data/assets/pdf_file/0004/3125470/STATE_MBET_July2019.pdf')
ref_6.Title('Monthly bulletin of economic trends: Economic activity in the major states')
ref_6.ref()
ref_6.info()
dump(ref_6, 'test.html')