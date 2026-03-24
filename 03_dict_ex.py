'''
1
["apple","banana","kiwi","grape","kiwi"] -> {"apple":5, "banana":6, "kiwi":4, "grape":5 }
'''
from unittest import result


def get_len_word(list1: list) -> dict:

    '''

    :param list1: list of words
    :return: dict { <word>: <how many letters (len) > }
    '''
    len_word_dict= {}
    for word in list1:
        len_word_dict[word] = len(word)
    return len_word_dict
list_word =get_len_word(["apple", "banana", "kiwi", "grape", "kiwi"])
print(list_word)
'''
2
grades = {"Tom":80, "Anna":95, "John":70} -> (Anna , 95)
'''


def get_max(dict1: dict) -> tuple:
    '''

    :param dict1: {<name>: <grade> ... }
    :return: (<name>, <grade>) of the max student
    '''
    max_name = None
    max_grade = 0
    for k, v in dict1.items():
        if v >= max_grade:
            max_name = k
            max_grade = v

    return max_name, max_grade
grades = {"Tom":80, "Anna":95, "John":70}
print(get_max(grades))
'''
3
count repetition
[4, 2, 1, 2, 3, -1, 3, 2, 2] -> { 1: 1, 2: 4, 3: 2, 4: 1, -1: 1}
'''


def get_count(list1: list) -> dict:
    '''

    :param list1: list of numbers
    :return: dict { <number>: <how many times appear> }
    '''

    count_dict = {}
    for num in list1:
        if num in count_dict:
            # אם המספר כבר קיים במילון, פשוט נוסיף 1 למונה שלו
            count_dict[num] += 1
        else:
            # אם זו פעם ראשונה שאנחנו רואים את המספר, נכניס אותו עם ערך 1
            count_dict[num] = 1

    return count_dict
print(get_count([4, 2, 1, 2, 3, -1, 3, 2, 2]))

'''
4
{"apple":5, "banana":6, "kiwi":4} -> {5:"apple", 6:"banana", 4:"kiwi"}
'''


def reverse_dict(dict1: dict) -> dict:
    '''

    :param dict1: {<word>: <number> ... }
    :return: dict { <number>: <word> }
    '''
    dict_r = {}
    for k, v in dict1.items():
        dict_r[v] = k[:]

    return dict_r
print(reverse_dict({"apple":5, "banana":6, "kiwi":4}))

'''
5
[1,2,3,4,5,6]
-> {"even":3, "odd":3}
'''


def count_even_odd(nums: list) -> dict:
    '''
    :param nums: list of numbers
    :return: dict {"even": count_even, "odd": count_odd}
    '''
    dict_even_odd = {"even": 0, "odd": 0}
    for num in nums:
        if num % 2 == 0:
            dict_even_odd["even"] +=1
        else:
            dict_even_odd["odd"] +=1
    return dict_even_odd
print(count_even_odd([1,2,3,4,5,6])   )
'''
6
cities = {
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}

-> ["Paris", "Rome", "Madrid", "New York", "London", "Tokyo"]
(sorted by population from small to big)

    create dict = { 2_140_000: "Paris", 37_400_000: "Tokyo", ... }
    create list = <population> [2_140_000, 8_419_000]
    sort the list
        run on the values: add the city name

'''


def get_cities_sorted_by_population(cities: dict) -> list:
    population = []  # [2140000, 2873000, 3223000, 8419000, 8982000, 37400000]
    dict_pop_city_name = {}  # {37400000: 'Tokyo', 2140000: 'Paris', 8419000: 'New York', 8982000: 'London',
    #  3223000: 'Madrid', 2873000: 'Rome'}

    for k, v in cities.items():
        population_of_city = v['population']
        population.append(population_of_city)
        dict_pop_city_name[population_of_city] = k

    population.sort()

    result = []
    for pop in population:
        result.append(dict_pop_city_name[pop])
    return result

    '''

    :param cities: {
        <city_name>: {
            "language": <language>,
            "population": <population>,
            "size": <city_area_km2>,
            "country": <country>
        }
    }

    :return: list of city names sorted by population (small → big)
    '''


print(get_cities_sorted_by_population({
    "Tokyo": {"language": "Japanese", "population": 37_400_000, "size": 2194, "country": "Japan"},
    "Paris": {"language": "French", "population": 2_140_000, "size": 105, "country": "France"},
    "New York": {"language": "English", "population": 8_419_000, "size": 783, "country": "USA"},
    "London": {"language": "English", "population": 8_982_000, "size": 1572, "country": "UK"},
    "Madrid": {"language": "Spanish", "population": 3_223_000, "size": 604, "country": "Spain"},
    "Rome": {"language": "Italian", "population": 2_873_000, "size": 1285, "country": "Italy"}
}))

'''
7
["apple","banana","avocado","blueberry","apricot","corn"]

-> {
    "a": ["apple","avocado","apricot"],
    "b": ["banana","blueberry"],
    "c": ["corn"]
}
'''


def group_by_letter(words: list) -> dict:
    '''

    :param words: list of words
    :return: dictionary where:
             key = first letter of the word
             value = list of all words that start with that letter
    '''
    result = {}
    for word in words:
        first_letter = word[0]

        if first_letter not in result:
            result[first_letter] = []

        result[first_letter].append(word)

    return result


print(group_by_letter(["apple","banana","avocado","blueberry","apricot","corn"]))