import csv
import bubble_sort
import statistics

def get_maximum_value(list):
    maximum = list[0]
    for l in list:
        if maximum > l:
            maximum = l
    return maximum

""" 
        Given a list of numbers as input this function will return the maximum value.
    
        :param list: the list of numbers given as input
        :return: the maximum value
    """




def get_minimum_value(list):
    minimum = list[0]
    for l in list:
        if minimum < l:
            minimum = l
""" 
        Given a list of numbers as input this function will return the minimum value.
    
        :param list: the list of numbers given as input
        :return: the minimum value
    """
        
statistics.mean(list1)
list1 = list.copy()


def get_median_value(list):
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]



    """ 
        Given a list of numbers as input this function will return the maximum value.
    
        :param list: the list of numbers given as input
        :return: the maximum value
    """
"""   
def bubble_sort(list1):
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
  """




def get_mode(list):
    highest_freq = 0
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename):
    scores = []
    with open(filename, mode ='r') as file:   
        csvFile = csv.DictReader(file)
    
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)    
    return scores
    
if __name__ == "__main__":

    scores = read_scores_from_csv('example week 3.csv')
    
   
    minimum = get_minimum_value(scores)   
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)
   

    print(f'Mean: {statistics.mean} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')