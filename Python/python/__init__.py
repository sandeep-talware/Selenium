from jproperties import Properties
print("hello world")

# def _readproperties():
configs = Properties()
with open('C:/Users/Sachin Joshi/PycharmProjects/Selenium/Python/config/app-config.properties','rb') as config_file:
    configs.load(config_file)
    items_pro = configs.items()
    for item in items_pro:
        print(item[0],"=",item[1].data)
