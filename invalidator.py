from boto.cloudfront import CloudFrontConnection
import getopt, sys


opts, args = getopt.getopt(sys.argv[1:],"a:s:b:",["access=","secret=","branch="])
aws_access_key =None
aws_secret_access_key = None
branch = None

for opt, arg in opts:
  if opt == '-a':
     aws_access_key = arg
  elif opt == '-s':
     aws_secret_access_key = arg
  elif opt == '-b':
     branch = arg

if aws_access_key and aws_secret_access_key and branch:
  objects = [ '*' ]
  conn = CloudFrontConnection(aws_access_key, aws_secret_access_key)
  if branch== 'master':
    print(conn.create_invalidation_request('<replace with cloudfront distro id>', objects))
  elif branch == 'dev':
    print(conn.create_invalidation_request('<replace with cloudfront distro id>', objects))
else:
  print('missing arguments')
