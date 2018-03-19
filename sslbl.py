import requests
import yaml
import os

inteltype = ['INTEL_ADDR']
path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/sslbl/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def import_ip_intel():
    try:
        source = cfg['enrichment_plugin']['SSLBL_IP_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '':
                a = s.split(",")
                tmp_dict = {}
                tmp_dict["EvtType"] = "IPv4"
                tmp_dict["EvtName"] = a[0].strip()
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["SSLBL"]
                tmp_dict2["IntelRefURL"] = [source]
                b_lst = []
                b_lst.append(a[2].strip())
                tmp_dict2["ThreatType"] = b_lst
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_ADDR'

