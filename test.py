STRING_HELPER = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "ten":10,
    "eleven":11,
    "twelve":12,
    "thirteen":13,
    "fourteen":14,
    "fifteen":15,
    "sixteen":16,
    "seventeen":17,
    "eighteen":18,
    "nineteen":19,
    "twenty":20,
    "thirty":30,
    "forty":40,
    "fifty":50,
    "sixty":60,
    "seventy":70,
    "eighty":80,
    "ninety":90,
    "hundred":100
}
def convert(text):
    return sum([STRING_HELPER[val] for val in text.split("-")])
print(convert("twenty-five"))


for i in range(len(data["Age"])):
    if not data["Age"][i].isnumeric():
        data["Age"][i] = convert(data["Age"][i])
    else: 
        data["Age"][i] = int(data["Age"][i])


bs_list = []
heartrate_list = []
for i in range(len(data["BS_HeartRate"])):
    bs = ""
    heartrate = ""

    if "," in data["BS_HeartRate"][i]:
        bs,heartrate = data["BS_HeartRate"][i].split(",")
    if ";" in data["BS_HeartRate"][i]:
        bs,heartrate = data["BS_HeartRate"][i].split(";")
    if "_" in data["BS_HeartRate"][i]:
        bs,heartrate = data["BS_HeartRate"][i].split("_")

    if not bs.replace(".","").isnumeric():
        bs_list.append(float(convert(bs)))
    else:
        bs_list.append(float(bs))
    
    if not heartrate.replace(".","").isnumeric():
        heartrate_list.append(float(convert(heartrate)))
    else:
        heartrate_list.append(float(heartrate))

data["bs"] = bs_list
data["heartrate"] = heartrate_list

data.drop("BS_HeartRate",inplace=True,axis=1)
