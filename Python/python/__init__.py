import pandas

from jproperties import Properties

# This method will capture all the properties file data and return the dictionary object
def _readproperties(filepath):
    configs = Properties()
    with open(filepath,'rb') as config_file:
        configs.load(config_file)
    items_pro = configs.items()
    prop_dict = {}
    for item in items_pro:
        prop_dict[item[0]]=item[1].data
    # print(item[0],"=",item[1].data)
    return prop_dict

# This method will read the csv data
def _readcsvdata(filepath):
    csvdata = pandas.read_csv(filepath)
    return csvdata