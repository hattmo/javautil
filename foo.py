from javautil import op_codes as op
code = op.bipush(2) + op.bipush(3)
print(code.to_bytes())