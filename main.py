import matplotlib.pyplot as plt
import requests
from Data import basic, University, Country

response = requests.get('https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3816281.txt?ru4kh1')
# Create Hashmap Countries and avg score
Countries = {}

data = response.json()
for i in data['data']:
    tempCountry = i['country']
    tempUniversity = University(i['title'], tempCountry)

    try:
        tempUniversity.ranking = float(i['score'])
        if tempUniversity.ranking == 0:
            continue
        else:
            if tempCountry in Countries:
                Countries[tempCountry][0].addUniversity(tempUniversity)
                Countries[tempCountry][1] = Countries[tempCountry][0].avg
            else:
                tmp = Country(tempCountry)
                tmp.addUniversity(tempUniversity)
                Countries[tempCountry] = [tmp, tmp.avg]

    except:
        continue

# Sort the Countries dictionary based on values[0]
sorted_countries = sorted(Countries.items(), key=lambda x: x[1][0].avg)
Countries = dict(sorted_countries)

x = Countries.keys()
y = [country[1] for country in Countries.values()]

plt.figure(figsize=(20, 5))
plt.bar(x, y)
plt.title('Average Score of Universities in Countries')
plt.xlabel('Countries')
plt.ylabel('Average Score')
#rotate
plt.xticks(rotation=90)
plt.margins(0.2)

# Add text annotations to the bars
for i, country in enumerate(sorted_countries):
    plt.text(i, country[1][0].avg,  len(country[1][0].universities), ha='center', va='bottom', rotation='vertical', fontsize=8)

info_text = 'Graph Information'
info_text += '\n-----------------------------'
info_text += '\nX-axis: Countries'
info_text += '\nY-axis: Average Score'
info_text += '\nOn Bars: Number of Universities'
plt.text(1, -0.25, info_text, ha='left', va='top', transform=plt.gca().transAxes)


plt.savefig('output.jpeg')
plt.show()
