result = 2 + 3 * 4
print(result)   # 14, because * has higher precedence than +
result = (2 + 3) * 4
print(result)   # 20, because parentheses have the highest precedence

 ###################################

#  Operator Precedence Table (High → Low)
# Precedence	Operators	Associativity
# 1 	()                              (Parentheses)	Left to Right
# 2	    **                              (Exponent)	Right to Left
# 3  	+x, -x, ~x                      (Unary plus, minus, bitwise NOT)	Right to Left
# 4 	*, /, //, %	                    Left to Right
# 5	    +, -	                         Left to Right
# 6	    <<, >>                          (Shift)	Left to Right
# 7	    &	                           Left to Right
# 8	    ^	                            Left to Right
# 9	    `	                            Left to Right
# 10   	<, <=, >, >=, ==, !=	        Left to Right
# 11	not	                            Right to Left
# 12	and	                            Left to Right
# 13	or	                            Left to Right
# 14	=, +=, -=, *=, /=, ...      	Right to Left