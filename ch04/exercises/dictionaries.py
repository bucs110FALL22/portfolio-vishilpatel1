article = 'Power outages plagued Tampa Bay area communities Wednesday as Hurricane Ian rolled through southwest Florida and headed toward Central Florida. As of 7 p.m., there were more than 370,000 outages reported in areas that include Hillsborough, Pasco and Pinellas counties. Outage numbers steadily increased all day.'
substitutions = {
  'outages':'crashes',
  'outage':'crash',
  'reported':'revealed',
  'power':'strength'
}
for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)