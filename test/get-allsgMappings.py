import isesdk

test = isesdk.ise.ISE('admin', 'asdf1234ASDF!@#$', '10.0.49.2')
r = test.sgMapping.getAll()
print(r)
