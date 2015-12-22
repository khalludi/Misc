import boto, logging

AWS_ACCESS_KEY = "AKIAJIYTLBO7QT5ESB6Q"
AWS_SECRET_KEY = "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"
bucket_name = "home-pic231" 

def push_picture_to_s3(id):
  from boto.s3.key import Key
  logging.getLogger('boto').setLevel(logging.CRITICAL)

  conn = boto.connect_s3(AWS_ACCESS_KEY, AWS_SECRET_KEY)
  bucket = conn.get_bucket(bucket_name)

  key = '%s.jpg' % id
  fn = '/home/kali/Desktop/%s.jpg' % id

  k = Key(bucket)
  k.key = key
  k.set_contents_from_filename(fn)

  #k.make_public()
  #os.remove(fn)

push_picture_to_s3("01")
