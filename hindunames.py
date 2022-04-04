import json
from os import name
from urllib.request import urlopen
import threading
import xmltodict

baseUrl = "https://hindunames.net/hindu-baby-names?page="
name_dict = []

# def save_page(x):
pages = 115
# pages = 115
x = 1
# while x < 115:
while x <= pages:
    # t1 = threading.Thread(target=save_page, args=(x))
    # t1.start()
    # savePage(x)

    name_xml = ""
    print("page fetching started : "+str(x))
    page = urlopen(baseUrl+str(x))

    html_bytes = page.read()
    html = str(html_bytes.decode("utf-8"))

    start_i = html.find(
        '<div class="bg-white overflow-hidden shadow-xl sm:rounded-lg')

    end_i = html.rfind('<div class="p-5 content-center">')

    # print(str(start_i)+" "+str(end_i))

    name_xml = html[start_i:end_i]
    # print(len(name_xml))
    header_start = name_xml.find("<header")
    header_end = name_xml.find("</header>")+9
    name_xml = name_xml.replace(name_xml[header_start:header_end], '')
    name_xml = name_xml.replace('Girl name', 'F')
    name_xml = name_xml.replace('Boy name', 'M')
    name_xml = name_xml.replace('&', 'and')  # to remove & in 7th page

    # if x == 7:  #only to find errors in page 7
    #     # print(name_xml)
    #     text_file = open("./77.xml", "w")
    #     text_file.write(name_xml)
    #     text_file.close()

    data_dict = xmltodict.parse(name_xml)

    # print(len(data_dict['div']['div']))

    for name in data_dict['div']['div']:
        # print(type(name))
        if '@class' not in name:  # to remove google ad html element and get only 50 name elements
            namedict = {}
            namedict['name'] = name['div']['div']['div'][0]['div'][0]['h2']['a']['#text']
            namedict['sex'] = name['div']['div']['div'][0]['div'][0]['h2']['span']['#text']
            namedict['meaning'] = name['div']['div']['div'][0]['div'][1]['h2']
            name_dict.append(namedict)
            # print(name['div']['div']['div'][0]['div'][0]['h2']['a']['#text'])
            # print(name['div']['div']['div'][0]
            #     ['div'][0]['h2']['span']['#text'])
            # print(name['div']['div']['div'][0]['div'][1]['h2'])
            # print(namedict['name'])
            # print(namedict['sex'])
            # print(namedict['meaning'])
            # print()

    names_json = json.dumps(data_dict)

    # print(names_json)

    # # writing to file

    # text_file = open("./"+str(x)+".json", "w")

    # text_file.write(names_json)

    # text_file.close()

    # text_file = open("./"+str(x)+".xml", "w")

    # text_file.write(name_xml)

    # text_file.close()

    # with open("./"+str(x)+".json", "w") as json_file:
    #     json_file.write(names_json)
    #     json_file.close()

    print("page completed : "+str(x))
    x += 1

print("total names : "+str(len(name_dict)))


with open("./nameData.json", "w") as json_file:
    json_file.write(json.dumps(name_dict))
    # json_file.write(json.dumps({"names":name_dict}))
    json_file.close()

# x = 1
# # while x < 115:
# while x < pages:
#     with open("./"+str(x)+".xml") as xml_file:

#         data_dict = xmltodict.parse(xml_file.read())
#         xml_file.close()

#         # generate the object using json.dumps()
#         # corresponding to json data

#         json_data = json.dumps(data_dict)

#         # Write the json data to output
#         # json file
#         with open("./"+str(x)+".json") as json_file:
#             json_file.write(json_data)
#             json_file.close()
