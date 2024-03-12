# \r (return) \n (linefeed) -> \r\n -> CRLF
# \n -> LF
print(12, 34, 2,  sep="-", end='\r\n')
print(56, 78, sep="-")