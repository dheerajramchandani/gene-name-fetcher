import pandas as pd
import requests
import os
import sys
#
def getRvNames(xlsx):
	df = pd.read_excel(xlsx, usecols=["Uniprot ID"])
	print("Total number of records to process: " + str(len(df)))
	# url_uniProt = "https://www.uniprot.org/uniprot/?query=" #%5BMYCP5_MYCTU%5D&sort=score"  # This is old URL
	url_uniProt = "https://rest.uniprot.org/uniprotkb/search?query="
	outfilename = "Output-from-" + xlsx.split('/')[-1][:-5] + ".txt"
	output = open(outfilename, "w")
	count = 0
	total_count = 0
	for each_id in df['Uniprot ID']:
		line = ''
		uri = url_uniProt + each_id + "&fields=gene_primary&format=tsv"
		resp = requests.get(uri)
		primary_name = getPrimaryName(resp)
		uri = url_uniProt + each_id + "&fields=gene_oln&format=tsv"
		resp = requests.get(uri)
		try:
			for i in resp.text.split('\n')[1:-1]:
				if 'Rv' in i:
					result = ' '.join([j[j.find('Rv'):] for j in i.split(' ') if 'Rv' in j])
					break
		except:
			("Error getting Rv Number for: " + each_id + ':' + resp.status_code)
		if result and len(result.split(' ')) > 1:
			print("More than one Rv Number present for: " + each_id + ". Please process this input manually.")
			continue
		if primary_name:
			line = each_id + ' ' + primary_name + ' ' + result + '\n'
		else:
			line = each_id + ' ' + result + '\n'
		output.write(line)
		count += 1
		if count == 100:
			total_count += count
			print(str(total_count) + " records processed...")
			count = 0
	output.close()
	total_count += count
	print("All " + str(total_count) + " records processed for file: " + xlsx)
#
def getPrimaryName(response):
	try:
		name = response.text.split('\n')[1]
	except IndexError:
		name = ''
	return name
#
if __name__ == "__main__":
	try:
		getRvNames(sys.argv[1])
	except IndexError:
		print("Please provide the input file.")