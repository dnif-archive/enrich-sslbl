## SSLBL   
https://sslbl.abuse.ch/

### Overview
SSL Blacklist (SSLBL) is a project maintained by abuse.ch. The goal is to provide a list of "bad" SSL certificates identified by abuse.ch to be associated with malware or botnet activities. SSLBL relies on SHA1 fingerprints of malicious SSL certificates and IPs associated with these.

#### SSLBL IP feeds
The SSL IP Blacklist (CSV) contains all hosts (IP addresses) that SSLBL has seen in the past 30 days being associated with a malicious SSL certificate. 
The CSV contains IP address and port number of malicious SSL hosts.

For more information on this feed go to: https://sslbl.abuse.ch/blacklist/sslipblacklist.csv

### Using the SSLBL feeds API
 The SSLBL feeds API is found on github at

 https://github.com/dnif/enrich-sslbl

#### Getting started with SSL feeds API

1. #####    Login to your AD, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. #####    Move to the ‘/dnif/<Deployment-key/enrichment_plugins’ folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugins/
```
3. #####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-sslbl.git sslbl
```
### API feed output structure
  | Fields        | Description  |
| ------------- |:-------------:|
| EvtType      | An IP |
| EvtName      | The IOC      |
| IntelRef | Feed Name      |
| IntelRefURL | Feed URL      |
| ThreatType | DNIF Feed Identification Name |      

An example of API feed output
```
{'EvtType': 'IPv4',
'EvtName': '89.35.228.199',
'AddFields': {
'IntelRef': ['SSLBL'],
'IntelRefURL': ['https://sslbl.abuse.ch/blacklist/sslipblacklist.csv'], 
'ThreatType': ['Adwind C&C'] }}
```
