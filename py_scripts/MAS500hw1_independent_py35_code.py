import mediacloud, datetime
mc = mediacloud.api.MediaCloud('API_Key')
res1 = mc.sentenceCount('( Trump )', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
res2 = mc.sentenceCount('( Clinton)', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
print ("# Trump was mentioned: ",res1['count']) # prints the number of sentences found
print ("# Clinton was mentioned: ",res2['count'])

n1 = 'Trump'
n2 = 'Clinton'
op1 = ' was talked about more frequently than '
op2 = 'They were talked about as frequently as each other.'

if res1['count'] > res2['count']:
   ver = n1 + op1 + n2 +' in September 2016.'
elif res1['count'] < res2['count']:
    ver = n2 + op1 + n1 +' in September 2016.'
else: 
    ver = op2
print(ver)
    