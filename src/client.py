import requests
import pandas as pd

from interfaces import Client, Cache

class UniprotClient(Client):

	def __init__(self, cache: Cache) -> None:
		self.cache = cache

	@property
	def base_url(self):
		return 'https://rest.uniprot.org/uniprotkb/search?query='
	
	def run(self, xlsx):
		df = pd.read_excel(xlsx, usecols=["Uniprot ID"])
		print("Total number of records to process: " + str(len(df)))
		# url_uniProt = "https://www.uniprot.org/uniprot/?query=" #%5BMYCP5_MYCTU%5D&sort=score"  # This is old URL
		# url_uniProt = "https://rest.uniprot.org/uniprotkb/search?query="
		outfilename = "Output-from-" + xlsx.split('/')[-1][:-5] + ".txt"
		output = open(self.output_dir + outfilename, "w")
		line = "UniprotID Gene OLN ORF\n"
		output.write(line)
		count = 0
		total_count = 0
		for each_id in df['Uniprot ID']:
			result = ''
			value = self.cache.get(each_id)
			if value != -1:
				result = value
			else:
				# go to Uniprot website and fetch
				line = ''
				uri = self.base_url + each_id + "&fields=gene_names&format=tsv"
				resp = requests.get(uri)
				try:
					for i in resp.text.split('\n')[1:-1]:
						if 'Rv' in i:
							result = i
				except:
					("Error getting Rv Number for: " + each_id + ':' + resp.status_code)
				if result.count(' Rv') > 1:
					print("More than one Rv Number present for: " + each_id + ". Please process this input manually.")
					continue
				# write to cache
				self.cache.put(each_id, result)
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