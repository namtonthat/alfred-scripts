import re
import clipboard
from urllib.parse import quote

clipboard_text = clipboard.paste()

# variables
re_logstream = re.compile(r"'logStreamName': '(?P<stream_name>.*?)'")
log_stream_name = re.findall(re_logstream, clipboard_text)[0]
log_group = "/aws/batch/job"


# write aws command
# aws_command = f"aws logs get-log-events --log-group-name {log_group} --log-stream-name {log_stream_name} --query 'events[*].message'"
# print(aws_command)

# log_stream_name = log_stream_name.replace('/', "$252F")
log_stream_name = quote(log_stream_name, safe="")
aws_url = f"https://ap-southeast-2.console.aws.amazon.com/cloudwatch/home?region=ap-southeast-2#logsV2:log-groups/log-group/$252Faws$252Fbatch$252Fjob/log-events/{log_stream_name}"

print(aws_url)
