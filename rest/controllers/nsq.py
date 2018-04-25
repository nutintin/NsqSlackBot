import requests
import time

from datetime import datetime
from rest.exceptions import BadRequest


class NsqController(object):

	def getNsqStats(self, topic, wb, channel):
		
		# self.validate_argument(topic)
		response = self.request_to_nsq(topic, channel)

		# save_to_db(response)
		self.send_to_slack(wb, topic, response)

	def validate_argument(self, topic):
		if not topic:
			raise BadRequest("data is needed")

		response = {}
		pass

	def request_to_nsq(self, topic, channel):
		params = (
			('format', 'json'),
			('topic', topic),
			('channel', channel),
		)

		response = requests.get('http://159.65.12.8:4151/stats', params=params)
		result = response.json()
		today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		try:
			total_message = result["topics"][0]["channels"][0]["message_count"]
		except:
			total_message = 0
		
		try:
			depth = result["topics"][0]["channels"][0]["depth"]
		except:
			depth = 0

		try:
			connections = len(result["topics"][0]["channels"][0]["clients"])
		except:
			connections = 0
		
		try:
			requeue_count = result["topics"][0]["channels"][0]["requeue_count"]
		except:
			requeue_count = 0

		try:
			timeout_count = result["topics"][0]["channels"][0]["timeout_count"]
		except:
			timeout_count = 0

		try:
			in_flight_count = result["topics"][0]["channels"][0]["in_flight_count"]
		except:
			in_flight_count = 0


		final_response = {
			"total_message": total_message,
			"depth": depth,
			"connections": connections,
			"requeue_count": requeue_count,
			"timeout_count": timeout_count,
			"in_flight_count": in_flight_count,
			"date": today
		}
		

		return final_response

	def save_to_db(self, response):
		# SAVE TO DB
		client = MongoClient('mongodb://localhost:27017/')
		db = client["managix_nsq"]
		
		result = db.daily_stat.insert_one(response)

	def send_to_slack(self, wb, topic, response):
		if wb:
			host_slack = wb
		else:
			host_slack = "https://hooks.slack.com/services/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"

		headers = {
			"Content-Type": "application/json"
		}

		attachment = {
			"response_type": "in_channel",
			"attachments" : [
				{
					"fallback": "New NSQ Stats",
					"color": "#2eb886",
					"title": topic,
					"text": "total_message: {},\ndepth: {},\nconnections: {},\nrequeue_count: {},\ntimeout_count: {},\nin_flight_count: {},\ndate: {}".format(response["total_message"], response["depth"], response["connections"], response["requeue_count"], response["timeout_count"], response["in_flight_count"], response["date"]),
					"ts": time.time()
				}
			]
		}



		requests.post(host_slack, headers=headers, json=attachment)	