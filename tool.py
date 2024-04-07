import sys, os, base64
from urllib.parse import unquote
from urllib.parse import quote


class HtmlObfuscator:
	def __init__(self):
		self.start_text = '''<!DOCTYPE html>
<script type="text/javascript">
document.write(decodeURIComponent(atob(\''''
		self.end_text = '''\')));
</script>
<noscript>You must enable javascript in your browser to view this webpage.</noscript>
'''

	@staticmethod
	def decode(data):
		data = data.encode("utf-8")
		data = base64.b64decode(data)
		data = data.decode("utf-8")
		data = unquote(data)
		return data

	def decode_data_lst(self, data_lst: list):
		for data in data_lst:
			yield self._decode(data[88:-102])

	@staticmethod
	def encode(data):
		data = quote(data)
		data = data.encode("utf-8")
		data = base64.b64encode(data)
		data = data.decode("utf-8")
		return data

	def encode_data_lst(self, data_lst: list):
		for data in data_lst:
			yield self.start_text + self._encode(file) + self.end_text


if __name__ == "__main__":
	usage = ['Usage: this.py [obf|deobf] [filename.html] [filename2.html] ...\n',
			 'NOTE: Files de-obfuscated with this tool MUST have been obfuscated with it as well.']
	if len(sys.argv) > 2:
		mode = sys.argv[1]
		files = sys.argv[2:]

		encoder = HtmlObfuscator()

		for file in files:
			if not os.path.isfile(file):
				print('''\nFile not found!''')
				sys.exit(0)
			file_data, message_insert = open(file, mode="r", encoding="utf-8").read(), ""
			if mode == "obf":
				finished_data, message_insert = encoder.encode(file_data), "Obfuscated"
			elif mode == "deobf":
				finished_data, message_insert = encoder.decode(file_data), "De-obfuscated"
			else:
				for chunk in usage:
					print(chunk)
				sys.exit(0)
			open(file, mode="w", encoding="utf-8").write(encoded_file_data)
			print("\nSuccessfully %s" % message_insert + file)
	else:
		for chunk in usage:
			print(chunk)
