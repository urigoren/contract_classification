from urllib import request, parse
import json, random

def submit(name,company,email,phone,user, test_data):
    """Submits a test data set to the pydata server, and returns accuracy"""
    try:
        test_data = {str(k).lower().replace(".txt", ""):str(v).lower().strip() for k,v in test_data.items()}
        data = parse.urlencode({"user":user, "submission": json.dumps(test_data), "name":name,"company":company,"phone":phone,"email":email}).encode()
        req =  request.Request("https://goren.ml/uattcontract/index.php?rand="+str(random.randint(167,1000000)), data=data)
        resp = request.urlopen(req)
        return float(resp.read().decode("utf8"))
    except Exception as e:
        print (str(e))
        return None
