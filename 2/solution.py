first = '((:?(\('
second = '\)|\['
third = '\]|\{'
fourth = '\}))*)'
depth = ''
for i in range(5):
    depth = fr'{first}' + fr'{depth}' + fr'{second}' + fr'{depth}' + fr'{third}' + fr'{depth}' + fr'{fourth}'
PARENTHESIS_REGEXP = '^' + depth + '$'


SENTENCES_REGEXP = r'(?P<sentence>((?=(?=.*:).*\n.*;)[\S\s]*?(\.\.\.|\?\!|\!\?|[.?!])\n)|((?<=\n)\d+\..*?(\.\.\.|\?\!|\!\?|[;.?!]))|((?<=[?!.\n] )(.*?)(\.\.\.|\?\!|\!\?|[?!.]))|((^).+?(\Z|\n|\.\.\.|\!|\?|\.|\$)))'


# проблемы:  Р. Паттинсона, т.е., т.д., т. е.
PERSONS_REGEXP = r'(?P<person>([A-Z]([a-z]+|\.)(?:\s+[A-Z]([a-z]+|\.))*\s+[A-Z]([a-z]+|\.)|[А-ЯЁ]([а-яё]+|\.)(?:\s+[А-ЯЁ]([а-яё]+|\.))*\s+[А-ЯЁ]([а-яё]+|\.)))'


NAME = r'(?P<name>(?<=<td><h1 class=\"level2\"><a class=\"all\" href=\"/series/77164/\">).*?(?=</a></h1></td>))'
EPISODES_COUNT = r'(?P<episodes_count>((?<=<tr>\n<td class=\"news\">)\w.*\w(?=</td>)))'

EPISODE_NUMBER_RUMANE = r'(?P<episode_number>(?<=Эпизод )\d+)(?=.*\n.*?<b>(?P<episode_name>(.*?))<)'
EPISODE_ORIGINAL_NAME_DATE = r'((?<=episodesOriginalName\">)(?P<episode_original_name>.*?)<.*\n.*?>(?P<episode_date>(.*?))<)'

SEASONS = r'(?P<season>((?<=Сезон )\d+))'
SEASON_YEAR_EPISODES = r'(?P<season_year>(\d+(?=, *эпизодов: (?P<season_episodes>\d+))))'

SERIES_REGEXP = fr'{NAME}|{EPISODES_COUNT}|{EPISODE_NUMBER_RUMANE}|{EPISODE_ORIGINAL_NAME_DATE}|{SEASONS}|{SEASON_YEAR_EPISODES}'
